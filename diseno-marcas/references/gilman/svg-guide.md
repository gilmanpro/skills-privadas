# Aplicación a SVG (logos / iconos) — gilman.pro

Cómo crear SVGs (logos, iconos, decoraciones) con el branding gilman.pro. **El logo Circuit G oficial está en `assets/logo_gilmanpro.svg`.**

## 1. LOGO "CIRCUIT G" — ANATOMÍA

```
viewBox: 0 0 200 80
- Icono (G estilizada como circuito): x=28-55, y=15-62
- Wordmark "gilman.pro": x=75, y=48, font-size=24, font-family=Rajdhani/Orbitron, font-weight=700
- Color wordmark: #10B981 (emerald 500)
- Gradiente icono: linear(135deg, #10B981 0%, #06B6D4 100%)
- Trazos: stroke-width=3, fill=none, stroke-linecap=round, stroke-linejoin=round
- Nodos en extremos: pequeños círculos (r=2-3) en colores del gradiente
- Glow filter: feGaussianBlur stdDeviation=1.5
```

## 2. PLANTILLA BASE — Crear logo nuevo con marca gilman

Si el usuario quiere un logo NUEVO con la marca gilman (no una variante del Circuit G):

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 80" role="img" aria-label="Logo - gilman.pro">
  <defs>
    <!-- Gradiente de marca: emerald → cyan, diagonal -->
    <linearGradient id="gilmanGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#10B981"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
    
    <!-- Glow filter -->
    <filter id="gilmanGlow">
      <feGaussianBlur stdDeviation="1.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- ICONO (60x60 en viewBox 0 0 60 60) -->
  <g stroke="url(#gilmanGradient)" stroke-width="3" fill="none" 
     stroke-linecap="round" stroke-linejoin="round" filter="url(#gilmanGlow)">
    <!-- Trazos del icono aquí -->
  </g>
  
  <!-- Nodos (círculos en los extremos) -->
  <circle cx="X" cy="Y" r="3" fill="#10B981"/>
  
  <!-- WORDMARK -->
  <text x="75" y="48" 
        font-family="Rajdhani, Orbitron, sans-serif" 
        font-size="24" 
        font-weight="700" 
        fill="#10B981">gilman.pro</text>
</svg>
```

## 3. VARIANTES DEL LOGO

### 3.1 Versión clara (default) — sobre fondo blanco

Usar `assets/logo_gilmanpro.svg`:
- Gradiente emerald → cyan
- Wordmark emerald

### 3.2 Versión dark — sobre fondo oscuro (slate-900)

Usar `assets/logo_gilmanpro-dark.svg`:
- Gradiente cyan → white
- Wordmark cyan (#22D3EE)

### 3.3 Versión monocromática — una sola tinta (impresiones, embossing)

Usar `assets/logo_gilmanpro-mono.svg`:
- Todos los trazos en `#10B981` sólido (sin gradiente)
- Wordmark `#10B981`
- Sin glow filter

### 3.4 Versión pequeña (favicon 32x32)

Solo el icono, sin wordmark:
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 60" role="img" aria-label="gilman.pro">
  <defs>
    <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#10B981"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
  </defs>
  <g stroke="url(#g)" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M30,15 L45,15 L45,22 L35,22"/>
    <path d="M35,22 L35,40 L28,40 L28,55"/>
    <path d="M28,55 L35,55 L35,62 L50,62"/>
    <path d="M50,62 L50,52 L42,52"/>
    <path d="M42,52 L42,38 L52,38"/>
    <path d="M52,38 L52,25 L48,25 L48,18 L55,18"/>
  </g>
  <circle cx="30" cy="15" r="3" fill="#10B981"/>
  <circle cx="45" cy="22" r="2.5" fill="#06B6D4"/>
  <circle cx="55" cy="18" r="2.5" fill="#10B981"/>
  <circle cx="52" cy="38" r="2" fill="#06B6D4"/>
  <circle cx="42" cy="52" r="2.5" fill="#10B981"/>
</svg>
```

## 4. ICONOS CON MARCA GILMAN

Si necesitas un set de iconos que combine con el branding (estilo circuit/tech):

### Plantilla para icono individual

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" 
     fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <!-- Path del icono aquí (compatible con Lucide) -->
  <path d="..."/>
</svg>
```

### Iconos sugeridos para marca gilman

