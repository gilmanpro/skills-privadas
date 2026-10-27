# Widgets ttkbootstrap

## Widgets TTK estándar
Aplica `bootstyle` a cualquier widget ttk estándar para color y tipo.

### Button
Usa `bootstyle` para variantes de botón.
```python
ttk.Button(text="Enviar", bootstyle="success")
ttk.Button(text="Cancelar", bootstyle=(DANGER, OUTLINE))
ttk.Button(text="Link", bootstyle="link")
```

### Label
```python
ttk.Label(text="Texto", bootstyle="inverse-primary")
ttk.Label(text="Info", bootstyle="info")
```

### Entry
```python
ttk.Entry(bootstyle="success")
ttk.Entry(bootstyle="danger")  # borde rojo
```

### Combobox
```python
ttk.Combobox(values=["A", "B", "C"], bootstyle="primary")
```

### Spinbox
```python
ttk.Spinbox(from_=0, to=100, bootstyle="info")
```

### Checkbutton / Radiobutton
```python
ttk.Checkbutton(text="Aceptar", bootstyle="success")
ttk.Radiobutton(text="Opción 1", value=1, bootstyle="primary")
```

### Progressbar
```python
ttk.Progressbar(length=300, bootstyle="success", mode="determinate")
ttk.Progressbar(bootstyle="success-striped")  # con rayas
```

### Scale
```python
ttk.Scale(from_=0, to=100, bootstyle="warning")
```

### Scrollbar
```python
ttk.Scrollbar(orient=VERTICAL, bootstyle="primary")
ttk.Scrollbar(bootstyle="primary-round")  # esquinas redondeadas
```

### Treeview
```python
ttk.Treeview(columns=("col1", "col2"), bootstyle="primary")
```

### Separator
```python
ttk.Separator(orient=HORIZONTAL)
```

### Notebook
```python
ttk.Notebook(bootstyle="primary")
```

### Labelframe
```python
ttk.Labelframe(text="Datos", bootstyle="primary")
```

### Sizegrip
```python
ttk.Sizegrip()
```

### Menubutton / OptionMenu
```python
ttk.Menubutton(text="Menú", bootstyle="primary")
```

### Panedwindow
```python
ttk.Panedwindow(orient=HORIZONTAL)
```

## Widgets personalizados
Usa estos widgets adicionales que proporciona ttkbootstrap.

### Meter
Crea un medidor radial con valor actual y máximo.
```python
ttk.Meter(
    metersize=180,           # tamaño del cuadrado en px
    padding=5,
    amounttotal=100,         # valor máximo
    amountused=25,           # valor actual
    amountformat="{:.0f}",   # formato del texto central
    metertype="full",        # "full" | "semi"
    meterthickness=10,       # grosor del arco
    bootstyle="primary",     # color del indicador
    interactive=False,       # interactivo (dial)
    showtext=True,           # muestra texto central
    textleft="$",            # texto izquierdo
    textright="%",           # texto derecho
    subtext="cargando...",   # texto debajo
    subtextstyle="default",  # estilo del subtexto
    stripethickness=0,       # >0 para rayas en el arco
    wedgesize=0,             # tamaño de cuña indicadora
    stepsize=1,              # incremento por interacción
    arcrange=None,           # rango del arco en grados
    arcoffset=None,          # offset inicial en grados
)
```
Métodos:
```python
meter.configure(amountused=50)
meter.step(10)
meter.step(-15)
```
Variables accesibles: `amountusedvar`, `amounttotalvar`, `labelvar`.

### Floodgauge
Crea una barra de progreso animada.
```python
ttk.Floodgauge(
    value=0,                # valor inicial
    maximum=100,            # valor máximo
    mode="determinate",     # "determinate" | "indeterminate"
    mask="Progress: {}%",   # formato del texto con {}
    text="",                # texto fijo
    font=("Helvetica", 12), # fuente
    bootstyle="primary",    # color
    orient="horizontal",    # "horizontal" | "vertical"
    length=200,             # largo
    thickness=50,           # grosor
    variable=IntVar(),      # variable vinculada
    textvariable=StringVar(),# variable de texto vinculada
)
```
Métodos:
```python
flood.start(step_size=1, interval=50)
flood.stop()
flood.step(amount=1)
```

