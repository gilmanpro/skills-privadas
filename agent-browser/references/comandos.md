# Referencia de comandos

Referencia completa de los comandos de `agent-browser` (version verificada: 0.39.4). Para el flujo de trabajo y patrones comunes, ver [SKILL.md](../SKILL.md). Esta referencia complementa a la upstream versionada: `agent-browser skills get core --full` (en ingles) sigue siendo la fuente canon si tu version difiere; tambien `agent-browser <comando> --help`.

**Indice**: [Navegacion](#navegacion) · [Snapshot](#snapshot-analisis-de-pagina) · [Interacciones](#interacciones-usar-refs-del-snapshot) · [Informacion y estado](#obtener-informacion-y-estado) · [Capturas y PDF](#capturas-y-pdf) · [Video](#grabacion-de-video) · [Esperas](#esperas) · [Raton](#raton) · [Localizadores](#localizadores-semanticos-alternativa-a-refs) · [Ajustes](#ajustes-del-navegador) · [Cookies y storage](#cookies-y-almacenamiento) · [Red](#red) · [Pestanas](#pestanas-y-ventanas) · [Frames y dialogos](#frames-y-dialogos) · [JavaScript](#javascript) · [Auth y plugins](#autenticacion-y-plugins) · [Estado y streaming](#estado-streaming-y-webmcp) · [Panel y MCP](#panel-y-servidor-mcp) · [Opciones globales](#opciones-globales) · [Depuracion](#depuracion) · [React](#react--web-vitals) · [a11y](#auditoria-de-accesibilidad) · [Init scripts](#init-scripts-y-cookies-curl) · [Variables de entorno](#variables-de-entorno)

## Navegacion

```bash
agent-browser open            # Lanza el navegador sin navegar (queda en about:blank);
                              # util con network route / cookies set --curl / addinitscript
                              # para preparar estado antes de la primera navegacion
agent-browser open <url>      # Lanza + navega (alias: goto, navigate)
                              # Soporta https://, http://, file://, about:, data://
                              # Si no hay protocolo, antepone https://
agent-browser read [url]      # Texto legible para agentes, o DOM renderido del tab activo
                              # Con URL explicita envia Accept: text/markdown, luego prueba .md
                              # Busca llms.txt en rutas ascendentes antes de caer a HTML
                              # Opciones: --raw, --require-md, --outline, --llms <index|full>,
                              #          --filter <texto>, --timeout <ms>
agent-browser back            # Atras
agent-browser forward         # Adelante
agent-browser reload          # Recargar
agent-browser pushstate <url> # Navegacion SPA lado cliente (auto-detecta el router de Next)
agent-browser close           # Cerrar el navegador (alias: quit, exit)
agent-browser connect 9222    # Conectar a un navegador via puerto CDP
```

Tras `connect`, la sesion queda pegada hasta `close`: los comandos siguientes sin bandera de conexion van contra ese mismo navegador; si desaparece, fallan en vez de lanzar uno local. `connect` y `--cdp` esperan hasta 2s a que se abra el puerto de depuracion.

### Preparacion previa a la navegacion (lote en una tanda)

```bash
agent-browser batch \
  '["open"]' \
  '["network","route","*","--abort","--resource-type","script"]' \
  '["cookies","set","--curl","cookies.curl","--domain","localhost"]' \
  '["navigate","http://localhost:3000/targeto"]'
```

`open` sin URL lanza limpio para que rutas, cookies o init scripts surtan efecto en la **primera** navegacion real. Con `--json`, `--omit-command` sustituye cada array `command` por un `index` estable (no hace la salida segura para secretos: `type`, `get value` y `eval` pueden devolver valores escritos).

## Snapshot (analisis de pagina)

```bash
agent-browser snapshot              # Arbol de accesibilidad completo
agent-browser snapshot -i           # Solo interactivos (recomendado)
agent-browser snapshot -c           # Salida compacta
agent-browser snapshot -d 3         # Tope de profundidad 3
agent-browser snapshot -s "#main"   # Acotado a selector CSS
agent-browser snapshot --delta      # Estado completo una vez, luego deltas estructurales acotados
agent-browser snapshot --delta --full  # Fuerza estado completo y refresca la base
```

El historial de deltas es por pestana y conjunto de opciones. La respuesta es `full`, `unchanged` o `delta`; cambios de URL o deltas grandes devuelven estado completo. En un delta se aplican los cambios (`add`, `remove`, `replace`) sobre los metadatos de refs partiendo el arbol anterior en lineas y reemplazando desde `startLine` durante `deleteCount` lineas, sobre `baseRevision` antes de avanzar a `revision`; con `--full` si la base no esta disponible.

## Interacciones (usar `@refs` del snapshot)

```bash
agent-browser click @e1             # Clic (falla si esta oculto/deshabilitado/fuera de viewport
                                    # o si lo tapa otro elemento: "covered by <div#banner>")
agent-browser click @e1 --new-tab   # Clic abriendo en pestana nueva (abre la URL directamente)
agent-browser dblclick @e1          # Doble clic
agent-browser focus @e1             # Foco
agent-browser fill @e2 "texto"      # Limpia y escribe
agent-browser type @e2 "texto"      # Escribe sin limpiar
agent-browser press Enter           # Tecla (alias: key); combinaciones: press Control+a
agent-browser keydown Shift         # Mantener tecla / keyup Shift soltar
agent-browser hover @e1             # Hover
agent-browser check @e1 / uncheck @e1
agent-browser select @e1 "valor"    # Por valor o etiqueta visible; varias: select @e1 "a" "b"
agent-browser scroll down 300       # up/down/left/right (defecto: down 300px)
agent-browser scrollintoview @e1    # Alias: scrollinto
agent-browser drag @e1 @e2          # Arrastrar y soltar
agent-browser upload @e1 archivo.pdf
```

El emparejado de etiquetas visibles trata igual espacio duro y normal. `click --new-tab` abre la URL del enlace, por lo que no aplica el chequeo de cobertura.

## Obtener informacion y estado

```bash
agent-browser get text @e1          # Texto del elemento
agent-browser get html @e1          # innerHTML
agent-browser get value @e1         # Valor del input
agent-browser get attr @e1 href     # Atributo
agent-browser get title             # Titulo de la pagina
agent-browser get url               # URL actual
agent-browser get cdp-url           # URL WebSocket del CDP
agent-browser get count ".item"     # Cuenta elementos que coinciden
agent-browser get box @e1           # Bounding box
agent-browser get styles @e1        # Estilos computados

agent-browser is visible @e1        # Comprobaciones de estado
agent-browser is enabled @e1
agent-browser is checked @e1
```

## Capturas y PDF

```bash
agent-browser screenshot            # Directorio temporal (ruta en stdout)
agent-browser screenshot ruta.png   # Ruta concreta
agent-browser screenshot --full     # Pagina completa
agent-browser screenshot --annotate mapa.png   # Etiquetas [N] ligadas a refs @eN
agent-browser screenshot --if-changed          # Recomendado: omitir si no cambio (ahorra tokens)
agent-browser screenshot --threshold 0.01      # Ignora cambios de hasta 1% de pixeles (implica --if-changed)
agent-browser pdf salida.pdf
```

`--threshold <0-1>` implica `--if-changed`; el historial condicional es por pestana y alcance. El JSON incluye `changed`, `revision`, `pixelChangeRatio`, `threshold` y `path` solo cuando hay cambio. Headless oculta las barras de scroll nativas: `--hide-scrollbars false` las conserva.

## Grabacion de video

```bash
agent-browser open https://example.com
agent-browser record start ./demo.webm              # 30 fps por defecto
agent-browser click @e1
agent-browser record stop                           # Guarda y detiene
agent-browser record restart ./toma2.webm           # Detiene la actual + inicia otra
agent-browser record start ./scroll.webm --fps 60   # 1..60; bajo (10) para sesiones largas
agent-browser record start ./demo.webm --cursor     # Puntero animado
agent-browser record start ./demo.webm --contact-sheet  # Resumen PNG con marcas de tiempo
```

Requiere `ffmpeg` en PATH y ruta con extension. `--contact-sheet-threshold <0-1>` ajusta la sensibilidad de keyframes e implica `--contact-sheet`. El cursor se renderiza con la pagina (arrastrables sincronizados), su overlay inerte esta oculto para los snapshots de accesibilidad y se elimina al parar.

## Esperas

```bash
agent-browser wait @e1                       # Elemento
agent-browser wait 2000                      # Milisegundos (ultimo recurso)
agent-browser wait --text "Exito"            # Texto (alias -t)
agent-browser wait --url "**/dashboard"      # Patron URL glob (alias -u)
agent-browser wait --load domcontentloaded   # Ciclo de vida (alias -l): domcontentloaded | load | networkidle
agent-browser wait --fn "window.ready"       # Condicion JS (alias -f)
```

Tras una accion que cambia la pagina, espera el selector/texto/URL/condicion que representa el resultado buscado. `networkidle` solo en paginas conocidas por calmarse (SSE, WebSockets, polling impiden que resuelva). Timeout por defecto 25s.

## Ratón

```bash
agent-browser mouse move 100 200
agent-browser mouse move 600 400 --duration 250 --steps 24
agent-browser mouse move 600 400 --human --seed 42   # trayectoria reproducible
agent-browser mouse down left / mouse up left
agent-browser mouse wheel 100
```

`--human` en `click`/`drag` cuando importa el trayecto del puntero: empieza en la posicion actual y termina en el objetivo; `--seed` lo hace reproducible. `--duration` es duracion total objetivo (incluye respuesta del navegador).

## Localizadores semanticos (alternativa a refs)

```bash
agent-browser find role button click --name "Submit"
agent-browser find role heading text --name "Skills"   # roles implicitos: <h2>=heading, <ul>=list, <header>=banner
agent-browser find text "Sign In" click                # --exact para coincidencia exacta
agent-browser find label "Email" fill "user@test.com"
agent-browser find placeholder "Search" fill "query"
agent-browser find alt "Logo" click
agent-browser find title "Close" click
agent-browser find testid "submit-btn" click
agent-browser find first ".item" click / find last ".item" click / find nth 2 "a" hover
```

## Ajustes del navegador

```bash
agent-browser set viewport 1920 1080           # Con 3er arg: 2x retina (mismo CSS, capturas en alta)
agent-browser set device "iPhone 14"           # Emular dispositivo
agent-browser set geo 37.7749 -122.4194        # Geolocalizacion (alias: geolocation)
agent-browser set offline on                   # Modo sin conexion
agent-browser set headers '{"X-Key":"v"}'      # Headers HTTP extra
agent-browser set credentials user pass        # HTTP basic auth (alias: auth)
agent-browser set media dark                   # Esquema de color; tambien: set media light reduced-motion
```

## Cookies y almacenamiento

```bash
agent-browser cookies                  # Todas
agent-browser cookies set nombre valor
agent-browser cookies clear
agent-browser storage local            # localStorage: / <clave> / set k v / clear
agent-browser cookies set --curl <f>    # Importa JSON/cURL/Cookie-header (auto-deteccion)
agent-browser cookies set --curl <f> --domain example.com
```

Formatos soportados: array JSON de `{name, value}`, cURL copiado de DevTools (Network → Copy as cURL) o cabecera Cookie pura. Los errores nunca imprimen valores de cookies.

## Red

```bash
agent-browser network route <url>              # Interceptar peticiones
agent-browser network route <url> --abort      # Bloquear
agent-browser network route <url> --body '{}'  # Mock de respuesta
agent-browser network unroute [url]            # Quitar rutas
agent-browser network requests [--filter api]  # Peticiones rastreadas
agent-browser network request <requestId>      # Detalle completo con body
agent-browser network har start [--content all|none]  # Grabar trafico (embebe bodies de texto por defecto)
agent-browser network har stop [salida.har]

agent-browser network route '*' --abort --resource-type script               # Por tipo de recurso
agent-browser network route '*' --resource-type image,font --body ''         # Stub de imagenes/fuentes
```

## Pestanas y ventanas

```bash
agent-browser tab                        # Lista con tabId (t1, t2, ...) y etiqueta
agent-browser tab new [url]              # Nueva (--label docs [url] para etiqueta)
agent-browser tab t2 / tab docs          # Cambiar por id o etiqueta (intercambiables)
agent-browser tab close [t2|docs]        # Cerrar actual o por id/etiqueta
agent-browser window new
```

Los ids son cadenas estables `t<N>`, nunca reusadas en la sesion; `tab 2` es error (usa `t2`). Las etiquetas son unicas por sesion, no se generan solas ni se reescriben al navegar. `tab list --json` tambien da el `targetId` del CDP (valido donde acepten ref de tab y estable reinicios de daemon, a diferencia de `t<N>`). Las pestanas nuevas heredan la configuracion de la sesion (user agent, headers, credenciales, init scripts, rutas, emulacion) antes de cargar su primer documento. `--pin-tab` fija la sesion a su tab: si lo cierran, error `tab_gone` (`code`, `data.targetId`, `data.lastUrl` sanearizado) en vez de tocar otro tab; `tab new`/`tab list` recuperan. Al cambiar a un tab descartado (Memory Saver) la pagina recarga: `"revived": true`; un tab pausado por dialogo da `"dialogBlocked": true` (resolver con `dialog`); cerrar el tab activo sobre uno descartado da `"activeTabRevived": true`.

## Frames y dialogos

```bash
agent-browser frame "#iframe"     # Por selector CSS
agent-browser frame @e3           # Por ref de elemento
agent-browser frame main          # Volver al main frame

agent-browser dialog accept [texto]   # Aceptar (con texto para prompt)
agent-browser dialog dismiss          # Cancelar
agent-browser dialog status           # Dialogo pendiente?
```

Los iframes se detectan en el snapshot y su contenido se inlinea un nivel (iframes dentro de iframes no se expanden); sus refs funcionan directamente. `frame` acepta ref, selector CSS o nombre/URL del frame. `alert` y `beforeunload` se aceptan solos por defecto (`--no-auto-dialog` lo desactiva).

## JavaScript

```bash
agent-browser eval "document.title"   # Solo expresiones simples
agent-browser eval -b "<base64>"      # Cualquier JS (base64)
agent-browser eval --stdin            # Script por stdin (heredoc)
```

Con comillas anidadas o caracteres especiales, usa `-b` o `--stdin`: el escaping de la shell es propenso a fallos.

## Autenticacion y plugins

```bash
agent-browser auth save <nombre> --url <url> --username <u> --password-stdin
agent-browser auth login <nombre>                    # Rellena + clic, espera el formulario
agent-browser auth login <nombre> --no-navigate      # Usa la pagina activa tras validar mismo origen
agent-browser auth login <nombre> --credential-provider <plugin> [--item <ref>] [--url <url>]
agent-browser auth login <nombre> --username-selector <s> --password-selector <s> [--submit-selector <s>]
agent-browser auth list / auth show <n> / auth delete <n>   # show nunca muestra contrasenas

agent-browser plugin add <ref>       # npm o GitHub (escribe ~/.agent-browser/config.json; --project → ./agent-browser.json)
agent-browser plugin list / plugin show <nombre>
agent-browser plugin run <nombre> <tipo> --payload <json>
```

`auth login` filtra controles por tamano, visibilidad calculada, opacidad y estado disabled/readonly; si el campo se reemplaza o roba el foco antes de escribir, falla sin enviar. `--no-navigate` exige una pagina HTTP(S) top-level activa cuyo esquema, host y puerto coincidan con la URL efectiva de la credencial (paths/query/fragments pueden diferir); un `--url` de comando tiene prioridad y pasa a ser la restriccion de origen. Los plugins de credenciales corren fuera de proceso con el protocolo stdio `agent-browser.plugin.v1` y deben declarar `credential.read` (`--confirm-actions plugin:<name>:credential.read` exige aprobacion explicita). Otras capacidades: `browser.provider` (`--provider <name> open <url>`), `launch.mutate` y `command.run` (`plugin run`).

## Estado, streaming y WebMCP

```bash
agent-browser state save auth.json   # Guarda cookies, storage y estado de auth
agent-browser state load auth.json   # Lo restaura

agent-browser stream status --json / stream enable [--port 9223] / stream disable
agent-browser webmcp list <tool> --frame <frame-id> --json   # Schema de una herramienta anunciada
agent-browser webmcp list --json                             # Catalogo completo (recuperacion de contexto)
agent-browser webmcp invoke <tool> --frame <id> --params '{"k":"v"}'
agent-browser webmcp invoke <tool> --params @entrada.json --detach
agent-browser webmcp result <invocation-id> / webmcp cancel <invocation-id>
```

Los clientes de streaming se conectan a `ws://127.0.0.1:<puerto>` y reciben `frame`, `status`, `tabs`, `url`, `console`; envian `input_mouse`, `input_keyboard`, `input_touch`, `{"type":"config","maxFps":N}` (1..120, `0` = sin tope) y `{"type":"config","pacing":"ack"}` con `{"type":"ack","seq":N}`. Ambas opciones pueden declararse en la URL (`?pacing=ack&maxFps=10`).

## Panel y servidor MCP

```bash
agent-browser dashboard start [--port 8080] [--allowed-origins https://dashboard.example.com]
agent-browser dashboard stop
agent-browser mcp [--tools core,network,react,...|all]
```

Loopback se permite por defecto (IPv4/IPv6) sin token; `--allowed-origins` (o `AGENT_BROWSER_DASHBOARD_ALLOWED_ORIGINS`) es una lista CSV de origenes HTTPS exactos tras proxy (puertos 1-65535); para esos origenes imprime URLs tokenizadas privadas (token en el fragmento inicial, luego cookie Secure host-bound). Un `start` repetido reutiliza el panel solo si coinciden puerto y origenes; usa `stop` antes de cambiarlos. Perfiles MCP: `core` (defecto), `network`, `state`, `debug`, `tabs`, `react`, `mobile`, `all`.

## Opciones globales

```bash
agent-browser --session <nombre> ...   # Sesion aislada
agent-browser --json ...               # Salida JSON
agent-browser --headed ...             # Ventana visible (en Linux sin display arranca Xvfb solo)
agent-browser --webgpu ...             # WebGPU (SwiftShader software en Linux, sin GPU)
agent-browser --no-webmcp ...          # Desactiva WebMCP experimental (o AGENT_BROWSER_NO_WEBMCP)
agent-browser --cdp <port|url> ...     # Conexion CDP
agent-browser --pin-tab / --no-pin-tab # Fijar/desfijar la sesion a su tab
agent-browser -p <provider> ...        # Proveedor de navegador o plugin
agent-browser --proxy <url> ...        # Proxy (--proxy-bypass <hosts> para exenciones)
agent-browser --headers <json> ...     # Headers HTTP del origen
agent-browser --executable-path <p>    # Binario de navegador propio
agent-browser --args "--a,--b=x,y"     # Argumentos de arranque (las comas dentro del valor se conservan)
agent-browser --extension <ruta> ...   # Cargar extension (repetible)
agent-browser --ignore-https-errors    # Ignorar errores de certificado SSL
agent-browser --ca-cert <ruta> / --no-ca-cert / --use-system-ca   # Confianza CA
agent-browser --hide-scrollbars false  # Conservar barras de scroll en capturas headless
agent-browser --help / --version       # -h / -V; ayuda por comando: <comando> --help
```

## Depuracion

```bash
agent-browser --headed open example.com  # Ventana visible
agent-browser --cdp 9222 snapshot        # Conectar por puerto CDP (o connect 9222)
agent-browser console [--clear]          # Mensajes de consola
agent-browser errors [--clear]           # Errores de pagina
agent-browser highlight @e1              # Resaltar elemento
agent-browser inspect                    # Abrir DevTools de la sesion
agent-browser trace start / trace stop traza.json
agent-browser profiler start / profiler stop perfil.json
```

En Windows el Chrome propio headless corre en un escritorio privado (evita rectangulos fantasma); `--headed` y las sesiones con extensiones usan el escritorio interactivo. Los arboles de Chrome propios se terminan al salir el daemon, incluso a la fuerza; adjuntar a un navegador externo no nos hace duenos de el.

## React / Web Vitals

Requiere `--enable react-devtools` al arrancar para `react ...`; `vitals` y `pushstate` valen en cualquier sitio:

```bash
agent-browser open --enable react-devtools <url>
agent-browser react tree / react inspect <fiberId>
agent-browser react renders start / renders stop [--json]
agent-browser react suspense [--only-dynamic] [--json]   # --only-dynamic oculta la lista "static"
agent-browser vitals [url] [--json]                      # LCP/CLS/TTFB/FCP/INP + hidratacion
agent-browser pushstate <url>
```

## Auditoria de accesibilidad

Auditoria axe-core embebida (sin CDN) que corre por CDP sobre el arbol de frames y fusiona resultados sin mensajes a la pagina: el CSP no la bloquea, `window.axe` de la pagina queda intacto y las infracciones de iframe conservan su selector de frame. No disponible en Safari/iOS.

```bash
agent-browser a11y                              # Audita la pagina activa
agent-browser a11y <url>                        # Navega y audita
agent-browser a11y --tags wcag2a,wcag2aa        # Solo reglas con esos tags axe
agent-browser a11y --selector "#main"           # Acota a un subarbol
agent-browser a11y <url> --json                 # Resultado estructurado
```

El JSON trae `counts` y los arrays `violations`/`incomplete` con `id`, `impact`, `help`, `helpUrl`, `tags`, `nodeCount` y hasta 10 `nodes` (`target` = rutas selector (preserva shadow DOM), `html`, `failureSummary`). `incomplete` son reglas que axe no pudo evaluar: revsalas a mano.

## Init scripts y cookies cURL

```bash
agent-browser open --init-script <ruta>     # Registrar antes de la primera navegacion (repetible)
agent-browser addinitscript <js>            # En runtime (devuelve identificador)
agent-browser removeinitscript <ident>      # Quita de todas las pestanas de la sesion
```

Los identificadores de init scripts son de la sesion: quitar uno lo borra de todas las pestanas abiertas donde se registro y del setup que se repite en pestanas futuras.

## Variables de entorno

```bash
AGENT_BROWSER_SESSION="mi-sesion"             # Sesion por defecto
AGENT_BROWSER_EXECUTABLE_PATH="/ruta/chrome"  # Binario propio
AGENT_BROWSER_EXTENSIONS="/e1,/e2"            # Rutas de extensiones (CSV)
AGENT_BROWSER_INIT_SCRIPTS="/a.js,/b.js"      # Rutas de init scripts (CSV)
AGENT_BROWSER_ENABLE="react-devtools"         # Features integradas (CSV)
AGENT_BROWSER_HIDE_SCROLLBARS="false"         # Conservar barras de scroll
AGENT_BROWSER_WEBGPU="1"                      # Preset de arranque WebGPU
AGENT_BROWSER_NO_XVFB="1"                     # Sin Xvfb automatico en Linux sin display
AGENT_BROWSER_PROVIDER="browserbase"          # Proveedor o plugin
AGENT_BROWSER_STREAM_PORT="9223"              # Puerto del stream WebSocket
AGENT_BROWSER_DASHBOARD_ALLOWED_ORIGINS="https://dashboard.example.com"
AGENT_BROWSER_CONFIG="./agent-browser.json"  # Config personalizada
AGENT_BROWSER_CDP="9222"                      # Puerto/URL CDP del daemon
AGENT_BROWSER_ALLOWED_DOMAINS="example.com"   # Restriccion de dominios de red
AGENT_BROWSER_PLUGINS='[{"name":"vault","command":"agent-browser-plugin-vault","capabilities":["credential.read"]}]'
BROWSER_USE_API_KEY / BROWSER_USE_PROFILE_ID / BROWSER_USE_PROXY_COUNTRY / BROWSER_USE_ENABLE_RECORDING
```

`AGENT_BROWSER_ALLOWED_DOMAINS` exige un contexto navegador fresco y controlable (sin perfil/restore/state replay ni plugins de pagina directa). Ciclo de Browser Use Cloud: creacion 10s + attach CDP 8s + parada 4s (limpieza de timeout 10s); `close` solo tiene exito si la nube confirma la parada (si falla, conserva el id de sesion para reintentar y bloquea un nuevo lanzamiento hasta liberarlo); si el daemon sale antes de parar con exito, inspecciona y para el navegador en la nube.
