# Aplicación del diseño Electrocontrol a SVG (logos, iconos, gráficos vectoriales)

Guía para crear SVGs con el sistema de diseño de IoT Tech / Electrocontrol. **Esta skill COMPLEMENTA a `svg-logo-designer`**. Usa ambas juntas.

---

## Cuándo usar esta guía

| Tarea | Cargar también |
|---|---|
| Recrear el logo de Electrocontrol en SVG | `svg-logo-designer` |
| Icono custom con estilo de marca | `svg-logo-designer` + esta guía |
| Infografía vectorial para slides/imprimir | Esta guía |
| Gráfico vectorial para web | Esta guía |
| Favicon SVG | Esta guía |
| Logo en SVG para usar en PDFs/impresión | Esta guía |
| Iconos técnicos (sensores, PLC, ECU) | `svg-logo-designer` + esta guía |

---

## Paleta de colores para SVG (mismos HEX de la marca)

| Color | HEX | Nombre Tailwind | Uso en SVG |
|---|---|---|---|
| Cyan principal | `#06B6D4` | cyan-500 | `fill="#06B6D4"` |
| Cyan brillante | `#22D3EE` | cyan-400 | Para texto destacado |
| Purple | `#A855F7` | purple-500 | Acentos secundarios |
| Purple brillante | `#C084FC` | purple-400 | Para texto destacado |
| Pink | `#EC4899` | pink-500 | Highlights |
| Pink brillante | `#F472B6` | pink-400 | Para texto destacado |
| Slate 900 | `#0F172A` | slate-900 | Fondo dark principal |
| Slate 800 | `#1E293B` | slate-800 | Fondo alterno |
| Slate 700 | `#334155` | slate-700 | Bordes, separadores |
| Slate 300 | `#CBD5E1` | slate-300 | Texto body |
| Slate 400 | `#94A3B8` | slate-400 | Texto secundario |
| Blanco | `#FFFFFF` | — | Texto destacado |
| Verde WhatsApp | `#10B981` | green-500 | Botón WhatsApp, confirmaciones |
| Verde brillante | `#22C55E` | green-500 | Servicio Automatización |
| Naranja | `#F97316` | orange-500 | Servicio ECU |
| Rojo | `#EF4444` | red-500 | Servicio ECU, errores |
| Amarillo | `#FDE047` | yellow-400 | Awards, experiencia |

**Definir siempre al inicio del SVG como gradientes reutilizables** (no repetir HEX en cada elemento):

```xml
<defs>
  <linearGradient id="grad-cyan-purple" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#06B6D4"/>
    <stop offset="100%" stop-color="#A855F7"/>
  </linearGradient>

  <linearGradient id="grad-cyan-purple-pink" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#22D3EE"/>
    <stop offset="50%" stop-color="#C084FC"/>
    <stop offset="100%" stop-color="#F472B6"/>
  </linearGradient>

  <linearGradient id="grad-body" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#0F172A"/>
    <stop offset="50%" stop-color="#1E293B"/>
    <stop offset="100%" stop-color="#0F172A"/>
  </linearGradient>

  <linearGradient id="grad-iot" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#06B6D4"/>
    <stop offset="100%" stop-color="#3B82F6"/>
  </linearGradient>

  <linearGradient id="grad-ecu" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#F97316"/>
    <stop offset="100%" stop-color="#EF4444"/>
  </linearGradient>

  <linearGradient id="grad-auto" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#22C55E"/>
    <stop offset="100%" stop-color="#10B981"/>
  </linearGradient>

  <linearGradient id="grad-code" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#A855F7"/>
    <stop offset="100%" stop-color="#EC4899"/>
  </linearGradient>
</defs>
```

---

## Tipografía en SVG

### Familias recomendadas

| Familia | Cuándo usarla | Dónde |
|---|---|---|
| **Inter** | Default para todo el texto | Google Fonts, o instalada en sistema |
| **Sora** | Headlines más futuristas | Google Fonts |
| **Bebas Neue** | Para replicar el texto "ELECTROCONTROL" del logo | Google Fonts |
| **Manrope** | Alternativa más cálida | Google Fonts |
| **Sistema** | Fallback universal | `system-ui, sans-serif` |

