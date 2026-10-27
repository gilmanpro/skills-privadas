# Guía: Aplicar Diseño MiBus a SVG

> Cómo crear íconos, logos, ilustraciones y gráficos vectoriales con la identidad visual de MiBus.

## 📋 Antes de empezar

1. Lee `assets/brand-mibus.json` y `assets/colors-mibus.md` de esta skill.
2. **Carga la skill `Diseñador de Logos SVG`** del sistema opencode.
3. Combina: identidad MiBus (esta skill) + técnicas de SVG (skill `Diseñador de Logos SVG`).

## 🎨 Paleta SVG (hex sin # para `fill`)

```javascript
const MIBUS_COLORS = {
  primary:      "283C90",
  primaryLight: "4F5FB5",
  primaryDark:  "1B2A66",
  secondary:    "205CA7",
  secondaryH:   "409EFF",
  accent:       "1DA1F2",
  dark:         "1A1A2E",
  white:        "FFFFFF",
  text:         "333333",
  border:       "E0E0E0",
  success:      "B5D531",
  error:        "BC0C06",
};
```

## 🚌 Íconos de MiBus (estilo flat, line)

### Plantilla de ícono MiBus

```svg
<svg xmlns="http://www.w3.org/2000/svg" 
     viewBox="0 0 24 24" 
     fill="none" 
     stroke="#205CA7" 
     stroke-width="2" 
     stroke-linecap="round" 
     stroke-linejoin="round">
  <!-- Tu path aquí -->
</svg>
```

### Íconos temáticos de MiBus (transporte)

**Bus:**
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <!-- Cuerpo del bus -->
  <rect x="8" y="20" width="48" height="28" rx="4" 
        fill="#283C90" stroke="#1B2A66" stroke-width="2"/>
  <!-- Ventanas -->
  <rect x="14" y="24" width="10" height="8" fill="#1DA1F2" rx="1"/>
  <rect x="27" y="24" width="10" height="8" fill="#1DA1F2" rx="1"/>
  <rect x="40" y="24" width="10" height="8" fill="#1DA1F2" rx="1"/>
  <!-- Puerta -->
  <rect x="14" y="36" width="6" height="10" fill="#205CA7" rx="1"/>
  <!-- Ruedas -->
  <circle cx="20" cy="50" r="5" fill="#1A1A2E"/>
  <circle cx="20" cy="50" r="2" fill="#FFFFFF"/>
  <circle cx="44" cy="50" r="5" fill="#1A1A2E"/>
  <circle cx="44" cy="50" r="2" fill="#FFFFFF"/>
</svg>
```

**Ruta (mapa):**
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <!-- Mapa base -->
  <path d="M8 16 L56 16 L56 48 L8 48 Z" 
        fill="#F0F0F0" stroke="#205CA7" stroke-width="2"/>
  <!-- Calles -->
  <path d="M16 16 L16 48 M32 16 L32 48 M48 16 L48 48" 
        stroke="#E0E0E0" stroke-width="1"/>
  <path d="M8 28 L56 28 M8 40 L56 40" 
        stroke="#E0E0E0" stroke-width="1"/>
  <!-- Ruta -->
  <path d="M16 40 Q24 24 32 32 T48 24" 
        stroke="#1DA1F2" stroke-width="3" fill="none" 
        stroke-linecap="round" stroke-dasharray="0"/>
  <!-- Marcadores -->
  <circle cx="16" cy="40" r="4" fill="#283C90"/>
  <circle cx="48" cy="24" r="4" fill="#283C90"/>
  <!-- Pin central -->
  <circle cx="32" cy="32" r="3" fill="#205CA7"/>
</svg>
```

**Tarjeta MetroBus:**
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <!-- Tarjeta -->
  <rect x="6" y="18" width="52" height="28" rx="3" 
        fill="#283C90" stroke="#1B2A66" stroke-width="2"/>
  <!-- Banda accent -->
  <rect x="6" y="24" width="52" height="6" fill="#1DA1F2"/>
  <!-- Chip -->
  <rect x="12" y="36" width="8" height="6" fill="#B5D531" rx="1"/>
  <!-- Líneas de texto -->
  <rect x="26" y="36" width="20" height="2" fill="#FFFFFF" rx="1"/>
  <rect x="26" y="40" width="14" height="2" fill="#FFFFFF" opacity="0.6" rx="1"/>
  <!-- Logo text -->
  <text x="32" y="14" font-family="Poppins, sans-serif" 
        font-size="8" font-weight="700" fill="#283C90" 
        text-anchor="middle">MiBus</text>
