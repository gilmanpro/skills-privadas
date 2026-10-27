# Mejores Prácticas y Patrones en Go

## Estructura de proyectos

### Layout recomendado
```
my-project/
├── cmd/               # ejecutables (uno por subdirectorio)
│   └── server/
│       └── main.go
├── internal/          # código privado (no importable externamente)
│   ├── handler/
│   └── service/
├── pkg/               # código compartible (API pública)
│   └── api/
├── api/               # definiciones de API (proto, OpenAPI, swagger)
├── config/            # configuración
├── db/                # migrations, seeds
├── docs/              # documentación
├── scripts/           # scripts de build/deploy
├── test/              # tests de integración
├── web/               # assets web (HTML, CSS, JS)
├── go.mod
├── go.sum
├── Makefile
├── Dockerfile
└── README.md
```

### Principios
- `cmd/`: cada subdirectorio es un binario diferente
- `internal/`: el compilador impide que otros módulos importen esto
- `pkg/`: código que otros módulos pueden importar (usa con cuidado)
- Mantén `main.go` pequeño: solo inicializa y arranca

## Patrones de diseño

### Constructor funcional (Functional Options)
```go
type Server struct {
    addr    string
    port    int
    timeout time.Duration
    logger  *slog.Logger
}

type Option func(*Server)

func WithPort(port int) Option {
    return func(s *Server) {
        s.port = port
    }
}

func WithTimeout(t time.Duration) Option {
    return func(s *Server) {
        s.timeout = t
    }
}

func NewServer(addr string, opts ...Option) *Server {
    s := &Server{
        addr:    addr,
        port:    8080,          // defaults
        timeout: 30 * time.Second,
        logger:  slog.Default(),
    }
    for _, opt := range opts {
        opt(s)
    }
    return s
}

// Uso:
s := NewServer("localhost", WithPort(9090), WithTimeout(10*time.Second))
```

### Middleware pattern
```go
type Middleware func(http.Handler) http.Handler

func Chain(handler http.Handler, middlewares ...Middleware) http.Handler {
    for i := len(middlewares) - 1; i >= 0; i-- {
        handler = middlewares[i](handler)
    }
    return handler
}
```

### Repository pattern
```go
type UserRepository interface {
    GetByID(ctx context.Context, id int) (User, error)
    Create(ctx context.Context, user User) (int, error)
    Update(ctx context.Context, user User) error
    Delete(ctx context.Context, id int) error
}

type PostgresUserRepo struct {
    db *sql.DB
}

func (r *PostgresUserRepo) GetByID(ctx context.Context, id int) (User, error) {
    row := r.db.QueryRowContext(ctx, "SELECT id, name, email FROM users WHERE id = $1", id)
    var u User
    err := row.Scan(&u.ID, &u.Name, &u.Email)
    return u, err
}
```

### Singleton con sync.Once
```go
var (
    instance *Service
    once     sync.Once
)

func GetService() *Service {
    once.Do(func() {
        instance = NewService()
    })
    return instance
}
```

## Manejo de errores idiomático

### 1. Errores con contexto
```go
// wrapping (Go 1.13+)
if err != nil {
    return fmt.Errorf("leyendo archivo %s: %w", filename, err)
}

// errors.Is() — comparar por cadena
if errors.Is(err, io.EOF) { ... }

// errors.As() — comparar por tipo
var perr *os.PathError
if errors.As(err, &perr) { ... }
```

### 2. Sentinel errors
```go
var ErrNotFound = errors.New("not found")
var ErrInvalidInput = errors.New("invalid input")
```

### 3. Errores tipados
```go
type ValidationError struct {
    Field string
    Value any
    Msg   string
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("validación: %s=%v: %s", e.Field, e.Value, e.Msg)
}

func (e *ValidationError) Unwrap() error {
    return fmt.Errorf("%s: %s", e.Field, e.Msg)
}
```

## Nombres y convenciones

### Paquetes
- Minúscula, una palabra, sin guiones bajos: `httputil`, `config`
- El nombre del paquete es la base del directorio
- No uses `import .` (excepto en tests)

### Variables
- Cortas y descriptivas: `i`, `r`, `w`, `err`, `ch`, `wg`
- Mayor alcance → nombre más largo: `userCount`, `requestTimeout`
- Abreviaturas enteras en mayúscula: `HTTP`, `URL`, `ID`

### Tipos exportados
- MixedCaps: `UserService`, `HTTPClient`
- Getters sin `Get`: `user.Name()` no `user.GetName()`

### Interfaces
- 1 método: nombre del método + `-er`: `Reader`, `Writer`, `Formatter`
- Múltiples métodos: nombre descriptivo: `Storage`, `Repository`

