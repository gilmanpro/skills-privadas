
# Compilación — Empaquetado Multiplataforma

Referencia práctica de comandos para compilar y distribuir aplicaciones Python, Go y Java en Windows, Linux, macOS, Android, iOS y Web.

---

## Python — PyInstaller (apps de escritorio, ttkbootstrap, tkinter)

**NO es cross-compiler** → build en cada SO destino.

### Onefile (un solo .exe)

```bash
pyinstaller --onefile --windowed --name AppName main.py
pyinstaller --onefile --windowed -i icon.ico --name AppName main.py
pyinstaller --onefile --windowed --add-data "assets;assets" --name AppName main.py  # (Windows usa ";", Linux/macOS ":")
```

### Onedir (carpeta con ejecutable)

```bash
pyinstaller --onedir --windowed --name AppName main.py
```

### Con .spec (recomendado para proyectos complejos)

```bash
# Primera vez (genera el .spec automáticamente)
pyinstaller --onefile --windowed --name AppName main.py

# Luego editas el .spec y haces rebuild con:
pyinstaller --noconfirm --distpath dist --workpath build_pyi AppName.spec
```

### ttkbootstrap / tkinter (hidden imports)

```bat
pyinstaller --onefile --windowed --name AppName ^
  --hidden-import=ttkbootstrap --hidden-import=tkinter ^
  --hidden-import=PIL._tkinter_finder --collect-all ttkbootstrap ^
  --add-data "assets;assets" main.py
```

### .spec para ttkbootstrap (ejemplo completo)

```python
# -*- mode: python ; coding: utf-8 -*-
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('assets', 'assets')],
    hiddenimports=['ttkbootstrap', 'tkinter', 'PIL._tkinter_finder'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz, a.scripts, a.binaries, a.datas, [],
    name='AppName', debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, upx_exclude=[], runtime_tmpdir=None,
    console=False, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None,
    codesign_identity=None, entitlements_file=None, icon='icon.ico',
)
app = BUNDLE(exe, name='AppName.app', icon=None, bundle_identifier=None)
```

### Flags importantes

| Flag | Efecto |
|---|---|
| `--onefile` | Un solo .exe |
| `--onedir` | Carpeta + ejecutable |
| `--windowed` / `--noconsole` | Sin terminal (GUI) |
| `--console` | Con terminal |
| `--hidden-import=X` | Fuerza inclusión de módulo |
| `--collect-all X` | Incluye todo de un paquete |
| `--add-data SRC;DST` | Archivos estáticos |
| `--icon X.ico` | Icono del .exe |
| `--version-file X.txt` | Metadatos Windows |
| `--noconfirm` | Sobrescribe sin preguntar |
| `--distpath DIR` | Carpeta de salida |
| `--workpath DIR` | Carpeta temporal |
| `--clean` | Limpia caché antes de build |

---

## Python — Flet (multiplataforma: Win/Mac/Linux/Android/iOS/Web)

**Soporta cross-compilation vía Flutter.** Build en Windows → Android (WSL), Linux, Web.

### Estructura del proyecto

```
mi-app/
├── pyproject.toml     # dependencias y configuración
├── src/
│   ├── main.py        # entry point con ft.run(main) (Flet <1.0: ft.app(main))
│   └── assets/
│       ├── icon.png           # 512x512 (fallback)
│       ├── icon_windows.ico   # 256x256 (Windows)
│       ├── icon_macos.png     # 1024x1024 (macOS)
│       ├── icon_android.png   # 192x192 (Android)
│       ├── icon_web.png       # 512x512 (Web)
│       └── splash.png         # pantalla de carga
```

### Comandos por plataforma

```bash
flet build windows               # .exe
flet build macos                  # .app
flet build linux                  # AppImage/ejecutable
flet build apk                    # Android .apk
flet build aab                    # Android App Bundle
flet build ipa                    # iOS .ipa (solo macOS)
flet build ios-simulator          # iOS Simulator (solo macOS) - verificar disponibilidad con flet build --help
flet build web                    # HTML/JS estático
```

### Ejemplo completo con opciones

```bat
REM Flags documentados: --product, --org, --bundle-id, --build-number, -o, --verbose
REM --company, --build-version, --exclude, --compile-app, --cleanup-app y -v:
REM verificar con: flet build windows --help (flags varían por versión)
flet build windows ^
  --product "Mi App" --company "MiEmpresa" ^
  --build-version 1.0.0 --build-number 1 ^
  --org com.miempresa --bundle-id com.miempresa.mi_app ^
  --exclude .git .venv tests ^
  --compile-app --cleanup-app ^
  -o ./dist -v
```

### pyproject.toml completo

