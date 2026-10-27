# Plantilla SVG / Gráficos Vectoriales — ITSE

Guía para crear logos, iconos, ilustraciones y elementos SVG con el estilo ITSE usando la skill `svg-logo-designer` + esta skill.

---

## 🚨 REGLA: Logo del ITSE ARRIBA en banners, posters y portadas SVG

> **En todo SVG que represente una portada, banner, poster, diploma o
> tarjeta institucional, el logo del ITSE va en la parte SUPERIOR — NUNCA
> en el centro vertical, NUNCA debajo del texto principal.**

- **Banners (1200×630):** Logo en la esquina superior izquierda, alto ~80–100 px
- **Posters / diplomas:** Logo en el top centrado o alineado a la izquierda
- **Tarjetas de presentación:** Logo en el top centrado
- **Infografías:** Logo pequeño en la esquina superior izquierda
- **Iconos (24×24, 48×48):** No llevan el logo completo; usan los iconos institucionales

---

## Especificaciones del SVG

| Parámetro | Valor |
|---|---|
| ViewBox recomendado | `0 0 100 100` (iconos) o `0 0 400 100` (logos) |
| Tamaño típico | 24-512 px |
| Formato | SVG estándar (no necesita SMIL ni JS) |
| Color | Usar HEX directos o `currentColor` para herencia |

---

## Paleta SVG oficial

```svg
<svg ...>
  <defs>
    <linearGradient id="itse-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFCE00"/>
      <stop offset="100%" stop-color="#FFB000"/>
    </linearGradient>
  </defs>
</svg>
```

**Colores sólidos:**
- `#FFB000` (dorado principal)
- `#FFCE00` (dorado claro)
- `#FFBC00` (dorado medio)
- `#424242` (gris carbón)
- `#FFFFFF` (blanco)
- `#225082` (azul)
- `#9EBE43` (verde)
- `#CD2E26` (rojo)
- `#AEAEAE` (gris borde)
- `#F7F7F7` (gris claro fondo)

---

## Logo del ITSE en SVG (versión limpia)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 80" width="280" height="80">
  <defs>
    <linearGradient id="itse-gold" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFCE00"/>
      <stop offset="100%" stop-color="#FFB000"/>
    </linearGradient>
  </defs>
  
  <text x="10" y="50" 
        font-family="Inter, Helvetica Neue, Helvetica, Arial, sans-serif" 
        font-size="48" font-weight="900" fill="#424242" letter-spacing="-1">
    ITSE
  </text>
  
  <rect x="10" y="14" width="6" height="40" fill="url(#itse-gold)"/>
  
  <line x1="10" y1="58" x2="180" y2="58" stroke="#AEAEAE" stroke-width="0.5"/>
  
  <text x="10" y="72" 
        font-family="Inter, Helvetica Neue, Helvetica, Arial, sans-serif" 
        font-size="9" font-weight="500" fill="#7B7B7B" letter-spacing="2">
    DE CICLO CORTO
  </text>
</svg>
```

⚠️ Para uso oficial institucional, solicita el SVG vectorial maestro al ITSE.

---

## Iconografía SVG (estilo ITSE)

### Estilo base
- **Trazo:** 2px sólido
- **Color:** `#424242` por defecto (o `currentColor`)
- **Esquinas:** redondeadas (`stroke-linecap="round"`, `stroke-linejoin="round"`)

### Iconos base (estilo outlined)

```svg
<!-- Computadora (Innovación Digital) -->
<svg width="48" height="48" viewBox="0 0 24 24" fill="none" 
     stroke="#424242" stroke-width="2" 
     stroke-linecap="round" stroke-linejoin="round">
  <rect x="2" y="3" width="20" height="14" rx="2"/>
  <line x1="8" y1="21" x2="16" y2="21"/>
  <line x1="12" y1="17" x2="12" y2="21"/>
</svg>

<!-- Engranaje (Tecnología Industrial) -->
<svg width="48" height="48" viewBox="0 0 24 24" fill="none"
     stroke="#424242" stroke-width="2"
     stroke-linecap="round" stroke-linejoin="round">
  <circle cx="12" cy="12" r="3"/>
  <path d="M12 1v6m0 6v6M4.22 4.22l4.24 4.24m7.07 7.07l4.24 4.24M1 12h6m6 0h6M4.22 19.78l4.24-4.24m7.07-7.07l4.24-4.24"/>
</svg>

<!-- Maleta (Negocios) -->
<svg width="48" height="48" viewBox="0 0 24 24" fill="none"
     stroke="#424242" stroke-width="2"
     stroke-linecap="round" stroke-linejoin="round">
  <rect x="2" y="7" width="20" height="14" rx="2"/>
  <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
</svg>

<!-- Tenedor (Hospitalidad y Turismo) -->
<svg width="48" height="48" viewBox="0 0 24 24" fill="none"
     stroke="#424242" stroke-width="2"
     stroke-linecap="round" stroke-linejoin="round">
  <path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/>
  <path d="M7 2v20"/>
  <path d="M21 15V2a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"/>
</svg>
```

