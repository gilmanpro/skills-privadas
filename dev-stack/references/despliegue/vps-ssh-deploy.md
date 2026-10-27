# VPS / Servidor Remoto — SSH, Transferencia y Despliegue

> Detalle de la seccion 15 de guia.md (rama Despliegue de dev-stack). Numeracion propia 1-11: el original tenia subsecciones duplicadas (dos 15.7 y dos 15.8), aqui se renumeran.


## 1. Instalación de Herramientas SSH en Windows

#### PuTTY (plink + pscp) — recomendado para Windows
```bash
# Descargar las herramientas DENTRO del proyecto (nunca en %TEMP%)
mkdir ".tmp\tools" 2>nul
curl -sL -o ".tmp\tools\plink.exe" "https://the.earth.li/~sgtatham/putty/latest/w64/plink.exe"
curl -sL -o ".tmp\tools\pscp.exe" "https://the.earth.li/~sgtatham/putty/latest/w64/pscp.exe"

# Usar directamente desde .tmp\tools (la carpeta NO se elimina al terminar)
".tmp\tools\plink.exe" -ssh -P <port> -l <user> -pw "<password>" -batch <host> "<command>"
".tmp\tools\pscp.exe" -P <port> -pw "<password>" -r <local_path> <user>@<host>:<remote_path>
```

#### OpenSSH (built-in en Windows 10/11)
```bash
# SSH simple
ssh -p <port> <user>@<host> "<command>"

# SCP transferencia
scp -P <port> -r <local_path> <user>@<host>:<remote_path>
```

## 2. Manejo del Host Key (Primera Conexión)

Al conectar por primera vez, el servidor no tiene la clave del host guardada.

**Con PLINK** (no interactivo):
```bash
# Opcion A: Obtener el fingerprint primero
".tmp\tools\plink.exe" -ssh -P 10000 -l debian 167.114.169.134
# -> Te muestra el fingerprint, copialo

# Opcion B: Usar -hostkey directo (ya conocido)
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" ^
  -hostkey "ssh-ed25519 255 SHA256:..." 167.114.169.134 "comando"
```

**Con OpenSSH**:
```bash
# La primera vez pregunta interactivamente
ssh -p 10000 debian@167.114.169.134

# O aceptar automaticamente (SOLO dev)
ssh -o StrictHostKeyChecking=no -p 10000 debian@167.114.169.134
```

## 3. Transferencia de Archivos al Servidor

#### SCP con OpenSSH
```bash
# Archivo individual
scp -P 10000 local/file.txt debian@167.114.169.134:/ruta/remota/

# Directorio completo recursivo
scp -P 10000 -r "C:\Users\usuario\.config\opencode\skills\mi-skill" ^
  debian@167.114.169.134:/root/.config/opencode/skills/

# Con compresion (-C)
scp -C -P 10000 -r ./carpeta debian@host:/destino/
```

#### PSCP con PuTTY (password inline)
```bash
# Archivo individual
".tmp\tools\pscp.exe" -P 10000 -pw "password" -hostkey "ssh-ed25519 255 SHA256:..." ^
  SKILL.md debian@167.114.169.134:/ruta/SKILL.md

# Directorio completo
".tmp\tools\pscp.exe" -P 10000 -pw "password" -hostkey "ssh-ed25519 255 SHA256:..." ^
  -r "C:\carpeta" debian@167.114.169.134:/ruta/destino/

# Nota: Si el directorio destino ya existe, PSCP crea una subcarpeta
# Ejemplo: references/ ya existe -> pscp crea references/references/
# Solucion: crear directorio destino VACIO o mover despues
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "mkdir -p /ruta/destino && mv /ruta/destino/subcarpeta/* /ruta/destino/ && rmdir /ruta/destino/subcarpeta"
```

#### Rsync (si esta disponible en remoto y local)
```bash
# Instalar en Windows: https://cygwin.com/ o WSL
rsync -avz -e "ssh -p 10000" ./mi-carpeta debian@host:/destino/

# Flags clave: -a (archivo), -v (verbose), -z (compresion), --delete (sincronizar)
```

## 4. Ejecución Remota de Comandos

#### PLINK (no interactivo, password inline)
```bash
# Comando simple
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "ls -la /root/"

# Multiples comandos encadenados
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "cd /proyecto && docker-compose down && git pull && docker-compose up -d"

# Verificar resultado
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "docker ps && echo OK"

# Script completo de deploy
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "
    set -e
    cd /opt/app
    git pull origin main
    docker-compose build --no-cache
    docker-compose up -d
    docker system prune -f
    echo 'Deploy completado'
  "
```

