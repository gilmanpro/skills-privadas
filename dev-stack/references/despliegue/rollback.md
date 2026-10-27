# Rollback Automatico

> Detalle de la seccion 11 de guia.md (rama Despliegue de dev-stack).


Sistema completo de rollback automático con detección de fallos, reversión y notificación. Cubre Docker Compose, VPS remoto, Kubernetes.

## 1. Script de Rollback Automatico (Docker Compose)

```bash
#!/bin/bash
# scripts/rollback.sh — Rollback automatico con health check
set -euo pipefail

APP_NAME="${1:-mi-app}"
COMPOSE_FILE="${2:-docker-compose.yml}"
HEALTH_URL="${3:-http://localhost:3000/health}"
RETRIES="${4:-12}"       # ~60s total (12 * 5s)
ROLLBACK_TAG="${5:-previous}"

echo "[ROLLBACK] Iniciando deploy de $APP_NAME..."

# 1. Taggear version actual como "previous"
docker tag "$APP_NAME:latest" "$APP_NAME:$ROLLBACK_TAG" 2>/dev/null || true

# 2. Pushear nueva version (taggeada como latest en el registry)
docker compose -f "$COMPOSE_FILE" pull 2>/dev/null || true

# 3. Levantar nueva version
docker compose -f "$COMPOSE_FILE" up -d --remove-orphans

# 4. Health check con timeout
echo "[ROLLBACK] Verificando health check ($HEALTH_URL)..."
for i in $(seq 1 $RETRIES); do
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$HEALTH_URL" 2>/dev/null || echo "000")
    if [ "$STATUS" = "200" ]; then
        echo "[ROLLBACK] ✔ Deploy exitoso — $HEALTH_URL respondio 200"
        
        # Limpiar imagenes viejas (excepto previous)
        docker image prune -f --filter "dangling=true" 2>/dev/null || true
        exit 0
    fi
    echo "[ROLLBACK] Intentando $i/$RETRIES — Status: $STATUS, esperando 5s..."
    sleep 5
done

# 5. HEALTH CHECK FALLÓ → Rollback automatico
echo "[ROLLBACK] ⚠ HEALTH CHECK FALLÓ después de $RETRIES intentos"
echo "[ROLLBACK] ▶ Ejecutando rollback a version $ROLLBACK_TAG..."

docker compose -f "$COMPOSE_FILE" down
docker tag "$APP_NAME:$ROLLBACK_TAG" "$APP_NAME:latest" 2>/dev/null || true
docker compose -f "$COMPOSE_FILE" up -d

# 6. Verificar que el rollback funcionó
sleep 5
ROLLBACK_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$HEALTH_URL" 2>/dev/null || echo "000")
if [ "$ROLLBACK_STATUS" = "200" ]; then
    echo "[ROLLBACK] ✔ Rollback exitoso — version anterior restaurada"
    exit 2
else
    echo "[ROLLBACK] ✗ ROLLBACK FALLÓ — intervencion manual requerida"
    exit 3
fi
```

## 2. Rollback con VPS Remoto (PLINK + Docker)

```bash
@REM scripts/rollback-vps.bat — Rollback automatico en VPS remoto
@echo off
set VPS_HOST=167.114.169.134
set VPS_PORT=10000
set VPS_USER=debian
set VPS_PASS=password_segura
set HOSTKEY=ssh-ed25519 255 SHA256:...
set APP_DIR=/opt/app
set HEALTH_URL=http://mi-app.com/health
set TIMEOUT_SEC=60

echo [ROLLBACK] Desplegando nueva version en VPS...

@REM 1. Pushear nueva imagen a registry
docker push myuser/myapp:latest
docker push myuser/myapp:%DATE:~-4%%TIME:~0,2%%TIME:~3,2%

@REM 2. Hacer pull y up en remoto
".tmp\tools\plink.exe" -ssh -P %VPS_PORT% -l %VPS_USER% -pw "%VPS_PASS%" ^
  -hostkey "%HOSTKEY%" %VPS_HOST% ^
  "cd %APP_DIR% && docker-compose pull && docker-compose up -d"

@REM 3. Health check loop (esperar hasta TIMEOUT segundos)
echo [ROLLBACK] Verificando health check...
for /l %%i in (1,1,%TIMEOUT_SEC%) do (
  curl -s -o nul -w "%%{http_code}" %HEALTH_URL% | find "200" >nul
  if !errorlevel! equ 0 (
    echo [ROLLBACK] ✔ Deploy exitoso
    goto :done
  )
  timeout /t 1 /nobreak >nul
)

@REM 4. Rollback automatico
echo [ROLLBACK] ⚠ Health check fallo — ejecutando rollback...
".tmp\tools\plink.exe" -ssh -P %VPS_PORT% -l %VPS_USER% -pw "%VPS_PASS%" ^
  -hostkey "%HOSTKEY%" %VPS_HOST% ^
  "cd %APP_DIR% && docker-compose down && docker tag myapp:previous myapp:latest && docker-compose up -d"

:done
@REM NO borrar .tmp\tools: queda en el proyecto para reutilizar y auditar
```

