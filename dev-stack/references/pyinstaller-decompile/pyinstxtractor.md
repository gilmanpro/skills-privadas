# pyinstxtractor — Extracción de .pyc desde ejecutables PyInstaller

## ¿Qué es pyinstxtractor?

Herramienta Python que extrae los archivos `.pyc` empaquetados dentro de ejecutables PyInstaller (.exe en Windows, .bin en Linux). Funciona con PyInstaller 2.x hasta 6.x.

**Repo oficial:** https://github.com/extremecoders-re/pyinstxtractor

## Instalación

No requiere instalación — es un script Python único:

```bash
# Descargar
curl -LO https://raw.githubusercontent.com/extremecoders-re/pyinstxtractor/master/pyinstxtractor.py

# Verificar que descargó correctamente
py -c "import py_compile; py_compile.compile('pyinstxtractor.py', doraise=True); print('✅ Script válido')"
```

## Uso básico

```bash
py pyinstxtractor.py pruebaV1.exe
```

**Output típico:**
```
[+] Processing pruebaV1.exe
[+] PyInstaller version: 6.10.0
[+] Python version: 3.12
[+] Length of package: 7340032 bytes
[+] Found 963 files in CArchive
[+] Successfully extracted to: pruebaV1.exe_extracted/
```

## Estructura de archivos extraídos

```
pruebaV1.exe_extracted/
├── pyimod01_os_path.pyc        ← Bootloader (no decompilar)
├── pyimod02_archive.pyc        ← Bootloader
├── pyimod03_importers.pyc      ← Bootloader
├── pyiboot01_bootstrap.pyc     ← Bootstrap
├── pruebaV1.pyc                ← ★ ENTRY POINT (el script principal)
├── PYZ-00.pyz                  ← Librerías comprimidas (stdlib + dependencias)
├── struct.pyc                  ← De PYZ (extraídas automáticamente)
├── ... (cientos de .pyc)       ← Dependencias
└── out00-PYZ.pyz               ← Extracción de PYZ (si existe)
```

### Identificar el entry point:

El entry point es el `.pyc` que:
1. Está en la **raíz** de la extracción (no dentro de PYZ)
2. Tiene el **mismo nombre que el .exe** (ej: `pruebaV1.pyc` → `pruebaV1.exe`)
3. **NO** es `pyiboot01_bootstrap.pyc` ni `pyimod*.pyc`

```python
import os, glob

extracted_dir = "pruebaV1.exe_extracted"
exe_name = "pruebaV1"

# El entry point suele ser así
entry = os.path.join(extracted_dir, f"{exe_name}.pyc")
if os.path.exists(entry):
    print(f"✅ Entry point: {entry}")
```

## Troubleshooting

### Error: "magic number mismatch"

El magic number del .pyc no coincide con la versión de Python que estás usando. Usa Python 3.12 para .pyc de Python 3.12:

```bash
# Ver magic number del .pyc
py -c "
import struct
with open('archivo.pyc', 'rb') as f:
    magic = f.read(4)
    print(f'Magic: {magic.hex()}')
    # Python 3.12: 0xCB0D0D0A
    # Python 3.11: 0xAB0D0D0A
    # Python 3.10: 0x6F0D0D0A
    # Python 3.9:  0x610D0D0A
"
```

### Error: "Failure to decompile" o el .pyc no es válido

Algunos .pyc pueden estar comprimidos o cifrados. Prueba:

```bash
# Verificar si el archivo empieza con el magic number correcto
py -c "
with open('archivo.pyc', 'rb') as f:
    header = f.read(16)
    print('Header hex:', header.hex())
    if header[:4] == b'\xCB\x0D\x0D\x0A':
        print('✅ Magic Python 3.12')
    elif header[:4] == b'\x6F\x0D\x0D\x0A':
        print('✅ Magic Python 3.10')
    else:
        print('❌ Magic desconocido - posible daño o cifrado')
"
```

### Error: "CArchive not found" o no se extrae nada

PyInstaller onefile moderno (6.x+) usa compresión zlib:

```bash
# Buscar manualmente el blob comprimido
py -c "
import zlib, struct

with open('pruebaV1.exe', 'rb') as f:
    data = f.read()

# Buscar firma PYZ
idx = data.find(b'PYZ')
if idx >= 0:
    print(f'PYZ encontrado en offset: {idx}')
    # Los siguientes 4 bytes son el tamaño
    size = struct.unpack('<I', data[idx+3:idx+7])[0]
    print(f'Tamaño PYZ: {size}')
    
# Extraer string PyInstaller manual
idx2 = data.rfind(b'PyInstaller')
if idx2 >= 0:
    end = data.find(b'\x00', idx2)
    print(f'PyInstaller versión: {data[idx2:end].decode()}')
"
```

## Extraer desde PYZ

El archivo `PYZ-00.pyz` contiene las librerías de la stdlib y dependencias:

```python
import importlib
import sys

# Agregar el directorio extraído al path para poder importar
sys.path.insert(0, "pruebaV1.exe_extracted")

# pyinstxtractor ya extrajo los .pyc del PYZ automáticamente
# pero si no, se puede hacer manual:
import zipfile
with zipfile.ZipFile("PYZ-00.pyz", 'r') as z:
    z.extractall("pyz_extracted/")
```

## PyInstaller 5.x/6.x — Notas especiales

- Los onefile modernos usan **CArchive** con compresión zlib
- pyinstxtractor v2.0+ soporta PyInstaller 6.x
- Si falla pyinstxtractor, intenta con `archive_viewer.py` (viene con PyInstaller)
- Python 3.12+ cambió el magic number — asegúrate de tener Python correcto
- Los .pyc extraídos tienen estructura completa: magic (4) + flags (4) + src_size (4, opcional) + marshal code object