#### SSH con OpenSSH
```bash
# Comando simple
ssh -p 10000 debian@167.114.169.134 "ls -la /root/"

# Script remoto
ssh -p 10000 debian@167.114.169.134 'bash -s' < local_script.sh

# Forwarding de puerto (tunel)
ssh -L 8080:localhost:80 -p 10000 debian@167.114.169.134
```

## 5. Despliegue de Docker en VPS Remoto

#### Pipeline completo: Build local → Push registry → Pull + Run remoto

```bash
# 1. BUILD local
docker build -t myapp:latest .

# 2. TAG para registry (Docker Hub, GHCR, registry propio)
docker tag myapp:latest myuser/myapp:latest
docker tag myapp:latest myuser/myapp:$(git rev-parse --short HEAD)

# 3. PUSH a registry
docker push myuser/myapp:latest
docker push myuser/myapp:$(git rev-parse --short HEAD)

# 4. DEPLOY remoto via SSH
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "
    cd /opt/app
    docker-compose pull
    docker-compose up -d
    docker system prune -f
  "
```

#### Deploy directo sin registry (copiar imagen via SSH)
```bash
# 1. Exportar imagen a archivo tar
docker save myapp:latest -o myapp.tar

# 2. Comprimir y transferir
gzip myapp.tar
scp -P 10000 myapp.tar.gz debian@host:/tmp/

# 3. Cargar imagen en remoto
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "docker load -i /tmp/myapp.tar.gz && docker-compose up -d"
```

## 6. Escenarios Avanzados de Deploy Docker en VPS

#### Escenario 1: Deploy con Docker-Compose Override (Multi-entorno)

```yaml
# docker-compose.yml — Configuracion base (compartida)
services:
  app:
    image: myapp:latest
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

```yaml
# docker-compose.prod.yml — Override para produccion
services:
  app:
    restart: always
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 512M
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

```bash
# Deploy en VPS con override
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "
    cd /opt/app
    docker compose -f docker-compose.yml -f docker-compose.prod.yml pull
    docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
  "
```

#### Escenario 2: Deploy con Migraciones de Base de Datos

```bash
#!/bin/bash
# scripts/deploy-with-migrations.sh
set -euo pipefail

APP_DIR="/opt/app"
DB_CONTAINER="app_db_1"

echo "[DEPLOY] Iniciando deploy con migraciones..."

# 1. Backup de BD antes de migrar
docker exec "$DB_CONTAINER" pg_dump -U app_user app_db > /tmp/backup-pre-deploy.sql
echo "[DEPLOY] Backup creado: /tmp/backup-pre-deploy.sql"

# 2. Pull nueva imagen
docker compose pull app

# 3. Correr migraciones ANTES de levantar la nueva version (sin downtime)
docker compose run --rm app npx prisma migrate deploy
echo "[DEPLOY] Migraciones ejecutadas"

# 4. Levantar nueva version
docker compose up -d app

# 5. Health check
for i in $(seq 1 12); do
  curl -sf http://localhost:3000/health && { echo "[DEPLOY] OK"; exit 0; }
  sleep 5
done

# 6. Rollback si falla
echo "[DEPLOY] Rollback..."
docker compose down app
docker compose up -d app
docker exec "$DB_CONTAINER" psql -U app_user app_db < /tmp/backup-pre-deploy.sql
```

```bash
# Deploy remoto con migraciones en VPS
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "bash /opt/app/scripts/deploy-with-migrations.sh"
```

#### Escenario 3: Deploy Zero-Downtime (Rolling Update)

```yaml
# docker-compose.zero-downtime.yml
services:
  app:
    image: myapp:latest
    ports:
      - "3000:3000"
    deploy:
      replicas: 3                    # 3 instancias
      update_config:
        parallelism: 1               # actualizar 1 a la vez
        delay: 10s                   # esperar 10s entre cada una
        order: start-first           # levantar nueva antes de parar vieja
        failure_action: rollback     # rollback si falla
      restart_policy:
        condition: any
```

```bash
# Deploy zero-downtime en VPS (Docker Swarm)
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "
    # Inicializar swarm si no existe
    docker swarm init 2>/dev/null || true
    
    # Deploy con rolling update
    docker stack deploy -c docker-compose.yml app --with-registry-auth
    
    # Verificar el rollout
    docker service ls
    docker service ps app_app
  "
```

