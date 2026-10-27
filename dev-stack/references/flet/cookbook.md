# Cookbook - Patrones comunes en Flet

## Routing y navegación

```python
import asyncio
import flet as ft

def main(page: ft.Page):
    page.title = "App con routing"

    def route_change(e):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.AppBar(title=ft.Text("Inicio")),
                    ft.ElevatedButton("Ir a Store", on_click=lambda _: asyncio.create_task(page.push_route("/store"))),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    route="/store",
                    controls=[
                        ft.AppBar(title=ft.Text("Store")),
                        ft.ElevatedButton("Volver", on_click=lambda _: page.views.pop() or page.update()),
                    ],
                )
            )
        page.update()

    async def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    route_change()

ft.app(main)
```

## Autenticación OAuth

```python
import flet as ft
from flet.auth.providers import GoogleOAuthProvider

def main(page: ft.Page):
    provider = GoogleOAuthProvider(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        redirect_url="http://localhost:8550/api/oauth/redirect",
    )

    def login_click(e):
        page.login(provider)

    def on_login(e):
        if e.error:
            print(f"Error: {e.error}")
        else:
            print(f"User: {page.auth.user}")

    page.on_login = on_login
    page.add(ft.ElevatedButton("Login with Google", on_click=login_click))

ft.app(main, port=8550)
```

## PubSub (comunicación entre sesiones)

```python
import flet as ft

def main(page: ft.Page):
    def on_message(msg):
        page.add(ft.Text(msg))
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        page.pubsub.send_all(f"{page.session_id}: {msg_input.value}")
        msg_input.value = ""
        page.update()

    msg_input = ft.TextField(hint_text="Mensaje")
    page.add(msg_input, ft.ElevatedButton("Enviar", on_click=send_click))

ft.app(main)
```

## Client Storage (persistencia local)

```python
import flet as ft

def main(page: ft.Page):
    def save_click(e):
        page.client_storage.set("key", text_field.value)
        page.add(ft.Text("Guardado!"))

    def load_click(e):
        value = page.client_storage.get("key")
        if value:
            page.add(ft.Text(f"Valor: {value}"))

    text_field = ft.TextField(hint_text="Escribe algo")
    page.add(
        text_field,
        ft.ElevatedButton("Guardar", on_click=save_click),
        ft.ElevatedButton("Cargar", on_click=load_click),
    )

ft.app(main)
```

## Session Storage

```python
page.session.set("user", {"name": "Juan", "role": "admin"})
user = page.session.get("user")
```

## Async app

```python
import asyncio
import flet as ft

async def main(page: ft.Page):
    page.add(ft.Text("Cargando..."))
    await asyncio.sleep(2)
    page.controls.clear()
    page.add(ft.Text("Listo!"))
    page.update()

ft.app(main)
```

## Theming

```python
page.theme = ft.Theme(
    color_scheme_seed=ft.Colors.INDIGO,
    color_scheme=ft.ColorScheme(
        primary=ft.Colors.GREEN,
        primary_container=ft.Colors.GREEN_200,
    ),
)
page.theme_mode = ft.ThemeMode.DARK
page.update()
```

## Custom fonts

```python
page.fonts = {
    "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
    "OpenSans": "assets/fonts/OpenSans-Regular.ttf",
}
page.add(ft.Text("Texto con fuente personalizada", font_family="RobotoSlab", size=30))
```

## Control Refs

```python
import flet as ft

def main(page: ft.Page):
    input_ref = ft.Ref[ft.TextField]()

    def button_click(e):
        input_ref.current.value = "Clicked!"
        page.update()

    page.add(
        ft.TextField(ref=input_ref, hint_text="Escribe algo"),
        ft.ElevatedButton("Click", on_click=button_click),
    )

ft.app(main)
```

## Drag and Drop

```python
import flet as ft

def main(page: ft.Page):
    def on_accept(e):
        source = page.get_control(e.data)
        source.visible = False
        e.control.content = ft.Text(f"Recibido: {source.content.value}")
        page.update()

    page.add(
        ft.Row([
            ft.Draggable(
                group="color",
                content=ft.Container(width=50, height=50, bgcolor=ft.Colors.RED),
                data="red",
            ),
            ft.DragTarget(
                group="color",
                content=ft.Container(width=100, height=100, bgcolor=ft.Colors.BLUE_GREY_100),
                on_accept=on_accept,
            ),
        ])
    )

ft.app(main)
```

