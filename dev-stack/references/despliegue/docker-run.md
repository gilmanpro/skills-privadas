# docker run — Referencia completa de opciones

**Uso:** `docker run [OPTIONS] IMAGE [COMMAND] [ARG...]`

## Opciones

### Nombre y IDs
| Flag | Descripción |
|------|-------------|
| `--name <string>` | Asignar un nombre al contenedor |
| `--cidfile <file>` | Escribir el ID del contenedor a un archivo |

### Publicación de puertos
| Flag | Descripción |
|------|-------------|
| `-p, --publish <host:container/proto>` | Publicar puerto del contenedor al host (ej: `-p 8080:80/tcp`) |
| `-P, --publish-all` | Publicar todos los puertos expuestos a puertos aleatorios |
| `--expose <port>` | Exponer un puerto sin publicarlo |

### Variables de entorno
| Flag | Descripción |
|------|-------------|
| `-e, --env <key>=<value>` | Setear variable de entorno |
| `--env-file <file>` | Leer variables desde un archivo |

### Volúmenes y montajes
| Flag | Descripción |
|------|-------------|
| `-v, --volume <host>:<container>` | Bind mount o named volume |
| `--mount type=bind,src=<host>,dst=<container>` | Bind mount (recomendado sobre -v) |
| `--mount type=volume,src=<vol>,dst=<container>` | Named volume |
| `--mount type=tmpfs,dst=<path>` | Montar tmpfs |
| `--tmpfs <path>:<options>` | Montar tmpfs (ej: `/run:rw,noexec,nosuid,size=65536k`) |
| `--volumes-from <container>[:ro\|:rw]` | Montar volúmenes desde otro contenedor |
| `--read-only` | Montar sistema de archivos root como solo lectura |
| `--volume-driver <driver>` | Driver de volumen opcional |

### Red
| Flag | Descripción |
|------|-------------|
| `--network <name>` | Conectar a una red (bridge, host, none, `<name>`) |
| `--network-alias <alias>` | Alias de red para el contenedor |
| `--ip <address>` | IPv4 address (ej: `172.30.100.104`) |
| `--ip6 <address>` | IPv6 address |
| `--mac-address <address>` | MAC address (ej: `92:d0:c6:0a:29:33`) |
| `--dns <ip>` | DNS server personalizado |
| `--dns-option <opt>` | Opciones DNS |
| `--dns-search <domain>` | Dominio de búsqueda DNS |
| `--add-host <host:ip>` | Añadir entrada a /etc/hosts (ej: `myhost:192.168.1.100`) |
| `--link <name>:<alias>` | Añadir enlace a otro contenedor |

### Restricciones de recursos
| Flag | Descripción |
|------|-------------|
| `-m, --memory <bytes>` | Límite de memoria (ej: `512m`, `2g`) |
| `--memory-reservation <bytes>` | Soft limit de memoria |
| `--memory-swap <bytes>` | Swap limit (`-1` para swap ilimitado) |
| `--memory-swappiness <0-100>` | Swappiness de memoria (por defecto -1) |
| `--cpus <number>` | Número de CPUs (ej: `1.5`) |
| `--cpu-shares <weight>` | Peso relativo de CPU (10-1000) |
| `--cpu-period <microseconds>` | Periodo del CFS scheduler |
| `--cpu-quota <microseconds>` | Cuota del CFS scheduler |
| `--cpuset-cpus <cpus>` | CPUs permitidas (ej: `0-3`, `0,1`) |
| `--cpuset-mems <mems>` | MEMs permitidas |
| `--blkio-weight <0-1000>` | Peso relativo de Block IO |
| `--device-read-bps <path>:<rate>` | Límite de lectura dispositivo |
| `--device-write-bps <path>:<rate>` | Límite de escritura dispositivo |
| `--device-read-iops <path>:<rate>` | Límite de IOPS lectura |
| `--device-write-iops <path>:<rate>` | Límite de IOPS escritura |
| `--pids-limit <n>` | Límite de PIDs (`-1` para ilimitado) |
| `--shm-size <bytes>` | Tamaño de `/dev/shm` |
| `--ulimit <type>=<soft>[:<hard>]` | Opciones ulimit |

### Restart policy
| Flag | Descripción |
|------|-------------|
| `--restart <policy>` | Política de reinicio: `no`, `on-failure[:max-retries]`, `always`, `unless-stopped` |

### Healthcheck
| Flag | Descripción |
|------|-------------|
| `--health-cmd <command>` | Comando para healthcheck |
| `--health-interval <duration>` | Intervalo entre checks (ms\|s\|m\|h) |
| `--health-retries <n>` | Fallos consecutivos para marcar unhealthy |
| `--health-start-period <duration>` | Periodo de inicio antes de health-retries |
| `--health-timeout <duration>` | Timeout por check |
| `--no-healthcheck` | Deshabilitar HEALTHCHECK de la imagen |

