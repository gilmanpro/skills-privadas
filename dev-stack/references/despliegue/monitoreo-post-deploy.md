# Monitoreo Post-Deploy

> Detalle de la seccion 10 de guia.md (rama Despliegue de dev-stack).


Sistema completo de monitoreo post-deploy que verifica health, rendimiento, errores, y notifica automaticamente.

## 1. Health Check Post-Deploy (Multi-endpoint)

```bash
#!/bin/bash
# scripts/post-deploy-health.sh
# Uso: ./post-deploy-health.sh <base_url> [timeout_segundos]
set -euo pipefail

BASE_URL="${1:-http://localhost:3000}"
TIMEOUT="${2:-60}"
INTERVAL=5
MAX_RETRIES=$((TIMEOUT / INTERVAL))
PASS=0
FAIL=0

echo "=== HEALTH CHECK POST-DEPLOY ==="
echo "Target: $BASE_URL"
echo "Timeout: ${TIMEOUT}s\n"

check_endpoint() {
    local NAME="$1"
    local URL="$2"
    local EXPECTED="${3:-200}"
    
    for i in $(seq 1 $MAX_RETRIES); do
        local STATUS CODE BODY
        CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$URL" 2>/dev/null || echo "000")
        BODY=$(curl -s --max-time 5 "$URL" 2>/dev/null || echo "")
        
        if [ "$CODE" = "$EXPECTED" ]; then
            echo "  ✔ $NAME — HTTP $CODE (intento $i)"
            PASS=$((PASS + 1))
            return 0
        fi
        echo "  ⏳ $NAME — HTTP $CODE, esperando $EXPECTED (intento $i/$MAX_RETRIES)..."
        sleep $INTERVAL
    done
    
    echo "  ✗ $NAME — FALLÓ después de $MAX_RETRIES intentos (ultimo: HTTP $CODE)"
    FAIL=$((FAIL + 1))
    return 1
}

# Endpoints críticos
check_endpoint "Pagina principal"   "$BASE_URL/" 200
check_endpoint "Health endpoint"   "$BASE_URL/health" 200
check_endpoint "API status"        "$BASE_URL/api/status" 200
check_endpoint "Static assets"     "$BASE_URL/favicon.ico" 200

echo ""
echo "=== RESUMEN ==="
echo "Pasaron: $PASS | Fallaron: $FAIL"
[ "$FAIL" -eq 0 ] && echo "✔ HEALTH CHECK GLOBAL: OK" || echo "✗ HEALTH CHECK GLOBAL: FALLÓ"
exit $FAIL
```

## 2. Monitoreo de Rendimiento (Benchmark Post-Deploy)

```bash
#!/bin/bash
# scripts/benchmark-deploy.sh — Compara rendimiento antes/despues del deploy
# Uso: ./benchmark-deploy.sh <url> [iteraciones]

URL="${1:-http://localhost:3000}"
ITERATIONS="${2:-10}"

echo "=== BENCHMARK POST-DEPLOY ==="
echo "URL: $URL"
echo "Muestras: $ITERATIONS\n"

total=0
min=999
max=0
p50_times=()

for i in $(seq 1 $ITERATIONS); do
    result=$(curl -s -o /dev/null -w "%{time_total}\t%{http_code}\t%{size_download}" --max-time 10 "$URL" 2>/dev/null)
    time_val=$(echo "$result" | cut -f1)
    http_code=$(echo "$result" | cut -f2)
    size=$(echo "$result" | cut -f3)
    
    total=$(echo "$total + $time_val" | bc 2>/dev/null || echo "0")
    min=$(echo "$time_val $min" | awk '{if ($1 < $2) print $1; else print $2}')
    max=$(echo "$time_val $max" | awk '{if ($1 > $2) print $1; else print $2}')
    p50_times+=("$time_val")
    
    printf "  Request %2d: %.4fs | HTTP %s | %s bytes\n" $i $time_val $http_code $size
done

avg=$(echo "scale=4; $total / $ITERATIONS" | bc)
jitter=$(echo "scale=4; $max - $min" | bc)

# Calcular p50
IFS=$'\n' sorted=($(sort <<<"${p50_times[*]}")); unset IFS
mid=$((ITERATIONS / 2))
p50="${sorted[$mid]}"

echo ""
echo "=== RESULTADOS ==="
echo "  Minimo:   ${min}s"
echo "  Maximo:   ${max}s"
echo "  Promedio: ${avg}s"
echo "  P50:      ${p50}s"
echo "  Jitter:   ${jitter}s"
echo ""

# Alertas
if (( $(echo "$avg > 2.0" | bc -l) )); then
    echo "⚠  LATENCIA ALTA — Promedio > 2s. Revisar si el deploy afecto rendimiento."
fi
if (( $(echo "$jitter > 1.0" | bc -l) )); then
    echo "⚠  JITTER ALTO — Variabilidad > 1s. Posible inestabilidad post-deploy."
fi
```

