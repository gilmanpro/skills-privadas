---
name: diseno-marcas
description: "Aplica la identidad visual de las marcas MiBus, ITSE, gilman.pro y Electrocontrol (colores, tipografia, logos y tono) a cualquier pieza de diseno. Usar SIEMPRE que el usuario mencione alguna de estas marcas o pida material grafico con su identidad (web, banners, presentaciones, documentos), aunque no diga 'marca' o 'identidad'."
---

# Sistemas de Diseño Corporativos

Detecta la marca del contexto y aplica su identidad visual en entregables digitales.

## Cuándo usar

- Aplicar identidad visual de marcas corporativas (MiBus, ITSE, gilman.pro, Electrocontrol)
- Crear documentos, presentaciones o sitios web con colores y tipografía oficiales
- Generar logos o assets gráficos siguiendo guías de marca
- Implementar modo oscuro con colores oficiales

## Modo oscuro

Todas las marcas soportan modo oscuro. Si el formato lo permite, expón ambos temas con CSS variables o `prefers-color-scheme`.

| Marca | Estrategia dark |
|---|---|
| MiBus | Header/footer `#1A1A2E`; dark completo: bg `#0F172A`, text `#F1F5F9`, primary `#4A7FD4` |
| ITSE | Light por defecto; dark: bg `#121212`, text `#F5F5F5`, dorado `#FFD54F` |
| gilman.pro | Dual nativo; ver tabla en `references/gilman.md` |
| Electrocontrol | Dark-first siempre |

## Detector de marca

| Marca | Señales de activación | Diseño rápido | Assets | Referencias |
|---|---|---|---|---|
| MiBus | MiBus, Transporte Masivo, mibus.com.pa | `references/mibus.md` | `assets/brand-mibus.json`, `assets/colors-mibus.md`, `assets/logo-urls-mibus.md` | `references/mibus/` |
| ITSE | ITSE, Instituto Técnico Superior Especializado, itse.ac.pa | `references/itse.md` | `assets/logo-itse-*.png` | `references/itse/` |
| gilman.pro | gilman, Gilberto Castillo, perfil.gilman.pro | `references/gilman.md` | `assets/logo_gilmanpro*.svg`, `assets/palette-gilman.json` | `references/gilman/` |
| Electrocontrol | Electrocontrol, IoT Tech, pag.electrocontrol.cloud | `references/electrocontrol.md` | `assets/logo-electrocontrol.jpg` | `references/electrocontrol/` |

## Flujo de uso

1. Identifica la marca con el detector.
2. Lee `references/{marca}.md` para colores, tipografía y reglas.
3. Si necesitas más detalle, lee `references/{marca}/`.
4. Según el formato, busca la guía específica en `references/{marca}/` (pptx, docx, xlsx, web, pdf, svg, redes).
5. Carga skills complementarias según formato: `@ofimatica` (docx/pptx/pdf/xlsx/md), `@dev-stack` (UI web y UX; absorbe frontend-design y ui-ux-pro-max), `@graphic-media`, etc.

## Reglas universales

- Esquinas redondeadas: 8-16px (MiBus: 1-4px).
- Iconos: Lucide o Heroicons outline, stroke 2px, color primary.
- Logo con padding mínimo del alto del logo; no deformar.
- No inventes colores; genera variantes oscureciendo/aclarando el primary.
- Espaciado generoso: py-16/24 entre secciones, gap-6/8 entre elementos.
- Modo oscuro con colores oficiales; nunca inviertas manualmente.
