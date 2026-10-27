# Scrolled widgets ttkbootstrap

## ScrolledFrame
Crea un frame con scrollbars automáticos.
```python
from ttkbootstrap.scrolled import ScrolledFrame

sf = ScrolledFrame(app, autohide=True, bootstyle="primary",
                   height=200, width=300, scrollheight=None)
sf.pack(fill=BOTH, expand=YES, padx=10, pady=10)
```
Métodos: `enable_scrolling()`, `disable_scrolling()`, `hide_scrollbars()`, `show_scrollbars()`, `autohide_scrollbar()`.

**Nota:** Los métodos de geometría (`pack`, `grid`, `place`) del `ScrolledFrame` actúan sobre el **container**. Para el **content frame**, usa `content_pack()`, `content_grid()`, `content_place()`.

## ScrolledText
Crea un widget Text con scrollbars.
```python
from ttkbootstrap.scrolled import ScrolledText

st = ScrolledText(app, padding=5, height=10, autohide=True,
                  vbar=True, hbar=False, bootstyle="primary")
st.pack(fill=BOTH, expand=YES)
st.insert(END, 'Texto aquí.')
```
Propiedades: `text` (widget Text interno), `vbar`, `hbar`.

## Uso en Notebook o Panedwindow
Añade el contenedor interno, no el widget scrolled.
```python
mynotebook.add(myscrolledframe.container)
```