```toml
[project]
name = "mi_app"
version = "1.0.0"
dependencies = ["flet"]

[tool.flet]
product = "Mi App"
org = "com.miempresa"
build_number = 1
company = "MiEmpresa"
copyright = "Copyright © 2025 MiEmpresa"

[tool.flet.app]
path = "src"
module = "main.py"
hide_window_on_start = false

[tool.flet.splash]
color = "#ffffff"
dark_color = "#333333"

[tool.flet.compile]
app = true
packages = true

[tool.flet.cleanup]
app = true
packages = true
app_files = ["**/*.c", "**/*.h"]

[tool.flet.permissions]
permissions = ["camera", "location"]
```

### Matriz de compilación Flet

| Build en → | Win | Android | iOS | macOS | Linux | Web |
|---|---|---|---|---|---|---|
| **macOS** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Windows** | ✅ | ✅ (WSL) | ❌ | ❌ | ✅ | ✅ |
| **Linux** | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ |

---

## Go (Golang) — Cross-compilation nativa

**Sí es cross-compiler** — un solo comando produce binarios para cualquier plataforma.

### Compilación básica

```bash
go build -o app.exe main.go
go build -ldflags="-s -w" -o app.exe main.go
go build -ldflags="-s -w -X main.version=1.0.0 -X main.commit=$(git rev-parse --short HEAD) -X main.date=$(date +%F)" -o app.exe main.go
```

### Cross-compilation (GOOS + GOARCH)

```bash
# Windows (AMD64)
GOOS=windows GOARCH=amd64 go build -ldflags="-s -w" -o dist/app.exe main.go

# Linux (AMD64)
GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o dist/app-linux main.go

# macOS Intel
GOOS=darwin GOARCH=amd64 go build -ldflags="-s -w" -o dist/app-macos-intel main.go

# macOS Apple Silicon
GOOS=darwin GOARCH=arm64 go build -ldflags="-s -w" -o dist/app-macos-arm64 main.go

# Raspberry Pi (ARM 32-bit)
GOOS=linux GOARCH=arm GOARM=7 go build -ldflags="-s -w" -o dist/app-arm main.go

# ARM64 (RPi 3+ / servers)
GOOS=linux GOARCH=arm64 go build -ldflags="-s -w" -o dist/app-arm64 main.go

# WebAssembly
GOOS=js GOARCH=wasm go build -ldflags="-s -w" -o dist/app.wasm main.go
```

Variante en Windows (cmd.exe) — sintaxis original con `set X=Y&&` y `%DATE%`:

```bat
REM Windows (AMD64)
set GOOS=windows&& set GOARCH=amd64&& go build -ldflags="-s -w" -o dist/app.exe main.go

REM Linux (AMD64)
set GOOS=linux&& set GOARCH=amd64&& go build -ldflags="-s -w" -o dist/app-linux main.go

REM macOS Intel
set GOOS=darwin&& set GOARCH=amd64&& go build -ldflags="-s -w" -o dist/app-macos-intel main.go

REM macOS Apple Silicon
set GOOS=darwin&& set GOARCH=arm64&& go build -ldflags="-s -w" -o dist/app-macos-arm64 main.go

REM Raspberry Pi (ARM 32-bit)
set GOOS=linux&& set GOARCH=arm&& set GOARM=7&& go build -ldflags="-s -w" -o dist/app-arm main.go

REM ARM64 (RPi 3+ / servers)
set GOOS=linux&& set GOARCH=arm64&& go build -ldflags="-s -w" -o dist/app-arm64 main.go

REM WebAssembly
set GOOS=js&& set GOARCH=wasm&& go build -ldflags="-s -w" -o dist/app.wasm main.go

REM Metadatos de version con fecha del sistema (cmd.exe usa %DATE%; en bash: $(date +%F))
go build -ldflags="-s -w -X main.version=1.0.0 -X main.date=%DATE%" -o app.exe main.go
```

### Script build todo-en-uno (batch)

```batch
@echo off
set LDFLAGS=-s -w -X main.version=1.0.0 -X main.commit=%GIT_COMMIT%
mkdir dist 2>nul

set GOOS=windows&& set GOARCH=amd64&& go build -ldflags="%LDFLAGS%" -o dist/app.exe main.go
set GOOS=linux&&   set GOARCH=amd64&& go build -ldflags="%LDFLAGS%" -o dist/app-linux main.go
set GOOS=darwin&&  set GOARCH=amd64&& go build -ldflags="%LDFLAGS%" -o dist/app-macos main.go
set GOOS=darwin&&  set GOARCH=arm64&& go build -ldflags="%LDFLAGS%" -o dist/app-macos-arm64 main.go

echo Build complete: dist/
dir dist
```