| Icono | Uso | Path Lucide |
|---|---|---|
| `briefcase` | Experiencia laboral | `<path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>` |
| `graduation-cap` | Formación | (Lucide native) |
| `award` | Certificaciones | (Lucide native) |
| `cpu` | Habilidades técnicas | (Lucide native) |
| `mail` | Contacto email | (Lucide native) |
| `phone` | WhatsApp | (Lucide native) |
| `linkedin` | LinkedIn social | (Lucide native) |
| `github` | GitHub social | (Lucide native) |
| `twitter` | Twitter/X | (Lucide native) |
| `file-text` | CV / Documento | (Lucide native) |
| `sparkles` | CV visual / IA | (Lucide native) |
| `arrow-right` | CTA "Ver más" | `<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>` |
| `chevron-down` | Scroll cue | `<path d="m6 9 6 6 6-6"/>` |
| `send` | Enviar mensaje | `<path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/>` |

**Recomendación:** usar los iconos Lucide directamente desde CDN (`https://unpkg.com/lucide@latest`) en lugar de mantener SVGs propios.

```html
<script src="https://unpkg.com/lucide@latest"></script>
<script>lucide.createIcons();</script>

<!-- Uso: -->
<i data-lucide="briefcase" class="w-5 h-5 text-emerald-600"></i>
```

## 5. SEPARADOR DECORATIVO COMO SVG (signature)

Para usar en PDFs, slides, o donde no se pueda hacer con HTML:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 12" width="200" height="12" role="img" aria-label="Separador decorativo gilman">
  <!-- Línea corta (0-40) -->
  <line x1="0" y1="6" x2="40" y2="6" stroke="#10B981" stroke-width="1.5"/>
  
  <!-- Punto 1 (50) -->
  <circle cx="50" cy="6" r="3" fill="#10B981"/>
  
  <!-- Línea larga (60-120) -->
  <line x1="60" y1="6" x2="120" y2="6" stroke="#10B981" stroke-width="1.5"/>
  
  <!-- Punto 2 violet (130) -->
  <circle cx="130" cy="6" r="3" fill="#8B5CF6"/>
  
  <!-- Línea corta (140-180) -->
  <line x1="140" y1="6" x2="180" y2="6" stroke="#8B5CF6" stroke-width="1.5"/>
</svg>
```

**Variantes:**

```svg
<!-- Versión dark mode: indigo en lugar de emerald -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 12" width="200" height="12">
  <line x1="0" y1="6" x2="40" y2="6" stroke="#6366F1" stroke-width="1.5"/>
  <circle cx="50" cy="6" r="3" fill="#6366F1"/>
  <line x1="60" y1="6" x2="120" y2="6" stroke="#6366F1" stroke-width="1.5"/>
  <circle cx="130" cy="6" r="3" fill="#8B5CF6"/>
  <line x1="140" y1="6" x2="180" y2="6" stroke="#8B5CF6" stroke-width="1.5"/>
</svg>
```

## 6. PATRONES DECORATIVOS GILMAN

### Patrón "circuito" (tech)

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <defs>
    <pattern id="circuit" x="0" y="0" width="40" height="40" patternUnits="userSpaceOnUse">
      <!-- Líneas horizontales y verticales -->
      <path d="M 0 20 L 20 20 L 20 0" stroke="#10B981" stroke-width="0.5" fill="none" opacity="0.3"/>
      <path d="M 20 40 L 20 30 L 40 30" stroke="#10B981" stroke-width="0.5" fill="none" opacity="0.3"/>
      <!-- Nodos -->
      <circle cx="20" cy="20" r="1" fill="#10B981" opacity="0.5"/>
      <circle cx="20" cy="30" r="1" fill="#10B981" opacity="0.5"/>
    </pattern>
  </defs>
  <rect width="100" height="100" fill="url(#circuit)"/>
</svg>
```

Uso en CSS: `background-image: url('circuit-pattern.svg');`

### Patrón "circuito sutil" (hero background)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" preserveAspectRatio="xMidYMid slice">
  <defs>
    <pattern id="circuitBoard" x="0" y="0" width="60" height="60" patternUnits="userSpaceOnUse">
      <path d="M 0 30 L 30 30 L 30 0 M 30 30 L 30 60 M 30 30 L 60 30" 
            stroke="white" stroke-width="0.5" fill="none" opacity="0.1"/>
      <circle cx="30" cy="30" r="1.5" fill="white" opacity="0.15"/>
      <circle cx="0"  cy="30" r="1"   fill="white" opacity="0.15"/>
      <circle cx="30" cy="0"  r="1"   fill="white" opacity="0.15"/>
      <circle cx="60" cy="30" r="1"   fill="white" opacity="0.15"/>
      <circle cx="30" cy="60" r="1"   fill="white" opacity="0.15"/>
    </pattern>
  </defs>
  <rect width="200" height="200" fill="url(#circuitBoard)"/>