## 3. Rollback con Monitoreo y Notificación

```bash
#!/bin/bash
# scripts/deploy-with-rollback.sh — Deploy + health check + rollback + notificacion
# Uso: ./deploy-with-rollback.sh [app_name] [health_url] [webhook_url]

APP="${1:-myapp}"
HEALTH="${2:-http://localhost:3000/health}"
WEBHOOK="${3:-}"

notify() {
    local MSG="$1"
    local LEVEL="$2"
    echo "[$LEVEL] $MSG"
    if [ -n "$WEBHOOK" ]; then
        curl -s -H "Content-Type: application/json" \
          -d "{\"text\":\"[$LEVEL] $MSG\",\"app\":\"$APP\",\"time\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}" \
          "$WEBHOOK" >/dev/null
    fi
}

notify "Iniciando deploy de $APP..." "INFO"

# Taggear version anterior
docker tag "$APP:latest" "$APP:rollback-$(date +%s)" 2>/dev/null

# Deploy
docker compose pull && docker compose up -d

# Health check
for i in 1 2 3 4 5 6 7 8 9 10 11 12; do
    if curl -sf "$HEALTH" >/dev/null 2>&1; then
        notify "Deploy exitoso — health check OK (intento $i)" "SUCCESS"
        exit 0
    fi
    sleep 5
done

# Rollback
notify "HEALTH CHECK FALLIDO — ejecutando rollback automatico" "CRITICAL"
docker compose down

# Encontrar el tag anterior mas reciente
PREV=$(docker images --format "{{.Tag}}" "$APP" | grep rollback | sort | tail -1)
docker tag "$APP:$PREV" "$APP:latest"
docker compose up -d

sleep 10
if curl -sf "$HEALTH" >/dev/null 2>&1; then
    notify "Rollback exitoso a $PREV" "WARNING"
else
    notify "ROLLBACK FALLÓ — intervencion manual urgente" "CRITICAL"
fi
```

## 4. Estrategia de Rollback con Git + Docker (Recomendada)

**¿Recomiendo tener git en el VPS?** Sí, pero con un propósito específico:
- **NO** para hacer `git checkout` y rebuild en el VPS (lento, riesgoso, dependencias variables)
- **SÍ** para tener el SHA del commit como referencia, etiquetar imágenes Docker con ese SHA, y poder rastrear qué código está corriendo

**Flujo recomendado (Docker tags + Git SHA):**

```bash
# El VPS tiene git SOLO para clone inicial y git pull (no para rebuild)
# El build siempre ocurre en CI/CD local o GitHub Actions

@REM En CI/CD local:
@REM 1. Build con git SHA como tag
set GIT_SHA=$(git rev-parse --short HEAD)
docker build -t myapp:%GIT_SHA% .
docker tag myapp:%GIT_SHA% myapp:latest

@REM 2. Push con ambos tags
docker push myapp:%GIT_SHA%
docker push myapp:latest

@REM 3. Deploy en VPS — solo pull, nunca rebuild
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "
    cd /opt/app
    git pull origin main              # actualiza docker-compose.yml, configs
    docker compose pull               # baja la imagen nueva
    docker compose up -d              # levanta con la nueva imagen
  "
```

**Ventajas de este enfoque:**
- **Velocidad**: rollback es cambiar un tag, no recompilar
- **Trazabilidad**: cada imagen Docker tiene su commit SHA
- **Consistencia**: lo que builds local es exactamente lo que corre en prod
- **Seguridad**: no necesitas toolchain de build en el VPS

**Tags por nivel de rollback:**

```bash
# Tags disponibles en todo momento:
docker images myapp
# REPOSITORY   TAG          SIZE      QUE ES
# myapp        latest       245MB     <-- actual en produccion
# myapp        a1b2c3d      245MB     <-- commit SHA actual (trazabilidad)
# myapp        previous     232MB     <-- version anterior (rollback inmediato)
# myapp        e4f5g6h      232MB     <-- commit SHA anterior
# myapp        stable-1     220MB     <-- version estable conocida
# myapp        v1.2.3       245MB     <-- version semver

# Al hacer deploy (CI/CD):
docker tag myapp:latest myapp:previous         # guardar anterior
docker tag myapp:latest myapp:$(git rev-parse --short HEAD)
docker build -t myapp:latest .                 # build nueva
docker push --all-tags myapp                   # push todo

# Rollback inmediato (1 comando):
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "
    docker compose down
    docker tag myapp:previous myapp:latest
    docker compose up -d
    echo 'Rollback a version anterior completado'
  "

# Rollback a version especifica:
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "
    docker compose down
    docker pull myapp:v1.2.2
    docker tag myapp:v1.2.2 myapp:latest
    docker compose up -d
    echo 'Rollback a v1.2.2 completado'
  "
```

**Git en VPS — para qué exactamente:**

