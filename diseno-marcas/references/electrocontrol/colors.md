# Paleta de Colores Oficial — Electrocontrol / IoT Tech

Extraído directamente del CSS de Tailwind del sitio oficial (http://pag.electrocontrol.cloud/) en junio 2026. Estos valores son la fuente única de verdad para cualquier material de Electrocontrol.

---

## 🎨 Colores primarios (modo dark)

La marca usa **SIEMPRE modo dark** como base. El fondo principal es slate-900 con acentos vibrantes cyan/purple/pink.

| Token | HEX | RGB | Nombre humano | Uso |
|---|---|---|---|---|
| `--bg-primary` | **`#0F172A`** | 15, 23, 42 | **Slate 900** | Fondo principal, hero, páginas |
| `--bg-secondary` | **`#1E293B`** | 30, 41, 59 | **Slate 800** | Secciones alternas, cards grandes, inputs |
| `--bg-tertiary` | **`#020617`** | 2, 6, 23 | **Slate 950** | Footer, fondo más profundo |
| `--accent-primary` | **`#06B6D4`** | 6, 182, 212 | **Cyan 500** | Botones, iconos, links, acentos principales |
| `--accent-secondary` | **`#A855F7`** | 168, 85, 247 | **Purple 500** | Acentos secundarios, degradados |
| `--accent-tertiary` | **`#EC4899`** | 236, 72, 153 | **Pink 500** | Highlights, degradados finales |
| `--text-primary` | **`#FFFFFF`** | 255, 255, 255 | **Blanco** | Títulos principales, contraste máximo |

**Regla 50-30-15-5:**
- 50% slate-900 (fondo)
- 30% slate-800 (cards, secciones alternas)
- 15% cyan-500 + purple-500 (acentos)
- 5% pink-500 (highlights especiales)

---

## 🌟 Acentos brillantes (variantes 400 para texto)

Las variantes 400 se usan en texto e iconos sobre fondo dark porque tienen mejor contraste:

| Token | HEX | RGB | Uso |
|---|---|---|---|
| `--cyan-400` | **`#22D3EE`** | 34, 211, 238 | Texto destacado, headings con degradado, iconos |
| `--purple-400` | **`#C084FC`** | 192, 132, 252 | Texto destacado alternativo |
| `--pink-400` | **`#F472B6`** | 244, 114, 182 | Texto destacado para énfasis |
| `--blue-500` | **`#3B82F6`** | 59, 130, 246 | Degradados con cyan (servicio IoT) |
| `--blue-400` | **`#60A5FA`** | 96, 165, 250 | Variante clara del azul |

---

## ✍️ Escala de grises para texto sobre dark

| Token | HEX | RGB | Uso |
|---|---|---|---|
| `--text-body` | **`#CBD5E1`** | 203, 213, 225 | **Slate 300** — Texto principal (párrafos, descripciones) |
| `--text-secondary` | **`#94A3B8`** | 148, 163, 184 | **Slate 400** — Texto secundario (labels, captions) |
| `--text-muted` | **`#64748B`** | 100, 116, 139 | **Slate 500** — Texto deshabilitado, metadatos, copyright |
| `--border-default` | **`#334155`** | 51, 65, 85 | **Slate 700** — Bordes sutiles |
| `--border-strong` | **`#1E293B`** | 30, 41, 59 | **Slate 800** — Bordes más fuertes, separadores |

---

## 🎯 Colores por servicio (paleta extendida)

Cada servicio tiene su propio gradiente signature que se usa en su card, icono y headings:

| Servicio | Token | HEX 1 | HEX 2 | CSS class Tailwind |
|---|---|---|---|---|
| **IoT & Desarrollo Tecnológico** | `--svc-iot` | `#06B6D4` cyan-500 | `#3B82F6` blue-500 | `from-cyan-500 to-blue-500` |
| **Reparación de ECU Automotriz** | `--svc-ecu` | `#F97316` orange-500 | `#EF4444` red-500 | `from-orange-500 to-red-500` |
| **Automatización Industrial** | `--svc-auto` | `#22C55E` green-500 | `#10B981` emerald-500 | `from-green-500 to-emerald-500` |
| **Programación Innovadora** | `--svc-code` | `#A855F7` purple-500 | `#EC4899` pink-500 | `from-purple-500 to-pink-500` |

**Regla:** Usa el gradiente del servicio correspondiente SOLO en ese servicio. No mezcles gradientes entre servicios.

---

## ✅ Colores de estado / acentos especiales

| Token | HEX | RGB | Uso |
|---|---|---|---|
| `--whatsapp` | **`#10B981`** | 16, 185, 129 | **Verde WhatsApp** — botón flotante, confirmaciones |
| `--award` | **`#FDE047`** | 253, 224, 71 | **Yellow 400** — Iconos de experiencia/logros |
| `--check` | **`#22D3EE`** | 34, 211, 238 | Cyan 400 — Iconos de check en listas de features |
| `--error` | **`#EF4444`** | 239, 68, 68 | Red 500 — Errores |
| `--warning` | **`#F59E0B`** | 245, 158, 11 | Amber 500 — Advertencias |
| `--success` | **`#10B981`** | 16, 185, 129 | Emerald 500 — Éxito |

---

## 🌑 Fondos translúcidos (glassmorphism)

El estilo glassmorphism sutil se logra con fondos semitransparentes sobre slate-800/900:

| Token | HEX (con alpha) | Uso |
|---|---|---|
| `bg-slate-800/50` | `#1E293B80` (50%) | Cards de servicios, paneles |
| `bg-slate-700/50` | `#33415580` (50%) | Stat cards, items pequeños |
| `bg-slate-800/30` | `#1E293B4D` (30%) | Overlays muy sutiles |
| `bg-slate-900/50` | `#0F172A80` (50%) | Overlays de fondo con blur |
| `border-slate-700/50` | `#33415580` (50%) | Bordes de cards glassmorphism |
| `border-slate-800` | `#1E293B` (100%) | Bordes de footer, separadores |

---

## 🎨 Degradados Signature (LA FIRMA VISUAL)

### 1. Gradiente de texto principal (headings hero)

```css
background: linear-gradient(to right, #22D3EE 0%, #C084FC 50%, #F472B6 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
```

**Equivalente Tailwind:** `bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-400 bg-clip-text text-transparent`

**Uso:** Hero principal H1, títulos de sección principales (H2). Máximo 2 veces por página.

### 2. Gradiente cyan → purple (botones y iconos)

```css
background: linear-gradient(to right, #06B6D4 0%, #A855F7 100%);
```

**Equivalente Tailwind:** `bg-gradient-to-r from-cyan-500 to-purple-500`

**Uso:** Botones primarios, iconos grandes en cards, badges de perfil. El más usado.

### 3. Gradiente de fondo (body principal)

```css
background: linear-gradient(to bottom right, #0F172A 0%, #1E293B 50%, #0F172A 100%);
```

**Equivalente Tailwind:** `bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900`

**Uso:** Background del `<body>`, secciones hero grandes.

### 4. Gradiente del servicio IoT

```css
background: linear-gradient(to bottom right, #06B6D4 0%, #3B82F6 100%);
```

**Tailwind:** `bg-gradient-to-br from-cyan-500 to-blue-500`

**Uso:** Icono de card del servicio IoT, overlay de imagen del servicio IoT.

### 5. Gradiente del servicio ECU

```css
background: linear-gradient(to bottom right, #F97316 0%, #EF4444 100%);
```

**Tailwind:** `bg-gradient-to-br from-orange-500 to-red-500`

**Uso:** Icono de card del servicio ECU, overlay de imagen del servicio ECU.

### 6. Gradiente de Automatización Industrial

```css
background: linear-gradient(to bottom right, #22C55E 0%, #10B981 100%);
```

**Tailwind:** `bg-gradient-to-br from-green-500 to-emerald-500`

**Uso:** Icono de card del servicio Automatización Industrial.

### 7. Gradiente de Programación

```css
background: linear-gradient(to bottom right, #A855F7 0%, #EC4899 100%);
```

**Tailwind:** `bg-gradient-to-br from-purple-500 to-pink-500`

**Uso:** Icono de card del servicio Programación.

---

## 🔮 Blobs decorativos (efectos blur de fondo)

Los blobs son círculos grandes con `blur-3xl` y opacidad baja que dan profundidad al fondo:

```css
.blob {
  position: absolute;
  width: 24rem;  /* w-96 */
  height: 24rem; /* h-96 */
  border-radius: 9999px;
  filter: blur(64px);  /* blur-3xl */
  animation: pulse-slow 4s ease-in-out infinite;
}

.blob-cyan {
  background: rgba(6, 182, 212, 0.10);  /* bg-cyan-500/10 */
}

.blob-purple {
  background: rgba(168, 85, 247, 0.10);  /* bg-purple-500/10 */
}
```

**Tailwind:** `absolute w-96 h-96 rounded-full blur-3xl animate-pulse-slow bg-cyan-500/10`

**Posición típica:**
- Cyan blob: `top-1/4 left-1/4`
- Purple blob: `bottom-1/4 right-1/4`

**Uso:** En el hero y secciones de servicios para dar profundidad.

---

## 🧪 Combinaciones aprobadas (contrastadas WCAG AA sobre dark)

| Combinación | Contraste aprox. | Uso OK |
|---|---|---|
| `#FFFFFF` sobre `#0F172A` | 18.7:1 | ✅ Texto normal y grande (máxima legibilidad) |
| `#CBD5E1` slate-300 sobre `#0F172A` | 13.2:1 | ✅ Texto principal (párrafos) |
| `#94A3B8` slate-400 sobre `#0F172A` | 8.9:1 | ✅ Texto secundario (labels) |
| `#22D3EE` cyan-400 sobre `#0F172A` | 11.8:1 | ✅ Texto destacado, headings |
| `#C084FC` purple-400 sobre `#0F172A` | 7.5:1 | ✅ Texto destacado |
| `#F472B6` pink-400 sobre `#0F172A` | 6.8:1 | ✅ Texto destacado |
| `#06B6D4` cyan-500 sobre `#0F172A` | 7.4:1 | ✅ Iconos, acentos, texto bold |
| `#64748B` slate-500 sobre `#0F172A` | 4.0:1 | ⚠️ Solo para texto ≥18px o captions no críticos |
| `#FFFFFF` sobre `#06B6D4` | 2.7:1 | ⚠️ Solo para texto bold grande (botones) |
| `#FFFFFF` sobre `#A855F7` | 3.0:1 | ⚠️ Solo para texto bold grande (botones) |

**Regla práctica:** Sobre fondo dark, cualquier texto slate-300+ es legible. Los colores de acento (cyan/purple/pink) en sus variantes 400 son seguros para texto. Las variantes 500 son para iconos y acentos.

---

## 🖌 Cómo aplicar la paleta a tu material

### 1. Fondo (casi todos los formatos)

```css
body {
  background: linear-gradient(to bottom right, #0F172A, #1E293B, #0F172A);
  color: #FFFFFF;
}

.section-alt {
  background-color: #1E293B;  /* slate-800 */
}

.footer {
  background-color: #020617;  /* slate-950 */
  border-top: 1px solid #1E293B;
}
```

### 2. Texto

```css
h1, h2, h3 {
  color: #FFFFFF;
}

.heading-gradient {
  background: linear-gradient(to right, #22D3EE, #C084FC, #F472B6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

p {
  color: #CBD5E1;  /* slate-300 */
}

.text-muted {
  color: #94A3B8;  /* slate-400 */
}

.text-disabled {
  color: #64748B;  /* slate-500 */
}
```

### 3. Acentos (botones, iconos, líneas)

```css
.btn-primary {
  background: linear-gradient(to right, #06B6D4, #A855F7);
  color: #FFFFFF;
  border: none;
  border-radius: 1rem;  /* rounded-2xl */
  box-shadow: 0 10px 30px rgba(6, 182, 212, 0.25);  /* shadow-cyan-500/25 */
  transition: all 0.3s;
}

.btn-primary:hover {
  box-shadow: 0 15px 40px rgba(6, 182, 212, 0.5);  /* shadow-cyan-500/50 */
  transform: translateY(-2px);
}

.accent-line {
  width: 60px;
  height: 4px;
  background: linear-gradient(to right, #06B6D4, #A855F7);
  border-radius: 2px;
}
```

### 4. Cards glassmorphism

```css
.card {
  background: rgba(30, 41, 59, 0.5);  /* bg-slate-800/50 */
  border: 1px solid rgba(51, 65, 85, 0.5);  /* border-slate-700/50 */
  border-radius: 1rem;  /* rounded-2xl */
  padding: 1.5rem;
  backdrop-filter: blur(12px);
}

.card-stat {
  background: rgba(51, 65, 85, 0.5);  /* bg-slate-700/50 */
  border-radius: 0.75rem;  /* rounded-xl */
  padding: 1rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
```

### 5. Inputs (formularios)

```css
.input {
  width: 100%;
  padding: 0.75rem 1rem;
  background: rgba(30, 41, 59, 0.5);  /* bg-slate-800/50 */
  border: 1px solid rgba(51, 65, 85, 0.5);  /* border-slate-700/50 */
  border-radius: 0.75rem;  /* rounded-xl */
  color: #FFFFFF;
  transition: border-color 0.2s;
}

.input:focus {
  outline: none;
  border-color: #06B6D4;  /* cyan-500 */
}
```

---

## 📋 Cheatsheet imprimible

```
ELECTROCONTROL BRAND COLORS
============================
BACKGROUNDS (siempre dark):
  #0F172A  ████  Slate 900  (fondo principal)
  #1E293B  ████  Slate 800  (secciones alternas)
  #020617  ████  Slate 950  (footer)

ACENTOS PRINCIPALES:
  #06B6D4  ████  Cyan 500    (botones, iconos)
  #A855F7  ████  Purple 500  (degradados)
  #EC4899  ████  Pink 500    (highlights)

ACENTOS BRILLANTES (texto):
  #22D3EE  ████  Cyan 400
  #C084FC  ████  Purple 400
  #F472B6  ████  Pink 400

SERVICIOS:
  IoT:            #06B6D4 → #3B82F6
  ECU:            #F97316 → #EF4444
  Automatización: #22C55E → #10B981
  Programación:   #A855F7 → #EC4899

TEXTO:
  #FFFFFF  ████  Títulos
  #CBD5E1  ████  Texto principal (párrafos)
  #94A3B8  ████  Texto secundario
  #64748B  ████  Texto deshabilitado

ESPECIAL:
  #10B981  ████  WhatsApp
  #FDE047  ████  Awards / experiencia

GRADIENTES SIGNATURE:
  Texto:    90deg  cyan-400 → purple-400 → pink-400
  Botones:  90deg  cyan-500 → purple-500
  Body:     135deg slate-900 → slate-800 → slate-900
```

---

## 🔗 Referencias oficiales

- Sitio web: http://pag.electrocontrol.cloud/
- CSS extraído de: `/_next/static/css/6ef3bf974eb20736.css`
- Stack: Next.js + Tailwind CSS
- Última verificación: junio 2026
