# Módulos en Go — Referencia Completa

## Conceptos clave

Un **módulo** es una colección de paquetes versionados y distribuidos juntos. Identificado por un **module path** (ruta del módulo), declarado en `go.mod`.

### Componentes de un módulo
- **go.mod**: Archivo de definición del módulo y sus dependencias
- **go.sum**: Checksums criptográficos de las dependencias (autenticación)
- **Paquetes**: Directorios con archivos `.go` dentro del módulo

## go.mod — Directivas

### `module` — Ruta del módulo
```go
module github.com/usuario/proyecto
```

### `go` — Versión mínima de Go
```go
go 1.23.0
```
Define la versión mínima de Go requerida. Desde Go 1.21+ es obligatoria.

### `toolchain` — Toolchain sugerida
```go
toolchain go1.23.0
```

### `require` — Dependencias
```go
require (
    github.com/gin-gonic/gin v1.9.1
    golang.org/x/text v0.14.0 // indirect
)
```
- `// indirect`: paquete importado por una dependencia, no directamente

### `replace` — Reemplazar dependencias
```go
replace github.com/original/mod => ./local/mod
replace github.com/original/mod v1.2.3 => github.com/fork/mod v1.2.4
```

### `exclude` — Excluir versiones
```go
exclude github.com/flaky/mod v1.0.0
```

### `retract` — Retirar versiones (Go 1.16+)
```go
retract v1.0.0 // publicada accidentalmente
retract [v1.0.0, v1.1.0]
```

### `tool` — Herramientas (Go 1.24+)
```go
tool golang.org/x/tools/cmd/stringer
```

## Versionado semántico (SemVer)

```
vMAJOR.MINOR.PATCH-prerelease+meta
v1.2.3
v1.2.3-beta
v2.0.0
```

- **MAJOR**: cambios incompatibles (v1→v2 requiere /v2 en module path)
- **MINOR**: nuevas funcionalidades (backward compatible)
- **PATCH**: bug fixes (backward compatible)
- **Pre-release**: `v1.0.0-alpha`, `v1.2.3-rc1`

### Major version suffixes
- `v2`+: el module path termina en `/v2`, `/v3`, etc.
- Ejemplo: `module github.com/user/mod/v2`

### Pseudo-versions
Cuando no hay tag semver, Go genera pseudo-versions:
```
v0.0.0-20240101123456-abcdef012345
```
Formato: `vX.0.0-YYYYMMDDHHMMSS-COMMITHASH12`

## Comandos de módulos

### Inicializar un módulo
```bash
go mod init github.com/usuario/proyecto
```

### Agregar dependencias
```bash
go get github.com/gin-gonic/gin@latest
go get github.com/gin-gonic/gin@v1.9.1
go get github.com/gin-gonic/gin@master  # commit específico
```

### Limpiar dependencias
```bash
go mod tidy
```
- Agrega dependencias faltantes
- Elimina dependencias no usadas
- Actualiza go.sum

### Verificar módulos
```bash
go mod verify   # verifica integridad del caché
go mod download # descarga todas las dependencias
go mod why      # explica por qué se necesita un módulo
```

### Vendor
```bash
go mod vendor   # copia dependencias a vendor/
go build -mod=vendor  # compila usando vendor/
```

## Workspaces (Go 1.18+)

Los workspaces permiten trabajar con múltiples módulos simultáneamente.

```bash
go work init ./modulo1 ./modulo2
```

### go.work
```go
go 1.23.0

use (
    ./modulo1
    ./modulo2
)

replace example.com/old => ./local/fork
```

## GOPROXY y privacidad

```bash
# Proxy público
go env -w GOPROXY=https://proxy.golang.org,direct

# Sin proxy (para módulos privados internos)
go env -w GONOPROXY=*.internal.company.com
go env -w GOPRIVATE=*.internal.company.com

# Sin checksum database
go env -w GONOSUMDB=*.internal.company.com
```

## Resolución de dependencias (MVS)

Go usa **Minimal Version Selection (MVS)**:
- No hay conflicto de versiones (a diferencia de npm/Maven)
- Se usa la VERSIÓN MÁS ALTA requerida por cualquier dependencia
- Todos los builds son deterministas

## Buenas prácticas con módulos

1. **Siempre inicializa con `go mod init`** para cada proyecto
2. **Corre `go mod tidy`** antes de commit
3. **No edites go.mod a mano** (usa `go get`, `go mod tidy`, `go mod edit`)
4. **Versiona semánticamente** si publicas un módulo
5. **Usa `/v2`, `/v3`** para breaking changes
6. **Prefiere `go get pkg@version`** sobre `replace` en go.mod
7. **Usa workspaces** para desarrollo multi-módulo local
8. **Revisa vulnerabilidades**: `govulncheck ./...`
