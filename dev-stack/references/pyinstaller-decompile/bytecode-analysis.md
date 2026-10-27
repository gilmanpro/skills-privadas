# Análisis de Bytecode Python (.pyc)

## Estructura del archivo .pyc

```
┌─────────────────────────────────────────────────────┐
│ Magic Number (4 bytes)                              │
│     Identifica la versión de Python                 │
│     Ej: 0xCB0D0D0A = Python 3.12                   │
├─────────────────────────────────────────────────────┤
│ Flags (4 bytes)                                     │
│     Bit 0: COMBINED_FLAG → source size presente     │
│     Bit 1-31: reservados                           │
├─────────────────────────────────────────────────────┤
│ Source Size (4 bytes) [OPCIONAL - solo si flag bit 0]│
│     Tamaño del archivo .py original                │
├─────────────────────────────────────────────────────┤
│ Objeto Code (serializado con marshal)              │
│     Contiene: constantes, nombres, bytecode, vars  │
└─────────────────────────────────────────────────────┘
```

## Lectura del .pyc con marshal

```python
import marshal, struct, dis

def leer_pyc(ruta):
    """Lee un .pyc y devuelve el objeto Code principal"""
    with open(ruta, 'rb') as f:
        magic = f.read(4)
        flags = struct.unpack('<I', f.read(4))[0]
        src_size_present = bool(flags & 1)
        if src_size_present:
            src_size = struct.unpack('<I', f.read(4))[0]
        code = marshal.load(f)
    return code

code = leer_pyc("pruebaV1.pyc")
```

## El objeto Code — Campos principales

| Atributo | Descripción | Ejemplo |
|---|---|---|
| `co_consts` | Tupla de constantes (strings, números, objetos code anidados) | `('mensaje', 10, <code object>)` |
| `co_names` | Tupla de nombres usados (imports, funciones, atributos) | `('pyautogui', 'print', 'range')` |
| `co_varnames` | Tupla de variables locales | `('x', 'inicio', 'contenido')` |
| `co_code` | Bytes del bytecode (instrucciones crudas) | `b'd\x01}\x00...'` |
| `co_stacksize` | Tamaño máximo de pila | `7` |
| `co_nlocals` | Número de variables locales | `1` |
| `co_argcount` | Número de argumentos | `0` (main), `1` (función) |
| `co_filename` | Nombre del archivo original | `'pruebaV1.py'` |
| `co_name` | Nombre de la función | `'<module>'` (main), `'mi_funcion'` |

## Análisis detallado de co_consts

Es el campo **más importante** para reconstruir el código. Contiene:

### Tipos de constantes:

```python
code = leer_pyc("archivo.pyc")

for i, c in enumerate(code.co_consts):
    tipo = type(c).__name__
    if isinstance(c, code.__class__):
        # ← ES UNA FUNCIÓN INTERNA
        print(f"[{i}] code: {c.co_name}(args={c.co_argcount}, locals={c.co_nlocals})")
        # Analizarla recursivamente
        for j, sub in enumerate(c.co_consts):
            print(f"  [{i}.{j}] {type(sub).__name__}: {repr(sub)[:80]}")
    elif isinstance(c, str):
        # ← STRING: mensaje, ruta, kwargs, o parte de print
        print(f"[{i}] str({len(c)}): {repr(c)}")
    elif isinstance(c, (int, float)):
        # ← NÚMERO: contador, timeout, repeticiones, sleep
        print(f"[{i}] num: {c}")
    elif isinstance(c, tuple):
        # ← TUPLA: secuencia de teclas, kwargs tuple, argumentos
        print(f"[{i}] tuple({len(c)}): {c}")
    elif isinstance(c, type(None)):
        print(f"[{i}] None")
    elif isinstance(c, bool):
        print(f"[{i}] bool: {c}")
    elif isinstance(c, bytes):
        print(f"[{i}] bytes({len(c)}): {c[:20]}")
    else:
        print(f"[{i}] {tipo}: {c}")
```

### Cómo interpretar cada constante:

#### Strings
- **Mensajes al usuario**: `'Esperando Ejecucion:'`, `'\nINICIANDO!'`
- **Formatos**: `'\r{i}'` (retorno de carro + número = cuenta regresiva en misma línea)
- **Rutas**: `'C:\\ruta\\archivo.xlsx'`
- **Kwargs**: `'interval'`, `'presses'` → aparecen como strings dentro de tuplas de kwargs
- **Teclas**: `'\t'` (TAB), `'backspace'`, `'down'`, `'space'`, `'up'`

#### Números
- **sleep(N)**: Si hay `time.sleep()` cerca, el número es segundos
- **range(N)**: Para loops
- **presses=N**: Cantidad de repeticiones de tecla
- **Timeout**: Segundos de espera

#### Tuplas
- **Secuencia de teclas**: `('\t', 'down', 'space')` → press en secuencia
- **Kwargs**: `('interval',)` → parte de `typewrite(x, interval=0.1)`
- **Múltiples argumentos**: `(x, y)` → llamada con dos args posicionales

#### Objetos Code (funciones internas)

