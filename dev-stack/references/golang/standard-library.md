# Standard Library de Go — Paquetes Clave

## net/http — Servidor y Cliente HTTP

### Servidor HTTP básico
```go
package main

import (
    "encoding/json"
    "log"
    "net/http"
)

func main() {
    http.HandleFunc("/hello", helloHandler)
    http.HandleFunc("/api/data", dataHandler)
    
    // Servir archivos estáticos
    http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("./static"))))
    
    log.Println("Servidor en :8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}

func helloHandler(w http.ResponseWriter, r *http.Request) {
    if r.Method != http.MethodGet {
        http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
        return
    }
    w.Header().Set("Content-Type", "text/plain")
    w.Write([]byte("Hello, Go!"))
}

func dataHandler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
}
```

### Server con middleware (patrón)
```go
func loggingMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        log.Printf("%s %s", r.Method, r.URL.Path)
        next.ServeHTTP(w, r)
    })
}

func main() {
    mux := http.NewServeMux()
    mux.HandleFunc("/", handler)
    
    server := &http.Server{
        Addr:         ":8080",
        Handler:      loggingMiddleware(mux),
        ReadTimeout:  10 * time.Second,
        WriteTimeout: 10 * time.Second,
        IdleTimeout:  60 * time.Second,
    }
    log.Fatal(server.ListenAndServe())
}
```

### Cliente HTTP
```go
client := &http.Client{
    Timeout: 10 * time.Second,
}

req, _ := http.NewRequestWithContext(ctx, "GET", "https://api.example.com/data", nil)
req.Header.Set("Authorization", "Bearer token")

resp, err := client.Do(req)
if err != nil {
    log.Fatal(err)
}
defer resp.Body.Close()

body, _ := io.ReadAll(resp.Body)
fmt.Println(string(body))
```

### ServeMux avanzado (Go 1.22+)
```go
mux := http.NewServeMux()
mux.HandleFunc("GET /users/{id}", getUser)           // path params
mux.HandleFunc("POST /users", createUser)
mux.HandleFunc("GET /users/{id}/posts/{postId}", getPost)
// r.PathValue("id") para acceder al parámetro
```

## encoding/json — JSON

### Marshal / Unmarshal
```go
type User struct {
    ID        int       `json:"id"`
    Name      string    `json:"name"`
    Email     string    `json:"email,omitempty"`
    CreatedAt time.Time `json:"created_at"`
    Password  string    `json:"-"`  // nunca se serializa
}

// Marshal (struct → JSON)
u := User{ID: 1, Name: "Ana", Email: "ana@test.com"}
data, _ := json.Marshal(u)
data, _ := json.MarshalIndent(u, "", "  ")  // pretty print

// Unmarshal (JSON → struct)
jsonStr := `{"id":1,"name":"Ana"}`
var u User
json.Unmarshal([]byte(jsonStr), &u)

// Decodificar directamente de un stream
decoder := json.NewDecoder(resp.Body)
decoder.Decode(&u)

// Codificar directamente a un stream
encoder := json.NewEncoder(w)
encoder.Encode(u)
```

### JSON raw y genérico
```go
// RawMessage para procesamiento diferido
type Response struct {
    Status string          `json:"status"`
    Data   json.RawMessage `json:"data"`
}

// map[string]any para JSON dinámico
var data map[string]any
json.Unmarshal([]byte(jsonStr), &data)
name := data["name"].(string)
```

## database/sql — Base de datos SQL

### Conexión
```go
import (
    "database/sql"
    _ "github.com/lib/pq"  // driver PostgreSQL
)

db, err := sql.Open("postgres", "postgres://user:pass@localhost/dbname?sslmode=disable")
if err != nil { log.Fatal(err) }
defer db.Close()

// Verificar conexión
if err := db.PingContext(ctx); err != nil {
    log.Fatal(err)
}

db.SetMaxOpenConns(25)
db.SetMaxIdleConns(5)
db.SetConnMaxLifetime(5 * time.Minute)
```

### Query
```go
// SELECT
type User struct {
    ID    int
    Name  string
    Email string
}

rows, err := db.QueryContext(ctx, "SELECT id, name, email FROM users WHERE active = $1", true)
if err != nil { return err }
defer rows.Close()

var users []User
for rows.Next() {
    var u User
    if err := rows.Scan(&u.ID, &u.Name, &u.Email); err != nil {
        return err
    }
    users = append(users, u)
}
if err := rows.Err(); err != nil {
    return err
}

// QueryRow (una sola fila)
var name string
err := db.QueryRowContext(ctx, "SELECT name FROM users WHERE id = $1", 1).Scan(&name)

// INSERT / UPDATE / DELETE
result, err := db.ExecContext(ctx, "INSERT INTO users (name, email) VALUES ($1, $2)", "Ana", "ana@test.com")
id, _ := result.LastInsertId()
affected, _ := result.RowsAffected()
```

### Prepared Statements
```go
stmt, err := db.PrepareContext(ctx, "INSERT INTO users(name, email) VALUES($1, $2)")
if err != nil { return err }
defer stmt.Close()

for _, u := range users {
    stmt.ExecContext(ctx, u.Name, u.Email)
}
```

### Transacciones
```go
tx, err := db.BeginTx(ctx, nil)
if err != nil { return err }
defer tx.Rollback() // si no se hace commit, hace rollback

_, err = tx.ExecContext(ctx, "UPDATE accounts SET balance = balance - $1 WHERE id = $2", 100, 1)
if err != nil { return err }

_, err = tx.ExecContext(ctx, "UPDATE accounts SET balance = balance + $1 WHERE id = $2", 100, 2)
if err != nil { return err }

return tx.Commit()
```

