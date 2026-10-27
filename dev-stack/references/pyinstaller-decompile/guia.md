
# DECONSTRUCCIÓN DE EJECUTABLES PYINSTALLER

Skill especializada en **deconstruir ejecutables PyInstaller** para recuperar el código fuente Python original, paso a paso, con preguntas interactivas al usuario.

> ⚠️ **ADVERTENCIA LEGAL**: Solo decompiles .exe que te pertenezcan o para los que tengas autorización explícita. No uses esta skill para ingeniería inversa de software del que no eres dueño.

---

## 1. FLUJO DE TRABAJO COMPLETO

```
┌─────────────────────────────────────────────────┐
│ 1. DETECTAR si es PyInstaller (file header)     │
├─────────────────────────────────────────────────┤
│ 2. EXTRAER .pyc con pyinstxtractor              │
├─────────────────────────────────────────────────┤
│ 3. IDENTIFICAR entry point (pruebaV1.pyc, etc)  │
├─────────────────────────────────────────────────┤
│ 4. LEER BYTECODE con marshal.load()             │
├─────────────────────────────────────────────────┤
│ 5. ANALIZAR: constantes, names, varnames        │
├─────────────────────────────────────────────────┤
│ 6. RECONSTRUIR source manualmente               │
├─────────────────────────────────────────────────┤
│ 7. PREGUNTAR al usuario sobre comportamiento    │
├─────────────────────────────────────────────────┤
│ 8. REFINAR basado en feedback                   │
├─────────────────────────────────────────────────┤
│ 9. VERIFICAR sintaxis (ast.parse)               │
├─────────────────────────────────────────────────┤
│ 10. ENTREGAR código + documentación             │
└─────────────────────────────────────────────────┘
```

---

## 2. PASO 1 — DETECTAR SI ES PYINSTALLER

Antes de nada, verifica si el .exe fue empaquetado con PyInstaller:

```bash
# Buscar la firma PyInstaller en el .exe
py -c "
data = open(r'CAMINO_AL.EXE', 'rb').read()
# PyInstaller onefile: buscar 'PyInstaller' en los últimos 10KB
idx = data.rfind(b'PyInstaller')
if idx >= 0:
    print(f'✅ ES PYINSTALLER (offset: {idx})')
    # Extraer versión
    end = data.find(b'\x00', idx)
    print(f'   Versión: {data[idx:end].decode(\"utf-8\", errors=\"replace\")}')
else:
    print('❌ NO es PyInstaller (o es onefile comprimido)')
    # Buscar otros indicadores
    if b'!<arch>' in data[:8]:
        print('   Parece Unix AR archivo')
    if data[:2] == b'MZ':
        print('   Es un .exe genérico Windows')
"
```

**Indicadores PyInstaller:**
- Contiene la string `PyInstaller` en los últimos bytes del .exe
- Contiene `_PYI` o `PYZ` en las secciones del archivo
- En onefile: tiene un gran blob comprimido (zlib) al final
- En onedir: la carpeta `_internal/` contiene los archivos .pyc

---

## 3. PASO 2 — EXTRAER .pyc CON PYINSTXTRACTOR

