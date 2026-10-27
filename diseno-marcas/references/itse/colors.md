# Paleta de Colores Oficial — ITSE

Extraído directamente de las CSS Variables del sitio oficial (https://www.itse.ac.pa/) en junio 2026. Estos valores son la fuente única de verdad para cualquier material del ITSE.

---

## 🎨 Colores primarios (brand)

Estos son los **3 colores oficiales** del ITSE. Todo material debe construirse alrededor de ellos.

| Token CSS | HEX | RGB | HSL | Nombre humano | Uso |
|---|---|---|---|---|---|
| `--color-primary` | **`#FFB000`** | 255, 176, 0 | 42°, 100%, 50% | **Dorado ITSE** | Acentos, botones primarios, líneas, iconos, badges |
| `--color-text` | **`#424242`** | 66, 66, 66 | 0°, 0%, 26% | **Gris Carbón** | Texto principal, títulos, fondo de secciones destacadas |
| `--color-white` | **`#FFFFFF`** | 255, 255, 255 | 0°, 0%, 100% | **Blanco** | Fondo principal, texto sobre fondos oscuros/dorados |

**Regla 60-30-10:**
- 60% blanco (fondos)
- 30% gris carbón (texto, secciones oscuras)
- 10% dorado (acentos, CTAs)

---

## 🌟 Colores primarios extendidos (variantes de dorado)

| Token CSS | HEX | RGB | Uso |
|---|---|---|---|
| `--color-primary-100` | **`#FFB000`** | 255, 176, 0 | **Dorado principal** (idéntico a `--color-primary`) |
| `--color-primary-200` | `#FFBC00` | 255, 188, 0 | Dorado medio (hover state, punto medio en gradientes) |
| `--color-primary-300` | `#FFCE00` | 255, 206, 0 | Dorado claro (inicio de gradientes, focus state) |

### Gradiente oficial

```css
background: linear-gradient(135deg, #FFCE00 0%, #FFB000 100%);
```

Este degradado es la **firma visual** del ITSE. Úsalo en:
- Hero banners
- Botones principales
- Tarjetas destacadas
- Iconos grandes
- Divisores decorativos

---

## 🎯 Colores secundarios (institucionales)

Estos son colores de apoyo para casos específicos. NO los uses como color principal.

| Token CSS | HEX | RGB | Nombre humano | Uso típico |
|---|---|---|---|---|
| `--color-alt-blue` | **`#225082`** | 34, 80, 130 | **Azul institucional** | Enlaces, badges de Innovación Digital, acentos fríos |
| `--color-alt-green` | **`#9EBE43`** | 158, 190, 67 | **Verde institucional** | Éxito, confirmaciones, badges de Hospitalidad y Turismo |
| `--color-alt-red` | **`#CD2E26`** | 205, 46, 38 | **Rojo institucional** | Errores, alertas, badges críticos |

---

## ✅ Colores de estado (semánticos)

| Token CSS | HEX | Uso |
|---|---|---|
| `--color-sucess` | **`#00A63E`** | Éxito, validaciones correctas, "Sí" |
| `--color-error` | **`#CD2E26`** | Errores, validaciones incorrectas, "No" |
| `--color-warning` | **`#F57C00`** | Advertencias, precauciones |
| `--color-info` | **`#1A73E8`** | Información, neutral |

---

## ⚫ Escala de grises

Escala neutra para texto, fondos y bordes.

| Token CSS | HEX | RGB | Uso |
|---|---|---|---|
| `--color-gray-100` | **`#7B7B7B`** | 123, 123, 123 | Texto secundario, labels, placeholders |
| `--color-gray-200` | **`#9D9D9C`** | 157, 157, 156 | Texto deshabilitado, captions |
| `--color-gray-300` | **`#AEAEAE`** | 174, 174, 174 | Bordes, divisores, líneas |
| `--color-gray-400` | **`#F7F7F7`** | 247, 247, 247 | Fondo de secciones alternas, cards, inputs |

---

## 🌑 Fondos y overlays especiales

| Color | HEX | Notas |
|---|---|---|
| Fondo principal | `#FFFFFF` | `--background` |
| Foreground (texto) | `#424242` | `--foreground` |
| Overlay oscuro translúcido | `#424242D9` (85% opacidad) | Texto sobre imágenes, modales |
| Overlay gris muy claro | `#AEAEAE1A` (10% opacidad) | Highlights sutiles sobre gris claro |
| Overlay blanco translúcido | `#FFFFFFE5` (90% opacidad) | Cards sobre imágenes |

---

## 🖌 Colores por área académica (auxiliares — NO oficiales)

Estos NO son colores oficiales del ITSE pero se usan como convención útil para diferenciar áreas en flyers, dashboards y reportes:

| Área académica | Color | HEX | Justificación |
|---|---|---|---|
| **Innovación Digital** | Azul institucional | `#225082` | Tecnología, software, datos |
| **Tecnología Industrial** | Gris carbón fuerte | `#424242` | Industria, acero, maquinaria |
| **Hospitalidad y Turismo** | Verde institucional | `#9EBE43` | Naturaleza, gastronomía, servicio |
| **Negocios** | Dorado | `#FFB000` | Lujo, valor, ejecutividad |

⚠️ Si el material es para una sola área, usa solo el color del ITSE (dorado/gris). Los colores por área son solo para piezas que necesitan diferenciar entre varias.

---

## 🧪 Combinaciones aprobadas (contrastadas WCAG AA)

| Combinación | Contraste | Uso OK |
|---|---|---|
| `#FFB000` sobre `#FFFFFF` | 2.4:1 | ⚠️ Solo para texto grande (≥18px) y elementos gráficos |
| `#424242` sobre `#FFFFFF` | 9.7:1 | ✅ Texto normal y grande |
| `#FFFFFF` sobre `#424242` | 9.7:1 | ✅ Texto sobre fondos oscuros |
| `#FFFFFF` sobre `#FFB000` | 2.4:1 | ⚠️ Solo para texto grande (≥18px), títulos bold |
| `#225082` sobre `#FFFFFF` | 8.9:1 | ✅ Texto sobre fondo blanco |
| `#AEAEAE` sobre `#FFFFFF` | 2.1:1 | ❌ NO usar para texto (solo bordes) |

**Regla práctica:** Si el texto es menor a 18px, usa SIEMPRE `#424242` sobre blanco. El dorado y el blanco son para acentos y texto grande (≥18px o bold ≥14px).

---

## 🎨 Cómo aplicar la paleta a tu material

### 1. Fondo

```css
body {
  background-color: #FFFFFF;
}

.section-alt {
  background-color: #F7F7F7;
}

.section-dark {
  background-color: #424242;
  color: #FFFFFF;
}
```

### 2. Texto

```css
h1, h2, h3 {
  color: #424242;
}

p {
  color: #424242;
}

.text-muted {
  color: #7B7B7B;
}
```

### 3. Acentos (botones, líneas, iconos)

```css
.btn-primary {
  background: linear-gradient(135deg, #FFCE00 0%, #FFB000 100%);
  color: #FFFFFF;
  border: none;
  border-radius: 8px;
}

.btn-primary:hover {
  background: #FFB000;
}

.accent-line {
  width: 60px;
  height: 4px;
  background: #FFB000;
  border-radius: 2px;
}
```

### 4. Cards

```css
.card {
  background: #FFFFFF;
  border: 1px solid #AEAEAE;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  padding: 24px;
}

.card-highlight {
  border-top: 4px solid #FFB000;
}
```

---

## 📋 Cheatsheet imprimible

```
ITSE BRAND COLORS
=================
PRIMARY:
  #FFB000  ████  Dorado (uso principal)
  #424242  ████  Gris Carbón (texto)
  #FFFFFF  ████  Blanco (fondo)

SECONDARY:
  #FFCE00  ████  Dorado claro
  #FFBC00  ████  Dorado medio
  #225082  ████  Azul
  #9EBE43  ████  Verde
  #CD2E26  ████  Rojo

GRAYS:
  #7B7B7B  ████  Texto secundario
  #9D9D9C  ████  Texto deshabilitado
  #AEAEAE  ████  Bordes
  #F7F7F7  ████  Fondo alterno

GRADIENT:
  135deg #FFCE00 → #FFB000
```

---

## 🔗 Referencias oficiales

- Sitio web: https://www.itse.ac.pa/
- CSS extraído de: `https://www.itse.ac.pa/themes/custom/itse_theme/dist/css/styles.css`
- Última verificación: junio 2026
