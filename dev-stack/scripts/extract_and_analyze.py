#!/usr/bin/env python3
"""
extract_and_analyze.py — Herramienta combinada para deconstruir ejecutables PyInstaller

Uso:
    py extract_and_analyze.py <archivo.exe>
    py extract_and_analyze.py <archivo.exe> --output <carpeta_salida>

Requiere:
    - Python 3.10+
    - pyinstxtractor.py en el mismo directorio o en PATH
    - Solo stdlib (no requiere pip install)

Este script:
    1. Detecta si el .exe es PyInstaller
    2. Extrae los .pyc con pyinstxtractor
    3. Identifica el entry point
    4. Analiza el bytecode (constantes, names, varnames, funciones)
    5. Muestra el bytecode desensamblado
    6. Genera un reporte de análisis completo
"""

import os
import sys
import struct
import marshal
import dis
import subprocess
import re
import argparse

# ─── Colores para terminal ───
class C:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


def log(msg, color=''):
    """Imprime mensaje con color si la terminal lo soporta"""
    if color and sys.stdout.isatty():
        print(f"{color}{msg}{C.END}")
    else:
        print(msg)


def detectar_pyinstaller(ruta_exe):
    """Detecta si un .exe fue empaquetado con PyInstaller"""
    log(f"\n{C.HEADER}🔍 Detectando PyInstaller...{C.END}")
    
    with open(ruta_exe, 'rb') as f:
        data = f.read()
    
    # Buscar firma PyInstaller
    idx = data.rfind(b'PyInstaller')
    if idx >= 0:
        end = data.find(b'\x00', idx)
        version = data[idx:end].decode('utf-8', errors='replace')
        log(f"✅ ES PYINSTALLER (offset: {idx})", C.GREEN)
        log(f"   Versión: {version}", C.GREEN)
        return True, version
    else:
        log("❌ No se encontró firma PyInstaller", C.FAIL)
        return False, None


def extraer_con_pyinstxtractor(ruta_exe, output_dir):
    """Ejecuta pyinstxtractor para extraer los .pyc"""
    log(f"\n{C.HEADER}📦 Extrayendo con pyinstxtractor...{C.END}")
    
    # Buscar pyinstxtractor
    script_dir = os.path.dirname(os.path.abspath(__file__))
    posibles = [
        os.path.join(script_dir, 'pyinstxtractor.py'),
        os.path.join(os.getcwd(), 'pyinstxtractor.py'),
        'pyinstxtractor.py',
    ]
    
    pyinstxtractor_path = None
    for p in posibles:
        if os.path.exists(p):
            pyinstxtractor_path = p
            break
    
    if not pyinstxtractor_path:
        log("⚠️  pyinstxtractor.py no encontrado. Descargando...", C.WARNING)
        import urllib.request
        url = "https://raw.githubusercontent.com/extremecoders-re/pyinstxtractor/master/pyinstxtractor.py"
        try:
            urllib.request.urlretrieve(url, 'pyinstxtractor.py')
            pyinstxtractor_path = 'pyinstxtractor.py'
            log("✅ Descargado pyinstxtractor.py", C.GREEN)
        except Exception as e:
            log(f"❌ Error descargando pyinstxtractor: {e}", C.FAIL)
            log("   Descarga manual: https://raw.githubusercontent.com/extremecoders-re/pyinstxtractor/master/pyinstxtractor.py")
            return None
    
    # Ejecutar pyinstxtractor
    try:
        result = subprocess.run(
            [sys.executable, pyinstxtractor_path, ruta_exe],
            capture_output=True, text=True, timeout=60
        )
        log(result.stdout)
        if result.returncode != 0:
            log(f"❌ Error: {result.stderr}", C.FAIL)
            return None
        
        # pyinstxtractor crea una carpeta con el nombre del .exe + _extracted
        base = os.path.splitext(os.path.basename(ruta_exe))[0]
        extracted = os.path.join(os.path.dirname(ruta_exe), f"{base}_extracted")
        if not os.path.exists(extracted):
            # Buscar en el directorio actual
            extracted = os.path.join(os.getcwd(), f"{base}_extracted")
        
        if not os.path.exists(extracted):
            log(f"❌ No se encontró la carpeta extraída", C.FAIL)
            return None
        
        return extracted
    
    except subprocess.TimeoutExpired:
        log("❌ pyinstxtractor excedió el tiempo máximo", C.FAIL)
        return None
    except Exception as e:
        log(f"❌ Error ejecutando pyinstxtractor: {e}", C.FAIL)
        return None