Usa `pyinstxtractor` (https://github.com/extremecoders-re/pyinstxtractor):

```bash
# Descargar pyinstxtractor
curl -LO https://raw.githubusercontent.com/extremecoders-re/pyinstxtractor/master/pyinstxtractor.py

# Extraer
py pyinstxtractor.py pruebaV1.exe
```

**Output esperado:**
```
[+] Processing pruebaV1.exe
[+] PyInstaller version: 6.x
[+] Python version: 3.12
[+] Length of package: 12345678 bytes
[+] Found 963 files in CArchive
[+] Successfully extracted to: pruebaV1.exe_extracted/
```

**Si pyinstxtractor falla:**
- Versión antigua de PyInstaller (< 3.0): usa `archive_viewer.py` que viene con PyInstaller
- PyInstaller 6+ onefile comprimido: extrae manual con zlib

Lee `references/pyinstaller-decompile/pyinstxtractor.md` para más detalles y troubleshooting.

---

## 4. PASO 3 — IDENTIFICAR ENTRY POINT

El entry point es el script principal del .exe:

```bash
# Listar archivos extraídos
dir /B pruebaV1.exe_extracted\

# Buscar el entry point (suele ser el nombre del .exe o 'main', '__main__', etc)
# El .pyc del entry point NO tiene estructura PYZ — es un .pyc plano
```

**Señales del entry point:**
- Nombrado como el .exe (ej: `pruebaV1.pyc`)
- O `__main__.pyc` o `main.pyc`
- En `pyiboot01_bootstrap.pyc` está el bootloader (no decompiles este)
- **NO es parte de PYZ** — está en la raíz de la extracción, no en `PYZ-00.pyz`

```python
# Verificar si un .pyc es entry point (tiene código, no es sólo import)
import dis, marshal, struct

with open('archivo.pyc', 'rb') as f:
    magic = f.read(4)          # Magic number
    flags = struct.unpack('<I', f.read(4))[0]  # Flags (bit 0 = source size present)
    if flags & 1:
        f.read(4)              # Source size (omitir)
    code = marshal.load(f)     # Cargar objeto code

print(f"Stack: {code.co_stacksize}, Args: {code.co_argcount}")
print(f"Nombres importados: {code.co_names}")
```

---

## 5. PASO 4 — LEER BYTECODE CON MARSHAL

### 5.1 Estructura de un .pyc

```
┌──────────────────────────────┐
│ Magic (4 bytes)              │ ← Python version marker
├──────────────────────────────┤
│ Flags (4 bytes)              │ ← Bit 0: source size present
├──────────────────────────────┤
│ Source Size (4 bytes, opt.)  │ ← Solo si flags & 1
├──────────────────────────────┤
│ Objeto Code (marshal)        │ ← Aquí está el bytecode
│ - co_consts                  │
│ - co_names                   │
│ - co_varnames                │
│ - co_code (bytes)            │
│ - co_stacksize               │
│ - co_nlocals                 │
└──────────────────────────────┘
```

### 5.2 Leer el objeto Code

```python
import marshal, struct, dis

with open('pruebaV1.pyc', 'rb') as f:
    magic = f.read(4)
    flags = struct.unpack('<I', f.read(4))[0]
    if flags & 1:
        f.read(4)  # source size
    code = marshal.load(f)

print("=== CÓDIGO PRINCIPAL ===")
print(f"Stack: {code.co_stacksize}")
print(f"Args: {code.co_argcount}")
print(f"Locals: {code.co_varnames}")
print(f"Constants ({len(code.co_consts)}):")
for i, c in enumerate(code.co_consts):
    print(f"  [{i}] {type(c).__name__}: {repr(c)[:100]}")
print(f"Names ({len(code.co_names)}):")
for i, n in enumerate(code.co_names):
    print(f"  [{i}] {n}")
print(f"\nBytecode:")
dis.dis(code)
```

Lee `references/pyinstaller-decompile/bytecode-analysis.md` para entender cada campo del objeto Code.

---

## 6. PASO 5 — ANALIZAR CONSTANTES, NAMES Y VARNAMES

Esta es la parte más crítica. Tienes que extraer el significado de cada constante y nombre.

### Qué buscar en co_consts:

| Tipo | Significado |
|------|-------------|
| `str` | Strings literales — pueden ser: mensajes, rutas, kwargs |
| `int` | Números — pueden ser: repeticiones, timeouts, índices |
| `tuple` | Tuplas — pueden ser: secuencias de teclas, kwargs, argumentos |
| `code` | Objeto código anidado — **FUNCIÓN INTERNA** |
| `None` | Return implícito |

### Qué buscar en co_names:

| Tipo | Significado |
|------|-------------|
| Nombres de módulo | `pyautogui`, `time`, `openpyxl`, `sys` |
| Funciones importadas | `load_workbook`, `sleep` |
| Variables globales | Nombres de variable del programa |
| Atributos | Nombres de método usados |
| Funciones built-in | `print`, `range`, `len`, `str`, `int` |
| Variables no declaradas | Pueden ser imports o builtins faltantes |

### Qué buscar en co_varnames:

Son las variables LOCALES de la función principal. Si hay funciones internas, tendrán sus propias `co_varnames`.

### EJEMPLO REAL (de la conversación):

```
Constants:
  [0] code      ← función leer_columna_excel_solo_numeros()
  [1] code      ← función transformar_a_string()
  [2] str: 'Esperando Ejecucion:'    ← mensaje
  [3] int: 9                          ← range start
  [4] int: -1                         ← range stop
  [5] int: -1                         ← range step
  [6] str: '\r{i}'                    ← formato countdown
  [7] str: ''                         ← end=""
  [8] bool: True                      ← flush=True
  [9] int: 1                          ← sleep(1)
  [10] int: 3                         ← sleep(3)
  [11] str: '\nINICIANDO!'
  [12] tuple: ('interval',)           ← kwargs de typewrite
  [13] str: ' - '
  [14] tuple: ('\t', 'down', 'space') ← secuencia de teclas
  [15] str: '\t'                      ← tecla TAB
  [16] int: 10                        ← presses=10 (repeticiones)
  [17] tuple: ('presses',)            ← kwargs de press
  [18] str: 'backspace'
  [19] str: 'tiempo: '

Names:
  [0] pyautogui           ← módulo importado
  [1] time                ← módulo importado
  [2] openpyxl            ← módulo importado
  [3] load_workbook       ← función importada
  [4] sys                 ← módulo importado
  ...
```

---

## 7. PASO 6 — RECONSTRUIR SOURCE MANUALMENTE

Basado en constantes + names + varnames + bytecode, reconstruye el código.

### Reglas de correspondencia bytecode → Python:

```python
# LOAD_CONST 0       →  código anidado (función)
# LOAD_CONST 2       →  "mensaje"
# LOAD_GLOBAL 0      →  pyautogui
# LOAD_GLOBAL 4      →  sys
# LOAD_ATTR 5        →  sys.argv
# CALL_FUNCTION n    →  llamar función con n args
# CALL_FUNCTION_KW n →  llamar función con n args + kwargs (kw desde co_consts)
# BUILD_TUPLE n      →  tupla de n elementos
# BUILD_LIST n       →  lista de n elementos
# FOR_ITER           →  for x in iterable
# STORE_FAST 0       →  x = (asignar a variable local)
# DELETE_FAST 0      →  del x
```

### Proceso de reconstrucción:

1. **Separa las funciones internas** (objetos code en co_consts)
2. **Identifica imports** desde co_names
3. **Reconstruye la lógica principal** siguiendo el flujo del bytecode
4. **Verifica con el usuario** la secuencia exacta de operaciones
5. **Documenta el % de certeza** de cada parte reconstruida

### Para Python 3.12+:

`decompyle3` y `uncompyle6` **NO soportan Python 3.12+**. La reconstrucción debe ser manual usando:
- `marshal.load()` para leer el bytecode
- `dis.dis()` para visualizar las instrucciones
- Conocimiento de la estructura bytecode de Python

`pycdc` (https://github.com/zrax/pycdc) tiene soporte parcial de 3.12 (probar antes de confiar) y requiere compilar desde C++.

---

## 8. PASO 7 — PREGUNTAR AL USUARIO (MUY IMPORTANTE)

**NUNCA asumas el significado de las constantes por tu cuenta.** Siempre PRESENTA tu análisis al usuario y PREGUNTA.

### Plantilla de preguntas al usuario:

```markdown
## 🔍 Análisis del bytecode

### Lo que encontré en el bytecode:

**Constantes identificadas:**
- `[N] STR: '...'` → posible mensaje o ruta
- `[N] INT: X` → podría ser un contador, repeticiones, o timeout
- `[N] TUPLE: (...)` → secuencia de argumentos o teclas

**Names (módulos/funciones detectados):**
- `pyautogui` → automatización de teclado/ratón
- `openpyxl` → lectura de Excel
- `sys` → argumentos de línea de comandos
- `time` → pausas/intervalos

### ❓ Preguntas para ti:

1. **Sobre la constante [N] INT={valor}:** Encontré este número en la secuencia de teclas. ¿Podría ser la cantidad de repeticiones de una tecla? ¿O es un timeout/intervalo?

2. **Sobre la secuencia de teclado:** Veo que usa `press([...])`. ¿Qué sistema tiene el foco cuando se ejecuta? ¿Es GoalReport, un formulario web, o una app específica?

3. **Sobre el comportamiento observado:** Cuando ejecutas el .exe, ¿qué ves? ¿Teclea números? ¿Cuántas veces presiona TAB? ¿Alguna vez viste que borre lo escrito?

4. **Sobre el Excel de entrada:** ¿Los datos en el Excel son solo números? ¿En qué columna están? ¿Hay encabezados?
```

### Por qué las preguntas son esenciales:

- Un `INT: 10` podría ser `presses=10` (repetir 10 veces) o `range(10)` o `sleep(10)`
- Una `TUPLE: ('\t', 'down', 'space')` puede tener significados distintos según el sistema destino
- El usuario conoce el **comportamiento observado** — tú solo tienes el bytecode
- **Caso real documentado:** En la conversación de referencia, el INT: 10 resultó ser `presses=10` (10 TABs), no un timeout. El usuario corrigió la interpretación inicial.

---

## 9. PASO 8 — REFINAR BASADO EN FEEDBACK

Una vez que el usuario responde:

1. **Actualiza la interpretación** de constantes ambiguas
2. **Corrige la secuencia** de operaciones
3. **Ajusta parámetros** (intervalos, repeticiones, orden de teclas)
4. **Reconstruye el código** con la nueva información
5. **Pregunta de nuevo** si hay dudas residuales

### Ejemplo de refinamiento (de la conversación):

```
VERSIÓN INICIAL (incorrecta):
  typewrite(num, interval=0.1)
  press(['\t', 'down', 'space'])
  press('backspace')

VERSIÓN CORREGIDA (con feedback del usuario):
  typewrite(num, interval=0.1)
  press(['\t', 'down', 'space'])
  press('\t', presses=10)     ← 10 TABs! no backspace directo
  press('backspace')
```

---

## 10. PASO 9 — VERIFICAR SINTAXIS

```bash
# Verificar que el código reconstruido tiene sintaxis válida
py -c "
import ast
with open('codigo_reconstruido.py', 'r', encoding='utf-8') as f:
    ast.parse(f.read())
print('✅ Sintaxis OK')
"
```

Si hay errores de sintaxis, corrige y verifica de nuevo. **NUNCA entregues código con errores de sintaxis.**

---

## 11. PASO 10 — ENTREGAR CÓDIGO + DOCUMENTACIÓN

### Estructura de entrega:

````markdown
---
## 📦 CÓDIGO FUENTE DECOMPILADO

### 🔬 Proceso completo
| Paso | Herramienta | Resultado |
|---|---|---|
| 1. Extraer .pyc | pyinstxtractor v2.0 | ✅ X archivos, entry point: script.pyc |
| 2. Analizar bytecode | marshal.load() + xdis | ✅ Stack=N, Args=0, Locals=... |
| 3. Reconstruir | Manual desde bytecode | ✅ ~N% fidelidad |

### 📁 Archivos generados
```
ruta/de/salida/
├── script_reconstruido.py    ← Código reconstruido
├── extracto_bytecode.txt     ← Análisis completo del bytecode
└── README.md                 ← Documentación
```

### 💻 Lo que hace el código
```python
# Descripción del comportamiento reconstruido
# 1. Lee Excel, columna A
# 2. Cuenta regresiva 9→0
# 3. Por cada número: tipea, navega, borra
```

### ⚠️ Lo que NO se pudo recuperar (% de certeza)
- Partes con 100% de certeza (bytecode sin ambigüedad)
- Partes con ~80-90% (requirió interpretación)
- Partes con <80% (basado en feedback del usuario)
````

---

## 12. HERRAMIENTAS DEL FLUJO

| Herramienta | Propósito | URL |
|---|---|---|
| **pyinstxtractor** | Extrae .pyc del .exe | https://github.com/extremecoders-re/pyinstxtractor |
| **marshal** (stdlib) | Lee objetos Code del .pyc | Built-in de Python |
| **dis** (stdlib) | Desensambla bytecode a legible | Built-in de Python |
| **xdis** (pip) | Analiza bytecode cross-version | `pip install xdis` |
| **decompyle3** (pip) | Decompila Python 3.7-3.8 | No soporta 3.12+ |
| **uncompyle6** (pip) | Decompila Python 3.x | No soporta 3.12+ |
| **pycdc** (C++) | Decompila Python 3.9+; soporte parcial en 3.12+ (probar antes de confiar) | https://github.com/zrax/pycdc |
| `ast.parse()` | Verifica sintaxis | Built-in de Python |

---

## 13. ANTIPATRONES Y ERRORES COMUNES

### ❌ Asumir el significado de constantes sin preguntar
**Correcto:** "Encontré un INT: 10 en el bytecode. ¿Podría ser la cantidad de repeticiones de una tecla?"

### ❌ Usar decompyle3 en .pyc de Python 3.12+
**Correcto:** Verificar la versión de Python del .pyc (el magic number) antes de elegir el decompilador.

### ❌ Ignorar funciones anidadas (objetos code en co_consts)
**Correcto:** Cada objeto `code` en `co_consts` es una función interna. Debes decompilarlas por separado.

### ❌ Entregar código sin verificar sintaxis
**Correcto:** Siempre ejecutar `ast.parse()` antes de entregar.

### ❌ No documentar el % de certeza
**Correcto:** Cada parte reconstruida debe tener su nivel de confianza documentado.

---

## 14. MÁS RECURSOS

- `references/pyinstaller-decompile/pyinstxtractor.md` — Guía detallada de pyinstxtractor + troubleshooting
- `references/pyinstaller-decompile/bytecode-analysis.md` — Cómo analizar bytecode Python manualmente
- `references/pyinstaller-decompile/interactive-flow.md` — Patrones de preguntas al usuario + ejemplos reales
- `scripts/extract_and_analyze.py` — Script automatizado: extrae + analiza bytecode en un solo comando
