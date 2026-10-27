# Dockerfile — Referencia completa de instrucciones

## Instrucciones soportadas

| Instrucción | Descripción |
|-------------|-------------|
| `FROM` | Crear nueva etapa de build desde una imagen base |
| `RUN` | Ejecutar comandos durante el build |
| `CMD` | Comando por defecto al ejecutar el contenedor |
| `ENTRYPOINT` | Ejecutable por defecto del contenedor |
| `COPY` | Copiar archivos/directorios |
| `ADD` | Añadir archivos locales o remotos |
| `ENV` | Variables de entorno |
| `ARG` | Variables de build-time |
| `EXPOSE` | Documentar puertos |
| `WORKDIR` | Cambiar directorio de trabajo |
| `USER` | Usuario/GID para ejecución |
| `VOLUME` | Crear punto de montaje |
| `LABEL` | Metadata de la imagen |
| `HEALTHCHECK` | Healthcheck del contenedor |
| `SHELL` | Cambiar shell por defecto |
| `STOPSIGNAL` | Señal para detener el contenedor |
| `ONBUILD` | Instrucciones diferidas para builds hijos |

## FROM

```dockerfile
FROM [--platform=<platform>] <image> [AS <name>]
FROM [--platform=<platform>] <image>[:<tag>] [AS <name>]
FROM [--platform=<platform>] <image>[@<digest>] [AS <name>]
```

- `--platform`: Forzar plataforma (ej: `linux/amd64`, `linux/arm64`)
- `AS <name>`: Nombrar la etapa para usar en multi-stage
- Debe ser la primera instrucción (excepto ARG y parser directives)
- Si no se especifica tag, usa `latest`
- Múltiples FROM permiten multi-stage builds

## RUN

```dockerfile
# Shell form (usa el shell por defecto)
RUN <command> ...
# Exec form (no shell, array JSON)
RUN ["<executable>", "<arg>", ...]
```

### Opciones avanzadas de RUN

**`RUN --mount=type=bind`** — Montar archivos/directorios en build (solo lectura por defecto)
| Opción | Descripción |
|--------|-------------|
| `target`, `dst`, `destination` | Ruta de montaje |
| `source` | Ruta origen en `from` (default: root) |
| `from` | Build stage, contexto o imagen de origen |
| `rw`, `readwrite` | Permitir escritura (se descarta al final) |

**`RUN --mount=type=cache`** — Cachear directorios entre builds
| Opción | Descripción |
|--------|-------------|
| `id` | ID para identificar el cache |
| `target` | Ruta de montaje |
| `ro`, `readonly` | Solo lectura |
| `sharing` | `shared` (default), `private`, `locked` |
| `from` | Stage, contexto o imagen base |
| `source` | Subpath en from |
| `mode` | Modo octal (default `0755`) |
| `uid` | User ID (default `0`) |
| `gid` | Group ID (default `0`) |

**`RUN --mount=type=tmpfs`** — Montar tmpfs
| Opción | Descripción |
|--------|-------------|
| `target` | Ruta de montaje |
| `size` | Tamaño máximo |

**`RUN --mount=type=secret`** — Acceder a secretos sin incluirlos en la imagen
| Opción | Descripción |
|--------|-------------|
| `id` | ID del secreto |
| `target` | Ruta destino (default: `/run/secrets/<id>`) |
| `env` | Variable de entorno en vez de archivo |
| `required` | `true` = error si no disponible |
| `mode` | Modo octal (default `0400`) |
| `uid` | User ID (default `0`) |
| `gid` | Group ID (default `0`) |

**`RUN --mount=type=ssh`** — Acceder a SSH agent
| Opción | Descripción |
|--------|-------------|
| `id` | ID del SSH agent (default: `default`) |
| `target` | Socket path |
| `required` | `true` = error si no disponible |
| `mode` | Modo octal (default `0600`) |
| `uid` | User ID (default `0`) |
| `gid` | Group ID (default `0`) |

