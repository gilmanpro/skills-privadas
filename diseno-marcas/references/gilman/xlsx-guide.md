# Aplicación a Excel (.xlsx) — gilman.pro

Cómo aplicar el branding gilman.pro a hojas de cálculo Excel usando `openpyxl`.

## 1. CONFIGURACIÓN INICIAL

```python
from openpyxl import Workbook
from openpyxl.styles import (
    Font, PatternFill, Alignment, Border, Side, NamedStyle
)
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import ColorScaleRule, DataBarRule
from openpyxl.chart import BarChart, LineChart, PieChart, Reference
from openpyxl.chart.label import DataLabelList

# ===== PALETA GILMAN (HEX sin # para openpyxl) =====
PRIMARY       = "10B981"  # Emerald 500 - primary
PRIMARY_600   = "059669"  # Emerald 600
PRIMARY_700   = "047857"  # Emerald 700
SECONDARY     = "2563EB"  # Blue 600
ACCENT_CYAN   = "22D3EE"  # Cyan 400
ACCENT_CYAN_500 = "06B6D4"  # Cyan 500
NAVBAR       = "1E293B"  # Slate 800
SLATE_700    = "334155"
SLATE_50     = "F8FAFC"
WHITE        = "FFFFFF"
GRAY_900     = "111827"
GRAY_500     = "6B7280"
GRAY_400     = "9CA3AF"
GRAY_200     = "E5E7EB"
GRAY_100     = "F3F4F6"

# DARK MODE
INDIGO_500   = "6366F1"
INDIGO_600   = "4F46E5"
VIOLET_500   = "8B5CF6"
SLATE_900    = "0F172A"
SLATE_800    = "1E293B"
SLATE_400    = "94A3B8"

# ===== TIPOGRAFÍA =====
FONT_HEADING = "Montserrat"
FONT_BODY    = "Lato"
FONT_DISPLAY = "Orbitron"
FONT_TECH    = "Rajdhani"
```

## 2. ESTILOS BASE (NAMED STYLES)

```python
def setup_styles(wb):
    """Crea named styles globales del libro."""
    
    # === HEADINGS ===
    
    h1 = NamedStyle(name="gilman_h1")
    h1.font = Font(name=FONT_HEADING, size=24, bold=True, color=PRIMARY_700)
    h1.alignment = Alignment(horizontal="left", vertical="center")
    wb.add_named_style(h1)
    
    h2 = NamedStyle(name="gilman_h2")
    h2.font = Font(name=FONT_HEADING, size=16, bold=True, color=GRAY_900)
    h2.alignment = Alignment(horizontal="left", vertical="center")
    wb.add_named_style(h2)
    
    h3 = NamedStyle(name="gilman_h3")
    h3.font = Font(name=FONT_HEADING, size=12, bold=True, color=PRIMARY_600)
    h3.alignment = Alignment(horizontal="left", vertical="center")
    wb.add_named_style(h3)
    
    # === HEADER DE TABLA ===
    
    th = NamedStyle(name="gilman_th")
    th.font = Font(name=FONT_BODY, size=11, bold=True, color=WHITE)
    th.fill = PatternFill("solid", fgColor=PRIMARY_600)
    th.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    th.border = Border(
        left=Side(style="thin", color=PRIMARY_700),
        right=Side(style="thin", color=PRIMARY_700),
        top=Side(style="thin", color=PRIMARY_700),
        bottom=Side(style="thin", color=PRIMARY_700),
    )
    wb.add_named_style(th)
    
    # === CELDAS DE DATOS (zebra) ===
    
    cell_odd = NamedStyle(name="gilman_cell_odd")
    cell_odd.font = Font(name=FONT_BODY, size=10, color=GRAY_900)
    cell_odd.fill = PatternFill("solid", fgColor=WHITE)
    cell_odd.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    cell_odd.border = Border(
        left=Side(style="thin", color=GRAY_200),
        right=Side(style="thin", color=GRAY_200),
        top=Side(style="thin", color=GRAY_200),
        bottom=Side(style="thin", color=GRAY_200),
    )
    wb.add_named_style(cell_odd)
    
    cell_even = NamedStyle(name="gilman_cell_even")
    cell_even.font = Font(name=FONT_BODY, size=10, color=GRAY_900)
    cell_even.fill = PatternFill("solid", fgColor=SLATE_50)
    cell_even.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    cell_even.border = Border(
        left=Side(style="thin", color=GRAY_200),
        right=Side(style="thin", color=GRAY_200),
        top=Side(style="thin", color=GRAY_200),
        bottom=Side(style="thin", color=GRAY_200),
    )
    wb.add_named_style(cell_even)
    
    # === NÚMERO Y MONEDA ===
    
    num = NamedStyle(name="gilman_num")
    num.font = Font(name=FONT_TECH, size=10, color=GRAY_900)
    num.alignment = Alignment(horizontal="right", vertical="center")
    num.number_format = "#,##0"
    wb.add_named_style(num)
    
    money = NamedStyle(name="gilman_money")
    money.font = Font(name=FONT_TECH, size=10, color=PRIMARY_700, bold=True)
    money.alignment = Alignment(horizontal="right", vertical="center")
    money.number_format = '"$"#,##0.00'
    wb.add_named_style(money)
    
    # === ACENTOS / BADGES ===
    
    badge_emerald = NamedStyle(name="gilman_badge_emerald")
    badge_emerald.font = Font(name=FONT_BODY, size=9, bold=True, color=PRIMARY_700)
    badge_emerald.fill = PatternFill("solid", fgColor="D1FAE5")  # emerald-100
    badge_emerald.alignment = Alignment(horizontal="center", vertical="center")
    wb.add_named_style(badge_emerald)
    
    badge_cyan = NamedStyle(name="gilman_badge_cyan")
    badge_cyan.font = Font(name=FONT_BODY, size=9, bold=True, color="0E7490")
    badge_cyan.fill = PatternFill("solid", fgColor="CFFAFE")  # cyan-100
    badge_cyan.alignment = Alignment(horizontal="center", vertical="center")
    wb.add_named_style(badge_cyan)
```