| Propósito | ¿Recomendado? | Por qué |
|-----------|--------------|---------|
| `git pull` del docker-compose.yml | ✅ Sí | Actualizar config de servicios sin rebuild |
| `git pull` de configs/nginx | ✅ Sí | Actualizar reverse proxy, env templates |
| `git checkout` + rebuild | ❌ No | Lento, inconsistente, toolchain pesado |
| `git log` para ver qué SHA corrió | ✅ Sí | Saber qué version esta en producción |
| `git tag` para marcar releases | ✅ Sí | Identificar versiones estables |

**Ejemplo de deploy completo (CI/CD → VPS):**

```bash
@REM deploy-completo.bat
@echo off
set VPS_HOST=167.114.169.134
set VPS_PORT=10000
set VPS_USER=debian
set VPS_PASS=password_segura
set HOSTKEY=ssh-ed25519 255 SHA256:...
set APP_DIR=/opt/app

@REM 1. Build con git SHA
for /f %%i in ('git rev-parse --short HEAD') do set GIT_SHA=%%i
docker build -t myapp:latest .
docker tag myapp:latest myapp:%GIT_SHA%

@REM 2. Push a registry
docker push myapp:latest
docker push myapp:%GIT_SHA%

@REM 3. Backup de version anterior en VPS
".tmp\tools\plink.exe" -ssh -P %VPS_PORT% -l %VPS_USER% -pw "%VPS_PASS%" ^
  -hostkey "%HOSTKEY%" %VPS_HOST% ^
  "docker tag myapp:latest myapp:previous 2>/dev/null; echo previous_tagged"

@REM 4. Git pull + deploy
".tmp\tools\plink.exe" -ssh -P %VPS_PORT% -l %VPS_USER% -pw "%VPS_PASS%" ^
  -hostkey "%HOSTKEY%" %VPS_HOST% ^
  "cd %APP_DIR% && git pull && docker compose pull && docker compose up -d"

@REM 5. Health check
for /l %%i in (1,1,12) do (
  curl -sf http://%VPS_HOST%/health >nul 2>&1 && (
    echo Deploy OK — SHA: %GIT_SHA%
    exit /b 0
  )
  timeout /t 5 /nobreak >nul
)

@REM 6. Rollback si falla health check
echo Health check fallo — ejecutando rollback...
".tmp\tools\plink.exe" -ssh -P %VPS_PORT% -l %VPS_USER% -pw "%VPS_PASS%" ^
  -hostkey "%HOSTKEY%" %VPS_HOST% ^
  "cd %APP_DIR% && docker compose down && docker tag myapp:previous myapp:latest && docker compose up -d"
```

## 5. Pipeline CI/CD con Rollback Automatico

```yaml
name: Deploy with Auto Rollback
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      
      - name: Login to registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: |
            ghcr.io/${{ github.repository }}:latest
            ghcr.io/${{ github.repository }}:previous
            ghcr.io/${{ github.repository }}:${{ github.sha }}
      
      - name: Deploy with health check
        uses: appleboy/ssh-action@v1
        id: deploy
        continue-on-error: true
        with:
          host: ${{ secrets.VPS_HOST }}
          port: ${{ secrets.VPS_PORT }}
          username: ${{ secrets.VPS_USER }}
          password: ${{ secrets.VPS_PASSWORD }}
          script: |
            set -e
            cd /opt/app
            docker compose pull
            docker compose up -d
            # Health check (60s timeout)
            for i in $(seq 1 12); do
              STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/health || echo "000")
              [ "$STATUS" = "200" ] && { echo "OK"; exit 0; }
              sleep 5
            done
            echo "HEALTH_FAILED" && exit 1
      
      - name: Rollback on failure
        if: steps.deploy.outcome == 'failure'
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.VPS_HOST }}
          port: ${{ secrets.VPS_PORT }}
          username: ${{ secrets.VPS_USER }}
          password: ${{ secrets.VPS_PASSWORD }}
          script: |
            cd /opt/app
            docker compose down
            docker tag ghcr.io/${{ github.repository }}:previous ghcr.io/${{ github.repository }}:latest
            docker compose up -d
      
      - name: Verify rollback
        if: steps.deploy.outcome == 'failure'
        run: |
          sleep 10
          curl -sf http://${{ secrets.VPS_HOST }}/health && echo "Rollback OK" || echo "Rollback FAILED"
      
      - name: Notify
        if: always()
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "Deploy ${{ job.status }} para ${{ github.repository }}"
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

## 6. Comandos Rapidos de Rollback

```bash
# Rollback inmediato en VPS (ultima version estable)
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "pass" -hostkey "..." ^
  167.114.169.134 "docker compose down && docker compose up -d"

# Rollback a version especifica
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "pass" -hostkey "..." ^
  167.114.169.134 ^
  "docker compose down && docker tag myapp:v1.2.2 myapp:latest && docker compose up -d"

# Rollback en Kubernetes
kubectl rollout undo deployment/myapp
kubectl rollout status deployment/myapp

# Rollback en Cloud Run
gcloud run services update-traffic myapp --to-revisions=myapp-00001-abc=100

# Listar revisiones disponibles
docker images myapp --format "table {{.Tag}}\t{{.Size}}\t{{.CreatedAt}}"
```
