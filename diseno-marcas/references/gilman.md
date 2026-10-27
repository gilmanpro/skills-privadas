# gilman.pro — Gilberto Castillo

## Identidad
- **Marca**: gilman.pro — Gilberto Castillo, Ingeniero en Telecomunicaciones | Especialista en Big Data y Data Science
- **Estilo**: Tech-corporate, circuito impreso, dual light/dark
- **Logo**: "Circuit G" — letra G estilizada como trazo de circuito PCB
- **Gradiente de marca**: Emerald `#10B981` → Cyan `#06B6D4` (diagonal)

## Colores — Modo Claro
| Token | HEX | Uso |
|-------|-----|-----|
| Primary | `#10B981` (emerald-500) | Botones, enlaces, acentos |
| Primary hover | `#059669` (emerald-600) | Hover |
| Secondary | `#2563EB` (blue-600) | Acentos secundarios |
| Accent | `#22D3EE` (cyan-400) | Decoración |
| Navbar/Footer | `#1E293B` (slate-800) | Header, footer |
| BG | `#FFFFFF` | Fondo principal |
| BG alterno | `#F8FAFC` (slate-50) | Secciones alternas |
| Text | `#111827` (gray-900) | Texto principal |
| Text secondary | `#6B7280` (gray-500) | Texto secundario |
| Border | `#E5E7EB` (gray-200) | Bordes |
| Card border | `#F3F4F6` (gray-100) | Borde de cards |

## Colores — Modo Oscuro
| Token | HEX | Uso |
|-------|-----|-----|
| Primary | `#6366F1` (indigo-500) | Botones, enlaces |
| Primary hover | `#4F46E5` (indigo-600) | Hover |
| Accent | `#8B5CF6` (violet-500) | Decoración |
| Accent hover | `#22D3EE` (cyan-400) | Hover decoración |
| BG | `#0F172A` (slate-900) | Fondo |
| BG alterno | `#1E293B` (slate-800) | Secciones alternas |
| Card bg | `rgba(30,41,59,0.8)` | Fondo de cards |
| Text | `#FFFFFF` | Texto principal |
| Text secondary | `#94A3B8` (slate-400) | Texto secundario |
| Border | `rgba(255,255,255,0.05)` | Bordes |
| Card border | `rgba(255,255,255,0.1)` | Borde de cards |

**Si el formato soporta tema oscuro, expón ambos. Si no, usa claro como base con header/footer oscuro.**

## Tipografía
| Familia | Rol | Pesos | Uso |
|---------|-----|-------|-----|
| **Montserrat** | heading | 400-800 | Títulos (H1-H4), navbar |
| **Lato** | body | 300, 400, 700 | Párrafos, descripciones |
| **Orbitron** | display | 400-900 | Números grandes, hero |
| **Rajdhani** | tech | 300-700 | Wordmark "gilman.pro", labels técnicas |

**Reglas**: Títulos Montserrat 700-800 ≥30px / Subtítulos Montserrat 600 20-24px / Cuerpo Lato 400 16px / Wordmark "gilman.pro" SIEMPRE Rajdhani 700 emerald.

## Firma visual (separador decorativo bajo H2)
```html
<span class="h-px w-10 bg-emerald-500 dark:bg-indigo-500"></span>
<span class="mx-2 w-2 h-2 rounded-full bg-emerald-500 dark:bg-indigo-500"></span>
<span class="h-px w-16 bg-emerald-500 dark:bg-indigo-500"></span>
<span class="mx-2 w-2 h-2 rounded-full bg-emerald-500 dark:bg-violet-500"></span>
<span class="h-px w-10 bg-emerald-500 dark:bg-violet-500"></span>
```

## Logo
- Claro: `assets/logo_gilmanpro.svg` (gradiente emerald→cyan)
- Oscuro: `assets/logo_gilmanpro-dark.svg` (cyan→white)
- Mono: `assets/logo_gilmanpro-mono.svg` (una tinta)
- Tamaño mínimo: 100×40px digital / 25×10mm impreso
- NUNCA deformar, rotar ni cambiar paleta del gradiente

## Patrones de diseño
- **Botón primary**: bg emerald-600 (dark: indigo-600), text white, rounded-lg, px-6 py-3, shadow-lg
- **Botón outline**: border-2 emerald-600, text emerald-600
- **Cards**: bg gray-50 (dark: slate-800/80), rounded-xl, p-5, border gray-100, hover border-emerald-300
- **Inputs**: rounded-xl, border gray-200, focus ring-emerald-500
- **Navbar**: fixed top, bg slate-800 (dark: slate-900/80), backdrop-blur
- **Footer**: bg slate-800, 3 columnas (marca, enlaces, social)
- **Hero**: min-h-screen, bg emerald-500 (dark: indigo-600), foto circular border-4 white
- **Animaciones**: fade-in 0.6s, transition-all 200-300ms, nunca más de 0.6s

## Anti-patrones
- ❌ Negro puro `#000000` → usar slate-900 o gray-900
- ❌ Blanco puro `#FFFFFF` para texto → usar slate-100/gray-100
- ❌ Texto blanco sobre emerald-500 sin overlay
- ❌ border-radius 0 o 9999px → usar lg(8px)/xl(12px)/2xl(16px)
- ❌ Animaciones >0.6s
- ❌ bg-blue-500 → usar blue-600 mínimo