# Integración Flet + FastAPI

## Instalación

```bash
pip install 'flet[all]' fastapi uvicorn
```

## Uso básico

```python
import flet as ft
from flet_fastapi import flet_app
from fastapi import FastAPI

app = FastAPI()

def main(page: ft.Page):
    page.title = "Flet + FastAPI"
    page.add(ft.Text("Hola desde Flet con FastAPI!"))

app.mount("/app", flet_app(main))
```

## Ejecutar

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Reference

### `flet_app`
```python
flet_app(
    main: Callable,
    assets_dir: str | None = None,
    upload_dir: str | None = None,
    web_renderer: WebRenderer | None = None,
    use_color_emoji: bool = False,
    route_url_strategy: RouteUrlStrategy | None = None,
    app_name: str | None = None,
    app_short_name: str | None = None,
    app_description: str | None = None,
    app_theme_color: str | None = None,
    oauth_state_timeout: int | None = None,
    session_timeout: int | None = None,
    max_upload_size: int | None = None,
    secret_key: str | None = None,
) -> FastAPI
```

### `FletApp`
Clase para control más granular:
```python
from flet_fastapi import FletApp

app = FastAPI()
fa = FletApp(main, upload_dir="uploads")
app.mount("/app", fa)
```

### `AppManager`
Para múltiples apps Flet en un mismo servidor FastAPI:
```python
from flet_fastapi import AppManager

app_manager = AppManager()
app_manager.add_app("app1", flet_app(main1))
app_manager.add_app("app2", flet_app(main2))
app.mount("/", app_manager)
```

### `FletOAuth`
Middleware para OAuth:
```python
from flet_fastapi import FletOAuth

app.add_middleware(FletOAuth)
```

### `FletStaticFiles`
Para servir archivos estáticos:
```python
from flet_fastapi import FletStaticFiles

app.mount("/static", FletStaticFiles(directory="static"), name="static")
```

### `FletUpload`
Para manejar uploads:
```python
from flet_fastapi import FletUpload

app.mount("/upload", FletUpload(upload_dir="uploads"))
```

## Ejemplo completo

```python
import flet as ft
from flet_fastapi import flet_app
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

def main(page: ft.Page):
    page.title = "App Completa"
    page.theme_mode = ft.ThemeMode.LIGHT

    def button_click(e):
        page.add(ft.Text(f"Click! {page.session.get('count', 0)}"))
        page.session.set("count", page.session.get("count", 0) + 1)
        page.update()

    page.add(
        ft.AppBar(title=ft.Text("FastAPI + Flet")),
        ft.ElevatedButton("Click me", on_click=button_click),
    )

app.mount("/", flet_app(main, upload_dir="uploads"))
```

## Rutas adicionales

```python
@app.get("/api/health")
async def health():
    return {"status": "ok"}

@app.get("/api/data")
async def get_data():
    return {"data": [1, 2, 3]}
```