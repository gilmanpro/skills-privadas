# Refero Styles — sistemas de diseño de productos reales (DESIGN.md legible por IA)

`https://styles.refero.design/` es una biblioteca de 2.000+ sistemas de diseño extraídos de sitios de productos reales (Notion, OpenAI, Figma, Raycast, Mercury, Wise...). Cada página de estilo está renderizada en servidor y trae un DESIGN.md completo, fetchable con `webfetch`/`curl` sin API keys: paleta de colores (hex + rol + token CSS/Tailwind), tipografía (escala real con weights/line-height/letter-spacing + fuente sustituta libre), spacing y forma (unidad base, radios por elemento, max-width, section gap), componentes con medidas exactas (botones, cards, pills), Do/Don't del sistema, superficies, elevación, imaginería, layout, "Similar Brands" y bloque Quick Start (CSS Custom Properties + Tailwind v4).

## Cuándo usarlo

- El usuario cita una referencia real ("hazlo como Notion/Stripe/Linear", "estilo Mercury") → busca ese estilo y usa sus tokens como base del design system.
- El usuario pide un acabado "profesional / de agencia" sin más detalle → explora categorías y elige un sistema coherente con el producto.
- Para aterrizar con medidas reales las recomendaciones de `py scripts/search.py --design-system`.

## Cómo encontrar un estilo (solo webfetch/curl; no hay API de búsqueda pública)

1. **Home**: `https://styles.refero.design/` — listas Trending/Popular/Newest (~40 estilos con nombre y enlace `/style/<uuid>`).
2. **Categorías curadas** (páginas server-rendered que listan estilos con nombre + UUID):

   | Categoría | URL |
   |---|---|
   | SaaS limpio | `/design-styles/clean-saas` |
   | Editorial | `/design-styles/editorial-websites` |
   | Dark mode | `/design-styles/dark-mode-websites` |
   | Fintech | `/design-styles/fintech-websites` |
   | Devtools | `/design-styles/devtools-websites` |
   | AI startups | `/design-styles/ai-startup-websites` |
   | E-commerce | `/design-styles/ecommerce-websites` |
   | Minimal | `/design-styles/minimal-websites` |
   | Agencias | `/design-styles/agency-websites` |
   | Productividad | `/design-styles/productivity-apps` |
   | Font pairings | `/design-styles/website-font-pairings` |

   (prefijo `https://styles.refero.design`)
3. **Página de estilo**: `https://styles.refero.design/style/<uuid>` — DESIGN.md completo + "More like this" + "Similar Brands": úsalos para saltar a la marca pedida o a alternativas cercanas.
4. **Sitemap** (1.300+ UUIDs sin nombre): `https://styles.refero.design/sitemaps/styles.xml` — solo para verificar que un UUID existe.
5. **Marca no encontrada** → fallback: `py scripts/search.py "<producto> <industria> <keywords>" --design-system` y usa la categoría Refero más cercana como inspiración.

## Qué extraer y cómo usarlo

- **Colores** → mapea a tokens semánticos del proyecto (primary/surface/accent/border) respetando los roles documentados (ej. Notion: "canvas #f6f5f4 y cards #ffffff — nunca invertir"; "#0075de solo para la acción primaria por pantalla").
- **Tipografía** → replica la escala (size/weight/line-height/tracking por rol). Las fuentes propietarias (NotionInter, Lyon Text) no se pueden cargar: usa la **Substitute** indicada (Inter, Source Serif Pro) vía Google Fonts.
- **Spacing/Shape** → unidad base, radios por elemento (cards/buttons/pills), max-width de página, section gap y card padding.
- **Componentes** → medidas exactas (padding, radius, color, tamaño de texto) como punto de partida; adáptalas al contenido del usuario.
- **Do/Don't** → adóptalos como reglas del proyecto: codifican la coherencia del sistema (ej. "sin sombras en cards, solo hairline borders", "sin gradientes").
- **Quick Start (CSS vars / Tailwind v4)** → base directa de tokens. Con Tailwind v3 CDN (stack de `frontend-design`), trasládalos a `tailwind.config = { theme: { extend: { colors: {...}, borderRadius: {...}, spacing: {...} } } }` dentro del `<script>` del CDN.

## Reglas de adaptación (importante)

- **Extrae el sistema, no clones el sitio**: nada de logos, nombres de marca, textos de marketing ni imágenes del producto original. Aplica tokens y proporciones al contenido del usuario.
- **Accesibilidad primero**: verifica contraste ≥4.5:1 en los pares que uses — Refero mide sitios reales que a veces incumplen WCAG; corrige, no heredes el fallo.
- **Marca del usuario manda**: si hay identidad definida (skill `diseno-marcas`), Refero solo aporta proporción/estructura, nunca colores ni tipografías.
- **Un estilo por proyecto**: no mezcles tokens de dos sistemas; si hace falta contraste, usa la jerarquía de superficies del propio estilo.

## Recursos complementarios

- `/ai-agents/design-md-examples`, `/ai-agents/design-prompts`, `/ai-agents/tailwind-design-tokens`, `/ai-agents/css-variables-design-tokens`, `/ai-agents/brand-matching-prompts`, `/ai-agents/agentic-ui-quality-checklist`
- Ejemplos por tipo de página: `/examples/pricing-page-design`, `/examples/dashboard-ui-design`, `/examples/api-documentation-websites`, `/examples/product-screenshot-heroes`
- MCP oficial (opcional, requiere configuración del usuario): `https://refero.design/mcp`
