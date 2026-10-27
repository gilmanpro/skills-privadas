# Utilidades ttkbootstrap

## Colorutils
Convierte y ajusta colores entre distintos modelos.
```python
from ttkbootstrap.colorutils import *

color_to_rgb("#FF5733")        # → (255, 87, 51)
color_to_hex((255, 87, 51))    # → "#ff5733"
color_to_hsl("#FF5733")        # → (348, 100, 60)
update_hsl_value("#FF5733", lum=80, inmodel=HEX, outmodel=HEX)
contrast_color("#FF5733")      # → "#000" o "#fff"
conform_color_model((255,0,0), RGB)  # → "rgb(255,0,0)"
```

## Utility functions
Usa funciones auxiliares para DPI y ventanas.
```python
from ttkbootstrap.utility import *

enable_high_dpi_awareness()              # Windows: antes de Tk()
enable_high_dpi_awareness(root, 1.5)     # Linux: después de Tk()
scale_size(widget, 300)                  # escalar para high-dpi
center_on_parent(win, parent)            # centrar ventana
get_image_name(photoimage)               # nombre tcl/tk del PhotoImage
```

## Localization
Traduce textos según la configuración regional.
```python
from ttkbootstrap.localization import MessageCatalog

MessageCatalog.translate("OK")   # traduce según locale
```
