# Otros comandos Docker — Referencia

## docker build / docker buildx build

**Uso:** `docker buildx build [OPTIONS] PATH | URL | -`

### Opciones principales
| Flag | Descripción |
|------|-------------|
| `-t, --tag <name>:<tag>` | Etiquetar imagen (formato: `[registry/]repository[:tag]`) |
| `-f, --file <path>` | Dockerfile personalizado |
| `--target <stage>` | Build target en multi-stage |
| `--build-arg <key>=<value>` | Variables build-time |
| `--build-context <name>=<path>` | Contexto adicional de build |
| `--platform <os/arch>` | Plataforma objetivo (ej: `linux/amd64,linux/arm64`) |
| `--load` | Cargar imagen a `docker images` (output type=docker) |
| `--push` | Pushear a registry (output type=registry) |
| `-o, --output <type>` | Tipo de output: `local`, `tar`, `oci`, `docker`, `image`, `registry` |
| `--cache-from <ref>` | Fuente de cache externa |
| `--cache-to <ref>` | Destino de cache externa |
| `--no-cache` | No usar cache |
| `--no-cache-filter <stages>` | No cachear stages específicos |
| `--pull` | Forzar pull de todas las imágenes referenciadas |
| `--progress <type>` | Output: `auto`, `plain`, `tty`, `quiet`, `rawjson` |
| `--secret <id>=<src>` | Exponer secreto al build |
| `--ssh <id>=<socket>` | Exponer SSH agent al build |
| `--add-host <host:ip>` | Añadir entrada a /etc/hosts |
| `--label <key>=<value>` | Metadata de la imagen |
| `--iidfile <file>` | Escribir ID de imagen a archivo |
| `--metadata-file <file>` | Escribir metadata de build a archivo |
| `--network <mode>` | Red para RUN durante build: `default`, `none`, `host` |
| `--shm-size <bytes>` | Tamaño de shared memory |
| `--ulimit <type>=<soft>[:<hard>]` | Ulimit options |
| `--cgroup-parent <path>` | Parent cgroup |
| `--attest type=<type>` | Atestaciones: `sbom`, `provenance` |
| `--sbom` | Shorthand para `--attest=type=sbom` |
| `--provenance` | Shorthand para `--attest=type=provenance` |
| `--check` | Validar Dockerfile sin construir |
| `--call <method>` | Frontend method: `build`, `check`, `outline`, `targets` |
| `--allow <entitlement>` | Entitlement extra: `network.host`, `security.insecure` |
| `--annotation <key>=<value>` | Añadir annotation OCI |
| `-q, --quiet` | Solo mostrar ID de imagen al final |

### Ejemplos

```bash
# Build básico
docker build -t myapp:latest .

# Build con tag múltiple y no-cache
docker build -t myapp:latest -t myapp:v1.0 --no-cache .

# Multi-platform build
docker buildx build --platform linux/amd64,linux/arm64 -t user/myapp:latest --push .

# Build con build args
docker build --build-arg NODE_ENV=production -t myapp:latest .

# Build con secretos
docker buildx build --secret id=api_key,src=./api_key.txt -t myapp:latest .

# Build con SSH agent
docker buildx build --ssh default=$SSH_AUTH_SOCK -t myapp:latest .
```

## docker exec

**Uso:** `docker exec [OPTIONS] CONTAINER COMMAND [ARG...]`

### Opciones
| Flag | Descripción |
|------|-------------|
| `-d, --detach` | Ejecutar en background |
| `-i, --interactive` | Mantener STDIN abierto |
| `-t, --tty` | Asignar pseudo-TTY |
| `-u, --user <name\|uid>[:<group\|gid>]` | Usuario |
| `-w, --workdir <path>` | Directorio de trabajo |
| `-e, --env <key>=<value>` | Variables de entorno |
| `--env-file <file>` | Archivo de variables |
| `--privileged` | Escalar privilegios para el comando |
| `--detach-keys <key>` | Override tecla de detach |

### Ejemplos

```bash
# Shell interactivo
docker exec -it mi-container bash
docker exec -it mi-container sh

# Comando en background
docker exec -d mi-container touch /tmp/hecho

# Comando con env temporal
docker exec -e DEBUG=true mi-container ./deploy.sh

# Como otro usuario
docker exec -u appuser mi-container whoami
```

## docker logs

**Uso:** `docker logs [OPTIONS] CONTAINER`

