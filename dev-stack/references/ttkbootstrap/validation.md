# Validación de entrada ttkbootstrap

## Validadores integrados
Aplica validadores predefinidos a un `ttk.Entry`.
```python
from ttkbootstrap.validation import *

entry = ttk.Entry()
entry.pack(padx=10, pady=10)

add_text_validation(entry)                  # solo texto (alfabético)
add_numeric_validation(entry)               # solo números
add_phonenumber_validation(entry)           # formato teléfono
add_regex_validation(entry, r'\d{4}-\d{2}') # regex personalizado
add_range_validation(entry, 0, 100)         # rango numérico
add_option_validation(entry, ['rojo', 'verde', 'azul'])  # lista opciones
```

## Validación personalizada
Define tu propia regla con el decorador `validator`.
```python
from ttkbootstrap.validation import validator, add_validation

@validator
def validate_long_text(event):
    return len(event.postchangetext) > 20

add_validation(entry, validate_long_text, when='focusout')
```

## Momentos de validación
Especifica cuándo ejecutar la validación con `when`.
Valores válidos: `'focus'`, `'focusin'`, `'focusout'`, `'key'`, `'all'`.
