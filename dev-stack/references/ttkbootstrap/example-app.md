# Ejemplo de aplicación completa

Aplicación con pestañas, formulario, progreso y lista scrollable.

```python
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame

root = ttk.Window(title="Mi App", themename="darkly", size=(800, 600))
root.place_window_center()

notebook = ttk.Notebook(root, bootstyle="primary")
notebook.pack(fill=BOTH, expand=YES, padx=10, pady=10)

# Pestaña 1: Formulario
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Formulario")

ttk.Label(tab1, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
ttk.Entry(tab1, width=30).grid(row=0, column=1, padx=5, pady=5)

ttk.Button(tab1, text="Guardar", bootstyle=SUCCESS).grid(row=1, column=1, sticky=E, pady=10)
ttk.Button(tab1, text="Cancelar", bootstyle=(DANGER, OUTLINE)).grid(row=1, column=0, sticky=E, pady=10)

# Pestaña 2: Progreso
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Progreso")

meter = ttk.Meter(tab2, metersize=150, amountused=65, metertype="semi",
                  subtext="completado", bootstyle="success", interactive=True)
meter.pack(pady=20)

flood = ttk.Floodgauge(tab2, mode="determinate", bootstyle="info",
                        mask="Progreso: {}%", length=300)
flood.pack(pady=10)
flood.start()

# Pestaña 3: Lista scrollable
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Lista")

sf = ScrolledFrame(tab3, autohide=True)
sf.pack(fill=BOTH, expand=YES)
for i in range(50):
    ttk.Checkbutton(sf, text=f"Opción {i}").pack(anchor=W)

root.mainloop()
```