### DateEntry
Crea un selector de fecha.
```python
ttk.DateEntry(
    dateformat="%x",         # formato strftime
    firstweekday=6,          # 0=lunes, 6=domingo
    startdate=datetime.today(),  # fecha inicial
    bootstyle="primary",     # color
    popup_title="Seleccionar fecha",
    raise_exception=False,   # lanzar error si fecha inválida
)
```
Atributos: `entry`, `button`.
Métodos:
```python
de.get_date()
de.set_date(datetime(2024, 1, 1))
de.enable()
de.disable()
```
Evento: `<<DateEntrySelected>>`.

## Tableview
Usa `Tableview` para tablas de datos con paginación y búsqueda.
```python
from ttkbootstrap.tableview import Tableview

coldata = [
    {"text": "LicenseNumber", "stretch": False},
    "CompanyName",
    {"text": "UserCount", "stretch": False},
]
rowdata = [
    ('A123', 'IzzyCo', 12),
    ('A136', 'Kimdee Inc.', 45),
]

dt = Tableview(
    master=app,
    coldata=coldata,
    rowdata=rowdata,
    paginated=True,
    searchable=True,
    bootstyle=PRIMARY,
    stripecolor=(colors.light, None),
)
dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)

dt.insert_row('end', ['Marzale LLC', 26])
```
Características: filas rayadas, paginación, columnas autoajustables, ordenamiento por click, menú contextual.

## ToolTip
Muestra ayuda emergente al pasar el cursor sobre un widget.
```python
from ttkbootstrap.tooltip import ToolTip

ToolTip(widget, text="Texto de ayuda")
ToolTip(widget, text="Peligro", bootstyle=(DANGER, INVERSE),
        delay=250, padding=10, wraplength=300,
        position="top left")  # "top", "bottom", "left", "right", "center"
```

## ToastNotification
Muestra notificaciones temporales en pantalla.
```python
from ttkbootstrap.toast import ToastNotification

toast = ToastNotification(
    title="Notificación",
    message="Mensaje importante",
    duration=3000,          # ms, None = clic para cerrar
    bootstyle=LIGHT,
    alert=False,
    icon="⚠️",
    position=(100, 100, 'ne'),  # (x, y, anchor)
    alpha=0.95,
)
toast.show_toast()
toast.hide_toast()
```

## Icons
Usa íconos integrados para diálogos e indicadores.
```python
from ttkbootstrap.icons import Icon

img = tk.PhotoImage(data=Icon.warning)
img = tk.PhotoImage(data=Icon.error)
img = tk.PhotoImage(data=Icon.question)
img = tk.PhotoImage(data=Icon.info)
img = tk.PhotoImage(data=Icon.icon)  # logo ttkbootstrap
```

## Emoji
Usa caracteres emoji como atributos de clase.
```python
from ttkbootstrap.icons import Emoji

label = ttk.Label(text=Emoji.HEART)
```

## Legacy widgets
Aplica estilo automático a widgets tkinter clásicos.
```python
# autostyle=True (default) → ttkbootstrap maneja el estilo
text = tk.Text(master, autostyle=True)

# autostyle=False → el usuario controla el estilo
text = tk.Text(master, autostyle=False)
```

## Ejemplo completo
Usa este esqueleto como punto de partida para una app con pestañas.
```python
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification

root = ttk.Window(title="Mi App", themename="darkly", size=(800, 600))
root.place_window_center()

notebook = ttk.Notebook(root, bootstyle="primary")
notebook.pack(fill=BOTH, expand=YES, padx=10, pady=10)

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Formulario")

ttk.Label(tab1, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
ttk.Entry(tab1, width=30).grid(row=0, column=1, padx=5, pady=5)

ttk.Button(tab1, text="Guardar", bootstyle=SUCCESS).grid(row=1, column=1, sticky=E, pady=10)
ttk.Button(tab1, text="Cancelar", bootstyle=(DANGER, OUTLINE)).grid(row=1, column=0, sticky=E, pady=10)

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Progreso")

meter = ttk.Meter(tab2, metersize=150, amountused=65, metertype="semi",
                  subtext="completado", bootstyle="success", interactive=True)
meter.pack(pady=20)

flood = ttk.Floodgauge(tab2, mode="determinate", bootstyle="info",
                        mask="Progreso: {}%", length=300)
flood.pack(pady=10)
flood.start()

tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Lista")

sf = ScrolledFrame(tab3, autohide=True)
sf.pack(fill=BOTH, expand=YES)
for i in range(50):
    ttk.Checkbutton(sf, text=f"Opción {i}").pack(anchor=W)

root.mainloop()
```