### Opciones
| Flag | Descripción |
|------|-------------|
| `-f, --follow` | Seguir output en tiempo real |
| `-n, --tail <n>` | Mostrar últimas N líneas (default: `all`) |
| `-t, --timestamps` | Mostrar timestamps RFC3339Nano |
| `--since <timestamp>` | Logs desde timestamp (ej: `2024-01-01T00:00:00Z`, `42m`) |
| `--until <timestamp>` | Logs hasta timestamp |
| `--details` | Mostrar detalles extra del log driver |

### Ejemplos

```bash
# Últimas 100 líneas
docker logs --tail 100 mi-container

# Follow en tiempo real
docker logs -f mi-container

# Logs de los últimos 30 minutos
docker logs --since 30m mi-container

# Rango temporal
docker logs --since "2024-01-01T00:00:00Z" --until "2024-01-02T00:00:00Z" mi-container

# Con timestamps
docker logs -t -f mi-container
```

## docker ps

**Uso:** `docker ps [OPTIONS]`
**Alias:** `docker container ls`, `docker container ps`

### Opciones
| Flag | Descripción |
|------|-------------|
| `-a, --all` | Todos los contenedores (no solo running) |
| `-f, --filter <key=value>` | Filtrar (id, name, label, exited, status, ancestor, before, since, volume, network, publish, expose, health, isolation) |
| `--format <template>` | Formato output: `table`, `json`, Go template |
| `-n, --last <n>` | Últimos N contenedores creados |
| `-l, --latest` | Último contenedor creado |
| `--no-trunc` | No truncar output |
| `-q, --quiet` | Solo IDs |
| `-s, --size` | Mostrar tamaño en disco |

### Filtros comunes
| Filtro | Ejemplo |
|--------|---------|
| `name` | `--filter name=myapp` |
| `status` | `--filter status=running`, `exited`, `paused` |
| `ancestor` | `--filter ancestor=nginx:alpine` |
| `exited` | `--filter exited=0` (exit code) |
| `label` | `--filter label=com.example.vendor=ACME` |
| `volume` | `--filter volume=myvolume` |
| `network` | `--filter network=mynet` |

### Placeholders --format
| Placeholder | Descripción |
|-------------|-------------|
| `.ID` | Container ID |
| `.Image` | Image ID |
| `.Command` | Comando |
| `.CreatedAt` | Fecha creación |
| `.RunningFor` | Tiempo desde que corre |
| `.Ports` | Puertos expuestos |
| `.State` | Estado |
| `.Status` | Estado con detalle |
| `.HealthStatus` | Healthcheck status |
| `.Size` | Tamaño en disco |
| `.Names` | Nombre(s) |
| `.Labels` | Labels |
| `.Mounts` | Volúmenes montados |
| `.Networks` | Redes conectadas |

### Ejemplos

```bash
# Todos los contenedores
docker ps -a

# Running + filtro por nombre
docker ps --filter name=myapp

# Solo IDs
docker ps -q

# Formato personalizado
docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Status}}"

# JSON
docker ps --format json

# Contenedores con volumen específico
docker ps -a --filter volume=my_volume

# Contenedores con error
docker ps -a --filter exited=1
```

## docker network

### docker network create
**Uso:** `docker network create [OPTIONS] NETWORK`

| Flag | Descripción |
|------|-------------|
| `-d, --driver <driver>` | Driver: `bridge` (default), `overlay`, `macvlan`, `ipvlan`, `none` |
| `--subnet <cidr>` | Subred (ej: `172.20.0.0/16`) |
| `--gateway <ip>` | Gateway (ej: `172.20.0.1`) |
| `--ip-range <cidr>` | Rango para asignar IPs |
| `--aux-address <name=ip>` | Direcciones auxiliares |
| `--ipv6` | Habilitar IPv6 |
| `--internal` | Red interna (sin acceso externo) |
| `--attachable` | Permitir attach manual (swarm) |
| `--label <key>=<value>` | Metadata |
| `-o, --opt <key>=<value>` | Opciones del driver |
| `--scope <scope>` | `local` (default), `swarm` |
| `--ingress` | Red de routing-mesh (swarm) |
| `--config-from <network>` | Copiar configuración de otra red |
| `--config-only` | Solo configuración (sin instanciar) |

