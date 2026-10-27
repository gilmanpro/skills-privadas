# Docker Compose — Referencia completa

## docker compose up

**Uso:** `docker compose up [OPTIONS] [SERVICE...]`

### Opciones
| Flag | Descripción |
|------|-------------|
| `-d, --detach` | Modo detached: ejecutar en background |
| `--build` | Construir imágenes antes de iniciar |
| `--no-build` | No construir imagen aunque la política lo indique |
| `--no-recreate` | Si los contenedores ya existen, no recrearlos |
| `--force-recreate` | Recrear contenedores aunque no haya cambios |
| `--no-deps` | No iniciar servicios vinculados |
| `--no-start` | Crear contenedores sin iniciarlos |
| `-V, --renew-anon-volumes` | Recrear volúmenes anónimos |
| `--abort-on-container-exit` | Detener todos si algún contenedor se detiene |
| `--abort-on-container-failure` | Detener todos si algún contenedor falla |
| `--exit-code-from <service>` | Devolver exit code del servicio especificado |
| `--remove-orphans` | Eliminar contenedores de servicios no definidos en el compose |
| `--scale <service>=<num>` | Escalar servicio a N instancias |
| `--pull <policy>` | Política de pull: `always`, `missing`, `never` (default: `policy`) |
| `--no-color` | Output monocromático |
| `--no-log-prefix` | No mostrar prefijo en logs |
| `--timestamps` | Mostrar timestamps |
| `--quiet-build` | Suprimir output de build |
| `--quiet-pull` | Pull sin mostrar progreso |
| `--attach <service>` | Restringir attach a servicios específicos |
| `--attach-dependencies` | Attach automático a dependencias |
| `--no-attach <service>` | No attach a servicios específicos |
| `--wait` | Esperar a que servicios estén running/healthy |
| `--wait-timeout <seconds>` | Timeout máximo para esperar |
| `-t, --timeout <seconds>` | Timeout para shutdown de contenedores |
| `--watch` | Watch source code y rebuild/refresh al cambiar archivos |
| `-y, --yes` | Asumir "yes" en todos los prompts |
| `--menu` | Habilitar shortcuts interactivos (incompatible con -d) |
| `--always-recreate-deps` | Recrear dependencias (incompatible con --no-recreate) |

## docker compose down

**Uso:** `docker compose down [OPTIONS]`

| Flag | Descripción |
|------|-------------|
| `-v, --volumes` | Eliminar volúmenes anónimos |
| `--remove-orphans` | Eliminar contenedores huérfanos |
| `-t, --timeout <seconds>` | Timeout para shutdown |
| `--rmi <type>` | Eliminar imágenes: `all`, `local` |

## Formato docker-compose.yml

### Versión y estructura general

```yaml
name: <project-name>    # Nombre del proyecto (default: nombre del directorio)

services:                # Define los servicios/contenedores
  <service-name>:        # Nombre del servicio
    ...

volumes:                 # Define volúmenes nombrados
  <volume-name>:
    ...

networks:                # Define redes
  <network-name>:
    ...

configs:                 # Define configuraciones (Swarm)
  <config-name>:
    ...

secrets:                 # Define secretos (Swarm)
  <secret-name>:
    ...
```

### Services — propiedades

#### Imagen y build
| Propiedad | Descripción |
|-----------|-------------|
| `image: <name>:<tag>` | Imagen a usar |
| `build: <path>` | Contexto de build (ruta al Dockerfile) |
| `build:` | Configuración de build extendida |
| `  context: <path>` | Contexto de build |
| `  dockerfile: <file>` | Nombre del Dockerfile |
| `  args:` | Build arguments |
| `    <key>: <value>` | |
| `  target: <stage>` | Target stage para multi-stage |
| `  shm_size: <size>` | Tamaño shared memory (ej: `2gb`) |
| `  cache_from:` | Cache sources |
| `    - <image>` | |
| `  extra_hosts:` | Hosts extra en /etc/hosts |
| `    - <host>:<ip>` | |
| `  tags:` | Tags adicionales |
| `    - <tag>` | |
| `pull_policy: <policy>` | `always`, `missing`, `never`, `build` |
| `platform: <os/arch>` | Plataforma objetivo |

