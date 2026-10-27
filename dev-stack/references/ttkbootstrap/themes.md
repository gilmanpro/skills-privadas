# Temas ttkbootstrap

## Clase Window
Crea la ventana principal con tema y geometría.
```python
ttk.Window(
    title="ttkbootstrap",       # título de la ventana
    themename="litera",         # tema a usar
    iconphoto="",               # ruta al icono
    size=(800, 600),            # (ancho, alto)
    position=(100, 100),        # (x, y) posición en pantalla
    minsize=(400, 300),         # tamaño mínimo
    maxsize=(1920, 1080),       # tamaño máximo
    resizable=(True, True),     # (horizontal, vertical)
    hdpi=True,                  # soporte high-dpi (Windows)
    scaling=None,               # factor de escalado
    transient=None,             # ventana transiente
    overrideredirect=False,     # sin bordes de ventana
    alpha=1.0,                  # transparencia (0.0 - 1.0)
)
```
Métodos útiles: `place_window_center()`, `style` (propiedad → Style), `destroy()`.

## Clase Toplevel
Crea ventanas secundarias.
```python
ttk.Toplevel(
    title="ttkbootstrap",
    iconphoto="",
    size=None, position=None, minsize=None, maxsize=None,
    resizable=None, transient=None, overrideredirect=False,
    windowtype=None, topmost=False, toolwindow=False, alpha=1.0
)
```
Método: `place_window_center()`, propiedad `style`.

## Clase Style
Controla el tema actual y los colores.
```python
style = ttk.Style()                    # tema default (litera)
style = ttk.Style(theme="superhero")   # con tema específico
```

### Formatos de bootstyle
Usa cualquiera de estas formas equivalentes para el parámetro `bootstyle`.
```python
bootstyle="info-outline"
bootstyle="infooutline"
bootstyle="info outline"
bootstyle="outline-info"
bootstyle=("info", "outline")
bootstyle=(INFO, OUTLINE)
```
Combina múltiples palabras clave con tuplas de constantes.

### Métodos principales
```python
style.theme_use("darkly")                     # cambiar tema en runtime
style.theme_names()                           # lista de temas disponibles
style.colors                                   # objeto Colors del tema actual
style.colors.primary / .get("primary")        # acceder colores
style.colors.label_iter()                     # iterar todos los colores
style.load_user_themes("themes.json")          # cargar temas JSON
style.load_user_theme(theme_definition)        # cargar un ThemeDefinition
style.use_dynamic_foreground(True)            # selección dinámica de color de texto
style.register_theme(definition)              # registrar un theme definition
style.theme_create("mio", parent="darkly")    # crear tema hijo
```

### Iterar colores
```python
for color in root.style.colors:
    b = ttk.Button(root, text=color, bootstyle=color)
    b.pack(side=LEFT, padx=5, pady=5)
```

## Clase Colors
Accede y manipula los colores del tema.
Propiedades: `primary`, `secondary`, `success`, `info`, `warning`, `danger`, `light`, `dark`, `bg`, `fg`, `selectbg`, `selectfg`, `border`, `inputfg`, `inputbg`, `active`.

```python
style.colors.bg      # color de fondo
style.colors.fg      # color de texto
```

Métodos estáticos:
```python
Colors.update_hsv("#9954bb", hd=0, sd=0, vd=0.15)   # ajustar HSV
Colors.hex_to_rgb("#fff")                             # hex → rgb
Colors.rgb_to_hex(255, 255, 255)                      # rgb → hex
Colors.make_transparent(0.5, "#f00", "#fff")          # simular transparencia
Colors.rgb_to_hsv(r, g, b)                            # rgb → hsv
```

## ThemeDefinition
Define un tema personalizado programáticamente.
```python
from ttkbootstrap.style import ThemeDefinition

td = ThemeDefinition(
    name="mio",
    colors={"primary": "#ff0000", ...},
    themetype="light"  # o "dark"
)
```

## Temas personalizados via JSON
Carga temas desde un archivo JSON.
```python
style.load_user_themes("mis_temas.json")
```

Estructura JSON:
```json
{
  "themes": [
    {
      "mi_tema": {
        "type": "dark",
        "colors": {
          "primary": "#2780e3",
          "secondary": "#7E8081",
          "success": "#3fb618",
          "info": "#9954bb",
          "warning": "#ff7518",
          "danger": "#ff0039",
          "light": "#F8F9FA",
          "dark": "#373A3C",
          "bg": "#ffffff",
          "fg": "#373a3c",
          "selectbg": "#7e8081",
          "selectfg": "#ffffff",
          "border": "#ced4da",
          "inputfg": "#373a3c",
          "inputbg": "#fdfdfe"
        }
      }
    }
  ]
}
```

## ThemeDefinition manual
Registra un tema construido con `Colors`.
```python
from ttkbootstrap.style import ThemeDefinition, Colors

td = ThemeDefinition(
    name="midnight",
    colors=Colors(
        primary="#2780e3", secondary="#7E8081",
        success="#3fb618", info="#9954bb",
        warning="#ff7518", danger="#ff0039",
        light="#F8F9FA", dark="#373A3C",
        bg="#ffffff", fg="#373a3c",
        selectbg="#7e8081", selectfg="#ffffff",
        border="#ced4da", inputfg="#373a3c",
        inputbg="#fdfdfe", active="#cccccc"
    ),
    themetype="light"
)
style.register_theme(td)
style.theme_use("midnight")
```

## TTK Creator GUI
Abre la herramienta gráfica para diseñar temas.
```bash
python -m ttkcreator
```
