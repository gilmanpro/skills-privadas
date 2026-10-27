
# Despliegue y DevOps — Super Skill Unificada (Docker + CI/CD + Cloud)

## METADATA DE INVOCACIÓN

**Agentes que me pueden cargar:**
- `@operario` — modo TOOLBOX (diagnóstico de deploy/Docker) y ACCIONES (operaciones puntuales)
- `@builder` — durante la construcción cuando se dockeriza el proyecto o se necesita CI/CD
- `@lector` — durante revisión de Dockerfile/compose/CI workflows/nginx.conf
- `@estratega` — para fundamentar decisiones de contenedorización y deployment
- `@operario` — cuando la consulta es puramente Docker o DevOps

**HERRAMIENTAS REQUERIDAS en el agente que me carga:**
- `bash` — para ejecutar Docker, `aws`, `az`, `gcloud`, `kubectl`, `nginx`, `certbot`
- `read` — para leer Dockerfile, compose, .env.example, nginx.conf
- `glob` — para encontrar archivos Docker/deploy en el proyecto
- `grep` — para buscar patrones en Dockerfile/compose/CI workflows
- `webfetch` — para consultar docs cloud actualizadas
- `skill` — para cargarme

**REFERENCIAS INCLUIDAS** (cargables con `read`): 9 archivos en `references/despliegue/` (4 Docker + 5 de despliegue) — ver **Indice de References** (seccion 16, al final del documento).

**CUÁNDO CARGARME (triggers):**
- **Docker puro:** "docker", "contenedor", "container", "imagen", "Dockerfile", "docker-compose", "docker compose", "docker run", "docker ps", "docker logs", "docker exec", "levanta este docker-compose", "construye esta imagen"
- **Rancher Desktop:** "Rancher Desktop", "rancher", "rdctl", "nerdctl", "containerd", "motor de contenedores", "alternativa a Docker Desktop"
- **Despliegue/DevOps:** "desplegar", "deploy", "deployment", "llevar a producción", "CI/CD", "pipeline", "GitHub Actions", "GitLab CI", "Jenkins", "AWS", "Azure", "GCP", "EC2", "ECS", "Lambda", "App Service", "Cloud Run", "Nginx", "reverse proxy", "SSL", "Let's Encrypt", "HTTPS", "blue-green", "canary", "rolling update", "rollback", "monitoreo", "health check", "staging", "produccion", ".env", "variables de entorno"
- **VPS/SSH:** "VPS", "servidor remoto", "SSH", "SCP", "transferir archivos", "PLINK", "PSCP", "PuTTY", "llevar al servidor", "deploy en VPS"
- **Rollback:** "rollback automatico", "revertir deploy", "deshacer deploy", "volver a version anterior", "recuperar produccion"
- **Post-deploy:** "verificar deploy", "health check post-deploy", "benchmark post-deploy", "checklist post-deploy", "monitorear deploy", "alertas post-deploy"
- Cualquier tarea de infra donde Docker, despliegue o DevOps sea la herramienta

**NO ME CARGUES SI:**
- La consulta es puramente teórica ("qué es Docker", "qué es CI/CD") → mejor `@omni`
- La tarea es de seguridad de infra → cargar skill `ciberseguridad`
- La consulta es de diseno UI de dashboards → cargar skill `dev-stack` (rama frontend-design / UI-UX Pro Max)

**SKILLS COMPLEMENTARIAS:**
- `@curl-expert` — para debugging de conectividad HTTP/TLS con el VPS
- `@ciberseguridad` — hardening del servidor, firewalls, certificados

---

## 1. Regla de Oro — Alcance de Esta Skill

Esta skill cubre **Docker + Despliegue + DevOps** en un solo lugar. Todo lo que necesitas está aquí o en las referencias oficiales Docker. NO improvises flags ni configuraciones.

- **Tarea 100% Docker** (Dockerfile, compose, comandos puntuales) → usa las referencias Docker de esta misma skill (sección 3).
- **Tarea de despliegue puro** (CI/CD, cloud, Nginx, SSL, monitoreo, estrategias) → usa las secciones DevOps (sección 4 en adelante).
- **Tarea mixta** (dockerizar + desplegar) → primero Docker (referencias), luego CI/CD (sección 4).

---

## 2. Flujo de Trabajo General