</svg>
```

Aplicar en CSS: `background-image: url('circuit-bg.svg'); background-size: 200px;` sobre un fondo emerald.

## 7. QR CODE / ISOTIPO

Si necesitas un isotipo (solo el icono) sin wordmark:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 60" width="60" height="60">
  <defs>
    <linearGradient id="iso" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#10B981"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
  </defs>
  <g stroke="url(#iso)" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M30,15 L45,15 L45,22 L35,22"/>
    <path d="M35,22 L35,40 L28,40 L28,55"/>
    <path d="M28,55 L35,55 L35,62 L50,62"/>
    <path d="M50,62 L50,52 L42,52"/>
    <path d="M42,52 L42,38 L52,38"/>
    <path d="M52,38 L52,25 L48,25 L48,18 L55,18"/>
  </g>
  <circle cx="30" cy="15" r="3" fill="#10B981"/>
  <circle cx="45" cy="22" r="2.5" fill="#06B6D4"/>
  <circle cx="55" cy="18" r="2.5" fill="#10B981"/>
  <circle cx="52" cy="38" r="2" fill="#06B6D4"/>
  <circle cx="42" cy="52" r="2.5" fill="#10B981"/>
</svg>
```

## 8. CONVERSIÓN LOGO → PNG

Los archivos .svg son vectoriales, pero a veces se necesita PNG (favicon, redes sociales). Usar:

### Con Python (cairosvg + cairocffi)

```python
import cairosvg
from pathlib import Path

src = Path("logo_gilmanpro.svg")
out_dir = Path("out")
out_dir.mkdir(exist_ok=True)

# Generar PNG en distintos tamaños
for size in [32, 64, 128, 256, 512, 1024]:
    cairosvg.svg2png(
        url=str(src),
        write_to=str(out_dir / f"logo-{size}.png"),
        output_width=size,
        output_height=int(size * 80 / 200),  # mantener aspect ratio
    )
```

### Con Inkscape (CLI)

```bash
inkscape --export-type=png --export-filename=logo.png -w 512 logo_gilmanpro.svg
```

### Con Node (sharp + svg2png)

```bash
npm install sharp
```

```javascript
const sharp = require('sharp');
const fs = require('fs');

const svg = fs.readFileSync('logo_gilmanpro.svg');
sharp(svg).resize(512).png().toFile('logo-512.png');
```

## 9. USO EN OTROS FORMATOS

### En PowerPoint
- Insertar > Imágenes > SVG (PowerPoint 2019+ soporta SVG nativamente)
- Si no soporta, convertir a PNG previamente

### En Word
- Insertar > Imágenes > SVG (Word 2019+ soporta)
- Si no, usar PNG de alta resolución (mínimo 1024px de ancho)

### En PDF (vía ReportLab)
```python
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg

drawing = svg2rlg("logo_gilmanpro.svg")
renderPDF.draw(drawing, canvas_obj, x, y)
```

### En PDF (vía HTML/WeasyPrint)
- Usar `<img src="logo_gilmanpro.svg">` directamente
- WeasyPrint renderiza SVG nativamente

### En Excel
- Convertir a PNG primero (Excel no soporta SVG nativamente en versiones antiguas)
- Insertar > Imágenes > PNG

## 10. REGLAS

1. **Gradiente oficial:** `#10B981` → `#06B6D4` (135°). NUNCA cambiar stops.
2. **Wordmark color:** `#10B981` (claro) o `#22D3EE` (dark). NO usar indigo en el wordmark.
3. **Font wordmark:** Rajdhani 700 (alternativa Orbitron 700). NO usar Montserrat/Lato.
4. **Stroke width:** 3px (estándar), 2px (versión pequeña), 4px (versión display).
5. **Fill:** `none` en trazos, gradiente solo en stroke.
6. **Nodos:** siempre con `fill` sólido (no `stroke`) en colores emerald/cyan.
7. **Glow filter:** opcional. Usar SOLO en hero/portada, NO en tamaños pequeños.
8. **ViewBox:** 200x80 para logo completo, 60x60 para isotipo, 24x24 para favicon.
9. **Aria-label:** siempre presente para accesibilidad.
10. **xmlns:** siempre `xmlns="http://www.w3.org/2000/svg"` para SVG standalone.

## 11. ERRORES COMUNES

- ❌ Cambiar el gradiente del logo (prohibido por marca)
- ❌ Usar Montserrat para el wordmark (es Rajdhani/Orbitron)
- ❌ Olvidar `xmlns` → no se renderiza en navegador
- ❌ `viewBox` con valores incorrectos → distorsión
- ❌ `<image href="..."/>` con paths relativos → no se carga al portar
- ❌ `stroke-width` muy grueso en tamaño pequeño → se ve pixelado
- ❌ Olvidar `aria-label` → problemas de accesibilidad
- ❌ Color de wordmark que no contrasta con fondo → ilegible
- ❌ Versión dark con gradiente emerald → no se ve, usar cyan-white
