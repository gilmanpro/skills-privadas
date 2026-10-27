# Tooling de Go — Referencia

## go command — Principales subcomandos

### Compilación y ejecución
```bash
go build ./...         # compila todo (sin generar binario para paquetes)
go build -o app .      # compila y genera binario
go run .               # compila y ejecuta (útil para desarrollo)
go run main.go         # ejecuta un archivo específico
go install .           # compila e instala en GOBIN
go clean -cache        # limpia caché de compilación
go clean -modcache     # limpia caché de módulos
go clean -testcache    # limpia caché de tests
```

### Flags de compilación útiles
```bash
go build -ldflags="-X main.version=1.0.0 -s -w" .  # inyectar vars + strip
go build -tags=production .                        # build tags
go build -race .                                   # detector de data races
go build -msan .                                   # detector de MemorySanitizer
go build -asan .                                   # detector de AddressSanitizer
go build -trimpath .                               # rutas limpias en binarios
```

### Testing
```bash
go test ./...                 # todos los tests
go test -v ./...              # verbose
go test -run TestName ./...   # filtrar por nombre
go test -count=1 ./...        # sin cache (fuerza re-ejecución)
go test -race ./...           # con race detector
go test -bench=. ./...        # benchmarks
go test -fuzz=Fuzz ./...      # fuzzing
go test -cover ./...          # cobertura
go test -coverprofile=coverage.out ./...
go test -shuffle=on ./...     # orden aleatorio (Go 1.17+)
```

### Análisis estático
```bash
go vet ./...                  # análisis básico
go vet -vettool=$(which shadow) ./...  # variable shadowing
```

### Formateo
```bash
gofmt -w archivo.go          # formatea y guarda
gofmt -d archivo.go          # muestra diff
go fmt ./...                 # gofmt en todo el módulo
gofmt -s archivo.go          # simplifica código
```

## gopls — Language Server Protocol

Instalación: `go install golang.org/x/tools/gopls@latest`

Características:
- Autocompletado
- Ir a definición
- Buscar referencias
- Renombrar símbolos
- Diagnósticos en tiempo real
- Documentación al hover
- Refactorización
- Importación automática

Configuración recomendada (VSCode settings.json):
```json
{
  "go.useLanguageServer": true,
  "gopls": {
    "ui.semanticTokens": true,
    "ui.completion.usePlaceholders": true,
    "ui.completion.matcher": "fuzzy",
    "ui.diagnostic.staticcheck": true,
    "analyses": {
      "unusedparams": true,
      "unusedvariable": true,
      "shadow": true
    },
    "codelenses": {
      "gc_details": true,
      "run_govulncheck": true,
      "tidy": true
    },
    "build.buildFlags": ["-tags=integration"]
  }
}
```

## Delve — Debugger

Instalación: `go install github.com/go-delve/delve/cmd/dlv@latest`

### Comandos principales
```bash
dlv debug .                           # debuggear paquete actual
dlv debug main.go                     # debuggear archivo específico
dlv test ./...                         # debuggear tests
dlv attach PID                        # adjuntar a proceso
dlv core <executable> <core>          # analizar core dump
dlv exec ./binario                    # debuggear binario existente
```

### Comandos dentro de Delve
```
break main.go:42          # breakpoint
break pkg.FuncName        # breakpoint en función
continue                  # continuar ejecución
next                      # siguiente línea
step                      # entrar en función
stepout                   # salir de función
print variable            # imprimir variable
locals                    # variables locales
stack                     # stack trace
goroutines                # listar goroutines
threads                   # listar hilos
restart                   # reiniciar
```

## Profiling (pprof)

### CPU profiling
```go
import "runtime/pprof"

f, _ := os.Create("cpu.prof")
pprof.StartCPUProfile(f)
defer pprof.StopCPUProfile()
```

### Memory profiling
```go
f, _ := os.Create("mem.prof")
pprof.WriteHeapProfile(f)
f.Close()
```

### Análisis de profiles
```bash
go tool pprof cpu.prof
(pprof) top10              # top funciones
(pprof) web                # gráfico en navegador
(pprof) list FuncName      # código fuente con tiempos
(pprof) peek FuncName      # callers y callees

# Profiling web (net/http/pprof)
import _ "net/http/pprof"
# Luego: http://localhost:6060/debug/pprof/
```

### Benchmarks con profiling
```bash
go test -bench=. -cpuprofile=cpu.prof -memprofile=mem.prof
```

## Tracing (runtime/trace)

```go
import "runtime/trace"

f, _ := os.Create("trace.out")
trace.Start(f)
defer trace.Stop()
```

Análisis:
```bash
go tool trace trace.out
```

## Cobertura de código

```bash
go test -coverprofile=coverage.out ./...
go tool cover -html=coverage.out     # HTML navegable
go tool cover -func=coverage.out     # resumen por función
```

## govulncheck — Vulnerabilidades

Instalación: `go install golang.org/x/vuln/cmd/govulncheck@latest`

```bash
govulncheck ./...
```

## go generate

Genera código a través de directivas en comentarios:
```go
//go:generate stringer -type=Pill
type Pill int
```

```bash
go generate ./...
```

## GOFLAGS y entornos comunes

```bash
# GOFLAGS persistentes
go env -w GOFLAGS="-mod=mod -count=1"

# Cross-compilation
GOOS=linux GOARCH=amd64 go build .
GOOS=windows GOARCH=amd64 go build .
GOOS=darwin GOARCH=arm64 go build .

# Sin cgo (para builds estáticos)
CGO_ENABLED=0 go build .
```

## Variables de entorno clave

| Variable | Default | Descripción |
|---|---|---|
| `GOROOT` | `C:\Go` o `/usr/local/go` | Directorio de instalación de Go |
| `GOPATH` | `$HOME/go` | Workspace de Go |
| `GOMODCACHE` | `$GOPATH/pkg/mod` | Caché de módulos |
| `GOBIN` | `$GOPATH/bin` | Destino de `go install` |
| `GOOS` | SO actual | OS target para cross-compile |
| `GOARCH` | arquitectura | Arquitectura target |
| `GOPROXY` | `https://proxy.golang.org,direct` | Proxy de módulos |
| `CGO_ENABLED` | `1` | Habilitar cgo |
| `GONOSUMCHECK` | - | Módulos sin checksum |
| `GONOPROXY` | - | Módulos sin proxy |
| `GOFLAGS` | - | Flags persistentes |

## Herramientas de la comunidad

| Herramienta | Instalación | Propósito |
|---|---|---|
| `gopls` | `go install golang.org/x/tools/gopls@latest` | LSP |
| `staticcheck` | `go install honnef.co/go/tools/cmd/staticcheck@latest` | Análisis estático avanzado |
| `golangci-lint` | `go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest` | Linter multi-herramienta |
| `gofumpt` | `go install mvdan.cc/gofumpt@latest` | Formateo más estricto |
| `dlv` | `go install github.com/go-delve/delve/cmd/dlv@latest` | Debugger |
| `govulncheck` | `go install golang.org/x/vuln/cmd/govulncheck@latest` | Vulnerabilidades |
| `gotests` | `go install github.com/cweill/gotests/gotests@latest` | Generar tests |
| `mockgen` | `go install go.uber.org/mock/mockgen@latest` | Generar mocks |
| `stringer` | `go install golang.org/x/tools/cmd/stringer@latest` | Generar String() |
| `swag` | `go install github.com/swaggo/swag/cmd/swag@latest` | Documentación API |