Cada objeto `code` anidado es una **función definida dentro del script**. Debe analizarse por separado:

```python
def analizar_funcion(code_obj, nombre="<main>", nivel=0):
    """Analiza recursivamente un objeto Code y sus sub-funciones"""
    prefix = "  " * nivel
    print(f"{prefix}─ {nombre} ({code_obj.co_name})")
    print(f"{prefix}  Stack:{code_obj.co_stacksize} Args:{code_obj.co_argcount} Locals:{len(code_obj.co_varnames)}")
    print(f"{prefix}  Vars: {code_obj.co_varnames}")
    print(f"{prefix}  Consts({len(code_obj.co_consts)}):")
    for i, c in enumerate(code_obj.co_consts):
        if isinstance(c, code_obj.__class__):
            analizar_funcion(c, f"func_{i}", nivel+1)
        else:
            print(f"{prefix}    [{i}] {type(c).__name__}: {repr(c)[:100]}")

analizar_funcion(code)
```

## Análisis de co_names

Los names son **todos los nombres globales** que el código referencia:

```python
for i, n in enumerate(code.co_names):
    print(f"[{i}] {n}")
```

### Categorías de names:

| Categoría | Ejemplos | Cómo identificarlos |
|---|---|---|
| Módulos importados | `pyautogui`, `time`, `sys`, `openpyxl` | `import X` o `import X as Y` |
| Funciones de módulos | `load_workbook`, `sleep` | `from X import Y` |
| Built-in functions | `print`, `range`, `len`, `str`, `int` | Sin import explícito |
| Atributos llamados | `sys.argv`, `time.time` | `LOAD_ATTR` en bytecode |
| Variables globales | `contenido`, `inicio`, `fin` | No son imports ni builtins |
| Posibles imports faltantes | `buscar` | Está en names pero no es builtin ni módulo conocido → preguntar al usuario |

### Detectar imports:

```python
# Módulos comunes que aparecen en co_names
BUILTINS = {'print', 'range', 'len', 'str', 'int', 'float', 'list', 'dict',
            'tuple', 'bool', 'type', 'open', 'input', 'dir', 'hasattr',
            'getattr', 'setattr', 'isinstance', 'issubclass', 'super',
            'abs', 'all', 'any', 'bin', 'chr', 'divmod', 'enumerate',
            'eval', 'exec', 'filter', 'format', 'frozenset', 'globals',
            'hex', 'id', 'iter', 'locals', 'map', 'max', 'min', 'next',
            'object', 'oct', 'ord', 'pow', 'property', 'repr', 'reversed',
            'round', 'set', 'slice', 'sorted', 'sum', 'vars', 'zip',
            'import', 'Exception', 'BaseException', 'True', 'False', 'None'}

MODULOS_CONOCIDOS = {'pyautogui', 'time', 'sys', 'os', 'openpyxl',
                     're', 'json', 'csv', 'math', 'random', 'datetime',
                     'collections', 'itertools', 'functools', 'pathlib',
                     'shutil', 'subprocess', 'threading', 'multiprocessing'}

names_set = set(code.co_names)
imports = []
for n in code.co_names:
    if n not in BUILTINS:
        imports.append(n)

print("Posibles imports:", [n for n in imports if n in MODULOS_CONOCIDOS])
print("Posibles variables globales:", [n for n in imports if n not in MODULOS_CONOCIDOS])
```

## Análisis de co_varnames

Variables **locales** de la función:

```python
print(f"Variables locales ({len(code.co_varnames)}):")
for i, v in enumerate(code.co_varnames):
    print(f"  [{i}] {v}")
```

- Si la función principal tiene `varnames = ('x',)`, el cuerpo principal usa una variable local `x`
- Los parámetros de función aparecen PRIMERO en varnames
- Las variables de loop (`for x in ...`) aparecen en varnames

## Lectura de bytecode con dis

```python
import dis
dis.dis(code)
```

### Output de dis:

```
 0 RESUME                   0
 2 LOAD_GLOBAL              0 (pyautogui)
 4 LOAD_ATTR                1 (typewrite)
 6 LOAD_FAST                0 (x)
 8 LOAD_CONST              12 ('interval')
10 LOAD_CONST              13 (0.1)
12 CALL_FUNCTION_KW        2
...
```

### Instrucciones clave y su significado:

| Instrucción | Significado en Python |
|---|---|
| `LOAD_CONST N` | Carga la constante[N] en la pila |
| `LOAD_GLOBAL N` | Carga names[N] (módulo/función global) |
| `LOAD_FAST N` | Carga varnames[N] (variable local) |
| `STORE_FAST N` | `varnames[N] = valor` |
| `LOAD_ATTR N` | `objeto.names[N]` |
| `CALL_FUNCTION n` | `func(args_n)` |
| `CALL_FUNCTION_KW n` | `func(args_n, kwargs)` — kwargs desde co_consts |
| `BUILD_TUPLE n` | `(elem1, ..., elemN)` |
| `BUILD_LIST n` | `[elem1, ..., elemN]` |
| `FOR_ITER` | Inicio de loop `for` |
| `POP_JUMP_IF_FALSE` | `if not cond: ...` |
| `POP_JUMP_IF_TRUE` | `if cond: ...` |
| `COMPARE_OP` | Comparación (`==`, `>`, `<`, `in`, etc.) |
| `BINARY_OP` | Operación aritmética |
| `RETURN_VALUE` | `return valor` |
| `NOP` | No operación |