```
INICIO
  │
  ├─ 1. ENTENDER EL TARGET
  │     - Tipo: app web, API, microservicio, batch, static site, ML
  │     - Stack: lenguaje, framework, base de datos, dependencias
  │     - Destino: ¿donde se va a desplegar? (Docker local, cloud, k8s, etc.)
  │     - Entornos: dev, staging, prod (cuantos, como se promueven)
  │
  ├─ 2. ANALIZAR EL PROYECTO
  │     - Leer package.json / requirements.txt / go.mod / etc.
  │     - Identificar entry point, puerto, comandos de build/start
  │     - Verificar si ya hay Dockerfile / compose / pipeline existente
  │     - Identificar variables de entorno necesarias
  │
  ├─ 3. ELEGIR ESTRATEGIA
  │     - Contenedor vs nativo
  │     - Cloud especifico o agnóstico
  │     - Pipeline simple vs complejo
  │     - Estrategia de rollout: rolling, blue-green, canary
  │
  ├─ 4. DOCKER (si aplica)
  │     - Construir Dockerfile usando `references/despliegue/dockerfile.md`
  │     - Crear docker-compose.yml usando `references/despliegue/docker-compose.md`
  │     - Usar `references/despliegue/docker-run.md` para comandos puntuales
  │     - Usar `references/despliegue/docker-commands.md` para ps/logs/exec
  │     - Si Docker no corre: arrancar Docker Desktop (sección 3.4)
  │
  ├─ 5. PREPARAR ARCHIVOS DEPLOYMENT (NO Docker)
  │     - Pipeline CI/CD (.github/workflows/*.yml, .gitlab-ci.yml)
  │     - .env.example (plantilla de variables, sin secretos)
  │     - nginx.conf (reverse proxy, si aplica)
  │     - scripts/deploy.sh, scripts/rollback.sh
  │     - docs/deployment.md (instrucciones)
  │
  ├─ 6. CONFIRMAR CON USUARIO
  │     - Mostrar plan completo
  │     - Preguntar antes de aplicar en produccion
  │     - Advertir comandos destructivos
  │
  ├─ 7. EJECUTAR
  │     - Trigger pipeline (push a rama, manual dispatch)
  │     - O ejecutar comandos cloud (aws, az, gcloud)
  │
  └─ 8. VERIFICAR Y REPORTAR
        - Health checks
        - Logs
        - URLs/endpoints accesibles
        - Comando de rollback documentado
```

---

## 3. Docker — Comandos Precisos (usa las referencias)

### 3.1 Reglas Estrictas para Docker

1. **NO improvises flags, opciones o sintaxis.** Cada flag que uses debe existir en las referencias oficiales.
2. **Siempre genera el comando completo** con todas las opciones necesarias, no fragments.
3. **Si no encuentras una opción en las referencias, no la uses.** Mejor omítela o pregunta al usuario.
4. **Usa rutas absolutas o relativas explícitas** en volúmenes y bind mounts.
5. **Explica brevemente cada flag** que uses para que el usuario entienda qué hace.

### 3.2 Como Usar las Referencias Docker

| Necesitas | Carga este archivo |
|-----------|--------------------|
| `docker run` con puertos, volúmenes, env, redes, recursos, restart | `references/despliegue/docker-run.md` |
| Crear/editar un `Dockerfile` (FROM, RUN, COPY, ENV, CMD, ENTRYPOINT, multi-stage) | `references/despliegue/dockerfile.md` |
| Crear/editar un `docker-compose.yml` (services, networks, volumes, healthcheck) | `references/despliegue/docker-compose.md` |
| `docker build`, `docker exec`, `docker logs`, `docker ps`, `docker network`, `docker volume`, `docker image` | `references/despliegue/docker-commands.md` |

**Regla:** Carga SOLO el archivo que necesites para la tarea actual. No los cargues todos si no hace falta.

### 3.3 Patrones Comunes Docker (Quick Reference)

**docker run — ejecutar un contenedor:**
```bash
docker run -d \
  --name <nombre> \
  -p <host>:<container>/<protocol> \
  -e <VAR>=<value> \
  -v <host_path>:<container_path> \
  --restart <policy> \
  <imagen>:<tag>
```

**docker-compose.yml — estructura base:**
```yaml
services:
  <nombre>:
    image: <imagen>:<tag>
    container_name: <nombre>
    ports:
      - "<host>:<container>"
    environment:
      - <VAR>=<value>
    volumes:
      - <host_path>:<container_path>
    restart: <policy>
```

**Dockerfile — estructura base:**
```dockerfile
FROM <imagen>:<tag>
WORKDIR /app
COPY . .
RUN <comando>
EXPOSE <puerto>
CMD ["<executable>", "<arg>"]
```