## 3. PORTADA / HOJA DE PRESENTACIÓN

```python
def add_cover_sheet(wb, title, subtitle, contact=""):
    """Hoja 0 con branding gilman: fondo emerald, logo, título, contacto."""
    ws = wb.active
    ws.title = "Portada"
    
    # Fondo
    ws.sheet_properties.tabColor = PRIMARY
    
    # Filas de altura
    ws.row_dimensions[1].height = 8
    for r in range(2, 7):
        ws.row_dimensions[r].height = 30
    ws.row_dimensions[8].height = 50  # título
    ws.row_dimensions[9].height = 30
    ws.row_dimensions[10].height = 25
    ws.row_dimensions[12].height = 25
    
    # Columnas
    for c in range(1, 9):
        ws.column_dimensions[get_column_letter(c)].width = 12
    
    # Fondo emerald en rango
    for row in range(2, 13):
        for col in range(1, 9):
            cell = ws.cell(row=row, column=col)
            cell.fill = PatternFill("solid", fgColor=PRIMARY)
    
    # Logo (si está en assets)
    from pathlib import Path
    logo = Path(__file__).parent / "assets" / "logo_gilmanpro.png"
    if logo.exists():
        # Convertir SVG a PNG primero si es necesario (usar cairosvg o similar)
        ws.add_image(str(logo), "B3")
    
    # Título
    ws.merge_cells("B8:G8")
    title_cell = ws["B8"]
    title_cell.value = title
    title_cell.font = Font(name=FONT_HEADING, size=32, bold=True, color=WHITE)
    title_cell.alignment = Alignment(horizontal="center", vertical="center")
    
    # Subtítulo
    ws.merge_cells("B9:G9")
    sub_cell = ws["B9"]
    sub_cell.value = subtitle
    sub_cell.font = Font(name=FONT_BODY, size=14, color=WHITE)
    sub_cell.alignment = Alignment(horizontal="center", vertical="center")
    
    # Contacto
    if contact:
        ws.merge_cells("B12:G12")
        c_cell = ws["B12"]
        c_cell.value = contact
        c_cell.font = Font(name=FONT_TECH, size=11, color=ACCENT_CYAN)
        c_cell.alignment = Alignment(horizontal="center", vertical="center")
```

## 4. FUNCIÓN GENÉRICA PARA TABLAS CON BRANDING