## 3. Logs Estructurados Post-Deploy

```javascript
// Ejemplo Node.js con Pino (logger estructurado)
const pino = require('pino');
const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  formatters: {
    level: (label) => ({ level: label }),
  },
  timestamp: () => `,"time":"${new Date().toISOString()}"`,
  redact: ['req.headers.authorization', 'req.body.password'], // NO loggear secretos
});

logger.info({ 
  event: 'deploy_completed',
  version: process.env.APP_VERSION,
  commit: process.env.COMMIT_SHA,
  duration: '45s',
  status: 'success'
}, 'Nueva version desplegada');
```

```bash
# Ver logs post-deploy desde VPS
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "docker logs --tail 100 --timestamps app_container"

# Logs en tiempo real post-deploy
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "docker logs -f --tail 50 app_container"
```

## 4. Dashboard de Monitoreo (Docker + VPS)

```yaml
# docker-compose.monitoring.yml — Stack de monitoreo + deploy
services:
  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    ports:
      - "9090:9090"
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    volumes:
      - grafana_data:/var/lib/grafana
    ports:
      - "3001:3000"  # No conflict con la app
    restart: unless-stopped

  node-exporter:
    image: prom/node-exporter:latest
    network_mode: host
    restart: unless-stopped

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
    ports:
      - "8080:8080"
    restart: unless-stopped

volumes:
  prometheus_data:
  grafana_data:
```

```bash
# Desplegar stack de monitoreo junto a la app
docker compose -f docker-compose.yml -f docker-compose.monitoring.yml up -d

# Deploy en VPS con monitoreo incluido
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "
    cd /opt/app
    docker compose -f docker-compose.yml -f docker-compose.monitoring.yml pull
    docker compose -f docker-compose.yml -f docker-compose.monitoring.yml up -d
  "
```

## 5. Alertas Post-Deploy

```yaml
# prometheus.yml — Reglas de alerta post-deploy
groups:
  - name: deploy_alerts
    rules:
      - alert: DeployFailed
        expr: up{job="app"} == 0
        for: 1m
        annotations:
          summary: "App caida despues del deploy"
      
      - alert: HighLatency
        expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 2
        for: 2m
        annotations:
          summary: "Latencia p95 > 2s post-deploy"
      
      - alert: ErrorRateSpike
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
        for: 1m
        annotations:
          summary: "Tasa de error > 5% post-deploy"
```

```bash
# Verificar alertas en VPS despues del deploy
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "
    curl -s http://localhost:9090/api/v1/alerts | jq '.data.alerts[] | select(.state==\"firing\")'
  "
```

## 6. Checklist de Verificacion Post-Deploy

```bash
# Ejecutar todo el checklist post-deploy en VPS
".tmp\tools\plink.exe" -ssh -P 10000 -l debian -pw "password" -hostkey "..." ^
  167.114.169.134 "
    echo '=== CHECKLIST POST-DEPLOY ==='
    
    # 1. Contenedores corriendo
    echo '[1/6] Contenedores:' && docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
    
    # 2. Logs sin errores (ultimas 50 lineas)
    echo '[2/6] Ultimos errores:' && docker logs app --tail 50 2>&1 | grep -i error || echo '  Sin errores'
    
    # 3. Health endpoint
    echo '[3/6] Health:' && curl -s -o /dev/null -w 'HTTP %{http_code}\n' http://localhost:3000/health
    
    # 4. Uso de recursos
    echo '[4/6] Recursos:' && docker stats app --no-stream --format 'CPU: {{.CPUPerc}} | RAM: {{.MemUsage}}'
    
    # 5. Disco disponible
    echo '[5/6] Disco:' && df -h / | tail -1 | awk '{print \"Usado: \" 100-\$5 \"% libre\"}'
    
    # 6. Version deployada
    echo '[6/6] Version:' && docker images myapp --format 'latest -> {{.CreatedAt}}' | head -1
    
    echo '=== CHECKLIST COMPLETADO ==='
  "
```
