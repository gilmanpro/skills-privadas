# Guía: Aplicar Diseño MiBus a Excel (.xlsx)

> Cómo crear hojas de cálculo con la identidad visual de MiBus: reportes, dashboards, plantillas, etc.

## 📋 Antes de empezar

1. Lee `assets/brand-mibus.json` y `assets/colors-mibus.md` de esta skill.
2. **Carga la skill `ofimatica`** del sistema opencode (seccion hojas de calculo — absorbio a la antigua `xlsx`) y sigue su flujo de trabajo.
3. Combina: identidad MiBus (esta skill) + buenas prácticas XLSX (skill `ofimatica`).

## 🎨 Paleta para XLSX

```python
MIBUS_COLORS_HEX = {
    "primary":      "283C90",
    "primary_dark": "1B2A66",
    "primary_light":"4F5FB5",
    "secondary":    "205CA7",
    "secondary_h":  "409EFF",
    "accent":       "1DA1F2",
    "dark":         "1A1A2E",
    "white":        "FFFFFF",
    "text":         "333333",
    "text_light":   "FFFFFF",
    "text_muted":   "666666",
    "border":       "E0E0E0",
    "border_subtle":"F0F0F0",
    "success":      "B5D531",
    "error":        "BC0C06",
    "warning":      "F39C12",
}
```

## 📐 Estructura recomendada

### Hoja 1: Portada / Dashboard
```
┌──────────────────────────────────────────┐
│  [Logo MiBus]    DASHBOARD DE MÉTRICAS   │ ← Header primary
│                  Mes: Junio 2026         │
├──────────────────────────────────────────┤
│                                          │
│  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐ │ ← KPI cards
│  │ 1436 │  │+4000 │  │  152 │  │ 450K │ │
│  │Unid. │  │ Trab │  │Rutas │  │Pasaj.│ │
│  └──────┘  └──────┘  └──────┘  └──────┘ │
│                                          │
│  [Gráfico de barras]                     │
│                                          │
│  [Tabla resumen]                         │
│                                          │
├──────────────────────────────────────────┤
│ MiBus · www.mibus.com.pa       #1/3     │ ← Footer
└──────────────────────────────────────────┘
```

### Hoja 2 en adelante: Datos
- Header primary con texto blanco
- Stripe pattern (gris/blanco) para filas
- Bordes sutiles `#E0E0E0`
- Fila de totales con background `#283C90` texto blanco

## 🔤 Tipografía para XLSX

| Elemento | Fuente | Tamaño |
|---|---|---|
| Título portada | Calibri Bold (Poppins si instalada) | 24pt |
| Subtítulo | Calibri Regular (Roboto) | 14pt |
| Header de columna | Calibri Bold (Poppins) | 11pt |
| Body | Calibri Regular (Roboto) | 10pt |
| Números | Calibri Regular (Roboto) | 10pt |
| Total row | Calibri Bold (Poppins) | 10pt |
| Footer | Calibri Regular | 8pt |

**Nota:** Excel no carga Google Fonts. Usa Calibri por defecto, o instala Poppins/Roboto en el sistema para usarlas en Excel.

## 🛠️ Implementación con openpyxl

### Setup básico

```python
from openpyxl import Workbook
from openpyxl.styles import (
    Font, PatternFill, Border, Side, Alignment, 
    NamedStyle, Color
)
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image
from openpyxl.formatting.rule import ColorScaleRule, DataBarRule

wb = Workbook()

# Colores MiBus
PRIMARY = "FF283C90"
PRIMARY_DARK = "FF1B2A66"
SECONDARY = "FF205CA7"
ACCENT = "FF1DA1F2"
DARK = "FF1A1A2E"
WHITE = "FFFFFFFF"
TEXT = "FF333333"
TEXT_LIGHT = "FFFFFFFF"
BORDER = "FFE0E0E0"
STRIPE = "FFF0F0F0"

# Fonts
FONT_HEADING = Font(name="Calibri", size=24, bold=True, color=PRIMARY)
FONT_SUBHEADING = Font(name="Calibri", size=14, bold=True, color=PRIMARY)
FONT_HEADER = Font(name="Calibri", size=11, bold=True, color=TEXT_LIGHT)
FONT_BODY = Font(name="Calibri", size=10, color=TEXT)
FONT_TOTAL = Font(name="Calibri", size=10, bold=True, color=TEXT_LIGHT)
```

### Named Styles (recomendado)