def identificar_entry_point(extracted_dir, nombre_exe):
    """Identifica el entry point (.pyc principal)"""
    log(f"\n{C.HEADER}🎯 Identificando entry point...{C.END}")
    
    entry = os.path.join(extracted_dir, f"{nombre_exe}.pyc")
    if os.path.exists(entry):
        log(f"✅ Entry point encontrado: {entry}", C.GREEN)
        return entry
    
    # Buscar otros candidatos
    candidatos = ['__main__.pyc', 'main.pyc']
    for c in candidatos:
        path = os.path.join(extracted_dir, c)
        if os.path.exists(path):
            log(f"✅ Entry point candidato: {path}", C.GREEN)
            return path
    
    log("⚠️  No se encontró entry point claro", C.WARNING)
    return None


def leer_pyc(ruta_pyc):
    """Lee un .pyc y devuelve el objeto Code, magic, flags"""
    with open(ruta_pyc, 'rb') as f:
        magic = f.read(4)
        flags_data = f.read(4)
        flags = struct.unpack('<I', flags_data)[0]
        if flags & 1:
            f.read(4)  # source size
        code = marshal.load(f)
    return code, magic, flags


def magic_to_version(magic):
    """Convierte magic number a versión de Python legible"""
    magics = {
        b'\xCB\x0D\x0D\x0A': '3.12',
        b'\xAB\x0D\x0D\x0A': '3.11',
        b'\x6F\x0D\x0D\x0A': '3.10',
        b'\x61\x0D\x0D\x0A': '3.9',
        b'\x55\x0D\x0D\x0A': '3.8',
        b'\x42\x0D\x0D\x0A': '3.7',
    }
    return magics.get(magic[:4], f'desconocido ({magic[:4].hex()})')


def analizar_code(code_obj, nivel=0, nombre="<main>"):
    """Analiza recursivamente un objeto Code y devuelve un diccionario con la info"""
    info = {
        'nombre': nombre,
        'name': code_obj.co_name,
        'filename': code_obj.co_filename,
        'argcount': code_obj.co_argcount,
        'nlocals': code_obj.co_nlocals,
        'stacksize': code_obj.co_stacksize,
        'varnames': list(code_obj.co_varnames),
        'names': list(code_obj.co_names),
        'consts': [],
        'sub_funcs': [],
    }
    
    for i, c in enumerate(code_obj.co_consts):
        if hasattr(c, 'co_code'):  # Objeto Code anidado
            sub_info = analizar_code(c, nivel + 1, f"func_{i}({c.co_name})")
            info['sub_funcs'].append(sub_info)
            info['consts'].append({
                'idx': i,
                'type': 'code',
                'value': f"<code object {c.co_name}>",
                'sub': sub_info
            })
        else:
            tipo = type(c).__name__
            # Truncar strings largos
            valor = repr(c)
            if len(valor) > 150:
                valor = valor[:147] + '...'
            info['consts'].append({
                'idx': i,
                'type': tipo,
                'value': valor,
            })
    
    return info


