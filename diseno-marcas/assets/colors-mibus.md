# Paleta de Colores MiBus — Guía Detallada

> Identidad visual extraída de mibus.com.pa (versión junio 2026)

## 🎨 Colores Primarios

### Primary Brand Blue
- **Hex:** `#283c90`
- **RGB:** `rgb(40, 60, 144)`
- **Uso:** Identidad de marca, títulos principales (H1, H2), links importantes, acentos de marca
- **Cuándo usarlo:** Títulos, branding, secciones de marca
- **Cuándo NO usarlo:** Texto de párrafo (muy oscuro para texto largo), fondos grandes (puede ser overwhelming)

### Primary Variants
- **Light** `#4F5FB5` — para hover, backgrounds sutiles, badges
- **Dark** `#1B2A66` — para pressed states, fondos oscuros, contraste fuerte

## 🔵 Colores Secundarios

### Secondary Blue
- **Hex:** `#205CA7`
- **RGBA:** `rgba(32, 92, 167, 1)`
- **Uso:** Botones primarios, CTAs, enlaces activos
- **Cuándo usarlo:** Botones "SUSCRIBIRSE", "Enviar", "Continuar", links
- **Hover:** `#409EFF`

### Secondary Hover
- **Hex:** `#409EFF`
- **RGBA:** `rgba(64, 158, 255, 1)`
- **Uso:** Estado hover de botones y links secundarios

## ✨ Color de Acento

### Accent (Twitter Blue)
- **Hex:** `#1DA1F2`
- **RGB:** `rgb(29, 161, 242)`
- **Uso:** Acentos, badges, secciones especiales, links destacados
- **Cuándo usarlo:** Llamadas a la acción secundarias, highlights, badges informativos

## ⚫ Colores Neutros

### Dark (Header/Footer)
- **Hex:** `#1A1A2E` (inferred)
- **Uso:** Fondos de header y footer, secciones oscuras
- **Variante común:** `#0F0F1E` (más oscuro si necesitas)

### Background
- **Hex:** `#FFFFFF`
- **Uso:** Fondo principal del contenido, contraste sobre azul oscuro

### Text Colors
- **Primary** `#333333` — Texto principal de párrafo
- **Secondary** `#666666` — Texto secundario, captions
- **Light** `#FFFFFF` — Texto sobre fondos oscuros
- **Muted** `#999999` — Texto deshabilitado, placeholders

### Border Colors
- **Default** `#E0E0E0` — Bordes sutiles
- **Subtle** `#F0F0F0` — Separadores muy sutiles

## 🚦 Colores de Estado

### Success
- **Hex:** `#B5D531` (también `#B5D331`)
- **Uso:** Éxito, confirmación, íconos positivos

### Error
- **Hex:** `#BC0C06`
- **Uso:** Errores, validaciones fallidas, alertas críticas

### Warning
- **Hex:** `#F39C12` (sugerido, no en sitio)
- **Uso:** Advertencias, validaciones

### Info
- **Hex:** `#1DA1F2` (= Accent)
- **Uso:** Información, tooltips

## 🌑 Colores de UI

| Token | Valor | Uso |
|---|---|---|
| Scroll-top icon | `#B5D531` | Ícono de scroll-to-top |
| Bullets inactivos | `rgba(125, 125, 125, 0.5)` | Bullets de slider inactivos |
| Bullets activos | `rgb(125, 125, 125)` | Bullets de slider activos |
| Overlay oscuro | `rgba(0, 0, 0, 0.5)` | Overlays de imágenes |
| Overlay más oscuro | `rgba(0, 0, 0, 0.75)` | Overlays fuertes |

## 📐 Reglas de aplicación

### Regla 60-30-10
- **60%** blanco (`#FFFFFF`)
- **30%** azul primary/secondary (`#283c90` / #205CA7)
- **10%** acento (`#1DA1F2`)

### Contraste mínimo (WCAG)
- Texto blanco sobre `#283c90`: ratio 8.6:1 ✓ AAA
- Texto blanco sobre `#205CA7`: ratio 5.1:1 ✓ AA
- Texto `#333333` sobre `#FFFFFF`: ratio 12.6:1 ✓ AAA
- Texto `#FFFFFF` sobre `#1DA1F2`: ratio 2.8:1 ✗ (no usar para texto, solo para fondos decorativos)

### Regla de uso
- ✅ Header/Footer → `#1A1A2E` (dark) o `#283c90` (primary)
- ✅ Botones principales → `#205CA7`
- ✅ Botones hover → `#409EFF`
- ✅ Títulos → `#283c90` o `#FFFFFF` (sobre dark)
- ✅ Texto de párrafo → `#333333` (sobre blanco) o `#FFFFFF` (sobre dark)
- ✅ Backgrounds sutiles → `#F0F0F0` o `#4F5FB5` con baja opacidad
- ❌ NUNCA uses rojo/verde/azul saturado fuera de la paleta
- ❌ NUNCA uses más de 3 azules diferentes en el mismo diseño

## 💡 Valores derivados (para ampliar la paleta)

Si necesitas un valor que no está, oscurece/aclara uno existente:

| Original | +10% light | +20% light | -10% dark | -20% dark |
|---|---|---|---|---|
| `#283c90` | `#4F5FB5` | `#7683CB` | `#1B2A66` | `#0E1733` |
| `#205CA7` | `#4A85D0` | `#73AEE8` | `#16407A` | `#0C244D` |
| `#1DA1F2` | `#4DB5F5` | `#7DC9F8` | `#1780C2` | `#0F5A8C` |
| `#1A1A2E` | `#474758` | `#747582` | `#000010` | `#000000` |