### Icono institucional ITSE redondo (badge)

```svg
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="badge-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFCE00"/>
      <stop offset="100%" stop-color="#FFB000"/>
    </linearGradient>
  </defs>
  
  <circle cx="50" cy="50" r="48" fill="url(#badge-gold)"/>
  <circle cx="50" cy="50" r="42" fill="white"/>
  
  <text x="50" y="58" 
        font-family="Inter, Helvetica Neue, Helvetica, Arial, sans-serif" 
        font-size="22" font-weight="900" fill="#424242"
        text-anchor="middle" letter-spacing="-0.5">
    ITSE
  </text>
  
  <circle cx="50" cy="68" r="2" fill="#FFB000"/>
</svg>
```

---

## Gráficos e infografías SVG

### Plantilla de infografía de proceso (5 pasos)

```svg
<svg viewBox="0 0 800 200" width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="step-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFCE00"/>
      <stop offset="100%" stop-color="#FFB000"/>
    </linearGradient>
  </defs>
  
  <!-- Paso 1 -->
  <circle cx="80" cy="100" r="40" fill="url(#step-gold)"/>
  <text x="80" y="110" text-anchor="middle" font-family="Inter, sans-serif" 
        font-size="28" font-weight="700" fill="white">1</text>
  <text x="80" y="170" text-anchor="middle" font-family="Inter, sans-serif" 
        font-size="14" font-weight="500" fill="#424242">Investigación</text>
  
  <line x1="120" y1="100" x2="200" y2="100" stroke="#AEAEAE" 
        stroke-width="2" stroke-dasharray="4,4"/>
  
  <!-- Paso 2 -->
  <circle cx="240" cy="100" r="40" fill="url(#step-gold)"/>
  <text x="240" y="110" text-anchor="middle" font-family="Inter, sans-serif" 
        font-size="28" font-weight="700" fill="white">2</text>
  <text x="240" y="170" text-anchor="middle" font-family="Inter, sans-serif" 
        font-size="14" font-weight="500" fill="#424242">Diseño</text>
  
  <line x1="280" y1="100" x2="360" y2="100" stroke="#AEAEAE" 
        stroke-width="2" stroke-dasharray="4,4"/>
  
  <!-- Paso 3 -->
  <circle cx="400" cy="100" r="40" fill="url(#step-gold)"/>
  <text x="400" y="110" text-anchor="middle" font-family="Inter, sans-serif" 
        font-size="28" font-weight="700" fill="white">3</text>
  <text x="400" y="170" text-anchor="middle" font-family="Inter, sans-serif" 
        font-size="14" font-weight="500" fill="#424242">Desarrollo</text>
  
  <line x1="440" y1="100" x2="520" y2="100" stroke="#AEAEAE" 
        stroke-width="2" stroke-dasharray="4,4"/>
  
  <!-- Paso 4 -->
  <circle cx="560" cy="100" r="40" fill="url(#step-gold)"/>
  <text x="560" y="110" text-anchor="middle" font-family="Inter, sans-serif" 
        font-size="28" font-weight="700" fill="white">4</text>
  <text x="560" y="170" text-anchor="middle" font-family="Inter, sans-serif" 
        font-size="14" font-weight="500" fill="#424242">Pruebas</text>
  
  <line x1="600" y1="100" x2="680" y2="100" stroke="#AEAEAE" 
        stroke-width="2" stroke-dasharray="4,4"/>
  
  <!-- Paso 5 -->
  <circle cx="720" cy="100" r="40" fill="url(#step-gold)"/>
  <text x="720" y="110" text-anchor="middle" font-family="Inter, sans-serif" 
        font-size="28" font-weight="700" fill="white">5</text>
  <text x="720" y="170" text-anchor="middle" font-family="Inter, sans-serif" 
        font-size="14" font-weight="500" fill="#424242">Lanzamiento</text>
</svg>
```

---

## Patrones de fondo SVG

### Patrón de puntos sutiles