### 3.4 Arranque Automatico del Motor de Contenedores (Windows)

Si el daemon no responde (`docker info` falla), intenta primero **Rancher Desktop** (`rdctl start --container-engine moby --kubernetes-enabled=false` o lanzar su ejecutable, esperando en loop hasta que `docker info` funcione) y, si no existe, **Docker Desktop** (abrir `docker-desktop://` o su ejecutable, esperando 10-60s al daemon). Verifica siempre con `docker info`. Con el motor `containerd` de Rancher Desktop el CLI es `nerdctl` (sintaxis casi identica a `docker`). Si NINGUN motor esta instalado, informar y sugerir Rancher Desktop (recomendado) o Docker Desktop — NO instalar sin autorizacion.

Detalle completo (deteccion de motores, `rdctl`, `nerdctl`, scripts de arranque): `references/despliegue/motor-contenedores-windows.md`.

### 3.5 Verificacion Post-Generacion Docker

1. Revisa que todos los flags usados existen en la referencia oficial
2. Verifica que los puertos no tengan typos (formato `host:container/protocol`)
3. Verifica que las rutas de volúmenes sean válidas (absolutas o relativas explícitas)
4. Confirma que el nombre del contenedor no tenga caracteres inválidos
5. Para docker-compose.yml: verifica indentación (2 espacios)
6. Para Dockerfile: verifica que las instrucciones estén en MAYÚSCULAS

### 3.6 Ejemplos Practicos Docker

**PostgreSQL con docker run:**
```
Usuario: "Levanta un PostgreSQL 16 con puerto 5432, contraseña segura, y volumen persistente"

Comando:
docker run -d \
  --name postgres-db \
  -p 5432:5432 \
  -e POSTGRES_PASSWORD=mi_password_segura \
  -e POSTGRES_DB=mydb \
  -v postgres_data:/var/lib/postgresql/data \
  --restart unless-stopped \
  postgres:16
```

**Node.js + MongoDB con docker-compose:**
```
Usuario: "Crea un docker-compose.yml para Node.js con MongoDB"

docker-compose.yml:
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - MONGO_URI=mongodb://mongo:27017/mydb
    depends_on:
      - mongo
    restart: unless-stopped

  mongo:
    image: mongo:7
    volumes:
      - mongo_data:/data/db
    restart: unless-stopped

volumes:
  mongo_data:
```

**Dockerfile multi-stage optimizado para Go:**
```
Usuario: "Necesito un Dockerfile optimizado para Go"

Dockerfile:
# syntax=docker/dockerfile:1
FROM golang:1.22 AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o /app/server .

FROM alpine:3.20
RUN apk add --no-cache ca-certificates
COPY --from=builder /app/server /server
EXPOSE 8080
CMD ["/server"]
```

---

## 4. Estructura Recomendada del Proyecto (Deployment)

```
proyecto/
├── Dockerfile                  # Construir con references/despliegue/dockerfile.md
├── .dockerignore               # Ver references/despliegue/dockerfile.md
├── docker-compose.yml          # Ver references/despliegue/docker-compose.md
├── .env.example                # Plantilla de variables (sin secretos)
├── .github/
│   └── workflows/
│       ├── ci.yml              # Tests + lint
│       └── deploy.yml          # Build + push + deploy
├── nginx/
│   └── default.conf            # Reverse proxy
├── scripts/
│       ├── deploy.sh           # Script de despliegue
│       ├── healthcheck.sh      # Verificacion post-deploy
│       └── rollback.sh         # Reversión
└── docs/
    └── deployment.md           # Guia completa
```

---

## 5. GitHub Actions CI/CD (template)

Template de pipeline completo: job de test (checkout, setup-node, lint, test), job build-and-push a GHCR con `docker/build-push-action` y cache de GitHub Actions, y job de deploy al servidor via `appleboy/ssh-action` (`docker compose pull` + `up -d`).

Plantilla YAML lista para copiar: `references/despliegue/cicd-nginx-templates.md` (seccion 1).

---

## 6. Nginx Reverse Proxy (template)

Template de `nginx.conf`: upstream a la app, redirect 80 a 443, certificados de Let's Encrypt, TLS 1.2/1.3, headers de seguridad (HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy), rate limiting, gzip, `proxy_pass` con headers de WebSocket y `X-Forwarded-*`, y location `/health`.