#### Escenario 4: Deploy Multi-Servicio (Microservicios)

```yaml
# docker-compose.microservices.yml
services:
  api-gateway:
    image: myapp/gateway:latest
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - users-service
      - orders-service
      - payments-service

  users-service:
    image: myapp/users:latest
    expose:
      - "4000"
    environment:
      - DATABASE_URL=postgres://user:pass@users-db:5432/users

  orders-service:
    image: myapp/orders:latest
    expose:
      - "4001"
    environment:
      - DATABASE_URL=postgres://user:pass@orders-db:5432/orders

  payments-service:
    image: myapp/payments:latest
    expose:
      - "4002"
    environment:
      - STRIPE_KEY=${STRIPE_KEY}

  users-db:
    image: postgres:16
    volumes:
      - users_data:/var/lib/postgresql/data

  orders-db:
    image: postgres:16
    volumes:
      - orders_data:/var/lib/postgresql/data

volumes:
  users_data:
  orders_data:
```

```bash
# Deploy de microservicios completo
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "
    cd /opt/app
    
    # Pull de todos los servicios
    for service in gateway users orders payments; do
      docker compose pull \"\$service-service\"
    done
    
    # Deploy completo
    docker compose up -d
    
    # Verificar cada servicio
    for service in api-gateway users-service orders-service payments-service; do
      docker ps --filter name=\"\$service\" --format '\$service: {{.Status}}'
    done
  "
```

#### Escenario 5: Deploy con Variables de Entorno por Ambiente

```bash
# .env.production (en el VPS, nunca en git)
DB_HOST=localhost
DB_NAME=app_prod
DB_USER=app_user
DB_PASS=password_segura
REDIS_URL=redis://:password@redis:6379
STRIPE_KEY=sk_live_...
APP_ENV=production
LOG_LEVEL=info

# .env.staging (igual pero con datos de staging)
```

```bash
# Deploy cargando .env especifico del VPS
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "
    cd /opt/app
    
    # Cargar .env desde el servidor (no desde git)
    export \$(grep -v '^#' /opt/app/.env.production | xargs)
    
    # Deploy con las variables cargadas
    docker compose pull
    docker compose up -d
  "
```

#### Escenario 6: Deploy con Cache de Build Remota

```bash
# Build local con cache compartida en registry
docker buildx build \
  --cache-from ghcr.io/myuser/myapp:cache \
  --cache-to ghcr.io/myuser/myapp:cache,mode=max \
  --push \
  -t ghcr.io/myuser/myapp:latest \
  -t ghcr.io/myuser/myapp:$GIT_SHA .

# Deploy usa cache para builds mas rapidos en VPS
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "
    cd /opt/app
    docker compose build --pull --no-cache 2>/dev/null || docker compose pull
    docker compose up -d
  "
```

## 7. Método Recomendado: Autenticación por Password + PLINK/PSCP

Este es el método preferido cuando compartes la password frecuentemente. Usa las herramientas PuTTY (PLINK + PSCP) que permiten pasar la password inline sin configuración previa de keys.

**Ventajas**:
- Sin configuración inicial (no necesitas generar ni copiar keys)
- Funciona en cualquier servidor inmediatamente
- Ideal cuando rotas contraseñas seguido
- Compatible con CI/CD usando `secrets.VPS_PASSWORD`

**Flujo completo** (demostrado en producción):

```bash
@REM 1. DESCARGAR HERRAMIENTAS DENTRO DEL PROYECTO (una sola vez, se conservan)
mkdir ".tmp\tools" 2>nul
curl -sL -o ".tmp\tools\plink.exe" "https://the.earth.li/~sgtatham/putty/latest/w64/plink.exe"
curl -sL -o ".tmp\tools\pscp.exe" "https://the.earth.li/~sgtatham/putty/latest/w64/pscp.exe"

@REM 2. OBTENER HOST KEY (primera vez)
".tmp\tools\plink.exe" -ssh -P 10000 -l debian 167.114.169.134
@REM Te muestra el fingerprint, lo copias y lo usas con -hostkey

@REM 3. CREAR DIRECTORIOS REMOTOS
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" ^
  -hostkey "ssh-ed25519 255 SHA256:..." 167.114.169.134 ^
  "mkdir -p /ruta/destino"

@REM 4. TRANSFERIR ARCHIVOS
".tmp\tools\pscp.exe" -P 10000 -pw "password" ^
  -hostkey "ssh-ed25519 255 SHA256:..." ^
  -r "C:\carpeta\local" debian@167.114.169.134:/ruta/destino/

@REM 5. EJECUTAR COMANDOS REMOTOS
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" ^
  -hostkey "ssh-ed25519 255 SHA256:..." 167.114.169.134 ^
  "cd /app && docker-compose up -d"

@REM 6. NO LIMPIAR: .tmp\tools queda dentro del proyecto para reutilizar y auditar
```

