# MiBus — Transporte Masivo de Panamá

## Identidad
- **Marca**: MiBus (Transporte Masivo de Panamá)
- **Web**: https://www.mibus.com.pa
- **Autor**: Gilberto Castillo — Analista de Programación, Código 13138
- **Estilo**: Corporativo institucional moderno, light mode con header/footer dark

## Colores
| Token | HEX | Uso |
|-------|-----|-----|
| Primary (`--mibus-primary`) | `#283C90` | Títulos, headings, identidad |
| Secondary (`--mibus-secondary`) | `#205CA7` | Botones, CTAs, enlaces activos |
| Secondary hover | `#409EFF` | Hover de botones |
| Accent (`--mibus-accent`) | `#1DA1F2` | Acentos, links destacados |
| Dark (`--mibus-dark`) | `#1A1A2E` | Header, footer |
| Success | `#B5D331` | Acento secundario (iconos scroll-top) |
| Error | `#BC0C06` | Mensajes de error |
| Text | `#333333` | Texto principal |
| Border | `#E0E0E0` | Bordes, separadores |
| BG | `#FFFFFF` | Fondo del contenido |

**Regla 60-30-10**: 60% blanco + 30% azul + 10% acento.

## Colores — Modo Oscuro
| Token | HEX | Uso |
|-------|-----|-----|
| Primary | `#4A7FD4` (azul claro) | Botones, enlaces, acentos en fondo oscuro |
| Primary hover | `#6B9FEF` | Hover |
| Secondary | `#205CA7` | Mantener coherencia de marca |
| Accent | `#1DA1F2` | Acentos decorativos |
| Dark | `#1A1A2E` | Header/footer (se mantiene) |
| BG | `#0F172A` (slate-900) | Fondo principal |
| BG alterno | `#1E293B` (slate-800) | Secciones alternas |
| Card bg | `rgba(30,41,59,0.8)` | Fondo de cards con glassmorphism |
| Text | `#F1F5F9` (slate-100) | Texto principal |
| Text secondary | `#94A3B8` (slate-400) | Texto secundario |
| Border | `rgba(255,255,255,0.08)` | Bordes sutiles |
| Success | `#B5D331` | Acentos positivos |

**Regla dark**: usar `#4A7FD4` para texto sobre fondo oscuro (mejor contraste que `#283C90`).

## Tipografía
- **Títulos**: Poppins (weights 600, 700, 900)
- **Cuerpo**: Roboto (weights 300, 400, 500, 700)
- **Import**: `https://fonts.googleapis.com/css?family=Roboto:300,400,500,600,700%7CPoppins:100,600,700,900&display=swap`
- **H1**: Poppins 700, 28-40px; **H2**: Poppins 600, 22-28px; **H3**: Poppins 600, 18-22px
- **Body**: Roboto 400, 14-16px; **Caption**: Roboto 400, 10-12px

## Logo
- Header: `https://www.mibus.com.pa/wp-content/uploads/2019/03/logo-1.png`
- Retina: `https://www.mibus.com.pa/wp-content/uploads/2020/05/retina-logo.png`
- Favicon: `https://www.mibus.com.pa/wp-content/uploads/2020/05/favicon.png`
- **Posición**: arriba-izquierda o centrado en portada
- **Tamaño mínimo**: 120px web / 1.5cm impreso
- **No deformar**, mantener proporción original

## Botones
- **Primary**: bg `#205CA7`, text white, border-radius 4px, hover `#409EFF`
- **Outline**: border `#205CA7` 2px, text `#205CA7`, hover invierte colores

## Textos corporativos
- **Stats reales**: 1,436 unidades, +4,000 trabajadores, 152 rutas, 450,000 pasajeros/día
- **CTAs**: "SUSCRIBIRSE", "Conocer más", "Trabajadores", "Ver rutas", "Contáctenos"
- **Secciones**: "NOTICIAS", "Rutas", "Nosotros", "Conoce tu Bus", "Servicio al Cliente"
- **Copyright**: "MiBus TODOS LOS DERECHOS RESERVADOS © 2019. PANAMÁ, REP. DE PANAMÁ."

## Errores comunes
- ❌ Texto blanco sobre fondo claro → solo sobre fondos azules oscuros
- ❌ Mezclar Arial con Poppins → Poppins títulos, Roboto body
- ❌ Botón rojo/verde → siempre azul `#205CA7`
- ❌ Header blanco → azul oscuro `#283C90` o negro `#1A1A2E`
- ❌ Degradados multicolor → solo primary → secondary
- ❌ Usar `#283C90` como texto en modo oscuro → usar `#4A7FD4` para mejor contraste