Opciones de driver para bridge:
- `com.docker.network.bridge.name=<name>` — Nombre del bridge Linux
- `com.docker.network.bridge.enable_ip_masquerade=<bool>` — IP masquerading
- `com.docker.network.bridge.enable_icc=<bool>` — Inter-container connectivity
- `com.docker.network.bridge.host_binding_ipv4=<ip>` — Default IP binding
- `com.docker.network.driver.mtu=<n>` — MTU

### Otros comandos de red
| Comando | Descripción |
|---------|-------------|
| `docker network ls` | Listar redes |
| `docker network inspect <name>` | Inspeccionar red |
| `docker network connect <net> <container>` | Conectar contenedor a red |
| `docker network disconnect <net> <container>` | Desconectar contenedor |
| `docker network rm <name>` | Eliminar red |
| `docker network prune` | Eliminar redes no usadas |

### Ejemplos

```bash
# Red bridge personalizada
docker network create --driver bridge --subnet 172.20.0.0/16 my-network

# Red overlay para swarm
docker network create -d overlay --attachable my-swarm-net

# Red interna (sin internet)
docker network create --internal --subnet 10.0.0.0/24 internal-net

# Conectar contenedor
docker network connect my-network mi-container
docker network connect --alias api my-network mi-container

# Bridge con MTU personalizado
docker network create -o com.docker.network.driver.mtu=1450 my-mtu-net
```

## docker volume

### docker volume create
**Uso:** `docker volume create [OPTIONS] [VOLUME]`

| Flag | Descripción |
|------|-------------|
| `-d, --driver <driver>` | Driver (default: `local`) |
| `--label <key>=<value>` | Metadata |
| `-o, --opt <key>=<value>` | Opciones del driver |
| `--type <type>` | Tipo de acceso: `mount`, `block` |
| `--sharing <mode>` | `none`, `readonly`, `onewriter`, `all` |
| `--availability <mode>` | `active`, `pause`, `drain` |
| `--required-bytes <n>` | Tamaño máximo en bytes |
| `--limit-bytes <n>` | Tamaño mínimo en bytes |

Opciones para driver `local`:
- `type=tmpfs`: Volumen tmpfs (ej: `o=size=100m,uid=1000`)
- `type=nfs`: Volumen NFS (ej: `o=addr=192.168.1.1,rw`, `device=:/path`)
- `type=btrfs`: Volumen btrfs (ej: `device=/dev/sda2`)

### Otros comandos de volumen
| Comando | Descripción |
|---------|-------------|
| `docker volume ls` | Listar volúmenes |
| `docker volume inspect <name>` | Inspeccionar volumen |
| `docker volume rm <name>` | Eliminar volumen |
| `docker volume prune` | Eliminar volúmenes no usados |

### Ejemplos

```bash
# Volumen básico
docker volume create app-data

# Volumen tmpfs
docker volume create --driver local --opt type=tmpfs --opt device=tmpfs --opt o=size=100m,uid=1000 tmp-vol

# Volumen NFS
docker volume create --driver local \
  --opt type=nfs \
  --opt o=addr=192.168.1.100,rw \
  --opt device=:/exports/data \
  nfs-volume
```

## Otros comandos útiles

| Comando | Descripción |
|---------|-------------|
| `docker images` | Listar imágenes |
| `docker pull <image>:<tag>` | Descargar imagen |
| `docker push <image>:<tag>` | Subir imagen |
| `docker rmi <image>` | Eliminar imagen |
| `docker rm <container>` | Eliminar contenedor |
| `docker start <container>` | Iniciar contenedor detenido |
| `docker stop <container>` | Detener contenedor |
| `docker restart <container>` | Reiniciar contenedor |
| `docker kill <container>` | Matar contenedor (SIGKILL) |
| `docker pause <container>` | Pausar contenedor |
| `docker unpause <container>` | Reanudar contenedor |
| `docker cp <src> <dest>` | Copiar archivos entre host y contenedor |
| `docker stats` | Estadísticas en vivo de recursos |
| `docker top <container>` | Procesos del contenedor |
| `docker inspect <container\|image>` | Metadatos detallados |
| `docker system df` | Uso de disco de Docker |
| `docker system prune` | Limpiar recursos no usados |
| `docker system prune -a --volumes` | Limpieza completa |
| `docker login <registry>` | Login a registry |
| `docker logout` | Logout |
| `docker tag <src> <target>` | Etiquetar imagen |
| `docker save -o <file> <image>` | Guardar imagen a tar |
| `docker load -i <file>` | Cargar imagen desde tar |
| `docker info` | Información del sistema Docker |
| `docker version` | Versión de Docker |
