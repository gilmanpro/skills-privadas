# Electrocontrol / IoT Tech — Malkom Córdoba

## Identidad
- **Empresa**: IoT Tech (Electrocontrol Panamá)
- **Fundador**: Malkom Daniel Córdoba — Especialista en Mecatrónica & Electrónica Automotriz
- **Web**: http://pag.electrocontrol.cloud/
- **Tagline**: "Innovación IoT & Tecnología Automotriz"
- **Estilo**: Dark mode + degradados vibrantes cyan→purple→pink + glassmorphism + futurismo tecnológico
- **País**: Panamá 🇵🇦 — +10 años — 200+ proyectos — +507 6250-9318

## 4 servicios + colores asociados
| Servicio | Gradiente |
|----------|-----------|
| IoT & Desarrollo Tecnológico | `#06B6D4 → #3B82F6` (cyan→blue) |
| Reparación de ECU Automotriz | `#F97316 → #EF4444` (orange→red) |
| Automatización Industrial | `#22C55E → #10B981` (green→emerald) |
| Programación Innovadora | `#A855F7 → #EC4899` (purple→pink) |

## Colores
| Token | HEX | Uso |
|-------|-----|-----|
| Slate 900 (bg) | `#0F172A` | Fondo principal |
| Slate 800 (bg alt) | `#1E293B` | Secciones alternas, cards grandes |
| Slate 950 (footer) | `#020617` | Footer, fondo más profundo |
| Cyan 500 (primary) | `#06B6D4` | Botones, iconos IoT, links |
| Purple 500 (secondary) | `#A855F7` | Acentos, servicio Programación |
| Pink 500 (tertiary) | `#EC4899` | Highlights, degradados finales |
| Slate 300 (text) | `#CBD5E1` | Párrafos, descripciones |
| Slate 400 (text sec) | `#94A3B8` | Labels, captions |
| Verde WhatsApp | `#10B981` | Botón flotante WhatsApp |
| Amarillo award | `#FDE047` | Iconos de logros, experiencia |

## Degradados signature (NO CAMBIAR)
```css
/* Hero principal (3 colores) */
gradient: to right, #22D3EE, #C084FC, #F472B6
/* Botones / iconos grandes */
gradient: to right, #06B6D4, #A855F7
/* Fondo body */
gradient: to bottom right, #0F172A, #1E293B, #0F172A
```
**Regla**: 1-2 degradados por slide máximo. Solo el hero principal usa los 3 colores.

## Tipografía
- **Familia**: `Inter, "Geist", system-ui, -apple-system, sans-serif`
- **Pesos**: 400 (regular), 500 (medium), 600 (semibold), 700 (bold)
- **H1 hero**: 48-72px bold / **H2**: 36-48px bold / **H3**: 24-30px bold
- **Body**: 16px normal / **Small**: 14px / **Caption**: 12px
- **Siempre antialiased** (`-webkit-font-smoothing: antialiased`)

## Logo
- Archivo: `assets/logo-electrocontrol.jpg` (descargado del sitio, 150×150 aprox.)
- Se recomienda convertir a PNG transparente (usar remove.bg) o vectorizar a SVG

## Reglas específicas
1. **MODO DARK SIEMPRE**. Sin fondos blancos (excepto documentos impresos si el cliente lo exige)
2. **Glassmorphism**: cards con bg semitransparente (`bg-slate-800/50`) + backdrop-blur
3. **Esquinas redondeadas generosas**: `rounded-2xl` (16-24px) — NO esquinas rectas
4. **Iconos Lucide siempre**: stroke 2px. w-4 (small), w-6 (medium), w-8 (hero)
5. **Cifras grandes** en text-3xl font-bold cyan-400 o blanco
6. **Sombras con tinte cyan**: `shadow-cyan-500/25` (no sombras negras genéricas)
7. **Botón flotante WhatsApp**: siempre en landing, verde `#10B981`, enlace `https://wa.me/50762509318`
8. **Espaciado**: py-24 entre secciones, px-6 mínimo, gap-8/12 entre elementos
9. **Usar datos reales de branding**: NO inventar años, proyectos o experiencia

## Pilares de valor
- Diagnóstico especializado — Garantía en servicios — Soporte técnico continuo — Soluciones personalizadas

## Tecnologías clave
- **IoT**: MQTT, WiFi, LoRa, Zigbee, sensores, dashboards
- **Automotriz**: ECU, inyección electrónica, transmisión, inmovilizadores, codificación
- **Automatización**: PLC (Siemens, Allen-Bradley, Mitsubishi, Omron), HMI, SCADA
- **Software**: React, Node.js, Python, Go, REST APIs, sistemas embebidos

## Estructura visual típica
1. Hero (fondo slate-900→800, logo grande, título con degradado cyan→purple→pink)
2. Sobre Mí (foto circular borde cyan + 4 stat cards)
3. Servicios (4 bloques alternados imagen+texto)
4. Contacto (3 cards info + formulario dark)
5. Footer (slate-950, 4 columnas)
6. WhatsApp flotante (botón fijo bottom-right, verde)