# Testing en Go — Referencia

## Filosofía

Go tiene testing como ciudadano de primera clase. No necesitas frameworks externos — la stdlib incluye pruebas unitarias, benchmarks, fuzzing, cobertura, y más.

## Tests Unitarios

### Estructura básica
```go
// archivo: math.go
package math

func Add(a, b int) int { return a + b }

// archivo: math_test.go (mismo paquete)
package math

import "testing"

func TestAdd(t *testing.T) {
    result := Add(2, 3)
    if result != 5 {
        t.Errorf("Add(2, 3) = %d; want 5", result)
    }
}
```

### Convenciones
- Archivo: `*_test.go`
- Función: `TestXxx(t *testing.T)`
- `t.Error()` / `t.Errorf()` — falla pero continúa
- `t.Fatal()` / `t.Fatalf()` — falla y detiene el test
- `t.Log()` / `t.Logf()` — log condicional (solo con `-v`)

### Table-Driven Tests (MUY idiomático)
```go
func TestDivide(t *testing.T) {
    tests := []struct {
        name     string
        a, b     float64
        want     float64
        wantErr  bool
    }{
        {name: "división normal",      a: 10, b: 2, want: 5, wantErr: false},
        {name: "división por cero",    a: 10, b: 0, want: 0, wantErr: true},
        {name: "números negativos",    a: -6, b: 3, want: -2, wantErr: false},
        {name: "resultado decimal",    a: 7,  b: 2, want: 3.5, wantErr: false},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got, err := Divide(tt.a, tt.b)
            if (err != nil) != tt.wantErr {
                t.Errorf("Divide() error = %v, wantErr %v", err, tt.wantErr)
                return
            }
            if got != tt.want {
                t.Errorf("Divide() = %v, want %v", got, tt.want)
            }
        })
    }
}
```

### Test helpers
```go
func TestUserCreation(t *testing.T) {
    db := setupTestDB(t)
    defer db.Close()

    user := createTestUser(t, db, "test@example.com")
    // ...
}

func setupTestDB(t *testing.T) *sql.DB {
    t.Helper()  // marca como helper (el error se reporta en la línea del caller)
    db, err := sql.Open("sqlite3", ":memory:")
    if err != nil {
        t.Fatalf("setup db: %v", err)
    }
    return db
}

func createTestUser(t *testing.T, db *sql.DB, email string) User {
    t.Helper()
    // ...
}
```

### Cleanup (t.Cleanup)
```go
func TestWithCleanup(t *testing.T) {
    tmpDir := t.TempDir()  // cleanup automático
    
    srv := httptest.NewServer(handler)
    t.Cleanup(func() {
        srv.Close()  // se ejecuta cuando el test termina
    })
    
    // usar srv.URL para hacer peticiones
}
```

### Subtests
```go
func TestTeam(t *testing.T) {
    t.Run("A", func(t *testing.T) { /* ... */ })
    t.Run("B", func(t *testing.T) { /* ... */ })
    t.Run("C", func(t *testing.T) { /* ... */ })
}
// Ejecutar subset: go test -run 'TestTeam/A'
```

### TestMain (setup global)
```go
func TestMain(m *testing.M) {
    // setup global (abrir DB, iniciar servidor, etc.)
    code := m.Run()   // ejecuta todos los tests
    // teardown
    os.Exit(code)
}
```

## Cobertura de código

```bash
go test -cover ./...
go test -coverprofile=coverage.out ./...
go tool cover -html=coverage.out
go tool cover -func=coverage.out
```

## Benchmarks

```go
func BenchmarkAdd(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Add(2, 3)
    }
}
```

### Reset Timer
```go
func BenchmarkProcess(b *testing.B) {
    data := loadLargeData()  // setup no se mide
    b.ResetTimer()
    
    for i := 0; i < b.N; i++ {
        Process(data)
    }
}
```

### Benchmarks con profiling
```bash
go test -bench=. -benchmem -cpuprofile=cpu.prof -memprofile=mem.prof ./...
```

## Fuzzing (Go 1.18+)

```go
func FuzzHex(f *testing.F) {
    // Seeds (casos de ejemplo)
    f.Add([]byte("hello"))
    f.Add([]byte(""))
    f.Add([]byte("!@#$%"))

    f.Fuzz(func(t *testing.T, data []byte) {
        encoded := hex.EncodeToString(data)
        decoded, err := hex.DecodeString(encoded)
        if err != nil {
            t.Errorf("DecodeString(%q) = %v", encoded, err)
        }
        if !bytes.Equal(data, decoded) {
            t.Errorf("round-trip: got %v, want %v", decoded, data)
        }
    })
}
```