### Modo de ejecución
| Flag | Descripción |
|------|-------------|
| `-d, --detach` | Ejecutar en background |
| `-i, --interactive` | Mantener STDIN abierto |
| `-t, --tty` | Asignar pseudo-TTY |
| `-a, --attach <stream>` | Adjuntar a STDIN/STDOUT/STDERR |
| `--detach-keys <key>` | Override tecla de detach |
| `--init` | Ejecutar init process (tini) dentro del contenedor |
| `--rm` | Eliminar contenedor automáticamente al salir |
| `--sig-proxy <bool>` | Proxy de señales al proceso |
| `--stop-signal <signal>` | Señal para detener el contenedor |
| `--stop-timeout <seconds>` | Timeout para detener el contenedor |

### Usuario y permisos
| Flag | Descripción |
|------|-------------|
| `-u, --user <name\|uid>[:<group\|gid>]` | Usuario o UID |
| `--group-add <group>` | Añadir grupos adicionales |
| `--privileged` | Escalar privilegios (⚠️ usar con cuidado) |
| `--cap-add <capability>` | Añadir Linux capability (ej: `SYS_PTRACE`) |
| `--cap-drop <capability>` | Quitar Linux capability |
| `--security-opt <opt>` | Opciones de seguridad |
| `--gpus <gpu>` | GPUs a añadir (ej: `all`, `device=GPU-xxxx`) |
| `--device <host>:<container>[:r|w|m]` | Añadir dispositivo host |
| `--device-cgroup-rule <rule>` | Regla cgroup para dispositivos |
| `--oom-kill-disable` | Deshabilitar OOM Killer |
| `--oom-score-adj <-1000 to 1000>` | Ajuste de puntuación OOM |
| `--no-new-privileges` | Evitar escalado de privilegios |

### Namespaces
| Flag | Descripción |
|------|-------------|
| `--pid <mode>` | PID namespace: `host` o `container:<name\|id>` |
| `--uts <mode>` | UTS namespace: `host` |
| `--ipc <mode>` | IPC mode: `none`, `private`, `shareable`, `host`, `container:<name>` |
| `--userns <mode>` | User namespace: `host` |
| `--cgroupns <mode>` | Cgroup namespace: `host` o `private` |
| `--cgroup-parent <path>` | Parent cgroup |

### Etiquetas y metadatos
| Flag | Descripción |
|------|-------------|
| `-l, --label <key>=<value>` | Añadir metadata |
| `--label-file <file>` | Leer labels desde archivo |
| `--annotation <key>=<value>` | Añadir anotación OCI (API 1.43+) |

### Logging
| Flag | Descripción |
|------|-------------|
| `--log-driver <driver>` | Driver de logging (ej: `json-file`, `syslog`, `journald`, `gelf`, `fluentd`, `awslogs`, `splunk`, `etwlogs`, `gcplogs`, `local`) |
| `--log-opt <key>=<value>` | Opciones del driver de logging |

### Misceláneos
| Flag | Descripción |
|------|-------------|
| `-w, --workdir <path>` | Directorio de trabajo dentro del contenedor |
| `--entrypoint <command>` | Override del ENTRYPOINT de la imagen |
| `--hostname, -h <name>` | Hostname del contenedor |
| `--domainname <name>` | NIS domain name |
| `--platform <os/arch>` | Forzar plataforma (ej: `linux/amd64`, `linux/arm64`) |
| `--pull <policy>` | Política de pull: `always`, `missing` (default), `never` |
| `--runtime <name>` | Runtime a usar |
| `--storage-opt <opt>` | Opciones del storage driver |
| `--sysctl <key>=<value>` | Opciones sysctl |
| `--isolation <type>` | Tecnología de aislamiento (Windows) |

## Ejemplos

```bash
# Contenedor básico con nombre
docker run --name mi-web -d nginx:alpine

# Con puerto, env, volumen, restart
docker run -d \
  --name app \
  -p 8080:3000 \
  -e NODE_ENV=production \
  -v /host/data:/app/data \
  -v app_vol:/app/config \
  --restart unless-stopped \
  node:20-alpine

# Límites de recursos + red
docker run -d \
  --name db \
  --network my-network \
  --network-alias database \
  --cpus 2 \
  --memory 1g \
  --memory-reservation 768m \
  --restart always \
  -p 5432:5432 \
  -e POSTGRES_PASSWORD=secret \
  -v pgdata:/var/lib/postgresql/data \
  postgres:16-alpine

# Interactivo con TTY + cleanup
docker run --rm -it \
  --name temp \
  -w /workspace \
  -v $(pwd):/workspace \
  node:20-alpine sh

# Healthcheck
docker run -d \
  --name api \
  --health-cmd "curl -f http://localhost/health || exit 1" \
  --health-interval 30s \
  --health-retries 3 \
  --health-start-period 10s \
  --health-timeout 5s \
  my-api:latest

# Con init process + read only + tmpfs
docker run -d \
  --name secure-app \
  --init \
  --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,size=64m \
  --tmpfs /var/run:rw,noexec,nosuid,size=32m \
  --security-opt no-new-privileges:true \
  my-app:latest

# GPU
docker run -d --gpus all \
  --name tf-gpu \
  tensorflow/tensorflow:latest-gpu
```
