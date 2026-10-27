# CLI de Flet - Referencia Completa

## Comandos principales

### `flet create [name]`
Crea un nuevo proyecto Flet con estructura básica.
```bash
flet create myapp
cd myapp
flet run
```

### `flet run [script]`
Ejecuta una app Flet.
```bash
flet run app.py                    # Ventana nativa
flet run --web app.py              # Navegador web
flet run --port 8080 app.py        # Puerto específico
flet run --host 0.0.0.0 app.py     # Accesible desde la red
flet run --directory src/          # Directorio de trabajo
flet run --assets assets/          # Directorio de assets
flet run --hidden                  # Ventana oculta al inicio
flet run --no-rack                 # Sin servidor Rack
flet run --no-web-server           # Sin servidor web
```

### `flet build <platform>`
Compila la app para distribución.
```bash
flet build apk                     # Android APK
flet build aab                     # Android AAB (Google Play)
flet build ipa                     # iOS
flet build windows                 # Windows
flet build macos                   # macOS
flet build linux                   # Linux
flet build web                     # Web
```

### `flet publish` (LEGACY)
> **LEGACY:** reemplazado por `flet build web` desde Flet 0.18. Se conserva solo como referencia histórica; puede no existir en versiones actuales (verificar con `flet --help`).

Publica app web estática en `dist/`.
```bash
flet publish                       # Publicar web
flet publish --output-dir docs/    # Directorio personalizado
flet publish --base-url /myapp/    # URL base
```

### `flet pack <script>` (LEGACY)
> **LEGACY:** reemplazado por `flet build windows` (y `flet build <platform>` para otros destinos) desde Flet 0.18. Se conserva solo como referencia histórica; puede no existir en versiones actuales (verificar con `flet --help`).

Empaqueta app con PyInstaller.
```bash
flet pack app.py                   # Empaquetar
flet pack --icon icon.ico app.py   # Con icono
flet pack --name "MiApp" app.py    # Nombre personalizado
flet pack --onedir app.py          # Directorio (vs onefile)
flet pack --console app.py         # Mostrar consola
flet pack --add-data "assets:assets" app.py  # Incluir assets
```

### `flet test`
Ejecuta tests de la app.
```bash
flet test                          # Ejecutar tests
flet test --verbose                # Modo verbose
flet test --coverage               # Con cobertura
```

> Comandos no confirmados en la documentación oficial — verifica disponibilidad con `flet --help` en tu versión antes de usarlos.

### `flet debug` (no documentado — verificar)
Prueba la app en un dispositivo móvil conectado.
```bash
flet debug                         # Debug en dispositivo
flet debug --device emulator-5554  # Dispositivo específico
```

### `flet devices` (no documentado — verificar)
Lista dispositivos conectados.
```bash
flet devices                       # Listar dispositivos
```

### `flet doctor`
Diagnostica el entorno de desarrollo.
```bash
flet doctor                        # Diagnóstico completo
```

### `flet clean` (no documentado — verificar)
Limpia cachés y archivos temporales.
```bash
flet clean                         # Limpiar todo
flet clean --build                 # Solo build
flet clean --cache                 # Solo caché
```

### `flet serve`
Sirve una app ya compilada.
```bash
flet serve                         # Servir app compilada
flet serve --port 8080             # Puerto específico
```

### `flet mcp` (no documentado — verificar)
Inicia el servidor MCP (Model Context Protocol).
```bash
flet mcp                           # Iniciar servidor MCP
```

### `flet emulators` (no documentado — verificar)
Gestiona emuladores Android.
```bash
flet emulators                     # Listar emuladores
flet emulators create              # Crear emulador
```

### `flet --version`
Muestra la versión instalada.
```bash
flet --version                     # Versión
flet -V                            # Versión (abreviado)
```

## Opciones globales

| Opción | Descripción |
|--------|-------------|
| `--help` | Muestra ayuda del comando |
| `--version` | Muestra versión |
| `--verbose` | Logs detallados |
| `--no-color` | Sin colores en output |

## Variables de entorno

| Variable | Descripción |
|----------|-------------|
| `FLET_DESKTOP_FLAVOR` | `full` o `light` (audio/video en Linux) |
| `FLET_WEB_PORT` | Puerto para servidor web |
| `FLET_WEB_HOST` | Host para servidor web |
| `FLET_ASSETS_DIR` | Directorio de assets |
| `FLET_UPLOAD_DIR` | Directorio de uploads |
| `FLET_SECRET_KEY` | Clave secreta para sesiones |
| `FLET_SESSION_TIMEOUT` | Timeout de sesión en minutos |
| `FLET_MAX_UPLOAD_SIZE` | Tamaño máximo de upload |
| `FLET_OAUTH_STATE_TIMEOUT` | Timeout de estado OAuth |
| `FLET_BUILD_NO_STRIP` | No stripear binarios |
| `FLET_BUILD_VERBOSE` | Logs detallados de build |
| `FLET_ANDROID_KEYSTORE_PATH` | Ruta al keystore Android |
| `FLET_ANDROID_KEYSTORE_PASSWORD` | Password del keystore |
| `FLET_ANDROID_KEY_ALIAS` | Alias del key |
| `FLET_ANDROID_KEY_PASSWORD` | Password del key |