```python
def add_branded_table(ws, start_row, start_col, headers, rows, title=None):
    """
    Inserta una tabla con header emerald, body zebra, totales destacados.
    
    ws: worksheet
    start_row, start_col: celda inicial
    headers: lista de strings
    rows: lista de listas
    title: H2 opcional arriba
    """
    
    # Título H2
    if title:
        ws.cell(row=start_row, column=start_col).value = title
        ws.cell(row=start_row, column=start_col).style = "gilman_h2"
        start_row += 2  # espacio
    
    # Headers
    for j, h in enumerate(headers):
        c = ws.cell(row=start_row, column=start_col + j)
        c.value = h
        c.style = "gilman_th"
    header_row = start_row
    ws.row_dimensions[start_row].height = 32
    
    # Body zebra
    for i, row in enumerate(rows):
        r = start_row + 1 + i
        for j, val in enumerate(row):
            c = ws.cell(row=r, column=start_col + j)
            c.value = val
            c.style = "gilman_cell_odd" if i % 2 == 0 else "gilman_cell_even"
        ws.row_dimensions[r].height = 22
    
    # Auto-width básico
    for j in range(len(headers)):
        col = get_column_letter(start_col + j)
        max_len = max(
            len(str(headers[j])),
            *(len(str(r[j])) for r in rows) if rows else [0]
        )
        ws.column_dimensions[col].width = min(max(max_len + 2, 10), 40)
    
    return start_row + 1 + len(rows)
```

## 5. GRÁFICOS CON PALETA GILMAN

```python
def make_bar_chart(ws, title, data_range, cat_range, anchor_cell):
    """Crea un gráfico de barras con paleta gilman."""
    chart = BarChart()
    chart.type = "col"
    chart.style = 11  # base
    chart.title = title
    chart.y_axis.title = None
    chart.x_axis.title = None
    chart.height = 10
    chart.width = 20
    
    data = Reference(ws, min_col=data_range[0], min_row=data_range[1],
                     max_col=data_range[2], max_row=data_range[3])
    cats = Reference(ws, min_col=cat_range[0], min_row=cat_range[1],
                     max_col=cat_range[2], max_row=cat_range[3])
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)
    
    # Aplicar color emerald a la primera serie
    from openpyxl.chart.shapes import GraphicalProperties
    from openpyxl.drawing.fill import ColorChoice
    if chart.series:
        chart.series[0].graphicalProperties = GraphicalProperties(solidFill=PRIMARY)
    
    chart.legend = None
    chart.dataLabels = DataLabelList(showVal=True)
    
    ws.add_chart(chart, anchor_cell)


def make_line_chart(ws, title, data_range, cat_range, anchor_cell):
    """Gráfico de líneas con gradiente emerald → cyan."""
    chart = LineChart()
    chart.title = title
    chart.style = 12
    chart.height = 10
    chart.width = 20
    
    data = Reference(ws, min_col=data_range[0], min_row=data_range[1],
                     max_col=data_range[2], max_row=data_range[3])
    cats = Reference(ws, min_col=cat_range[0], min_row=cat_range[1],
                     max_col=cat_range[2], max_row=cat_range[3])
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)
    
    if chart.series:
        from openpyxl.chart.shapes import GraphicalProperties
        from openpyxl.drawing.line import LineProperties
        chart.series[0].graphicalProperties = GraphicalProperties(
            line=LineProperties(solidFill=PRIMARY, w=28575)  # 2.25pt
        )
    
    ws.add_chart(chart, anchor_cell)
```

## 6. FORMATO CONDICIONAL GILMAN

```python
def apply_emerald_scale(ws, range_str):
    """Escala de color emerald para valores numéricos."""
    rule = ColorScaleRule(
        start_type='min', start_color='F0FDF4',  # emerald-50
        mid_type='percentile', mid_value=50, mid_color='6EE7B7',  # emerald-300
        end_type='max', end_color=PRIMARY_700
    )
    ws.conditional_formatting.add(range_str, rule)


def apply_data_bar(ws, range_str):
    """Barra de datos emerald."""
    rule = DataBarRule(
        start_type='min',
        end_type='max',
        color=PRIMARY,
        showValue=True
    )
    ws.conditional_formatting.add(range_str, rule)
```

## 7. SEPARADOR DECORATIVO EN EXCEL

Excel no tiene equivalente exacto al separador signature, pero podemos simularlo con una fila de bordes:

