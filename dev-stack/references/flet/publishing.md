# Publicación de Apps Flet

## Requisitos previos

```bash
pip install 'flet[all]'
```

## Comandos de build

| Plataforma | Comando | Requisitos |
|------------|---------|------------|
| Android APK | `flet build apk` | Android SDK |
| Android AAB | `flet build aab` | Android SDK |
| iOS | `flet build ipa` | macOS + Xcode |
| Windows | `flet build windows` | Windows |
| macOS | `flet build macos` | macOS |
| Linux | `flet build linux` | Linux |
| Web | `flet build web` | — |

## Opciones comunes de build

| Opción | Descripción |
|--------|-------------|
| `--project <name>` | Nombre del proyecto |
| `--company <name>` | Nombre de la compañía |
| `--description <text>` | Descripción de la app |
| `--version <x.y.z>` | Versión de la app |
| `--build-number <n>` | Número de build |
| `--icon <path>` | Ruta al icono de la app |
| `--splash <path>` | Ruta a la splash screen |
| `--include-packages <pkgs>` | Paquetes adicionales a incluir |
| `--exclude-packages <pkgs>` | Paquetes a excluir |
| `--compile` | Compilar a bytecode (por defecto desde v0.86) |
| `--no-compile` | No compilar a bytecode |
| `--output-dir <path>` | Directorio de salida |
| `--release` | Build de release |
| `--debug` | Build de debug |

## Publicación Web

### Sitio estático
```bash
flet publish
```
Esto genera una carpeta `dist/` con los archivos estáticos.

### Hosting
- **Cloudflare Pages**: Subir carpeta `dist/`
- **GitHub Pages**: Subir `dist/` a `gh-pages` branch
- **Netlify**: Arrastrar `dist/` al panel

### Sitio dinámico (FastAPI)
```bash
flet build web
```
Luego servir con FastAPI:
```python
from flet_fastapi import flet_app
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/", flet_app(main))
```

### Hosting dinámico
- **Fly.io**: Usar Dockerfile con `flet build web`
- **Replit**: Usar `flet run --web`
- **Self-hosting**: Servidor Python con FastAPI + Gunicorn/Uvicorn

## Publicación Android

```bash
# APK (debug)
flet build apk --debug

# APK (release - requiere keystore)
flet build apk --release

# AAB (Google Play)
flet build aab --release
```

### Configuración Android
```bash
flet build apk \
  --project "MiApp" \
  --company "com.miempresa" \
  --description "Descripción" \
  --version "1.0.0" \
  --build-number 1 \
  --icon "assets/icon.png" \
  --splash "assets/splash.png"
```

### Keystore para release
```bash
keytool -genkey -v -keystore release.keystore -alias my-key -keyalg RSA -keysize 2048 -validity 10000
flet build apk --release --keystore-path release.keystore --keystore-password <pass> --keystore-alias my-key
```

## Publicación iOS

```bash
flet build ipa
```
Requiere macOS con Xcode y una cuenta de desarrollador de Apple.

## Publicación Windows

```bash
flet build windows
```
Genera un ejecutable `.exe` en `build/windows/`.

## Publicación macOS

```bash
flet build macos
```
Genera un `.app` bundle en `build/macos/`.

## Publicación Linux

```bash
flet build linux
```
Genera un ejecutable en `build/linux/`.

## pyproject.toml (configuración de proyecto)

```toml
[tool.flet]
project = "MiApp"
company = "com.miempresa"
description = "Descripción de la app"
version = "1.0.0"
build_number = 1
icon = "assets/icon.png"
splash = "assets/splash.png"
compile = true
desktop_flavor = "full"

[tool.flet.android]
package = "com.miempresa.miapp"
permissions = ["INTERNET", "CAMERA"]

[tool.flet.ios]
bundle_id = "com.miempresa.miapp"
```

## Variables de entorno para build

| Variable | Descripción |
|----------|-------------|
| `FLET_DESKTOP_FLAVOR` | `full` o `light` (audio/video) |
| `FLET_BUILD_NO_STRIP` | No stripear binarios |
| `FLET_BUILD_VERBOSE` | Logs detallados |
| `FLET_ANDROID_KEYSTORE_PATH` | Ruta al keystore |
| `FLET_ANDROID_KEYSTORE_PASSWORD` | Password del keystore |
| `FLET_ANDROID_KEY_ALIAS` | Alias del key |
| `FLET_ANDROID_KEY_PASSWORD` | Password del key |