### Aplicar tipografía

```xml
<text x="100" y="100" font-family="Inter, system-ui, sans-serif" font-size="32" font-weight="700" fill="#FFFFFF">
  Hola Mundo
</text>
```

### Texto con degradado (signature)

```xml
<defs>
  <linearGradient id="text-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#22D3EE"/>
    <stop offset="50%" stop-color="#C084FC"/>
    <stop offset="100%" stop-color="#F472B6"/>
  </linearGradient>
</defs>

<text x="100" y="100" font-family="Inter, sans-serif" font-size="48" font-weight="700" fill="url(#text-gradient)">
  ELECTROCONTROL
</text>
```

**Importante:** el `fill="url(#gradient)"` en `<text>` requiere que el navegador/SVG renderer soporte gradient en texto. Funciona en todos los navegadores modernos y en Figma/Illustrator. Para máxima compatibilidad, conviértelo a paths.

### Convertir texto a paths (vectorial puro)

```bash
# Opción 1: con Inkscape CLI
inkscape input.svg --export-text-to-path --export-plain-svg -o output.svg

# Opción 2: con svgo + plugin
npx svgo --pretty input.svg

# Opción 3: con Python (fontTools)
python -c "
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
font = TTFont('Inter-Bold.ttf')
glyph = font['glyf']['A']
pen = SVGPathPen(font.getGlyphSet())
font.getGlyphSet()['A'].draw(pen)
print(pen.getCommands())
"
```

---

## Recrear el logo ELECTROCONTROL en SVG

Prompt sugerido para `svg-logo-designer`:

```
Crea el logo de ELECTROCONTROL:

Símbolo:
- Letra "e" minúscula estilizada, color naranja/rojo (#FF5722 o #FF4500)
- Ancho del trazo: grueso
- La letra tiene efecto "pixelado" o "glitch" en la parte izquierda: 
  salen pequeños cuadrados de varios tamaños desde la "e" hacia la 
  izquierda, como si se estuviera descomponiendo o "rompiendo" en píxeles
- Los cuadrados del efecto pixelado deben respetar una grilla (ej. 5-8 
  cuadrados formando un patrón que se desvanece hacia la izquierda)
- Estilo: geométrico, industrial, futurista

Texto:
- "ELECTROCONTROL" debajo del símbolo
- Tipografía sans-serif bold/extra-bold
- MAYÚSCULAS
- Color: el mismo naranja/rojo (#FF5722 o #FF4500)
- Tracking amplio (letter-spacing: +0.05em o +0.1em)

Fondo:
- Cuadrado, color azul oscuro navy (#0A1A2E o #0F172A)
- Tamaño: 800x800 px (puedes hacer viewBox="0 0 800 800")

Estilo general:
- Tecnológico, industrial, profesional
- De aspecto "circuit board" o "tech company"
- Nada de emojis, nada de texto fuera del logo

Exporta como SVG y también como PNG 800x800.
```

---

## SVG del logo (plantilla base)