#### Puertos
| Propiedad | Descripción |
|-----------|-------------|
| `ports:` | Lista de puertos |
| `  - "<host>:<container>"` | Formato string |
| `  - target: <container>` | Formato largo |
| `    host_ip: <ip>` | |
| `    published: <host>` | |
| `    protocol: <tcp\|udp>` | |
| `    mode: <ingress\|host>` | |
| `expose:` | Puertos expuestos (no publicados) |
| `  - "<port>"` | |

#### Redes
| Propiedad | Descripción |
|-----------|-------------|
| `networks:` | Redes a conectar |
| `  - <network-name>` | |
| `  <name>:` | Configuración avanzada |
| `    aliases:` | Alias de red |
| `      - <alias>` | |
| `    ipv4_address: <ip>` | IPv4 estática |
| `    ipv6_address: <ip>` | IPv6 estática |
| `dns:` | DNS servers |
| `dns_opt:` | Opciones DNS |
| `dns_search:` | Dominios de búsqueda DNS |
| `extra_hosts:` | Hosts extra en /etc/hosts |
| `  - "<host>:<ip>"` | |

#### Variables de entorno
| Propiedad | Descripción |
|-----------|-------------|
| `environment:` | Variables de entorno |
| `  <key>: <value>` | Formato clave-valor |
| `  - <key>=<value>` | Formato lista |
| `env_file: <file>` | Archivo de variables |
| `  - <file>` | Múltiples archivos |

#### Volúmenes
| Propiedad | Descripción |
|-----------|-------------|
| `volumes:` | Volúmenes a montar |
| `  - <vol>:<path>` | Named volume |
| `  - <host>:<path>` | Bind mount |
| `  - type: volume` | Configuración larga |
| `    source: <vol>` | |
| `    target: <path>` | |
| `    read_only: true` | Solo lectura |
| `  - type: bind` | Bind mount largo |
| `    source: <host>` | |
| `    target: <path>` | |
| `  - type: tmpfs` | tmpfs |
| `    target: <path>` | |

#### Recursos
| Propiedad | Descripción |
|-----------|-------------|
| `deploy:` | Configuración de despliegue (Swarm/compose) |
| `  resources:` | Límites de recursos |
| `    limits:` | Límites máximos |
| `      cpus: "<n>"` | CPUs máximas |
| `      memory: <size>` | Memoria máxima |
| `    reservations:` | Reservas mínimas |
| `      cpus: "<n>"` | CPUs mínimas |
| `      memory: <size>` | Memoria mínima |
| `  replicas: <n>` | Número de réplicas |
| `  restart_policy:` | Política de reinicio |
| `    condition: <any\|on-failure\|none>` | |
| `    delay: <duration>` | |
| `    max_attempts: <n>` | |
| `    window: <duration>` | |
| `  placement:` | Restricciones de placement |
| `    constraints:` | |
| `      - <expr>` | |
| `  labels:` | Labels del servicio |
| `    <key>: <value>` | |

#### Restart policy (compose v2)
| Propiedad | Descripción |
|-----------|-------------|
| `restart: <policy>` | `no`, `always`, `on-failure`, `unless-stopped` |

#### Healthcheck
| Propiedad | Descripción |
|-----------|-------------|
| `healthcheck:` | Healthcheck |
| `  test: ["CMD", "<comando>"]` | Comando de test |
| `  interval: <duration>` | Intervalo |
| `  timeout: <duration>` | Timeout |
| `  retries: <n>` | Número de reintentos |
| `  start_period: <duration>` | Periodo inicial |
| `  start_interval: <duration>` | Intervalo inicial |