def imprimir_analisis(info, nivel=0):
    """Imprime el análisis formateado"""
    prefix = "  " * nivel
    
    print(f"\n{prefix}{'─' * 50}")
    print(f"{prefix}{C.BOLD}FUNCIÓN: {info['nombre']}{C.END}")
    print(f"{prefix}  name: {info['name']}")
    print(f"{prefix}  filename: {info['filename']}")
    print(f"{prefix}  args: {info['argcount']}, locals: {info['nlocals']}, stack: {info['stacksize']}")
    
    if info['varnames']:
        print(f"{prefix}  ── varnames ({len(info['varnames'])}) ──")
        for i, v in enumerate(info['varnames']):
            print(f"{prefix}    [{i}] {v}")
    
    if info['names']:
        print(f"{prefix}  ── names ({len(info['names'])}) ──")
        for i, n in enumerate(info['names']):
            print(f"{prefix}    [{i}] {C.CYAN}{n}{C.END}")
    
    print(f"{prefix}  ── consts ({len(info['consts'])}) ──")
    for c in info['consts']:
        if c['type'] == 'code':
            print(f"{prefix}    [{c['idx']}] {C.WARNING}<code object>{C.END}")
            imprimir_analisis(c['sub'], nivel + 2)
        elif c['type'] in ('str',):
            print(f"{prefix}    [{c['idx']}] {C.GREEN}{c['type']}{C.END}: {c['value']}")
        elif c['type'] in ('int', 'float'):
            print(f"{prefix}    [{c['idx']}] {C.BLUE}{c['type']}{C.END}: {c['value']}")
        elif c['type'] == 'tuple':
            print(f"{prefix}    [{c['idx']}] {C.BLUE}{c['type']}{C.END}: {c['value']}")
        else:
            print(f"{prefix}    [{c['idx']}] {c['type']}: {c['value']}")
    
    for sub in info['sub_funcs']:
        imprimir_analisis(sub, nivel + 1)


def generar_reporte(info, ruta_pyc, magic, nombre_exe):
    """Genera un reporte de texto con el análisis completo"""
    lines = []
    lines.append("=" * 60)
    lines.append(f"  REPORTE DE ANÁLISIS — {nombre_exe}")
    lines.append("=" * 60)
    lines.append(f"")
    lines.append(f"Archivo: {ruta_pyc}")
    lines.append(f"Python:  {magic_to_version(magic)}")
    lines.append(f"")
    
    def agregar_info(info, nivel=0):
        prefix = "  " * nivel
        lines.append(f"{prefix}FUNCIÓN: {info['nombre']}")
        lines.append(f"{prefix}  name: {info['name']}")
        lines.append(f"{prefix}  args: {info['argcount']}, locals: {info['nlocals']}")
        
        if info['names']:
            lines.append(f"{prefix}  NAMES ({len(info['names'])}):")
            for i, n in enumerate(info['names']):
                lines.append(f"{prefix}    [{i}] {n}")
        
        if info['varnames']:
            lines.append(f"{prefix}  VARNAMES ({len(info['varnames'])}):")
            for i, v in enumerate(info['varnames']):
                lines.append(f"{prefix}    [{i}] {v}")
        
        lines.append(f"{prefix}  CONSTS ({len(info['consts'])}):")
        for c in info['consts']:
            if c['type'] == 'code':
                lines.append(f"{prefix}    [{c['idx']}] <code object>")
                agregar_info(c['sub'], nivel + 2)
            else:
                lines.append(f"{prefix}    [{c['idx']}] {c['type']}: {c['value']}")
        
        for sub in info['sub_funcs']:
            agregar_info(sub, nivel + 1)
    
    agregar_info(info)
    
    # Agregar bytecode
    lines.append(f"\n{'─' * 60}")
    lines.append(f"  BYTECODE COMPLETO")
    lines.append(f"{'─' * 60}")
    
    # Capturar output de dis
    import io
    code, _, _ = leer_pyc(ruta_pyc) if ruta_pyc else (None, None, None)
    if code:
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        dis.dis(code)
        bytecode_output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        lines.append(bytecode_output)
    
    return '\n'.join(lines)


def guardar_reporte(reporte, output_dir, nombre_exe):
    """Guarda el reporte en un archivo"""
    ruta = os.path.join(output_dir, f"{nombre_exe}_analisis.txt")
    with open(ruta, 'w', encoding='utf-8') as f:
        f.write(reporte)
    log(f"📄 Reporte guardado: {ruta}", C.GREEN)
    return ruta