Plantilla completa: `references/despliegue/cicd-nginx-templates.md` (seccion 2).

---

## 7. Estrategias de Despliegue

### 7.1 Rolling Update
- **Como:** actualizar instancias una a una (o en pequenos grupos)
- **Pros:** sin downtime, simple
- **Contras:** durante el rollout hay 2 versiones coexistiendo
- **Ideal para:** apps stateless, microservicios

### 7.2 Blue-Green
- **Como:** dos entornos identicos, switch instantaneo de trafico
- **Pros:** rollback trivial (volver al anterior), cero riesgo
- **Contras:** duplicacion de recursos durante el deploy
- **Ideal para:** apps criticas, deploys riesgosos

### 7.3 Canary
- **Como:** desplegar nueva version a 5-10% del trafico, monitorear, expandir
- **Pros:** validacion real con usuarios, riesgo minimizado
- **Contras:** requiere router que divida trafico (NGINX, service mesh)
- **Ideal para:** validar cambios grandes, A/B testing

### 7.4 Feature Flags
- **Como:** desplegar codigo inactivo, activarlo remotamente
- **Pros:** desacopla deploy de release, kill switch instantaneo
- **Contras:** complejidad en el codigo, deuda tecnica si no se limpia
- **Ideal para:** features grandes, gradual rollout

---

## 8. Cloud — Comandos Rapidos

### AWS
```bash
# EC2
aws ec2 run-instances --image-id ami-xxx --instance-type t3.micro --key-name mi-key
aws ec2 describe-instances --filters "Name=tag:Name,Values=mi-app"

# ECS
aws ecs update-service --cluster mi-cluster --service mi-service --force-new-deployment

# ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin xxx.dkr.ecr.us-east-1.amazonaws.com
docker push xxx.dkr.ecr.us-east-1.amazonaws.com/mi-app:latest

# S3
aws s3 sync ./build s3://mi-bucket --delete
```

### Azure
```bash
az login
az webapp create --resource-group mi-rg --plan mi-plan --name mi-app --deployment-container-image-name mi-acr.azurecr.io/mi-app:latest
az webapp restart --name mi-app --resource-group mi-rg
```

### GCP
```bash
gcloud auth login
gcloud run deploy mi-app --image gcr.io/mi-proyecto/mi-app --platform managed --region us-central1 --allow-unauthenticated
```

---

## 9. SSL/TLS con Let's Encrypt

```bash
# Instalar certbot
sudo apt install certbot python3-certbot-nginx

# Obtener certificado
sudo certbot --nginx -d ejemplo.com -d www.ejemplo.com

# Verificar renovacion automatica
sudo certbot renew --dry-run

# Cron job (usualmente ya configurado, pero por si acaso)
0 0 1 * * certbot renew --quiet
```

---

## 10. Monitoreo Post-Deploy

Sistema de verificacion post-deploy: health check multi-endpoint con reintentos (`post-deploy-health.sh`), benchmark de rendimiento antes/despues (`benchmark-deploy.sh`), logs estructurados con Pino y lectura remota via PLINK, dashboard Prometheus + Grafana + node-exporter + cAdvisor (`docker-compose.monitoring.yml`), reglas de alerta (DeployFailed, HighLatency, ErrorRateSpike) y checklist de 6 puntos ejecutable en el VPS.

Scripts, configs y comandos completos: `references/despliegue/monitoreo-post-deploy.md`.

---

## 11. Rollback Automatico

Rollback automatico con deteccion de fallos: `rollback.sh` en Docker Compose (health check y reversion al tag `previous`), rollback en VPS remoto via PLINK (`rollback-vps.bat`), deploy con notificacion a webhook (`deploy-with-rollback.sh`), estrategia Git + Docker recomendada (imagenes taggeadas con git SHA y `previous`, nunca rebuild en el VPS), pipeline CI/CD con auto-rollback y comandos rapidos de reversion (VPS, Kubernetes, Cloud Run).

Scripts y ejemplos completos: `references/despliegue/rollback.md`.

---

## 12. Integracion con Otras Skills y Agentes

| Necesidad | Recurso |
|---|---|
| Comandos Docker exactos / Dockerfile / compose | Usar `references/despliegue/docker-*.md` de esta skill |
| Auditoria de seguridad del deploy | Cargar skill `ciberseguridad` |
| Revisar configuracion de deploy existente | Derivar a `@lector` para escaneo a fondo |
| Aplicar cambios al codigo | Derivar a `@builder` o `@operario` (ACCIONES) |
| Configurar SSL | Seccion 9 de esta skill + consultar docs oficiales |
| Troubleshooting de red/proxy | `curl -v`, `nslookup`, `dig`, `traceroute` |
| Diseno UI de dashboards de monitoreo | Cargar skill `dev-stack` (rama frontend-design / UI-UX Pro Max) |

