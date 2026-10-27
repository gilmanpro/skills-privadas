---
name: dev-stack
description: "Stack unificado de desarrollo con dispatch por tipo de trabajo. UI web: landing, dashboard, tablas, formularios con Tailwind CDN, HTML vanilla, Lucide y Alpine sin build, dark mode y estetica anti-AI-slop. Escritorio Python: ttkbootstrap/tkinter con temas Bootstrap. Flet: apps Python web, desktop y mobile sobre Flutter con flet build y FastAPI. Go: APIs REST, CLI, concurrencia, worker pools, testing. UI/UX: design system con 50+ estilos, 161 paletas, guias UX y stacks React, Vue, Svelte, Flutter, Tailwind, shadcn/ui; diseno de sitios citados via Refero Styles. Compilacion: PyInstaller, flet build, GOOS/GOARCH, jpackage. Decompilacion: recuperar source de .exe PyInstaller. DevOps: Docker, Rancher Desktop, CI/CD, Nginx, SSL, despliegue, rollback. Usar SIEMPRE que el usuario pida UI web o de escritorio, GUI Python, app Flet, codigo Go, compilar o empaquetar una app, decompilar un .exe PyInstaller, dockerizar, desplegar o CI/CD, o elegir paletas, tipografia o design system, aunque no nombre la skill."
---

# Dev-Stack — desarrollo de software y diseno de interfaces

Cuatro ramas de codificacion, una de inteligencia UI/UX y tres de ciclo de vida (compilar, decompilar, desplegar) bajo una sola skill. Elige la rama segun el tipo de trabajo y lee SOLO los archivos de esa rama (un nivel de profundidad).

## Dispatch