def main():
    parser = argparse.ArgumentParser(
        description="Extrae y analiza el bytecode de ejecutables PyInstaller",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  py extract_and_analyze.py pruebaV1.exe
  py extract_and_analyze.py pruebaV1.exe --output mi_analisis
        """
    )
    parser.add_argument('exe_path', help="Ruta al ejecutable .exe")
    parser.add_argument('--output', '-o', help="Directorio de salida (defecto: carpeta del .exe)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.exe_path):
        log(f"❌ Archivo no encontrado: {args.exe_path}", C.FAIL)
        sys.exit(1)
    
    ruta_exe = os.path.abspath(args.exe_path)
    nombre_exe = os.path.splitext(os.path.basename(ruta_exe))[0]
    output_base = args.output or os.path.dirname(ruta_exe)
    
    log(f"{C.BOLD}{'='*60}{C.END}", C.BOLD)
    log(f"{C.BOLD}  DECONSTRUCCIÓN PYINSTALLER — {nombre_exe}{C.END}", C.BOLD)
    log(f"{C.BOLD}{'='*60}{C.END}", C.BOLD)
    
    # Paso 1: Detectar PyInstaller
    es_pyinstaller, version = detectar_pyinstaller(ruta_exe)
    if not es_pyinstaller:
        log("El archivo no parece ser un ejecutable PyInstaller.", C.FAIL)
        log("¿Seguro que fue empaquetado con PyInstaller?", C.WARNING)
        sys.exit(1)
    
    # Paso 2: Extraer .pyc
    extracted_dir = extraer_con_pyinstxtractor(ruta_exe, output_base)
    if not extracted_dir:
        log("❌ No se pudo extraer el contenido del .exe", C.FAIL)
        sys.exit(1)
    
    log(f"📁 Archivos extraídos en: {extracted_dir}", C.CYAN)
    
    # Paso 3: Identificar entry point
    entry_pyc = identificar_entry_point(extracted_dir, nombre_exe)
    if not entry_pyc:
        log("❌ No se pudo identificar el entry point", C.FAIL)
        log("   Revisa manualmente los archivos en:", extracted_dir)
        sys.exit(1)
    
    # Paso 4: Leer y analizar bytecode
    log(f"\n{C.HEADER}🔬 Analizando bytecode...{C.END}")
    
    code, magic, flags = leer_pyc(entry_pyc)
    
    log(f"   Magic: {magic.hex()} → Python {magic_to_version(magic)}", C.CYAN)
    log(f"   Flags: {flags} {'(source size present)' if flags & 1 else ''}", C.CYAN)
    
    info = analizar_code(code)
    imprimir_analisis(info)
    
    # Mostrar bytecode desensamblado
    log(f"\n{C.HEADER}📋 Bytecode completo:{C.END}")
    dis.dis(code)
    
    # Generar reporte
    reporte = generar_reporte(info, entry_pyc, magic, nombre_exe)
    ruta_reporte = guardar_reporte(reporte, output_base, nombre_exe)
    
    # Resumen
    log(f"\n{C.BOLD}{'='*60}{C.END}", C.BOLD)
    log(f"{C.BOLD}✅ ANÁLISIS COMPLETADO{C.END}", C.GREEN)
    log(f"{C.BOLD}{'='*60}{C.END}", C.BOLD)
    print(f"\n📁 Archivos extraídos: {extracted_dir}")
    print(f"📄 Reporte: {ruta_reporte}")
    print(f"🎯 Entry point: {entry_pyc}")
    print(f"\n➡️  Próximos pasos:")
    print(f"   1. Revisa el reporte de análisis")
    print(f"   2. Identifica las constantes y names ambiguos")
    print(f"   3. Pregunta al usuario sobre el comportamiento observado")
    print(f"   4. Reconstruye el código basado en el análisis + feedback")


if __name__ == '__main__':
    main()