**`RUN --network=<TYPE>`**
- `default`: Red normal
- `none`: Sin acceso a red
- `host`: Red del host

**`RUN --security=<sandbox|insecure>`**
- `sandbox`: Modo seguro (default)
- `insecure`: Sin sandbox (como `--privileged`)

**`RUN --device=<name>[required]`** — Solicitar CDI devices (labs syntax)

## CMD

```dockerfile
# Exec form (preferida)
CMD ["<executable>", "<arg>", ...]
# Default args para ENTRYPOINT
CMD ["<arg1>", "<arg2>", ...]
# Shell form
CMD <command> <arg> ...
```

- Solo un CMD por Dockerfile (el último prevalece)
- Proporciona defaults para el contenedor
- Se puede sobrescribir con `docker run <image> <command>`

## ENTRYPOINT

```dockerfile
# Exec form (preferida)
ENTRYPOINT ["<executable>", "<arg>", ...]
# Shell form
ENTRYPOINT <command> <arg> ...
```

- Configura el contenedor como ejecutable
- Con exec form, CMD provee argumentos default
- Se puede sobrescribir con `docker run --entrypoint`

## COPY

```dockerfile
COPY [--chown=<user>:<group>] [--from=<stage>] <src>... <dest>
COPY [--chown=<user>:<group>] [--from=<stage>] ["<src>", ..., "<dest>"]
```

- `--chown`: Cambiar owner (solo Linux)
- `--from`: Copiar desde otra build stage o contexto externo
- `--link`: Usar hard links para copias más eficientes
- `<src>` puede ser relativo al build context
- Soporta glob patterns (`.dockerignore` aplica)

## ADD

```dockerfile
ADD [--chown=<user>:<group>] <src>... <dest>
ADD [--chown=<user>:<group>] ["<src>", ..., "<dest>"]
```

- Igual que COPY pero adicionalmente:
  - Soporta URLs como source
  - Auto-extrae tar archives locales
- **NO recomendado** para URLs (mejor usar RUN curl/wget)
- Usar COPY por defecto, ADD solo cuando sea necesario

## ENV

```dockerfile
ENV <key>=<value> [<key>=<value>...]
ENV <key> <value>   # Sintaxis alternativa (menos usada)
```

- Persisten en el contenedor al ejecutarlo
- Se pueden sobrescribir con `docker run -e`
- Soportan `${variable}` substitution en otras instrucciones

## ARG

```dockerfile
ARG <name>[=<default>]
ARG <name> <name>...
```

- Solo disponibles durante build, NO en contenedor final
- Se pasan con `docker build --build-arg <name>=<value>`
- Tienen valores default opcionales
- Built-in args: `TARGETPLATFORM`, `TARGETOS`, `TARGETARCH`, `TARGETVARIANT`, `BUILDPLATFORM`, `BUILDOS`, `BUILDARCH`, `BUILDVARIANT`

## EXPOSE

```dockerfile
EXPOSE <port>[/<protocol>]
EXPOSE 80
EXPOSE 80/udp
EXPOSE 80/tcp 80/udp
```

- Solo documentación, NO publica puertos
- Protocolo default: TCP

## WORKDIR

```dockerfile
WORKDIR <path>
```

- Cambia directorio de trabajo para RUN, CMD, ENTRYPOINT, COPY, ADD siguientes
- Crea el directorio si no existe
- Se puede usar múltiples veces, rutas relativas son relativas al WORKDIR anterior

## USER

```dockerfile
USER <user>[:<group>]
USER <uid>[:<gid>]
USER <user|uid>
```

- Usuario para RUN, CMD, ENTRYPOINT siguientes
- Buenas prácticas: crear usuario específico (no root)

## VOLUME

```dockerfile
VOLUME ["<path>", ...]
VOLUME <path> [<path>...]
```