### Traducción de secuencias bytecode → Python:

```python
# Secuencia típica de llamada con kwargs:
# LOAD_GLOBAL    pyautogui          →  pyautogui
# LOAD_ATTR      typewrite          →  .typewrite(
# LOAD_FAST      x                  →      x,
# LOAD_CONST     'interval'         →      interval=
# LOAD_CONST     0.1                →      0.1
# CALL_FUNCTION_KW  2               →  )
# = pyautogui.typewrite(x, interval=0.1)

# Secuencia típica de press con lista:
# LOAD_GLOBAL    pyautogui
# LOAD_ATTR      press
# LOAD_CONST     ('\t', 'down', 'space')  ← tupla en constantes
# CALL_FUNCTION  1
# = pyautogui.press(['\t', 'down', 'space'])

# NOTA: si es una tupla en constantes y se llama con CALL_FUNCTION,
# la tupla se pasa como argumento posicional
```

## Funciones con kwargs (CALL_FUNCTION_KW)

Cuando ves `CALL_FUNCTION_KW n`, significa que la función se llama con argumentos de palabra clave. Los nombres de los kwargs se toman de `co_consts`:

```python
# Bytecode:
#   LOAD_CONST  12 ('interval')
#   LOAD_CONST  13 (0.1)
#   CALL_FUNCTION_KW  2
#
# Significa: el kwarg 'interval' con valor 0.1
# Python: funcion(x, interval=0.1)
#
# Otro ejemplo:
#   LOAD_CONST  15 ('\t')
#   LOAD_CONST  16 (10)
#   LOAD_CONST  17 ('presses')
#   CALL_FUNCTION_KW  2
#
# Significa: pyautogui.press('\t', presses=10)
```

## Magic Numbers de Python

| Python | Magic (hex) | Magic (bytes) |
|---|---|---|
| 3.12.0 | `0xCB0D0D0A` | `\xCB\x0D\x0D\x0A` |
| 3.11.0 | `0xAB0D0D0A` | `\xAB\x0D\x0D\x0A` |
| 3.10.0 | `0x6F0D0D0A` | `\x6F\x0D\x0D\x0A` |
| 3.9.0 | `0x610D0D0A` | `\x61\x0D\x0D\x0A` |
| 3.8.0 | `0x550D0D0A` | `\x55\x0D\x0D\x0A` |
| 3.7.0 | `0x420D0D0A` | `\x42\x0D\x0D\x0A` |

## Script completo de análisis

```python
#!/usr/bin/env python3
"""
analyze_pyc.py — Analiza un .pyc extraído de PyInstaller
"""

import marshal, struct, dis, sys

def analizar(code_obj, nivel=0, nombre="<main>"):
    prefix = "  " * nivel
    print(f"{prefix}{'─' * min(50, 50 - nivel*2)}")
    print(f"{prefix}FUNCIÓN: {nombre}")
    print(f"{prefix}  name: {code_obj.co_name}")
    print(f"{prefix}  filename: {code_obj.co_filename}")
    print(f"{prefix}  args: {code_obj.co_argcount}")
    print(f"{prefix}  locals: {code_obj.co_nlocals}")
    print(f"{prefix}  stack: {code_obj.co_stacksize}")
    
    print(f"{prefix}  ── varnames ({len(code_obj.co_varnames)}) ──")
    for i, v in enumerate(code_obj.co_varnames):
        print(f"{prefix}    [{i}] {v}")
    
    print(f"{prefix}  ── names ({len(code_obj.co_names)}) ──")
    for i, n in enumerate(code_obj.co_names):
        print(f"{prefix}    [{i}] {n}")
    
    print(f"{prefix}  ── consts ({len(code_obj.co_consts)}) ──")
    for i, c in enumerate(code_obj.co_consts):
        if hasattr(c, 'co_code'):  # Es un objeto Code anidado
            print(f"{prefix}    [{i}] <code object {c.co_name}>")
            analizar(c, nivel + 1, f"func_{i}({c.co_name})")
        else:
            tipo = type(c).__name__
            valor = repr(c)[:120]
            print(f"{prefix}    [{i}] {tipo}: {valor}")
    
    print(f"{prefix}  ── bytecode ──")
    dis.dis(code_obj)

if len(sys.argv) < 2:
    print("Uso: py analyze_pyc.py <archivo.pyc>")
    sys.exit(1)

with open(sys.argv[1], 'rb') as f:
    magic = f.read(4)
    flags = struct.unpack('<I', f.read(4))[0]
    if flags & 1:
        f.read(4)
    code = marshal.load(f)

print(f"Magic: {magic.hex()} (Python {'.'.join(str(v) for v in [3, 12, 0])})\n")
analizar(code)
```