</svg>
```

**Estadísticas (gráfico de barras):**
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <!-- Eje -->
  <line x1="10" y1="56" x2="60" y2="56" stroke="#333333" stroke-width="1.5"/>
  <line x1="10" y1="8" x2="10" y2="56" stroke="#333333" stroke-width="1.5"/>
  <!-- Barras -->
  <rect x="16" y="36" width="8" height="20" fill="#205CA7" rx="1"/>
  <rect x="28" y="20" width="8" height="36" fill="#283C90" rx="1"/>
  <rect x="40" y="28" width="8" height="28" fill="#1DA1F2" rx="1"/>
  <rect x="52" y="12" width="8" height="44" fill="#4F5FB5" rx="1"/>
  <!-- Etiquetas -->
  <text x="20" y="62" font-family="Roboto, sans-serif" font-size="5" 
        fill="#666" text-anchor="middle">U</text>
  <text x="32" y="62" font-family="Roboto, sans-serif" font-size="5" 
        fill="#666" text-anchor="middle">R</text>
  <text x="44" y="62" font-family="Roboto, sans-serif" font-size="5" 
        fill="#666" text-anchor="middle">P</text>
</svg>
```

## 🏷️ Logo / Isotipo derivado (no uses el original, crea variantes)

**Isotipo "M" con estilo MiBus (alternativa, no usar el logo oficial):**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 60" fill="none">
  <defs>
    <linearGradient id="mibusGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#283C90"/>
      <stop offset="100%" stop-color="#205CA7"/>
    </linearGradient>
  </defs>
  
  <!-- Bus icon -->
  <g transform="translate(8, 12)">
    <rect x="0" y="6" width="36" height="22" rx="3" fill="url(#mibusGradient)"/>
    <rect x="4" y="9" width="7" height="5" fill="#1DA1F2" rx="1"/>
    <rect x="13" y="9" width="7" height="5" fill="#1DA1F2" rx="1"/>
    <rect x="22" y="9" width="7" height="5" fill="#1DA1F2" rx="1"/>
    <circle cx="8" cy="32" r="3" fill="#1A1A2E"/>
    <circle cx="28" cy="32" r="3" fill="#1A1A2E"/>
  </g>
  
  <!-- Texto "MiBus" -->
  <text x="56" y="38" font-family="Poppins, sans-serif" 
        font-size="28" font-weight="700" fill="#283C90">MiBus</text>
  <text x="56" y="52" font-family="Roboto, sans-serif" 
        font-size="9" fill="#666">Transporte Masivo de Panamá</text>