```python
def create_mibus_styles(wb):
    """Crea NamedStyles reutilizables con identidad MiBus."""
    
    # Header principal
    header_style = NamedStyle(name="mibus_header")
    header_style.font = Font(name="Calibri", size=11, bold=True, color=TEXT_LIGHT)
    header_style.fill = PatternFill(start_color=PRIMARY, end_color=PRIMARY, fill_type="solid")
    header_style.alignment = Alignment(horizontal="center", vertical="center")
    header_style.border = Border(
        bottom=Side(style="medium", color=PRIMARY_DARK)
    )
    wb.add_named_style(header_style)
    
    # Body
    body_style = NamedStyle(name="mibus_body")
    body_style.font = Font(name="Calibri", size=10, color=TEXT)
    body_style.alignment = Alignment(vertical="center")
    body_style.border = Border(
        bottom=Side(style="thin", color=BORDER)
    )
    wb.add_named_style(body_style)
    
    # Body stripe (fila alterna)
    stripe_style = NamedStyle(name="mibus_stripe")
    stripe_style.font = Font(name="Calibri", size=10, color=TEXT)
    stripe_style.alignment = Alignment(vertical="center")
    stripe_style.fill = PatternFill(start_color=STRIPE, end_color=STRIPE, fill_type="solid")
    stripe_style.border = Border(
        bottom=Side(style="thin", color=BORDER)
    )
    wb.add_named_style(stripe_style)
    
    # Total row
    total_style = NamedStyle(name="mibus_total")
    total_style.font = Font(name="Calibri", size=10, bold=True, color=TEXT_LIGHT)
    total_style.fill = PatternFill(start_color=PRIMARY, end_color=PRIMARY, fill_type="solid")
    total_style.alignment = Alignment(vertical="center")
    wb.add_named_style(total_style)
    
    # KPI Card
    kpi_label_style = NamedStyle(name="mibus_kpi_label")
    kpi_label_style.font = Font(name="Calibri", size=9, bold=True, color="FF666666")
    kpi_label_style.alignment = Alignment(horizontal="center", vertical="center")
    kpi_label_style.fill = PatternFill(start_color="FFF0F0F0", end_color="FFF0F0F0", fill_type="solid")
    wb.add_named_style(kpi_label_style)
    
    kpi_value_style = NamedStyle(name="mibus_kpi_value")
    kpi_value_style.font = Font(name="Calibri", size=24, bold=True, color=PRIMARY)
    kpi_value_style.alignment = Alignment(horizontal="center", vertical="center")
    kpi_value_style.fill = PatternFill(start_color="FFF0F0F0", end_color="FFF0F0F0", fill_type="solid")
    wb.add_named_style(kpi_value_style)
```

### Función para aplicar estilo MiBus a tabla

```python
def style_table(ws, start_row, start_col, end_row, end_col, has_header=True):
    """Aplica estilo MiBus a un rango de celdas."""
    
    # Header
    if has_header:
        for col in range(start_col, end_col + 1):
            cell = ws.cell(row=start_row, column=col)
            cell.style = "mibus_header"
            cell.fill = PatternFill(start_color=PRIMARY, end_color=PRIMARY, fill_type="solid")
            cell.font = Font(name="Calibri", size=11, bold=True, color=TEXT_LIGHT)
            cell.alignment = Alignment(horizontal="center", vertical="center")
            cell.border = Border(
                bottom=Side(style="medium", color=PRIMARY_DARK),
                top=Side(style="thin", color=BORDER),
                left=Side(style="thin", color=BORDER),
                right=Side(style="thin", color=BORDER)
            )
    
    # Body
    for row in range(start_row + (1 if has_header else 0), end_row + 1):
        for col in range(start_col, end_col + 1):
            cell = ws.cell(row=row, column=col)
            is_stripe = (row - start_row) % 2 == 0
            cell.font = Font(name="Calibri", size=10, color=TEXT)
            cell.alignment = Alignment(vertical="center")
            cell.border = Border(
                bottom=Side(style="thin", color=BORDER),
                left=Side(style="thin", color=BORDER),
                right=Side(style="thin", color=BORDER)
            )
            if is_stripe:
                cell.fill = PatternFill(start_color=STRIPE, end_color=STRIPE, fill_type="solid")
```

### Función para crear KPI cards

```python
def add_kpi_card(ws, row, col, value, label, width=4, height=4):
    """Crea una tarjeta KPI con valor grande y label abajo."""
    
    # Merge para label (parte superior)
    label_start = f"{get_column_letter(col)}{row}"
    label_end = f"{get_column_letter(col + width - 1)}{row}"
    ws.merge_cells(f"{label_start}:{label_end}")
    
    # Merge para value (parte inferior, más alto)
    value_start = f"{get_column_letter(col)}{row + 1}"
    value_end = f"{get_column_letter(col + width - 1)}{row + height - 1}"
    ws.merge_cells(f"{value_start}:{value_end}")
    
    # Label
    label_cell = ws[label_start]
    label_cell.value = label.upper()
    label_cell.style = "mibus_kpi_label"
    
    # Value
    value_cell = ws[value_start]
    value_cell.value = value
    value_cell.style = "mibus_kpi_value"
    
    # Borders
    for r in range(row, row + height):
        for c in range(col, col + width):
            cell = ws.cell(row=r, column=c)
            cell.border = Border(
                top=Side(style="medium", color=PRIMARY),
                bottom=Side(style="medium", color=PRIMARY),
                left=Side(style="thin", color=BORDER),
                right=Side(style="thin", color=BORDER)
            )
```