---

## 13. Comportamientos Obligatorios

- ✅ **SIEMPRE** responder en espanol
- ✅ **SIEMPRE** usar las referencias Docker (`references/despliegue/docker-*.md`) en vez de improvisar flags
- ✅ **SIEMPRE** confirmar antes de desplegar a produccion
- ✅ **SIEMPRE** validar sintaxis YAML/JSON antes de aplicar
- ✅ **SIEMPRE** documentar comandos para que el usuario los repita
- ✅ **SIEMPRE** usar variables de entorno para secretos (nunca hardcoded)
- ✅ **SIEMPRE** dejar documentado el comando de rollback
- ✅ **SIEMPRE** arrancar el motor de contenedores automaticamente si no corre (Rancher Desktop primero, luego Docker Desktop)
- ✅ **SIEMPRE** verificar si el usuario usa Rancher Desktop antes de asumir Docker Desktop
- ❌ **NUNCA** desplegar a produccion sin confirmacion explicita
- ❌ **NUNCA** exponer credenciales en archivos commiteados
- ❌ **NUNCA** pedir al usuario que abra el motor de contenedores manualmente

---

## 14. Ejemplos de Uso

| Solicitud del usuario | Que hacer |
|---|---|
| "Levanta un PostgreSQL 16 con docker" | Seccion 3.6 (PostgreSQL) + `references/despliegue/docker-run.md` |
| "Crea un Dockerfile multi-stage para Go" | Seccion 3.6 (Go) + `references/despliegue/dockerfile.md` |
| "Crea un docker-compose para Node + Mongo" | Seccion 3.6 (Node + Mongo) + `references/despliegue/docker-compose.md` |
| "Configura CI/CD con GitHub Actions" | Seccion 5 (template de pipeline) + `references/despliegue/cicd-nginx-templates.md` (seccion 1) |
| "Despliega a produccion" | Pedir confirmacion, ejecutar pipeline, verificar health |
| "Haz un blue-green deployment" | Seccion 7.2 + configurar dos entornos + router |
| "Configura SSL con Let's Encrypt" | Seccion 9 (Certbot) |
| "Crea pipeline de deploy a AWS" | GitHub Actions + ECR + ECS o Elastic Beanstalk |
| "Como hago rollback?" | Seccion 11 (Docker, k8s, Cloud Run) + `references/despliegue/rollback.md` |
| "Docker no arranca" | Seccion 3.4 + `references/despliegue/motor-contenedores-windows.md` |
| "Usar Rancher Desktop" | Seccion 3.4 + `references/despliegue/motor-contenedores-windows.md` (rdctl, moby vs containerd, nerdctl) |
| "rdctl comandos" | `references/despliegue/motor-contenedores-windows.md` (rdctl start, rdctl set) |
| "nerdctl en vez de docker" | `references/despliegue/motor-contenedores-windows.md` (nerdctl compose, nerdctl build, nerdctl run) |
| "Lleva archivos al VPS" | Seccion 15 + `references/despliegue/vps-ssh-deploy.md` seccion 3 (SCP/PSCP) |
| "Ejecuta comando en el VPS" | Seccion 15 + `references/despliegue/vps-ssh-deploy.md` seccion 4 (SSH/PLINK remoto) |
| "Despliega Docker en VPS remoto" | Seccion 15 + `references/despliegue/vps-ssh-deploy.md` seccion 5 (Build local + push + deploy remoto) |
| "Transfiere skill/config a servidor" | `references/despliegue/vps-ssh-deploy.md` seccion 3 (rsync, pscp, scp) |
| "Rollback automatico con health check" | `references/despliegue/rollback.md` secciones 1-5 (scripts deploy-with-rollback.sh) |
| "Rollback con git + Docker tags" | `references/despliegue/rollback.md` seccion 4 (estrategia hibrida) |
| "Monitoreo post-deploy" | `references/despliegue/monitoreo-post-deploy.md` seccion 1 (health check multi-endpoint) |
| "Benchmark de rendimiento post-deploy" | `references/despliegue/monitoreo-post-deploy.md` seccion 2 (benchmark-deploy.sh) |
| "Dashboard de monitoreo con Docker" | `references/despliegue/monitoreo-post-deploy.md` seccion 4 (Prometheus + Grafana + cAdvisor) |
| "Deploy zero-downtime" | `references/despliegue/vps-ssh-deploy.md` seccion 6, Escenario 3 (rolling update Docker Swarm) |
| "Deploy con migraciones de BD" | `references/despliegue/vps-ssh-deploy.md` seccion 6, Escenario 2 (deploy-with-migrations.sh) |
| "Deploy multi-servicio/microservicios" | `references/despliegue/vps-ssh-deploy.md` seccion 6, Escenario 4 (docker-compose.microservices.yml) |
| "Deploy multi-entorno (staging/prod)" | `references/despliegue/vps-ssh-deploy.md` seccion 6, Escenario 1 (docker-compose override) |
| "Alertas post-deploy" | `references/despliegue/monitoreo-post-deploy.md` seccion 5 (Prometheus alerts + Slack webhook) |
| "Checklist de verificacion post-deploy" | `references/despliegue/monitoreo-post-deploy.md` seccion 6 (6 puntos de verificacion automatizada) |

