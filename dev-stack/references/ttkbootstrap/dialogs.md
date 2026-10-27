# Dialogs ttkbootstrap

## Messagebox
Muestra diálogos predefinidos con botones estándar.
```python
from ttkbootstrap.dialogs import Messagebox

Messagebox.show_info("mensaje", "Título")
Messagebox.show_warning("mensaje", "Título")
Messagebox.show_error("mensaje", "Título")
Messagebox.show_question("pregunta", "Título")
Messagebox.ok("mensaje")
Messagebox.okcancel("mensaje")          # retorna str o None
Messagebox.yesno("mensaje")             # retorna "Yes" o "No"
Messagebox.yesnocancel("mensaje")       # retorna str
Messagebox.retrycancel("mensaje")       # retorna str
```

## Querybox
Solicita datos al usuario con validación integrada.
```python
from ttkbootstrap.dialogs import Querybox

Querybox.get_string(prompt="Nombre:", title="Input")
Querybox.get_integer(prompt="Edad:", title="Número",
                     initialvalue=18, minvalue=0, maxvalue=150)
Querybox.get_float(prompt="Precio:", title="Decimal")
Querybox.get_date(title="Fecha", startdate=date.today(),
                  bootstyle="primary")
Querybox.get_color(title="Color", initialcolor="#ff0000")
Querybox.get_item(prompt="Opción:", items=["A","B","C"])
Querybox.get_font()
```

## Dialog
Crea diálogos personalizados heredando de la clase base.
```python
from ttkbootstrap.dialogs import Dialog

class MiDialog(Dialog):
    def create_body(self, master):
        # construir widgets
        pass
    def create_buttonbox(self, master):
        # construir botones
        pass

d = MiDialog(parent=ventana, title="Mi diálogo")
d.show()
```

## MessageDialog
Construye diálogos con botones personalizables.
```python
from ttkbootstrap.dialogs import MessageDialog

d = MessageDialog(
    message="¿Está seguro?",
    title="Confirmar",
    buttons=["Cancelar", "Aceptar:primary"],
    default="Aceptar",
    icon=Icon.question,
    padding=(20, 20),
    width=50,
)
d.show()
print(d.result)
```

## QueryDialog
Crea diálogos de entrada con tipo de dato y lista opcional.
```python
from ttkbootstrap.dialogs import QueryDialog

d = QueryDialog(prompt="Nombre:", title="Entrada",
                initialvalue="", datatype=str,
                items=["A","B","C"])  # Combobox si hay items
d.show()
print(d._result)
```

## FontDialog
Permite al usuario seleccionar una fuente.
```python
from ttkbootstrap.dialogs import FontDialog

d = FontDialog(title="Seleccionar fuente",
               default_font="TkDefaultFont")
d.show()
font = d.result  # tkinter.font.Font object
```