```svg
<svg width="40" height="40" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="dots" x="0" y="0" width="40" height="40" patternUnits="userSpaceOnUse">
      <circle cx="20" cy="20" r="1" fill="#AEAEAE" opacity="0.3"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#dots)"/>
</svg>
```

### Patrón de líneas diagonales (acento dorado)

```svg
<svg width="20" height="20" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="diagonals" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <line x1="0" y1="20" x2="20" y2="0" stroke="#FFB000" stroke-width="1" opacity="0.15"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#diagonals)"/>
</svg>
```

---

## Plantilla de banner para redes sociales

```svg
<svg viewBox="0 0 1200 630" width="1200" height="630" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#424242"/>
      <stop offset="100%" stop-color="#2A2A2A"/>
    </linearGradient>
  </defs>
  
  <rect width="1200" height="630" fill="url(#bg-gold)"/>
  <rect x="0" y="0" width="20" height="630" fill="#FFB000"/>
  
  <g transform="translate(80, 80)">
    <text x="0" y="40" font-family="Inter, sans-serif" font-size="56" 
          font-weight="900" fill="white" letter-spacing="-1">ITSE</text>
    <line x1="0" y1="60" x2="200" y2="60" stroke="#AEAEAE" stroke-width="0.5"/>
    <text x="0" y="80" font-family="Inter, sans-serif" font-size="14" 
          font-weight="500" fill="#AEAEAE" letter-spacing="2">DE CICLO CORTO</text>
  </g>
  
  <text x="80" y="380" font-family="Inter, sans-serif" font-size="72" 
        font-weight="700" fill="white">Inscripciones</text>
  <text x="80" y="450" font-family="Inter, sans-serif" font-size="72" 
        font-weight="700" fill="#FFB000">Abiertas {año}</text>
    <!-- {año} = año actual -->
  
  <text x="80" y="510" font-family="Inter, sans-serif" font-size="24" 
        font-weight="400" fill="#AEAEAE">15 carreras técnicas superiores en 4 áreas</text>
  
  <g transform="translate(80, 540)">
    <rect x="0" y="0" width="240" height="50" rx="8" fill="#FFB000"/>
    <text x="120" y="32" text-anchor="middle" font-family="Inter, sans-serif" 
          font-size="18" font-weight="700" fill="white">Inscríbete →</text>
  </g>
</svg>
```

---

## Buenas prácticas para SVG del ITSE

✅ **Sí:**
- Usar `viewBox` para escalabilidad
- Definir gradientes en `<defs>` y reutilizar
- Usar `currentColor` para iconos que cambian de color
- Optimizar el SVG (minificar) antes de publicar
- Usar tipografía Inter/Helvetica/Arial
- Aplicar `stroke-linecap="round"` y `stroke-linejoin="round"`

❌ **No:**
- NO uses tipografías no estándar
- NO uses efectos de filtro pesados
- NO uses SMIL ni JavaScript dentro del SVG
- NO uses imágenes raster embebidas si puedes usar vectores
- NO uses viewBox incorrecto que deforme los iconos

---

## Cheatsheet

```
ITSE SVG
========
ViewBox: 0 0 100 100 (iconos), 0 0 400 100 (logos)
Trazo: 2px, color #424242 o currentColor
Esquinas: stroke-linecap="round", stroke-linejoin="round"
Gradiente: linear 135deg #FFCE00 → #FFB000
Carrera de referencia: T.S. en Big Data y Ciencia de Datos

LOGO: ARRIBA en banners, posters, portadas SVG
      Esquina sup. izq. (80-100px) en banners 1200x630
      Top centrado en posters / diplomas
      No aplica en iconos pequeños

COLORES EN SVG:
  #FFB000 (dorado principal)
  #FFCE00 (dorado claro)
  #FFBC00 (dorado medio)
  #424242 (gris carbón)
  #FFFFFF (blanco)
  #225082 (azul)
  #9EBE43 (verde)
  #CD2E26 (rojo)
  #F7F7F7 (gris claro)

GRADIENTE OFICIAL:
  <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#FFCE00"/>
    <stop offset="100%" stop-color="#FFB000"/>
  </linearGradient>
```

---

## Recursos adicionales

- `references/itse/colors.md` — paleta completa
- `references/itse/typography.md` — sistema tipográfico
- `references/itse/logo.md` — uso del logo
- `references/itse/branding.md` — datos institucionales
- Skill complementaria: `graphic-media` (unifica `svg` y `canvas-design`, archivadas el 2026-10-15)