```python
def add_signature_separator(ws, row, start_col, end_col, use_dark=False):
    """Fila con bordes y celdas de color para simular el separador signature."""
    color1 = PRIMARY if not use_dark else INDIGO_500
    color2 = VIOLET_500 if use_dark else PRIMARY
    
    # Línea corta | punto | línea larga | punto (violet) | línea corta
    # 1: línea (3 cols)
    for c in range(start_col, start_col + 3):
        cell = ws.cell(row=row, column=c)
        cell.fill = PatternFill("solid", fgColor=color1)
    # 2: gap
    # 3: punto (1 col)
    cell = ws.cell(row=row, column=start_col + 4)
    cell.fill = PatternFill("solid", fgColor=color1)
    # 4: gap
    # 5: línea larga (4 cols)
    for c in range(start_col + 6, start_col + 10):
        cell = ws.cell(row=row, column=c)
        cell.fill = PatternFill("solid", fgColor=color1)
    # 6: gap
    # 7: punto violet (1 col)
    cell = ws.cell(row=row, column=start_col + 12)
    cell.fill = PatternFill("solid", fgColor=color2)
    # 8: gap
    # 9: línea corta (3 cols)
    for c in range(start_col + 14, start_col + 17):
        cell = ws.cell(row=row, column=c)
        cell.fill = PatternFill("solid", fgColor=color2)
    
    ws.row_dimensions[row].height = 4
```

## 8. USO COMPLETO

```python
from openpyxl import Workbook

wb = Workbook()
setup_styles(wb)

# Portada
add_cover_sheet(wb, "Reporte Mensual", "Gilberto Castillo — Ing. Telecomunicaciones | Big Data y Data Science | Desarrollador de Soluciones", "contacto@gilman.pro")

# Hoja de datos
ws = wb.create_sheet("Ventas")
ws.sheet_properties.tabColor = PRIMARY

add_branded_table(
    ws, 2, 1,
    headers=["Mes", "Unidades", "Ingresos (USD)", "Margen (%)"],
    rows=[
        ["Enero", 150, 12500, 32.5],
        ["Febrero", 180, 15000, 35.0],
        ["Marzo", 210, 18000, 38.2],
    ],
    title="Ventas Q1 2026"
)

# Formato condicional en columna de margen
apply_emerald_scale(ws, "D4:D6")

# Gráfico
make_bar_chart(
    ws, "Ingresos Mensuales",
    data_range=(3, 1, 3, 6),  # ingresos (col 3) filas 1-6
    cat_range=(1, 4, 1, 6),   # categorías (col 1) filas 4-6
    anchor_cell="F2"
)

wb.save("reporte-gilmanpro.xlsx")
```

## 9. REGLAS

1. **Tipografía:** Montserrat, Lato, Rajdhani. Si no están, usar Calibri.
2. **Header de tabla:** siempre emerald-600 fill + texto blanco bold.
3. **Body zebra:** alternar `WHITE` y `SLATE_50` (NO usar emerald-50 para zebra, sería demasiado saturado).
4. **Números:** Rajdhani (look condensado) + alineados a la derecha.
5. **Moneda:** emerald-700 bold (color de marca, denota dinero positivo).
6. **Charts:** color principal = `PRIMARY` (emerald). NO usar todos los colores del arcoíris.
7. **Bordes:** siempre `GRAY_200` (1px), nunca negro.
8. **Tab color:** emerald para hojas principales, slate para secundarias.
9. **Alineación:** texto a la izquierda, números a la derecha, headers centrados.
10. **Ancho de columna:** `max(len + 2, 10)` mínimo, máximo 40.
11. **NO** usar `wrap_text` en celdas numéricas (sí en headers y descripciones).

## 10. ERRORES COMUNES

- ❌ Olvidar `wb.add_named_style(style)` → style no se aplica
- ❌ Usar `Font(color="10B981")` con `#` → falla, usar sin `#`
- ❌ Aplicar `fill` sin `"solid"` como primer argumento
- ❌ Usar `patternType="darkDown"` etc. — no se ven en Excel
- ❌ Asignar chart a `ws` sin `add_chart(chart, "A1")` — desaparece
- ❌ `Reference` con `min_col`/`max_col` en orden inverso → gráfico vacío
