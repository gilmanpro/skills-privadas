# Arranque Automatico del Motor de Contenedores (Windows)

> Detalle de la seccion 3.4 de guia.md (rama Despliegue de dev-stack). Pasos esenciales en guia.md.

> **NOTA:** Esto NO es sobre comandos Docker — es sobre asegurar que el motor de contenedores este disponible. El usuario puede usar **Docker Desktop** o **Rancher Desktop** (recomendado como alternativa gratuita y open-source).

## 1. Detectar qué motor está instalado

```bash
@REM Detectar Docker Desktop
where docker >nul 2>&1 && echo docker CLI disponible

@REM Detectar Rancher Desktop
where rdctl >nul 2>&1 && echo rdctl disponible
where nerdctl >nul 2>&1 && echo nerdctl disponible

@REM Detectar si el daemon responde
docker info >nul 2>&1 && echo Daemon corriendo || echo Daemon NO corriendo
```

## 2. Opcion A: Rancher Desktop (recomendado como alternativa)

Rancher Desktop es open-source, incluye Kubernetes (K3s) integrado, y soporta tanto `dockerd` (moby) como `containerd` como motor.

```bash
@REM Detectar si Rancher Desktop esta instalado
where rdctl >nul 2>&1
if %errorlevel% equ 0 (
    echo Rancher Desktop instalado
    rdctl list-settings >nul 2>&1
    if %errorlevel% equ 0 (
        echo Rancher Desktop corriendo
    ) else (
        echo Rancher Desktop NO corriendo
    )
)

@REM Arrancar Rancher Desktop
@REM Usa moby (dockerd) para compatibilidad total con docker CLI
start "" "%LOCALAPPDATA%\Programs\Rancher Desktop\Rancher Desktop.exe"
@REM O via rdctl:
rdctl start --container-engine moby --kubernetes-enabled=false

@REM Esperar a que el daemon responda
for /l %i in (1,1,24) do (
  docker info >nul 2>&1 && (
    echo Rancher Desktop listo
    goto :ready
  )
  echo Esperando Rancher Desktop... intento %i de 24
  timeout /t 5 /nobreak >nul
)
:ready

@REM Configurar Rancher Desktop sin Kubernetes (si no se necesita)
rdctl set --kubernetes-enabled=false

@REM Verificar que DOCKER_HOST este configurado (Rancher lo hace automaticamente)
echo DOCKER_HOST=%DOCKER_HOST%
```

**Nota sobre `nerdctl`**: Si usas Rancher Desktop con `containerd` (no `moby`), el CLI es `nerdctl` en vez de `docker`. La sintaxis es casi idéntica:
```bash
nerdctl ps                     # como docker ps
nerdctl compose up -d          # como docker compose
nerdctl build -t myapp .       # como docker build
nerdctl run -d --name test nginx  # como docker run
nerdctl images                 # como docker images
```

**Ventajas de Rancher Desktop sobre Docker Desktop:**
- Gratuito y open-source (sin licencia comercial)
- Kubernetes integrado (K3s) liviano
- Menor consumo de recursos
- Soporta `containerd` nativamente
- `rdctl` CLI para automatización

## 3. Opcion B: Docker Desktop

```bash
@REM Detectar Docker Desktop
where docker >nul 2>&1 && echo docker CLI disponible

@REM Arranque via protocolo URI
start "" "docker-desktop://"
@REM O via ejecutable directo
start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
start "" "%LOCALAPPDATA%\Programs\Docker\Docker\Docker Desktop.exe"

@REM Espera al daemon (10-60s)
for /l %i in (1,1,12) do (
  docker info >nul 2>&1 && (
    echo Docker Desktop listo
    goto :dd-ready
  )
  echo Esperando Docker Desktop... intento %i de 12
  timeout /t 5 /nobreak >nul
)
:dd-ready
```

## 4. Si NINGUN motor esta instalado

Informar al usuario y sugerir:
1. **Rancher Desktop** (recomendado): https://rancherdesktop.io/
2. **Docker Desktop**: https://www.docker.com/products/docker-desktop/

NO intentar instalar automaticamente sin autorizacion.