## io / io/fs — Interfaces de E/S

### Interfaces fundamentales
```go
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}

type Closer interface {
    Close() error
}

type Seeker interface {
    Seek(offset int64, whence int) (int64, error)
}

// Compuestas
type ReadWriter interface {
    Reader
    Writer
}

type ReadWriteCloser interface {
    Reader
    Writer
    Closer
}
```

### Utilidades
```go
io.Copy(w, r)             // copia de Reader a Writer
io.ReadAll(r)             // lee todo (reemplaza ioutil.ReadAll)
io.NopCloser(r)           // Reader sin Close
io.LimitReader(r, n)      // Reader que solo lee n bytes
io.MultiReader(r1, r2)    // concatena Readers
io.MultiWriter(w1, w2)    // escribe a múltiples Writers
io.Discard                // /dev/null
io.EOF                    // señal de fin de archivo
```

### fs.FS (Go 1.16+)
```go
// Sistema de archivos virtual
type FS interface {
    Open(name string) (File, error)
}

// Implementaciones
os.DirFS("/ruta")         // sistema de archivos real
embed.FS                  // archivos embebidos en binario
```

## embed (Go 1.16+)

Incrusta archivos en el binario compilado.

```go
import "embed"

//go:embed templates/*.html
var templates embed.FS

//go:embed config.yaml
var config []byte

//go:embed logo.png
var logo embed.FS

// Uso
tmpl := template.Must(template.ParseFS(templates, "templates/index.html"))
```

## time — Tiempo y duraciones

```go
now := time.Now()
later := now.Add(2 * time.Hour)
diff := later.Sub(now)           // 2h0m0s

// Formateo (layout es MAGIC: Mon Jan 2 15:04:05 MST 2006 = 1 2 3 4 5 6 -7)
now.Format("2006-01-02 15:04:05")  // "2026-07-07 15:04:05"

// Parsing
t, _ := time.Parse("2006-01-02", "2026-07-07")

// Duraciones
d := 5 * time.Second
d := 100 * time.Millisecond
d := 2*time.Hour + 30*time.Minute

// Timers y Tickers
timer := time.NewTimer(1 * time.Second)
<-timer.C

ticker := time.NewTicker(1 * time.Second)
for range ticker.C {
    fmt.Println("tick")
}

time.AfterFunc(2*time.Second, func() {
    fmt.Println("ejecutado después de 2s")
})
```

## strings / bytes

```go
strings.Contains(s, substr)
strings.HasPrefix(s, prefix)
strings.HasSuffix(s, suffix)
strings.Index(s, substr)
strings.Join([]string{"a", "b"}, ",")
strings.ReplaceAll(s, old, new)
strings.Split(s, sep)
strings.ToLower(s)
strings.ToUpper(s)
strings.TrimSpace(s)
strings.NewReader(s)         // Reader desde string

strings.Builder              // Builder eficiente para concatenación
var b strings.Builder
b.WriteString("hello")
b.WriteString(" world")
result := b.String()

// bytes (análogo a string pero para []byte)
bytes.Contains(b, subslice)
bytes.Equal(a, b)
bytes.Repeat(b, n)
```

## log / log/slog — Logging

### log estándar
```go
log.Println("mensaje")
log.Printf("formato %d", 42)
log.Fatalf("fatal: %v", err)     // log + os.Exit(1)
log.Panicf("panic: %v", err)     // log + panic()
```

### log/slog — Logging estructurado (Go 1.21+)
```go
import "log/slog"

// Logger por defecto
slog.Info("servidor iniciado", "puerto", 8080)
slog.Error("error al conectar", "err", err)

// Logger personalizado
handler := slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{
    Level: slog.LevelDebug,
    AddSource: true,
})
logger := slog.New(handler)
logger.Info("mensaje", "key", "value")
```

## sort

```go
sort.Ints([]int{3, 1, 2})
sort.Strings([]string{"c", "a", "b"})
sort.Slice(s, func(i, j int) bool {
    return s[i].Edad < s[j].Edad
})
sort.Search(n, func(i int) bool { return arr[i] >= x })
```

## flag — Línea de comandos

```go
var (
    port    = flag.Int("port", 8080, "Puerto del servidor")
    verbose = flag.Bool("verbose", false, "Log verbose")
    config  = flag.String("config", "config.yaml", "Archivo de configuración")
)

func main() {
    flag.Parse()
    fmt.Println("Puerto:", *port)
}
```

## regexp

```go
re := regexp.MustCompile(`^[a-z]+@[a-z]+\.[a-z]+$`)
matched := re.MatchString("user@example.com")

re = regexp.MustCompile(`(\d{4})-(\d{2})-(\d{2})`)
matches := re.FindStringSubmatch("Fecha: 2026-07-07")

// Replace
result := re.ReplaceAllString("2026-07-07", "$3/$2/$1")  // "07/07/2026"
```

## slices / maps (Go 1.21+)

```go
import "slices"

slices.Contains(s, val)
slices.Index(s, val)
slices.Delete(s, i, j)
slices.Insert(s, i, vals...)
slices.Replace(s, i, j, vals...)
slices.Compact(s)         // elimina duplicados consecutivos
slices.Sort(s)
slices.Reverse(s)
slices.Clip(s)            // reduce capacidad a longitud
slices.Grow(s, n)         // preasigna capacidad
slices.Equal(a, b)

import "maps"

maps.Clone(m)
maps.Copy(dst, src)
maps.DeleteFunc(m, func(k, v) bool { return v == 0 })
maps.Equal(m1, m2)
```