#### Otras propiedades comunes
| Propiedad | Descripción |
|-----------|-------------|
| `container_name: <name>` | Nombre del contenedor |
| `hostname: <name>` | Hostname |
| `user: <uid[:gid]>` | Usuario |
| `working_dir: <path>` | Directorio de trabajo |
| `entrypoint: ["<cmd>", "<arg>"]` | Override ENTRYPOINT |
| `command: ["<cmd>", "<arg>"]` | Override CMD |
| `stdin_open: true` | Equivalente a -i |
| `tty: true` | Equivalente a -t |
| `privileged: true` | Modo privilegiado |
| `cap_add:` | Añadir capabilities |
| `  - <cap>` | |
| `cap_drop:` | Quitar capabilities |
| `  - <cap>` | |
| `security_opt:` | Opciones de seguridad |
| `  - "<opt>"` | |
| `read_only: true` | Root filesystem RO |
| `tmpfs:` | Montajes tmpfs |
| `  - <path>` | |
| `depends_on:` | Dependencias entre servicios |
| `  <service>:` | |
| `    condition: <condition>` | `service_started`, `service_healthy`, `service_completed_successfully` |
| `init: true` | Init process (tini) |
| `sysctls:` | Sysctl options |
| `  <key>: <value>` | |
| `ulimits:` | Ulimit options |
| `  <type>:` | |
| `    soft: <n>` | |
| `    hard: <n>` | |
| `logging:` | Configuración de logging |
| `  driver: <driver>` | |
| `  options:` | |
| `    <key>: <value>` | |
| `labels:` | Labels del contenedor |
| `  <key>: <value>` | |
| `profiles:` | Perfiles para incluir/excluir servicios |
| `  - <name>` | |
| `scale: <n>` | Número de instancias |

### Volumes — propiedades
| Propiedad | Descripción |
|-----------|-------------|
| `driver: <driver>` | Driver del volumen (default: `local`) |
| `driver_opts:` | Opciones del driver |
| `  <key>: <value>` | |
| `external: true` | Usar volumen externo (ya creado) |
| `external:` | |
| `  name: <name>` | Nombre externo real |
| `labels:` | Labels |
| `  <key>: <value>` | |

### Networks — propiedades
| Propiedad | Descripción |
|-----------|-------------|
| `driver: <driver>` | Driver: `bridge`, `overlay`, `host`, `none`, `macvlan`, `ipvlan` |
| `driver_opts:` | Opciones del driver |
| `  <key>: <value>` | |
| `attachable: true` | Permitir attach manual de contenedores |
| `enable_ipv6: true` | Habilitar IPv6 |
| `ipam:` | Configuración IPAM |
| `  driver: <default>` | |
| `  config:` | |
| `    - subnet: <cidr>` | |
| `      gateway: <ip>` | |
| `internal: true` | Red interna (sin acceso externo) |
| `external: true` | Red externa |
| `labels:` | Labels |
| `  <key>: <value>` | |

## Ejemplos completos

### Web app con Node.js + PostgreSQL

```yaml
name: myapp

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
      target: production
      args:
        - NODE_ENV=production
    container_name: myapp-web
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DB_HOST=db
      - DB_PORT=5432
    env_file:
      - .env
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - uploads:/app/uploads
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "--spider", "http://localhost:3000/health"]
      interval: 30s
      timeout: 5s
      retries: 3
    networks:
      - frontend
      - backend

  db:
    image: postgres:16-alpine
    container_name: myapp-db
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_USER=myapp
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./db/init:/docker-entrypoint-initdb.d
    restart: always
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U myapp"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - backend

volumes:
  pgdata:
    driver: local
  uploads:

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true
```

### Stack con Redis, Nginx y worker

```yaml
name: stack-demo

services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - app
    restart: unless-stopped

  app:
    build: ./app
    expose:
      - "3000"
    environment:
      - REDIS_URL=redis://redis:6379
    depends_on:
      - redis
    restart: unless-stopped

  worker:
    build: ./worker
    environment:
      - REDIS_URL=redis://redis:6379
    depends_on:
      - redis
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5

volumes:
  redis_data:
```