```xml
<svg width="800" height="800" viewBox="0 0 800 800" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="e-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF6B35"/>
      <stop offset="100%" stop-color="#FF4500"/>
    </linearGradient>
  </defs>

  <!-- Fondo navy -->
  <rect width="800" height="800" fill="#0A1A2E"/>

  <!-- Grid sutil de fondo (opcional) -->
  <g opacity="0.05" stroke="#FFFFFF" stroke-width="0.5">
    <line x1="0" y1="100" x2="800" y2="100"/>
    <line x1="0" y1="200" x2="800" y2="200"/>
    <line x1="0" y1="300" x2="800" y2="300"/>
    <line x1="0" y1="400" x2="800" y2="400"/>
    <line x1="0" y1="500" x2="800" y2="500"/>
    <line x1="0" y1="600" x2="800" y2="600"/>
    <line x1="0" y1="700" x2="800" y2="700"/>
    <line x1="100" y1="0" x2="100" y2="800"/>
    <line x1="200" y1="0" x2="200" y2="800"/>
    <line x1="300" y1="0" x2="300" y2="800"/>
    <line x1="400" y1="0" x2="400" y2="800"/>
    <line x1="500" y1="0" x2="500" y2="800"/>
    <line x1="600" y1="0" x2="600" y2="800"/>
    <line x1="700" y1="0" x2="700" y2="800"/>
  </g>

  <!-- Efecto pixelado a la izquierda (cuadrados que salen de la "e") -->
  <g fill="url(#e-gradient)">
    <rect x="180" y="280" width="20" height="20"/>
    <rect x="220" y="240" width="30" height="30"/>
    <rect x="200" y="350" width="25" height="25"/>
    <rect x="160" y="380" width="15" height="15"/>
    <rect x="180" y="430" width="35" height="35"/>
    <rect x="220" y="460" width="20" height="20"/>
    <rect x="200" y="510" width="25" height="25"/>
    <rect x="160" y="490" width="18" height="18"/>
  </g>

  <!-- Letra "e" estilizada -->
  <g transform="translate(300, 200)">
    <circle cx="150" cy="200" r="180" fill="url(#e-gradient)"/>
    <!-- Hueco horizontal de la "e" -->
    <rect x="50" y="180" width="200" height="40" fill="#0A1A2E"/>
    <!-- Hueco inferior de la "e" -->
    <circle cx="150" cy="280" r="50" fill="#0A1A2E"/>
  </g>

  <!-- Texto "ELECTROCONTROL" -->
  <text x="400" y="650" font-family="Bebas Neue, Inter, sans-serif" font-size="80" font-weight="700" fill="#FF4500" text-anchor="middle" letter-spacing="8">
    ELECTROCONTROL
  </text>
</svg>
```

**Nota:** esta es una plantilla simplificada. Para un logo profesional, usa `svg-logo-designer` y deja que el modelo genere la geometría exacta del efecto pixelado y la letra "e" estilizada.

---

## Iconos SVG con estilo de marca

Los iconos de la marca siguen el estilo **Lucide** (stroke-width 2, líneas redondeadas, esquinas redondeadas). Tamaños:

- `w-4 h-4` (16px) — small (listas, captions)
- `w-6 h-6` (24px) — medium (UI estándar)
- `w-7 h-7` (28px) — large (cards de servicio)
- `w-8 h-8` (32px) — hero (stat cards, perfil)

```xml
<!-- Icono WiFi (IoT) -->
<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="url(#grad-iot)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M12 20h.01"/>
  <path d="M2 8.82a15 15 0 0 1 20 0"/>
  <path d="M5 12.859a10 10 0 0 1 14 0"/>
  <path d="M8.5 16.429a5 5 0 0 1 7 0"/>
</svg>

<!-- Icono Auto (ECU) -->
<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="url(#grad-ecu)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/>
  <circle cx="7" cy="17" r="2"/>
  <path d="M9 17h6"/>
  <circle cx="17" cy="17" r="2"/>
</svg>

<!-- Icono Settings (Automatización) -->
<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="url(#grad-auto)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/>
  <circle cx="12" cy="12" r="3"/>
</svg>

<!-- Icono Code (Programación) -->
<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="url(#grad-code)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <polyline points="16 18 22 12 16 6"/>
  <polyline points="8 6 2 12 8 18"/>
</svg>
```

---

## Iconos de contacto

```xml
<!-- Phone -->
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#22D3EE" stroke-width="2">
  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
</svg>

<!-- Mail -->
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#C084FC" stroke-width="2">
  <rect width="20" height="16" x="2" y="4" rx="2"/>
  <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
</svg>

<!-- Map Pin -->
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#22C55E" stroke-width="2">
  <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/>
  <circle cx="12" cy="10" r="3"/>
</svg>

<!-- WhatsApp -->
<svg width="32" height="32" viewBox="0 0 24 24" fill="#10B981">
  <path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>
</svg>
```

---

## Favicon SVG

```xml
<svg width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
  <rect width="32" height="32" rx="6" fill="#0F172A"/>
  <g transform="translate(8, 6)">
    <!-- Versión simplificada de la "e" -->
    <circle cx="8" cy="10" r="7" fill="#FF4500"/>
    <rect x="2" y="9" width="12" height="2" fill="#0F172A"/>
    <circle cx="8" cy="14" r="2" fill="#0F172A"/>
  </g>
</svg>
```