- Crea punto de montaje en tiempo de ejecución
- Docker gestiona el volumen automáticamente

## LABEL

```dockerfile
LABEL <key>=<value> [<key>=<value>...]
LABEL "com.example.vendor"="ACME Incorporated"
LABEL version="1.0"
```

- Metadata en formato clave=valor
- Se heredan de imágenes base
- Se ven con `docker image inspect`

## HEALTHCHECK

```dockerfile
HEALTHCHECK [OPTIONS] CMD <command>
HEALTHCHECK NONE    # Deshabilitar healthcheck de la imagen base
```

Opciones:
| Opción | Descripción | Default |
|--------|-------------|---------|
| `--interval=<duration>` | Tiempo entre checks | `30s` |
| `--timeout=<duration>` | Timeout por check | `30s` |
| `--start-period=<duration>` | Periodo de gracia inicial | `0s` |
| `--retries=<n>` | Fallos consecutivos para unhealthy | `3` |

Comando debe devolver 0 (healthy) o 1 (unhealthy).

## SHELL

```dockerfile
SHELL ["<executable>", "<param>", ...]
SHELL ["/bin/bash", "-c"]     # Default Linux
SHELL ["powershell", "-Command"]  # Windows
```

- Cambia el shell para RUN, CMD, ENTRYPOINT en shell form

## STOPSIGNAL

```dockerfile
STOPSIGNAL <signal>
STOPSIGNAL SIGTERM    # Default
STOPSIGNAL SIGQUIT
```

## ONBUILD

```dockerfile
ONBUILD <INSTRUCTION>
ONBUILD ADD . /app/src
ONBUILD RUN bundle install
```

- Instrucciones que se ejecutan cuando esta imagen se usa como FROM en otro build

## Parser Directives

Deben ir al inicio del Dockerfile (antes de cualquier comentario o instrucción):

```dockerfile
# syntax=docker/dockerfile:1
# escape=\
# check=skip=<check-name>
```

- `# syntax=docker/dockerfile:1`: Usa la última versión estable del syntax
- `# escape=\`: Cambia caracter de escape
- `# check=skip=<name>`: Salta checks específicos

## Environment replacement

```dockerfile
${variable_name}       # Sintaxis básica
${variable:-word}      # Default si no está set o está vacía
${variable-word}       # Default si no está set
${variable:+word}      # word si variable está set y no vacía
${variable+word}       # word si variable está set
```

## Ejemplos

### Node.js app optimizada

```dockerfile
# syntax=docker/dockerfile:1
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm \
    npm ci --only=production

FROM node:20-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

FROM node:20-alpine AS runner
WORKDIR /app
RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 appuser
COPY --from=builder /app/dist ./dist
COPY --from=deps /app/node_modules ./node_modules
USER appuser
EXPOSE 3000
ENV NODE_ENV=production
CMD ["node", "dist/index.js"]
```

### Python app

```dockerfile
FROM python:3.12-slim
WORKDIR /app
RUN adduser --system --uid 1001 appuser
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt
COPY . .
USER appuser
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0"]
```

### Go app multi-stage

```dockerfile
# syntax=docker/dockerfile:1
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-w -s" -o /server .

FROM alpine:3.20
RUN apk add --no-cache ca-certificates tzdata
RUN adduser -D -u 1001 appuser
COPY --from=builder /server /server
USER appuser
EXPOSE 8080
CMD ["/server"]
```

### Build con secretos y SSH

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.12-slim AS builder
WORKDIR /app
# Clonar repo privado con SSH
RUN --mount=type=ssh \
    mkdir -p -m 0600 ~/.ssh && \
    ssh-keyscan github.com >> ~/.ssh/known_hosts && \
    git clone git@github.com:user/private-repo.git .

# Usar secreto para API key
RUN --mount=type=secret,id=api_key \
    API_KEY=$(cat /run/secrets/api_key) ./deploy.sh
```