## Animaciones

```python
container = ft.Container(
    width=150,
    height=150,
    bgcolor=ft.Colors.RED,
    animate=ft.Animation(duration=1000, curve=ft.AnimationCurve.BOUNCE_OUT),
)

def animate(e):
    container.width = 300 if container.width == 150 else 150
    container.height = 300 if container.height == 150 else 150
    container.bgcolor = ft.Colors.BLUE if container.bgcolor == ft.Colors.RED else ft.Colors.RED
    container.update()
```

## File Picker

```python
import flet as ft

def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            for f in e.files:
                page.add(ft.Text(f.name))
        page.update()

    file_picker = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(file_picker)

    page.add(ft.ElevatedButton("Seleccionar archivos", on_click=lambda _: file_picker.pick_files(allow_multiple=True)))

ft.app(main)
```

## Upload de archivos

```python
import flet as ft

def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            upload_list = []
            for f in e.files:
                upload_list.append(
                    ft.FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600),
                    )
                )
            file_picker.upload(upload_list)

    file_picker = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(file_picker)
    page.add(ft.ElevatedButton("Subir archivos", on_click=lambda _: file_picker.pick_files(allow_multiple=True)))

ft.app(main, upload_dir="uploads")
```

## Control personalizado con @ft.control

```python
import flet as ft

@ft.control
class Counter(ft.Column):
    def __init__(self, initial: int = 0):
        super().__init__()
        self._count = initial
        self.controls = [
            ft.Text(f"Count: {self._count}"),
            ft.Row([
                ft.IconButton(ft.Icons.ADD, on_click=self._increment),
                ft.IconButton(ft.Icons.REMOVE, on_click=self._decrement),
            ]),
        ]

    def _increment(self, e):
        self._count += 1
        self.controls[0].value = f"Count: {self._count}"
        self.update()

    def _decrement(self, e):
        self._count -= 1
        self.controls[0].value = f"Count: {self._count}"
        self.update()
```

## Componente declarativo con @ft.component

```python
import flet as ft

@ft.component
def Counter(initial: int = 0):
    count = ft.use_state(initial)

    def increment(e):
        count.set(count.value + 1)

    def decrement(e):
        count.set(count.value - 1)

    return ft.Column([
        ft.Text(f"Count: {count.value}"),
        ft.Row([
            ft.IconButton(ft.Icons.ADD, on_click=increment),
            ft.IconButton(ft.Icons.REMOVE, on_click=decrement),
        ]),
    ])
```

## Large lists (virtualización)

```python
import flet as ft

def main(page: ft.Page):
    items = [ft.Text(f"Item {i}") for i in range(10000)]
    page.add(
        ft.ListView(
            controls=items,
            spacing=10,
            padding=20,
            expand=True,
        )
    )

ft.app(main)
```

## Keyboard shortcuts

```python
def on_keyboard(e: ft.KeyboardEvent):
    if e.key == "Enter" and e.ctrl:
        # Ctrl+Enter
        pass
    elif e.key == "Escape":
        # Escape
        pass

page.on_keyboard_event = on_keyboard
```

## Adaptive apps (Material + Cupertino)

```python
# Usar controles adaptativos que cambian según la plataforma
ft.AdaptiveControl(
    adaptive=ft.Switch(value=True),
    cupertino=ft.CupertinoSwitch(value=True),
)
```

## Multi-threading

```python
import time

def long_task():
    time.sleep(5)
    return "Resultado"

def start_task(e):
    page.run_thread(lambda: long_task())

page.add(ft.ElevatedButton("Iniciar tarea", on_click=start_task))
```

## Multi-processing

```python
import multiprocessing

def worker(q):
    q.put("Resultado del worker")

def start_process(e):
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(q,))
    p.start()
    p.join()
    page.add(ft.Text(q.get()))
    page.update()
```

## Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("Mensaje de debug")
```

## Encrypting sensitive data

```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
encrypted = cipher.encrypt(b"datos sensibles")
decrypted = cipher.decrypt(encrypted)
```

## Accessibility

```python
ft.Text("Texto con semántica", semantics_label="Etiqueta alternativa")
ft.Semantics(
    content=ft.Container(...),
    label="Descripción para lectores de pantalla",
    button=True,
)
```

## Flet MCP (Model Context Protocol)

```bash
flet mcp
```
Inicia un servidor MCP que permite a asistentes de IA interactuar con apps Flet en tiempo real.