### CGO cross-compilation

```bash
# Windows desde Linux/macOS (requiere mingw-w64)
CGO_ENABLED=1 GOOS=windows GOARCH=amd64 CC=x86_64-w64-mingw32-gcc go build -o app.exe

# Linux desde macOS
CGO_ENABLED=1 GOOS=linux GOARCH=amd64 CC=x86_64-linux-gnu-gcc go build -o app-linux
```

### Reducción de tamaño

```bash
# Strip debug symbols
go build -ldflags="-s -w" -o app.exe main.go

# UPX compression (instalar UPX primero)
upx --best --lzma dist/app.exe
upx --best --lzma dist/app-linux

# Binario 100% estático (sin CGO)
CGO_ENABLED=0 go build -ldflags="-s -w" -o app.exe main.go
```

### Lista de combinaciones soportadas

```bash
go tool dist list
```

**GOOS:** `linux`, `darwin`, `windows`, `freebsd`, `netbsd`, `openbsd`, `android`, `ios`, `dragonfly`, `illumos`, `solaris`, `plan9`, `aix`, `js`, `wasip1`

**GOARCH:** `amd64`, `386`, `arm`, `arm64`, `ppc64`, `ppc64le`, `mips`, `mips64`, `mipsle`, `mips64le`, `s390x`, `riscv64`, `loong64`, `wasm`

---

## Java — JAR y jpackage

### JAR ejecutable

```bash
javac -d out src/miempresa/Main.java
echo Main-Class: miempresa.Main > MANIFEST.MF
jar cfm app.jar MANIFEST.MF -C out .
java -jar app.jar
```

### Fat JAR con Maven (Shade Plugin)

```bash
mvn clean package
# target/app.jar con todas las dependencias
```

### jpackage (instaladores nativos, JDK 16+, NO cross-compiler)

```bash
# App image (carpeta portable)
jpackage --type app-image -n App -i input --main-jar app.jar --main-class miempresa.Main

# Windows .exe
jpackage --type exe -n App --app-version 1.0.0 --icon icon.ico -i input --main-jar app.jar --main-class miempresa.Main --win-menu --win-shortcut

# Windows .msi
jpackage --type msi -n App --app-version 1.0.0 -i input --main-jar app.jar --main-class miempresa.Main

# macOS .dmg
jpackage --type dmg -n App --app-version 1.0.0 --icon icon.icns -i input --main-jar app.jar --main-class miempresa.Main

# macOS .pkg
jpackage --type pkg -n App --app-version 1.0.0 -i input --main-jar app.jar --main-class miempresa.Main

# Linux .deb
jpackage --type deb -n app --app-version 1.0.0 -i input --main-jar app.jar --main-class miempresa.Main

# Linux .rpm
jpackage --type rpm -n app --app-version 1.0.0 -i input --main-jar app.jar --main-class miempresa.Main

# JRE mínimo (jlink)
jpackage --type exe -n App -i input --main-jar app.jar --main-class miempresa.Main --add-modules java.base,java.desktop

# Con runtime image custom
jlink --output runtime --add-modules java.base,java.desktop --strip-debug --no-header-files --no-man-pages
jpackage --type exe -n App --runtime-image runtime -i input --main-jar app.jar --main-class miempresa.Main
```

---

## Resumen multiplataforma

| App tipo | Herramienta | ¿Cross-compile? | Comando principal |
|---|---|---|---|
| Python desktop (tk, ttkbootstrap) | PyInstaller | ❌ (build por SO) | `pyinstaller --onefile --windowed app.spec` |
| Python Flet | `flet build` | ✅ (vía Flutter) | `flet build windows / apk / web` |
| Go CLI/server | `go build` | ✅ (GOOS+GOARCH) | `go build -ldflags="-s -w" -o app` |
| Java desktop | `jpackage` | ❌ (build por SO) | `jpackage --type exe -n App --main-jar app.jar` |

### Build en Windows para múltiples plataformas

| Quiero → | Uso |
|---|---|
| .exe Windows (Python) | PyInstaller en Windows |
| .exe Windows (Go) | `GOOS=windows GOARCH=amd64 go build` |
| Linux binary (Go) | `GOOS=linux GOARCH=amd64 go build` |
| macOS binary (Go) | `GOOS=darwin GOARCH=amd64 go build` |
| Android .apk (Flet) | `flet build apk` (con WSL si estás en Windows) |
| Web (Flet) | `flet build web` |
| Java .exe/.msi | `jpackage` en Windows |
| Java .dmg | `jpackage` en macOS |
| Java .deb/.rpm | `jpackage` en Linux |