#### Almacenar la contraseña en variable de entorno (para scripts)
```bash
@REM Definir una sola vez al inicio de la terminal
set VPS_PASS=miPasswordSegura

@REM Usar en comandos (con ! para expansión retardada en batch)
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "%VPS_PASS%" -hostkey "..." host "comando"
```

#### CI/CD con password en GitHub Actions
```yaml
name: Deploy to VPS
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Deploy via SSH with password
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.VPS_HOST }}
          port: ${{ secrets.VPS_PORT }}
          username: ${{ secrets.VPS_USER }}
          password: ${{ secrets.VPS_PASSWORD }}  # <-- password directa
          script: |
            cd /opt/app
            git pull
            docker-compose up -d --build
```

## 8. Alternativa: SSH Keys (Autenticación sin Password)

Solo si prefieres no escribir la password cada vez. Útil para deploys frecuentes desde tu máquina local.

```bash
# 1. Generar clave SSH
ssh-keygen -t ed25519 -C "deploy@vps" -f "%USERPROFILE%\.ssh\id_ed25519"

# 2. Copiar clave publica al servidor (una sola vez, con password)
type "%USERPROFILE%\.ssh\id_ed25519.pub" | plink -ssh -P 10000 -l debian -pw "password" host ^
  "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"

# 3. A partir de ahi, conexion sin password:
ssh -p 10000 -i "%USERPROFILE%\.ssh\id_ed25519" debian@host
```

## 9. Pipeline CI/CD con Deploy a VPS via SSH

```yaml
# GitHub Actions — Deploy a VPS via SSH
name: Deploy to VPS
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Build Docker image
        run: docker build -t myapp:${{ github.sha }} .
      
      - name: Push to registry
        run: |
          docker tag myapp:${{ github.sha }} ghcr.io/${{ github.repository }}:latest
          docker push ghcr.io/${{ github.repository }}:latest
      
      - name: Deploy via SSH
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.VPS_HOST }}
          port: ${{ secrets.VPS_PORT }}
          username: ${{ secrets.VPS_USER }}
          key: ${{ secrets.VPS_SSH_KEY }}
          script: |
            cd /opt/app
            docker-compose pull
            docker-compose up -d
            docker system prune -f
```

## 10. Debugging de Conexión al VPS

```bash
# Probar conectividad basica
curl -v telnet://167.114.169.134:10000

# Probar puerto SSH con curl timing
curl -w "Connect: %{time_connect}s\n" telnet://167.114.169.134:10000

# Verificar si el puerto esta abierto con plink
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "test" -batch ^
  167.114.169.134 "echo connected" 2>&1

# Ver logs de failed attempts en el VPS
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "sudo tail -f /var/log/auth.log | grep ssh"
```

## 11. Buenas Practicas para VPS

1. **NUNCA** hardcodees passwords en scripts — usar variables de entorno o secrets de CI/CD
2. **SIEMPRE** usar `-hostkey` con PLINK para evitar MITM
3. **Trabajar dentro del proyecto**: descargar herramientas a `.tmp\tools\` del proyecto y **NO borrarlas** al terminar — quedan para reutilizar y auditar. Nunca usar `%TEMP%`
4. **Prefiere SSH keys** sobre passwords para deploys automatizados
5. **Usa `set -e`** en scripts remotos para que fallen si algo sale mal
6. **Health check** despues del deploy: verificar que el contenedor corra y responda 200
7. **Rollback plan**: tener la version anterior de la imagen taggeada para revertir rapido
8. **Git en VPS sí, pero solo para config**: `git pull` del compose y configs, nunca rebuild en el VPS
9. **Taggea imágenes con git SHA**: cada imagen debe tener el commit hash como tag para trazabilidad
10. **NUNCA hagas `git checkout` + rebuild en producción**: build siempre en CI/CD, deploy solo pull