## Rendimiento

### Escritura de código eficiente
```go
// Preasignar capacidad de slice (evita reallocations)
users := make([]User, 0, len(ids))

// Usar strings.Builder para concatenación
var b strings.Builder
for _, s := range parts {
    b.WriteString(s)
}
result := b.String()

// Preferir range sobre index (más legible, igual velocidad)
for i, v := range slice { }

// Evitar reflection en hot paths
// Preferir encoding/json sobre reflection manual
```

### Escape analysis
```go
// Se queda en stack (rápido)
func sum(a, b int) int {
    result := a + b
    return result
}

// Escapa a heap (más lento)
func sumPtr(a, b int) *int {
    result := a + b
    return &result  // escapa
}
```

### GC y allocaciones
- Reduce allocaciones: reusa buffers, preasigna slices
- Usa `sync.Pool` para objetos temporales frecuentes
- Prefiere valores sobre punteros cuando el tipo es pequeño
- Profilea antes de optimizar: `go test -bench . -benchmem`

## Seguridad

### SQL Injection
```go
// SEGURO — usa parámetros ($1, $2, etc.)
db.Query("SELECT * FROM users WHERE id = $1", userInput)

// INSEGURO — interpolación de strings
db.Query("SELECT * FROM users WHERE id = '" + userInput + "'")
```

### XSS
```go
// Usa html/template (NO text/template) para HTML
import "html/template"
tmpl, _ := template.New("page").Parse("<h1>{{.Title}}</h1>")
tmpl.Execute(w, data)  // escapa automáticamente
```

### Input validation
```go
import "net/mail"

func ValidateEmail(email string) error {
    _, err := mail.ParseAddress(email)
    return err
}
```

### Secrets
```go
// Usa os.Getenv (nunca hardcodees secrets)
dbPassword := os.Getenv("DB_PASSWORD")
```

## Documentación

### Doc comments
```go
// Package user proporciona tipos y funciones para gestionar usuarios.
package user

// User representa un usuario del sistema.
type User struct {
    ID   int64  `json:"id"`
    Name string `json:"name"`
}

// Greet devuelve un saludo personalizado para el usuario.
// Si el usuario no tiene nombre, devuelve un saludo genérico.
func (u *User) Greet() string {
    if u.Name == "" {
        return "Hola, desconocido"
    }
    return fmt.Sprintf("Hola, %s", u.Name)
}
```

### Ejemplo ejecutable
```go
func ExampleGreet() {
    u := &User{Name: "Ana"}
    fmt.Println(u.Greet())
    // Output: Hola, Ana
}
```

## Integración continua

### Makefile típico
```makefile
.PHONY: build test lint clean

build:
	go build -o bin/app ./cmd/server

test:
	go test -race -count=1 -coverprofile=coverage.out ./...
	go tool cover -func=coverage.out

lint:
	golangci-lint run ./...

clean:
	go clean -cache
	rm -rf bin/

run:
	go run ./cmd/server
```

### GitHub Actions básico
```yaml
name: Go CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: '1.23'
      - run: go mod tidy
      - run: go vet ./...
      - run: go test -race -count=1 ./...
```

## Go Modules — Checklist de publicación

- [ ] `go mod tidy` — limpiar dependencias
- [ ] `go vet ./...` — análisis estático
- [ ] `go test -race ./...` — tests con race detector
- [ ] `golangci-lint run ./...` — linter completo
- [ ] `govulncheck ./...` — revisar vulnerabilidades
- [ ] Tag semver: `git tag v1.0.0 && git push --tags`
- [ ] `GOPROXY=proxy.golang.org,direct go list -m github.com/user/mod@v1.0.0` — verificar disponibilidad

## Errores frecuentes de novatos

1. ❌ `var s []int; s[0] = 1` → pánico (slice nil, usa `make` o literal)
2. ❌ Iterar map sin orden → usa `slices.Sorted(maps.Keys(m))`
3. ❌ Usar `goroutine` sin `WaitGroup` o channel → leakt
4. ❌ Ignorar `err` con `_` → el error se pierde
5. ❌ `defer wg.Done()` después de `wg.Add(1)` en el loop → panic
6. ❌ Usar `json.Marshal` en `http.ResponseWriter` sin `Content-Type`
7. ❌ No cerrar `resp.Body` en cliente HTTP → file descriptor leak
8. ❌ Copiar `sync.Mutex` por valor → deadlock
9. ❌ Usar `time.Sleep` para esperar goroutines → frágil
10. ❌ No comprobar `rows.Err()` después de `rows.Next()` loop