### Header con logo

```python
def add_mibus_header(ws, logo_path="ASSETS/logo.png", title="REPORTE MIBUS"):
    """Añade un header con logo y título en la hoja."""
    
    # Logo (esquina superior izquierda)
    if os.path.exists(logo_path):
        img = Image(logo_path)
        img.width = 120
        img.height = 60
        ws.add_image(img, "A1")
    
    # Título (a la derecha del logo)
    ws.merge_cells("C1:H2")
    title_cell = ws["C1"]
    title_cell.value = title
    title_cell.font = Font(name="Calibri", size=24, bold=True, color=PRIMARY)
    title_cell.alignment = Alignment(horizontal="left", vertical="center")
    
    # Subtítulo
    ws.merge_cells("C3:H3")
    sub_cell = ws["C3"]
    sub_cell.value = "MiBus · Transporte Masivo de Panamá"
    sub_cell.font = Font(name="Calibri", size=11, color=TEXT)
    sub_cell.alignment = Alignment(horizontal="left", vertical="center")
    
    # Línea divisora
    for col in range(1, 9):
        cell = ws.cell(row=4, column=col)
        cell.border = Border(
            bottom=Side(style="medium", color=PRIMARY)
        )
```

### Footer corporativo

```python
def add_mibus_footer(ws, row, total_cols=8):
    """Añade un footer corporativo al final de la hoja."""
    
    # Background
    for col in range(1, total_cols + 1):
        cell = ws.cell(row=row, column=col)
        cell.fill = PatternFill(start_color=DARK, end_color=DARK, fill_type="solid")
        cell.font = Font(name="Calibri", size=8, color=TEXT_LIGHT)
    
    # Texto
    cell = ws.cell(row=row, column=1)
    cell.value = "MiBus · Transporte Masivo de Panamá · www.mibus.com.pa"
    cell.alignment = Alignment(horizontal="left", vertical="center")
    
    # Página (a la derecha)
    if total_cols >= 2:
        cell = ws.cell(row=row, column=total_cols)
        cell.value = "Página 1 de 1"
        cell.alignment = Alignment(horizontal="right", vertical="center")
```

### Gráficos con colores MiBus

```python
from openpyxl.chart import BarChart, LineChart, PieChart, Reference
from openpyxl.chart.label import DataLabelList

def add_mibus_bar_chart(ws, data_range, title="Métricas"):
    """Crea un gráfico de barras con colores MiBus."""
    
    chart = BarChart()
    chart.type = "col"
    chart.style = 2
    chart.title = title
    chart.y_axis.title = "Cantidad"
    chart.x_axis.title = "Categoría"
    
    data = Reference(ws, min_col=data_range['min_col'], 
                     min_row=data_range['min_row'],
                     max_col=data_range['max_col'],
                     max_row=data_range['max_row'])
    chart.add_data(data, titles_from_data=True)
    
    # Colores MiBus
    from openpyxl.chart.shapes import GraphicalProperties
    from openpyxl.drawing.fill import PatternFillProperties, ColorChoice
    from openpyxl.drawing.colors import ColorChoice
    
    chart.varyColors = True
    
    # Set color series
    series = chart.series[0]
    series.graphicalProperties = GraphicalProperties(solidFill="283C90")
    
    ws.add_chart(chart, "A10")
```

## ✅ Checklist para XLSX MiBus

- [ ] Logo MiBus en hoja 1 (portada)
- [ ] Header primary con texto blanco en todas las tablas
- [ ] Stripe pattern (gris/blanco alternado) en filas
- [ ] Fila de totales con background primary
- [ ] Borders sutiles `#E0E0E0`
- [ ] Títulos primary `#283C90`
- [ ] Sin colores saturados fuera de paleta
- [ ] Footer con info MiBus
- [ ] Gráficos con colores MiBus (no default Excel)
- [ ] KPI cards si es dashboard

## 🚫 Errores comunes

- ❌ Header de tabla sin color (default blanco)
- ❌ Filas todas blancas sin stripe pattern
- ❌ Borders negros gruesos
- ❌ Múltiples colores de relleno (rojo, amarillo, verde)
- ❌ Gráficos con colores default de Excel
- ❌ Texto justificado o centrado forzado
- ❌ Números como texto (sin formato de número)