```bash
go test -fuzz=FuzzHex -fuzztime=30s
```

## httptest — Testing de HTTP

```go
func TestHandler(t *testing.T) {
    handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        w.Write([]byte(`{"status":"ok"}`))
    })

    // Crear servidor de prueba
    server := httptest.NewServer(handler)
    defer server.Close()

    resp, err := http.Get(server.URL + "/test")
    if err != nil {
        t.Fatal(err)
    }
    defer resp.Body.Close()

    body, _ := io.ReadAll(resp.Body)
    if string(body) != `{"status":"ok"}` {
        t.Errorf("got %s, want ok", body)
    }
}

// ResponseRecorder (sin servidor, más rápido)
func TestHandlerDirect(t *testing.T) {
    req := httptest.NewRequest("GET", "/", nil)
    w := httptest.NewRecorder()
    
    myHandler(w, req)
    
    resp := w.Result()
    body, _ := io.ReadAll(resp.Body)
    
    if resp.StatusCode != http.StatusOK {
        t.Errorf("status = %d, want %d", resp.StatusCode, http.StatusOK)
    }
}
```

## testify/assert (framework popular)

```go
import "github.com/stretchr/testify/assert"

func TestSomething(t *testing.T) {
    assert.Equal(t, 123, result)
    assert.NotNil(t, obj)
    assert.Error(t, err)
    assert.NoError(t, err)
    assert.True(t, condition)
    assert.Contains(t, str, "substring")
    assert.Len(t, slice, 5)
    assert.JSONEq(t, `{"a":1}`, `{"a":1}`)
}

// require (detiene el test si falla)
import "github.com/stretchr/testify/require"
require.NoError(t, err)
```

## Mocks

### Con testify/mock
```go
type MockRepository struct {
    mock.Mock
}

func (m *MockRepository) GetUser(id int) (User, error) {
    args := m.Called(id)
    return args.Get(0).(User), args.Error(1)
}

func TestService(t *testing.T) {
    repo := new(MockRepository)
    repo.On("GetUser", 1).Return(User{ID: 1, Name: "Ana"}, nil)
    
    svc := NewService(repo)
    user, err := svc.GetUser(1)
    
    assert.NoError(t, err)
    assert.Equal(t, "Ana", user.Name)
    repo.AssertExpectations(t)
}
```

### Con go.uber.org/mock (anteriormente golang/mock)
```bash
go install go.uber.org/mock/mockgen@latest
mockgen -source=repository.go -destination=mock_repository.go -package=mocks
```

## Integration Tests con build tags

```go
// archivo: handler_test.go
//go:build integration

package handler_test

func TestIntegration(t *testing.T) {
    if testing.Short() {
        t.Skip("saltando test de integración")
    }
    // test que requiere DB real...
}
```

```bash
# Solo tests unitarios
go test -short ./...

# Tests unitarios + integración
go test -tags=integration ./...
```

## Golden Files (para tests de archivos generados)

```go
func TestGenerateConfig(t *testing.T) {
    got := generateConfig()
    
    // escribir golden file
    // t更新: go test -update
    golden := filepath.Join("testdata", "config.golden")
    
    if *update {
        os.WriteFile(golden, got, 0644)
    }
    
    expected, _ := os.ReadFile(golden)
    if !bytes.Equal(got, expected) {
        t.Errorf("config mismatch")
    }
}
```

## Ejecución de tests

```bash
go test ./...                           # todo el módulo
go test -v ./...                        # verbose
go test -run TestName                   # filtrar por nombre
go test -count=1 ./...                  # sin cache
go test -race ./...                     # con race detector
go test -shuffle=on ./...               # orden aleatorio
go test -short ./...                    # saltar tests lentos
go test -v -run 'TestA/TestB' ./...     # subtests específicos
go test -timeout 30s ./...              # timeout global
go test -parallel 4 ./...               # paralelismo
```

## Cobertura avanzada

```go
// Excluir código del reporte de cobertura
//go:build !testcoverage

// En go.mod
tool -coverpkg=./...
```

```bash
go test -covermode=atomic -coverprofile=coverage.out ./...
go tool cover -html=coverage.out -o coverage.html
```