</svg>
```

## 🎨 Infografía MiBus (ejemplo completo)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" 
     xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#283C90"/>
      <stop offset="100%" stop-color="#1B2A66"/>
    </linearGradient>
    <linearGradient id="bar" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1DA1F2"/>
      <stop offset="100%" stop-color="#205CA7"/>
    </linearGradient>
  </defs>
  
  <!-- Background primary -->
  <rect width="800" height="600" fill="url(#bg)"/>
  
  <!-- Header con logo -->
  <g transform="translate(40, 30)">
    <text font-family="Poppins, sans-serif" font-size="36" font-weight="700" fill="#FFFFFF">
      MiBus en Cifras
    </text>
    <text y="30" font-family="Roboto, sans-serif" font-size="14" fill="#1DA1F2">
      Transporte Masivo de Panamá · 2026
    </text>
  </g>
  
  <!-- KPI Cards -->
  <g transform="translate(40, 100)">
    <!-- Card 1 -->
    <g>
      <rect width="170" height="100" rx="8" fill="#1B2A66" opacity="0.5"/>
      <text x="85" y="50" font-family="Poppins, sans-serif" font-size="36" 
            font-weight="900" fill="#FFFFFF" text-anchor="middle">1436</text>
      <text x="85" y="75" font-family="Roboto, sans-serif" font-size="12" 
            fill="#1DA1F2" text-anchor="middle" letter-spacing="2">UNIDADES</text>
    </g>
    
    <!-- Card 2 -->
    <g transform="translate(180, 0)">
      <rect width="170" height="100" rx="8" fill="#1B2A66" opacity="0.5"/>
      <text x="85" y="50" font-family="Poppins, sans-serif" font-size="36" 
            font-weight="900" fill="#FFFFFF" text-anchor="middle">+4,000</text>
      <text x="85" y="75" font-family="Roboto, sans-serif" font-size="12" 
            fill="#1DA1F2" text-anchor="middle" letter-spacing="2">TRABAJADORES</text>
    </g>
    
    <!-- Card 3 -->
    <g transform="translate(360, 0)">
      <rect width="170" height="100" rx="8" fill="#1B2A66" opacity="0.5"/>
      <text x="85" y="50" font-family="Poppins, sans-serif" font-size="36" 
            font-weight="900" fill="#FFFFFF" text-anchor="middle">152</text>
      <text x="85" y="75" font-family="Roboto, sans-serif" font-size="12" 
            fill="#1DA1F2" text-anchor="middle" letter-spacing="2">RUTAS</text>
    </g>
    
    <!-- Card 4 -->
    <g transform="translate(540, 0)">
      <rect width="170" height="100" rx="8" fill="#1B2A66" opacity="0.5"/>
      <text x="85" y="50" font-family="Poppins, sans-serif" font-size="32" 
            font-weight="900" fill="#FFFFFF" text-anchor="middle">450,000</text>
      <text x="85" y="75" font-family="Roboto, sans-serif" font-size="12" 
            fill="#1DA1F2" text-anchor="middle" letter-spacing="1">PASAJEROS/DÍA</text>
    </g>
  </g>
  
  <!-- Gráfico de barras -->
  <g transform="translate(40, 250)">
    <text font-family="Poppins, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">
      Crecimiento mensual
    </text>
    
    <!-- Barras -->
    <g transform="translate(0, 30)">
      <!-- Eje X -->
      <line x1="0" y1="200" x2="720" y2="200" stroke="#4F5FB5" stroke-width="1"/>
      
      <!-- Barras con colores MiBus -->
      <rect x="20" y="100" width="50" height="100" fill="url(#bar)" rx="2"/>
      <rect x="90" y="80" width="50" height="120" fill="url(#bar)" rx="2"/>
      <rect x="160" y="60" width="50" height="140" fill="url(#bar)" rx="2"/>
      <rect x="230" y="50" width="50" height="150" fill="url(#bar)" rx="2"/>
      <rect x="300" y="40" width="50" height="160" fill="url(#bar)" rx="2"/>
      <rect x="370" y="30" width="50" height="170" fill="url(#bar)" rx="2"/>
      <rect x="440" y="20" width="50" height="180" fill="url(#bar)" rx="2"/>
      <rect x="510" y="10" width="50" height="190" fill="url(#bar)" rx="2"/>
      <rect x="580" y="0" width="50" height="200" fill="url(#bar)" rx="2"/>
      <rect x="650" y="-10" width="50" height="210" fill="url(#bar)" rx="2"/>
      
      <!-- Labels -->
      <g font-family="Roboto, sans-serif" font-size="11" fill="#1DA1F2" text-anchor="middle">
        <text x="45" y="220">Ene</text>
        <text x="115" y="220">Feb</text>
        <text x="185" y="220">Mar</text>
        <text x="255" y="220">Abr</text>
        <text x="325" y="220">May</text>
        <text x="395" y="220">Jun</text>
        <text x="465" y="220">Jul</text>
        <text x="535" y="220">Ago</text>
        <text x="605" y="220">Sep</text>
        <text x="675" y="220">Oct</text>
      </g>
    </g>
  </g>
  
  <!-- Footer con copyright -->
  <text x="400" y="580" font-family="Roboto, sans-serif" font-size="10" 
        fill="#4F5FB5" text-anchor="middle">
    MiBus · Transporte Masivo de Panamá · www.mibus.com.pa
  </text>
</svg>
```

## 🖼️ Snippet para exportar SVG con colores MiBus (Node.js)

```javascript
// render-svg.js
const fs = require('fs');
const path = require('path');

function mibusSVG(content, options = {}) {
  const {
    width = 800,
    height = 600,
    background = '283C90', // primary
  } = options;
  
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     viewBox="0 0 ${width} ${height}" 
     width="${width}" 
     height="${height}">
  <rect width="${width}" height="${height}" fill="#${background}"/>
  ${content}
</svg>`;
}

// Uso
const svg = mibusSVG(`
  <text x="400" y="300" font-family="Poppins" font-size="48" 
        font-weight="700" fill="white" text-anchor="middle">
    MiBus
  </text>
`, { width: 800, height: 400, background: '283C90' });

fs.writeFileSync('mibus-card.svg', svg);
```

## ✅ Checklist para SVG MiBus

- [ ] Solo colores de la paleta MiBus
- [ ] Tipografía Poppins/texto + Roboto/secondary
- [ ] Tamaño consistente en íconos (24x24 o 64x64 viewBox)
- [ ] Stroke-width consistente (1.5-2px en íconos line)
- [ ] Logo MiBus oficial cuando se requiera (descargado de mibus.com.pa)
- [ ] viewBox bien definido para escalabilidad
- [ ] Sin dependencias externas (fuentes embebidas o fallback)

## 🚫 Errores comunes

- ❌ Colores fuera de paleta (rojo, verde, amarillo)
- ❌ Múltiples estilos de íconos mezclados
- ❌ Stroke-width inconsistente
- ❌ Íconos demasiado complejos (no escalan bien)
- ❌ Sin viewBox (rompe el responsive)
- ❌ Texto pixelado (usar siempre vector o embeber fuente)
- ❌ Logo deformado o con cambio de proporción