En el HTML:
```html
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
```

---

## Gráficos vectoriales (infografías, diagramas)

### Diagrama de procesos (automatización industrial)

```xml
<svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad-cyan-purple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06B6D4"/>
      <stop offset="100%" stop-color="#A855F7"/>
    </linearGradient>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#06B6D4"/>
    </marker>
  </defs>

  <style>
    .step-bg { fill: #1E293B; stroke: #334155; stroke-width: 1; }
    .step-text { font-family: 'Inter', sans-serif; font-size: 14px; fill: #FFFFFF; font-weight: 600; }
    .step-sub { font-family: 'Inter', sans-serif; font-size: 11px; fill: #94A3B8; }
    .title { font-family: 'Inter', sans-serif; font-size: 20px; fill: #FFFFFF; font-weight: 700; }
  </style>

  <text x="400" y="40" text-anchor="middle" class="title">Flujo de Automatización Industrial</text>

  <!-- Step 1 -->
  <rect x="40" y="100" width="140" height="100" rx="16" class="step-bg"/>
  <text x="110" y="140" text-anchor="middle" class="step-text">1. Sensor</text>
  <text x="110" y="160" text-anchor="middle" class="step-sub">Captura datos</text>

  <!-- Arrow -->
  <line x1="180" y1="150" x2="220" y2="150" stroke="url(#grad-cyan-purple)" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Step 2 -->
  <rect x="220" y="100" width="140" height="100" rx="16" class="step-bg"/>
  <text x="290" y="140" text-anchor="middle" class="step-text">2. PLC</text>
  <text x="290" y="160" text-anchor="middle" class="step-sub">Procesa señales</text>

  <line x1="360" y1="150" x2="400" y2="150" stroke="url(#grad-cyan-purple)" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Step 3 -->
  <rect x="400" y="100" width="140" height="100" rx="16" class="step-bg"/>
  <text x="470" y="140" text-anchor="middle" class="step-text">3. HMI</text>
  <text x="470" y="160" text-anchor="middle" class="step-sub">Visualiza control</text>

  <line x1="540" y1="150" x2="580" y2="150" stroke="url(#grad-cyan-purple)" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Step 4 -->
  <rect x="580" y="100" width="140" height="100" rx="16" class="step-bg"/>
  <text x="650" y="140" text-anchor="middle" class="step-text">4. SCADA</text>
  <text x="650" y="160" text-anchor="middle" class="step-sub">Supervisión remota</text>

  <!-- Leyenda -->
  <text x="400" y="280" text-anchor="middle" class="step-sub" fill="#64748B">Sistema integral IoT + Automatización de Electrocontrol</text>
</svg>
```

---

## Ilustración técnica (sensores IoT)

Para diagramas de arquitectura IoT:

```xml
<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad-iot" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06B6D4"/>
      <stop offset="100%" stop-color="#3B82F6"/>
    </linearGradient>
  </defs>

  <style>
    .device { fill: #1E293B; stroke: #334155; stroke-width: 1.5; }
    .device-icon { fill: url(#grad-iot); }
    .label { font-family: 'Inter', sans-serif; font-size: 12px; fill: #94A3B8; }
    .label-strong { font-family: 'Inter', sans-serif; font-size: 13px; fill: #FFFFFF; font-weight: 600; }
  </style>

  <!-- 3 dispositivos IoT -->
  <g transform="translate(60, 80)">
    <rect class="device" width="100" height="100" rx="12"/>
    <circle class="device-icon" cx="50" cy="50" r="20"/>
    <text x="50" y="130" text-anchor="middle" class="label-strong">Sensor Temp</text>
    <text x="50" y="146" text-anchor="middle" class="label">DHT22</text>
  </g>

  <g transform="translate(250, 80)">
    <rect class="device" width="100" height="100" rx="12"/>
    <circle class="device-icon" cx="50" cy="50" r="20"/>
    <text x="50" y="130" text-anchor="middle" class="label-strong">Microcontrolador</text>
    <text x="50" y="146" text-anchor="middle" class="label">ESP32</text>
  </g>

  <g transform="translate(440, 80)">
    <rect class="device" width="100" height="100" rx="12"/>
    <circle class="device-icon" cx="50" cy="50" r="20"/>
    <text x="50" y="130" text-anchor="middle" class="label-strong">Gateway</text>
    <text x="50" y="146" text-anchor="middle" class="label">MQTT/WiFi</text>
  </g>

  <!-- Conexiones -->
  <path d="M 160 130 Q 200 130 220 130 L 250 130" stroke="url(#grad-iot)" stroke-width="2" fill="none"/>
  <path d="M 350 130 Q 400 130 420 130 L 440 130" stroke="url(#grad-iot)" stroke-width="2" fill="none"/>
</svg>
```