---

## 15. VPS / Servidor Remoto — SSH, Transferencia y Despliegue

Trabajo con servidores remotos desde Windows: PLINK/PSCP descargados en `.tmp\tools` del proyecto (NO borrar), manejo del host key, transferencia con SCP/PSCP/rsync, ejecucion remota de comandos y deploy Docker (build local -> push a registry -> pull remoto; sin registry con `docker save`/`load`). Escenarios avanzados: compose override multi-entorno, migraciones de BD, zero-downtime con Swarm, microservicios, `.env` por ambiente y cache de build. Autenticacion: password con PLINK/PSCP (recomendada) o SSH keys; pipeline CI/CD a VPS via SSH y debugging de conexion.

Detalle completo (11 secciones renumeradas): `references/despliegue/vps-ssh-deploy.md`.

---

## 16. Indice de References

| Archivo | Que contiene | Cuando cargarlo (trigger) |
|---|---|---|
| `references/despliegue/docker-run.md` | Todas las opciones de `docker run` (puertos, volumenes, env, redes, recursos, restart) | Necesitas un `docker run` con flags exactos |
| `references/despliegue/dockerfile.md` | Todas las instrucciones de Dockerfile (FROM, RUN, COPY, ENV, CMD, ENTRYPOINT, multi-stage) | Crear o editar un `Dockerfile` |
| `references/despliegue/docker-compose.md` | Formato completo de `docker-compose.yml` (services, networks, volumes, healthcheck) | Crear o editar un `docker-compose.yml` |
| `references/despliegue/docker-commands.md` | `docker build`, `docker exec`, `docker logs`, `docker ps`, `docker network`, `docker volume`, `docker image` | Comandos de imagenes, contenedores, redes y volumenes |
| `references/despliegue/motor-contenedores-windows.md` | Arranque del motor en Windows: deteccion, Rancher Desktop (`rdctl`, `nerdctl`), Docker Desktop, espera del daemon | "Docker no arranca", "Rancher Desktop", "rdctl", "nerdctl", motor caido |
| `references/despliegue/cicd-nginx-templates.md` | Template de pipeline GitHub Actions (test, build/push GHCR, deploy SSH) y template de `nginx.conf` reverse proxy con SSL | "Configura CI/CD", "GitHub Actions", "nginx", "reverse proxy" |
| `references/despliegue/monitoreo-post-deploy.md` | Health check multi-endpoint, benchmark, logs estructurados, dashboard Prometheus/Grafana, alertas y checklist post-deploy | "verificar deploy", "health check", "monitoreo/alertas/checklist post-deploy" |
| `references/despliegue/rollback.md` | Scripts de rollback (compose, VPS/PLINK, notificacion), estrategia Git+Docker, pipeline con auto-rollback, comandos rapidos | "rollback", "revertir deploy", "volver a version anterior" |
| `references/despliegue/vps-ssh-deploy.md` | PLINK/PSCP y host key, SCP/PSCP/rsync, ejecucion remota, deploy Docker en VPS, escenarios avanzados, auth password vs keys, CI/CD a VPS, debugging | "VPS", "servidor remoto", "SSH", "SCP", "PLINK", "llevar al servidor" |

**Regla:** Carga SOLO el archivo que necesites para la tarea actual. No los cargues todos si no hace falta.