| Senal en la peticion | Rama | Donde leer |
|---|---|---|
| UI web, landing, dashboard, navbar, modal, card, tabla, formulario, Tailwind, "un solo HTML" | [UI web](#rama-ui-web) | `references/frontend-design/` |
| tkinter, ttkbootstrap, GUI Python de escritorio, ventanas/temas de escritorio | [Escritorio Python](#rama-escritorio-python-ttkbootstrap) | `references/ttkbootstrap/` |
| Flet, app Python web+desktop+mobile, `flet build`, Flutter bajo el capot | [Flet](#rama-flet) | `references/flet/` |
| Go, golang, archivo `.go`, gorutinas, channels, worker pool | [Go](#rama-go) | `references/golang/` |
| design system, paletas, tipografia, guias UX, revisar UI existente, stack React/Vue/Svelte/SwiftUI/Flutter/shadcn | [UI/UX Pro Max](#rama-uiux-pro-max-vendor) | `ui-ux-pro-max/` + `references/reglas-ux.md` |
| "hazlo como Notion/Stripe/Linear", acabado profesional/de agencia | Refero | `references/refero-styles.md` |
| compilar, empaquetar, hacer .exe, build, onefile, .spec, instalador, distribuir app, cross-compile | [Compilación](#rama-compilacion) | `references/compilacion/guia.md` |
| decompilar .exe, extraer codigo de un ejecutable PyInstaller, bytecode, pyinstxtractor, marshal | [Decompilación PyInstaller](#rama-decompilacion-pyinstaller) | `references/pyinstaller-decompile/` |
| Docker, Dockerfile, docker-compose, desplegar, deploy, CI/CD, Nginx, SSL, rollback, VPS | [Despliegue y DevOps](#rama-despliegue-y-devops) | `references/despliegue/` |

Anti-dispatch (no usar esta skill para): logos o iconografia vectorial → skill `graphic-media`; documentos de texto → skill `ofimatica`; pentesting → la antigua skill `kali-linux` (ARCHIVADA el 2026-10-13 en `~/.agents/skills-archive/kali-linux`, sin sucesora activa).

## Rama UI web

Stack default: Tailwind CSS v3 CDN, HTML5 semantico, Lucide Icons CDN, Alpine.js SOLO si hay interactividad, Google Fonts con tipografias distintivas (NO Inter, NO Roboto, NO Arial, NO Space Grotesk). Un solo `.html` autocontenido, sin Node.js ni npm.

Dark mode default cuando el usuario no especifique: fondo `bg-gray-950` o `bg-zinc-950`; texto `text-gray-100` (primario) y `text-gray-400` (secundario); superficies `bg-white/5` y `bg-white/10` con bordes `border-white/5`; UN color de acento entre `indigo`, `violet`, `emerald`, `sky` o `amber`; radios `rounded-2xl` (cards), `rounded-xl` (botones), `rounded-full` (badges); espaciado generoso (`p-8`/`p-12`, `gap-8`, `space-y-6`); mobile-first con `sm:` `md:` `lg:` `xl:`; animaciones `transition-all duration-300` solo sobre `transform`/`opacity`.

Design thinking ANTES de codificar: proposito, audiencia, tono estético (brutalista minimal, maximalista, retro-futurista, luxury, playful, editorial, glassmorphism, cyberpunk) y diferenciador. Minimos de UX: touch targets 44x44 px, nav de 5-7 items, feedback en cada accion, contraste WCAG AA.

Workflow: 1) reunir requerimientos (si faltan, asume y comunica criterio); si cita un sitio real, extrae primero su DESIGN.md con Refero (`references/refero-styles.md`); 2) consultar docs de Tailwind con Context7 (`resolve-library-id` "Tailwind CSS" → `query-docs` específico); 3) escribir el HTML autocontenido (CDN en `<head>`, Lucide antes de `</body>`, todo con clases Tailwind salvo keyframes); 4) VALIDAR con Chrome DevTools: `navigate_page` al `file:///ruta`, `take_snapshot`, `list_console_messages` types error+warn — no entregar con errores en consola.

Cuando leer: `references/frontend-design/boilerplate.md` al iniciar cualquier entrega (plantilla HTML completa); `references/frontend-design/components.md` al armar navbar, hero, bento grid, pricing o footer; `references/frontend-design/anti-patterns.md` antes de entregar (gradientes purpura sobre blanco, lorem ipsum, plantillas genericas repetidas → alternativas recomendadas).

## Rama Escritorio Python (ttkbootstrap)

`pip install ttkbootstrap`. Extension de tkinter con estilos Bootstrap.

```python
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(title="App", themename="darkly", size=(800, 600))  # ventana + tema en una linea
b1 = ttk.Button(root, text="Ok", bootstyle=(SUCCESS, OUTLINE))
b1.pack(side=LEFT, padx=5, pady=10)
root.mainloop()
```

18 temas: light `cosmo` `flatly` `litera` `lumen` `minty` `pulse` `sandstone` `yeti` `morph` `journal` `united` `simplex` `cerculean`; dark `darkly` `superhero` `solar` `cyborg` `vapor`. Cambio en runtime: `root.style.theme_use("superhero")`.

Reglas de oro: importa `ttkbootstrap as ttk` (no `tkinter.ttk`); prefiere `ttk.Window`; usa constantes de `ttkbootstrap.constants` en `bootstyle` (tuplas para combinar color+tipo: `(DANGER, OUTLINE)`, tipos `outline` `link` `toolbutton` `round` `inverse` `striped`); el bootstyle aplica color y tipo, NO layout — recuerda `pack`/`grid`/`place`; `ScrolledFrame` con `autohide=True` para listas largas; `Tableview` con `paginated=True` para mas de 100 filas; `Floodgauge` con `mode="indeterminate"` para progreso desconocido; llama `enable_high_dpi_awareness()` antes de crear la ventana en Windows.

Cuando leer: `references/ttkbootstrap/widgets.md` para catalogo completo de widgets; `dialogs.md` para Messagebox/Querybox/Dialog; `scrolled.md` para ScrolledFrame/ScrolledText; `validation.md` para validacion de entradas; `themes.md` para Window/Toplevel/Style/Colors, temas personalizados y TTK Creator; `utilities.md` para utilidades, colorutils e i18n; `example-app.md` para una app completa de referencia.

## Rama Flet

`pip install 'flet[all]'` → verifica con `flet --version` y `flet doctor`. Apps web, desktop y mobile desde un solo codigo Python.

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Mi App"
    page.add(ft.Text("Hola Mundo"))

ft.run(main)  # Flet <1.0: ft.app(main)
```

Patrones: imperativo (`page.add()`, `page.update()`), declarativo (`page.views = [...]` para routing), async (`async def main` + `await page.add_async()`).

Controles clave: layout `Row` `Column` `Stack` `Container` `ResponsiveRow`; datos `DataTable` `GridView` `ListView`; input `TextField` `Dropdown` `Checkbox` `Switch` `Slider` `DatePicker`; navegacion `NavigationBar` `Tabs` `AppBar`. Servicios nativos: `FilePicker`, `Clipboard`, `Geolocator`, `SecureStorage`, `Audio`, `Share`, etc.

Publicacion: `flet build apk|aab|ipa|windows|macos|linux|web`. Nota: `flet build` reemplazo a `flet publish` y `flet pack` desde 0.18 — no uses los legados. FastAPI: monta `flet_app(main)` con `flet_fastapi`.

Buenas practicas: `ft.Ref[T]` para referenciar controles; `page.on_route_change` + `page.views` para multi-pagina; `page.pubsub` entre sesiones; persistencia con `page.client_storage` y sesion con `page.session`; controles propios con `@ft.control` (Flet 1.x); navegacion programatica con `page.go()`.

Cuando leer: `references/flet/controls.md` para catalogo de controles; `services.md` para servicios nativos; `types.md` para tipos/enums/eventos; `publishing.md` al compilar por plataforma; `cookbook.md` para routing/auth/animaciones; `cli.md` para flags de `flet build`/`flet run`; `fastapi.md` para backend dinamico con Flet.

## Rama Go

Comandos fundamentales:

```bash
go mod init <module> && go mod tidy
go run . && go build ./...
go test ./... -race
go vet ./... && go fmt ./...
```

Reglas de oro: `gofmt` siempre; llaves en la misma linea y sin parentesis en `if`/`for`/`switch`; errores explicitos con envoltura `fmt.Errorf("...: %w", err)`; nombres cortos en scopes cortos; composicion sobre herencia e interfaces pequenas; table-driven tests; `any` en vez de `interface{}`; `go test -race` en todo codigo concurrente; `context.WithTimeout` para operaciones con deadline; prefiere stdlib y justifica cada dependencia externa.

Concurrencia: prefiere worker pools sobre "una gorutina por elemento". Patron minimo: canal de trabajo con buffer, N workers consumiendo `for item := range jobs`, `sync.WaitGroup` para esperar, cerrar `jobs` antes de `wg.Wait()` y luego cerrar `results`.

Cuando leer: `references/golang/concurrency.md` para gorutinas/channels/select/context/sync y patrones completos; `standard-library.md` para net/http, database/sql, encoding/json; `modules.md` para go.mod/go.sum/workspaces; `testing.md` para benchmarks y fuzzing; `tooling.md` para gopls/pprof/cover/vet; `best-practices.md` para estructura de proyecto (cmd/, internal/, pkg/) y patrones.

## Rama UI/UX Pro Max (vendor)

Base de datos consultable de inteligencia de diseno. El vendor vive en `ui-ux-pro-max/` dentro de esta skill (arbol upstream en `ui-ux-pro-max/repo/`, NO editar: se regenera con su instalador). Ejecuta la CLI desde la carpeta `ui-ux-pro-max/` (usa las junctions `data/` y `scripts/`):

```bash
py scripts/search.py "<producto> <industria> <keywords>" --design-system -p "Nombre Proyecto"
py scripts/search.py "<keyword>" --domain <dominio> [-n <max>]
py scripts/search.py "<keyword>" --stack <stack>
py scripts/search.py "<consulta>" --design-system --persist -p "Proyecto"   # persiste entre sesiones
py scripts/search.py "fintech crypto" --design-system -f markdown           # salida markdown
```

Dominios: `product` `style` `typography` `color` `landing` `chart` `ux` `google-fonts` `react` `web` `prompt`. Stacks: `react` `nextjs` `nuxtjs` `vue` `svelte` `angular` `astro` `laravel` `threejs` `flutter` `swiftui` `react-native` `jetpack-compose` `shadcn` `html-tailwind` `javafx`.

Reglas por prioridad (accesibilidad y tactil = CRITICO; estilo, layout y navegacion = ALTO; ver detalle en `references/reglas-ux.md`): nunca quitar anillos de foco, no depender solo de hover, no usar emoji como icono, no hardcodear hex (usa tokens semanticos), no animar width/height, no scroll horizontal en movel, placeholder no es etiqueta.

Checklist pre-entrega: contraste >=4.5:1 en claro y oscuro; tactiles >=44x44 pt; 375/768/1440 px probados; `reduced-motion` soportado; animaciones 150-300 ms con easing nativo; consola sin errores; labels visibles en formularios; nav inferior <=5 items.

Si el usuario cita un sitio real ("como Notion/Stripe") o pide acabado de agencia: extrae su sistema de diseno real (paleta con roles, escala tipografica, spacing, componentes, tokens CSS/Tailwind) desde https://styles.refero.design/ con `webfetch` — flujo completo y reglas de adaptacion (nada de clonar logos/textos; la marca del usuario manda) en `references/refero-styles.md`.

Sub-skills del vendor: `ui-ux-pro-max/repo/.claude/skills/` contiene `banner-design` `brand` `design` `design-system` `slides` `ui-styling` y `ui-ux-pro-max` (la inglesa upstream), registradas cada una como skill propia por opencode. Dejalas intactas; su `name` coincide con su carpeta.

Mantenimiento de junctions: `ui-ux-pro-max/data` y `ui-ux-pro-max/scripts` son junctions de Windows hacia `ui-ux-pro-max/repo/src/ui-ux-pro-max/`. Si `py scripts/search.py` falla con "no existe", recrearlas desde la raiz de la skill:

```bat
cmd /c rmdir /q "ui-ux-pro-max\data" & cmd /c mklink /J "ui-ux-pro-max\data" "ui-ux-pro-max\repo\src\ui-ux-pro-max\data"
```

(mismo patron con `scripts`; `rmdir` sin `/s` elimina solo el enlace, nunca el destino).

## Rama Compilación

Python desktop → PyInstaller: NO es cross-compiler (build en cada SO destino). `pyinstaller --onefile --windowed --name AppName main.py`; `--add-data "src;dst"` (`;` en Windows, `:` en Unix); hidden imports con `--collect-all ttkbootstrap` para GUI; `.spec` para proyectos complejos (rebuild: `pyinstaller --noconfirm AppName.spec`). Flet → `flet build windows|macos|linux|apk|aab|ipa|web` (cross vía Flutter; en Windows Android exige WSL). Go → cross-compile nativo: `GOOS=<so> GOARCH=<arq> go build -ldflags="-s -w" -o dist/app` (lista de objetivos: `go tool dist list`); CGO con mingw-w64. Java → `jar`/`jpackage` (`.exe` `.msi` `.dmg` `.deb` `.rpm`; NO cross-compiler).

Cuando leer: `references/compilacion/guia.md` para la tabla de flags de PyInstaller, `.spec` completo de ttkbootstrap, `pyproject.toml` de Flet, matriz de compilación, script batch multi-objetivo y ejemplos de jpackage.

## Rama Decompilación PyInstaller

Recuperar el source Python de un .exe PyInstaller (solo tuyos o con autorización explícita). Flujo: detectar la firma `PyInstaller` → extraer `.pyc` con pyinstxtractor → identificar el entry point (NO está dentro de `PYZ`) → leer bytecode con `marshal.load()` + `dis` → analizar `co_consts`/`co_names`/`co_varnames` → reconstruir a mano (decompyle3/uncompyle6 no llegan a Python 3.12+; pycdc solo parcial) → preguntar al usuario las constantes ambiguas → verificar con `ast.parse` → entregar código + % de certeza por tramo.

Reglas de oro: nunca asumes el significado de una constante sin preguntar; cada objeto `code` en `co_consts` es una función interna a decompilar por separado; documentas siempre el nivel de confianza de cada tramo reconstruido.

Cuando leer: `references/pyinstaller-decompile/guia.md` (flujo completo); `pyinstxtractor.md` para troubleshooting; `bytecode-analysis.md` para los campos del objeto Code; `interactive-flow.md` para las preguntas al usuario; script `scripts/extract_and_analyze.py` para extracción + análisis en un comando.

## Rama Despliegue y DevOps

Docker: nunca improvises flags — cada flag que uses debe existir en las referencias oficiales empaquetadas. Si `docker info` falla, arranca Rancher Desktop primero (`rdctl start --container-engine moby --kubernetes-enabled=false`) y, si no existe, Docker Desktop; con motor containerd el CLI es `nerdctl`. Si NINGUN motor está instalado, informar y sugerir — NO instalar sin autorización.

Flujo: entender target → analizar proyecto → elegir estrategia → Docker (si aplica) → archivos de deployment (workflows, `.env.example`, nginx.conf, scripts) → **confirmar antes de tocar producción** → ejecutar → verificar health y dejar documentado el rollback. Estrategias: rolling, blue-green, canary, feature flags. Secretos SOLO en variables de entorno; validar YAML antes de aplicar.

Cuando leer: `references/despliegue/guia.md` (guía completa e índice de las 9 referencias: `docker-run.md`, `dockerfile.md`, `docker-compose.md`, `docker-commands.md`, `motor-contenedores-windows.md`, `cicd-nginx-templates.md`, `monitoreo-post-deploy.md`, `rollback.md`, `vps-ssh-deploy.md`). Carga SOLO la que necesites para la tarea actual.

## Anti-patrones globales

- No elijas el stack por moda: si la UI web es un solo HTML, Tailwind CDN gana; si el entregable es Python de escritorio, ttkbootstrap; si necesita mobile, Flet. Cinco alternativas por tarea es indecision delegada.
- No uses rama web para GUI de escritorio ni ttkbootstrap para paginas: son dominios separados del dispatch.
- No improvises flags: `flet build`/`go` → `references/flet/publishing.md` / `references/golang/tooling.md`; Docker y PyInstaller → `references/despliegue/` y `references/compilacion/guia.md`.
- No edites el vendor `ui-ux-pro-max/repo/`: es upstream y se reinstala, no se parchea.
- No entregues UI sin validar consola limpia ni antes de pasar el checklist de la rama correspondiente.

## Evals

`evals/evals.json` (heredados de la rama Go): 5 evals de rendimiento con aserciones verificables; `evals/evals-despliegue.json` (heredados de la rama Despliegue) y `evals/evals-pyinstaller-decompile.json` (heredados de la rama Decompilación). Ejecutar con `python skill-creator/scripts/run_eval.py --eval-set dev-stack/evals/evals.json --skill-path dev-stack --model <provider/model> --verbose` (mismo patrón apuntando a los otros dos archivos).