---

## Optimización de SVGs

### Reducir tamaño

```bash
# Con svgo (Node)
npx svgo input.svg -o output.svg

# Con svgcleaner (más configurable)
svgcleaner input.svg output.svg

# Con inkscape (recomendado para SVG complejos)
inkscape input.svg --export-plain-svg --export-text-to-path -o output.svg
```

### Convertir SVG a PNG

```bash
# Con ImageMagick (rápido)
magick input.svg -resize 800x800 -background none output.png

# Con Inkscape (mejor calidad)
inkscape input.svg --export-png=output.png --export-width=800 --export-height=800

# Con rsvg-convert (línea de comandos)
rsvg-convert -w 800 -h 800 input.svg -o output.png

# Con Playwright/Chromium (cuando hay CSS avanzado)
python -c "
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 800, 'height': 800})
    page.goto('file:///input.svg')
    page.screenshot(path='output.png', omit_background=True)
    browser.close()
"
```

### SVG inline en HTML vs archivo externo

| Caso | Recomendación |
|---|---|
| Logo en header, no cambia nunca | Archivo externo (`/logo.svg`) |
| Iconos que se repiten muchas veces | SVG sprite (`<symbol>`) |
| Logo con variaciones según el tema (dark/light) | SVG inline con `<style>` interno que use `prefers-color-scheme` |
| Icono decorativo único | Inline (más rápido, cacheable) |
| Ilustración compleja animada | Archivo externo con CSS animation |

---

## SVG sprite (para múltiples iconos)

```html
<!-- En el HTML, una sola vez: -->
<svg style="display:none">
  <symbol id="icon-wifi" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M12 20h.01"/>
    <path d="M2 8.82a15 15 0 0 1 20 0"/>
    <path d="M5 12.859a10 10 0 0 1 14 0"/>
    <path d="M8.5 16.429a5 5 0 0 1 7 0"/>
  </symbol>
  <symbol id="icon-car" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <!-- ... -->
  </symbol>
</svg>

<!-- Uso: -->
<svg class="w-8 h-8 text-cyan-500"><use href="#icon-wifi"/></svg>
```

---

## Recursos

- **Logo original (referencia):** `assets/logo-electrocontrol.jpg`
- **Skill complementaria:** `svg-logo-designer` (cargar ANTES para tareas de creación)
- **Iconos Lucide:** [lucide.dev](https://lucide.dev) (buscar por nombre y descargar SVG)
- **Optimizador:** [svgo](https://github.com/svg/svgo)
- **Visor online:** [svgviewer.dev](https://www.svgviewer.dev)

---

## Checklist antes de entregar

- [ ] ¿ViewBox correcto y aspect ratio respetado?
- [ ] ¿Colores de marca usados consistentemente?
- [ ] ¿Gradientes reutilizables definidos en `<defs>`?
- [ ] ¿Texto con `fill="url(#gradient)"` o convertido a paths?
- [ ] ¿SVG optimizado (sin paths innecesarios, sin metadata)?
- [ ] ¿Tamaño del archivo razonable? (<50KB idealmente para iconos)
- [ ] ¿Funciona en Chrome, Firefox, Safari, Edge?
- [ ] ¿Accesibilidad (`<title>`, `role="img"`, `aria-label`)?
- [ ] ¿Versiones PNG generadas como respaldo?
- [ ] ¿Favicon SVG creado si es para web?
