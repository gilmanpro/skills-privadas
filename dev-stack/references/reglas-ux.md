# Referencia UX Completa — 225 Reglas en 10 Categorías

Reglas detalladas por categoría de prioridad. Para revisiones rápidas usa el Checklist Pre-Entrega de SKILL.md; esta referencia es la fuente completa. Complemento consultable: `py scripts/search.py "<keyword>" --domain ux` (base de datos web-céntrica de 99 reglas con ejemplos de código).

## Índice

1. [Accesibilidad (CRÍTICO)](#1-accesibilidad--crítico) — 14 reglas
2. [Táctil e Interacción (CRÍTICO)](#2-táctil-e-interacción--crítico) — 17 reglas
3. [Rendimiento (ALTO)](#3-rendimiento--alto) — 19 reglas
4. [Selección de Estilo (ALTO)](#4-selección-de-estilo--alto) — 13 reglas
5. [Layout y Responsive (ALTO)](#5-layout-y-responsive--alto) — 16 reglas
6. [Tipografía y Color (MEDIO)](#6-tipografía-y-color--medio) — 15 reglas
7. [Animación (MEDIO)](#7-animación--medio) — 24 reglas
8. [Formularios y Feedback (MEDIO)](#8-formularios-y-feedback--medio) — 31 reglas
9. [Patrones de Navegación (ALTO)](#9-patrones-de-navegación--alto) — 26 reglas
10. [Gráficos y Datos (BAJO)](#10-gráficos-y-datos--bajo) — 30 reglas
11. [Apéndice A: Reglas comunes para UI profesional (Apps)](#apéndice-a-reglas-comunes-para-ui-profesional-apps)
12. [Apéndice B: Checklist pre-entrega para Apps](#apéndice-b-checklist-pre-entrega-para-apps)

Fuentes entre paréntesis: Apple HIG (HIG), Material Design (MD), WCAG.

---

## 1. Accesibilidad — CRÍTICO

Anti-patrones clave: quitar anillos de foco; botones solo-icono sin etiqueta.

| ID | Regla | Fuente |
|----|-------|--------|
| `color-contrast` | Mínimo 4.5:1 para texto normal (texto grande 3:1) | MD, WCAG |
| `focus-states` | Anillos de foco visibles en elementos interactivos (2-4px) | HIG, MD |
| `alt-text` | Texto alt descriptivo para imágenes significativas | WCAG |
| `aria-labels` | aria-label para botones solo icono; accessibilityLabel en nativo | HIG |
| `keyboard-nav` | Orden de tabulación coincide con orden visual; soporte completo de teclado | HIG |
| `form-labels` | Usar label con atributo for | WCAG |
| `skip-links` | Saltar al contenido principal para usuarios de teclado | WCAG |
| `heading-hierarchy` | Jerarquía secuencial h1→h6, sin saltos de nivel | WCAG |
| `color-not-only` | No transmitir información solo por color (añadir icono/texto) | WCAG |
| `dynamic-type` | Soporte de escalado de texto del sistema; evitar truncamiento al crecer | HIG, MD |
| `reduced-motion` | Respetar prefers-reduced-motion; reducir/deshabilitar animaciones cuando se solicite | HIG, MD |
| `voiceover-sr` | accessibilityLabel/accessibilityHint con significado; orden de lectura lógico para VoiceOver/lectores de pantalla | HIG, MD |
| `escape-routes` | Proporcionar cancelar/atrás en modales y flujos multi-paso | HIG |
| `keyboard-shortcuts` | Preservar atajos del sistema y accesibilidad; ofrecer alternativas de teclado para drag-and-drop | HIG |

## 2. Táctil e Interacción — CRÍTICO

Anti-patrones clave: depender solo de hover; cambios de estado instantáneos (0ms).

| ID | Regla | Fuente |
|----|-------|--------|
| `touch-target-size` | Mín 44x44pt (Apple) / 48x48dp (Material); extender área de impacto si es necesario | HIG, MD |
| `touch-spacing` | Mínimo 8px/8dp de separación entre objetivos táctiles | HIG, MD |
| `hover-vs-tap` | Usar click/tap para interacciones principales; no depender solo de hover | — |
| `loading-buttons` | Deshabilitar botón durante operaciones asíncronas; mostrar spinner o progreso | MD |
| `error-feedback` | Mensajes de error claros cerca del problema | MD |
| `cursor-pointer` | Añadir cursor-pointer a elementos cliqueables (web) | — |
| `gesture-conflicts` | Evitar swipe horizontal en contenido principal; preferir scroll vertical | HIG |
| `tap-delay` | Usar touch-action: manipulation para reducir retardo de 300ms (web) | — |
| `standard-gestures` | Usar gestos estándar de plataforma consistentemente; no redefinir (swipe-back, pinch-zoom) | HIG |
| `system-gestures` | No bloquear gestos del sistema (Centro de Control, swipe atrás, etc.) | HIG |
| `press-feedback` | Feedback visual al presionar (ripple/resalte; capas de estado) | MD |
| `haptic-feedback` | Usar hápticos para confirmaciones y acciones importantes; evitar uso excesivo | HIG |
| `gesture-alternative` | No depender de interacciones solo-por-gesto; controles visibles para acciones críticas | HIG |
| `safe-area-awareness` | Mantener objetivos táctiles primarios alejados de notch, Dynamic Island, barra de gestos y bordes | HIG |
| `no-precision-required` | Evitar requerir toques de precisión en iconos pequeños o bordes finos | HIG |
| `swipe-clarity` | Acciones de swipe con indicador claro (chevron, etiqueta, tutorial) | HIG |
| `drag-threshold` | Umbral de movimiento antes de iniciar arrastre para evitar arrastres accidentales | MD |

## 3. Rendimiento — ALTO

Anti-patrones clave: layout thrashing; Cumulative Layout Shift.

| ID | Regla | Fuente |
|----|-------|--------|
| `image-optimization` | WebP/AVIF, imágenes responsive (srcset/sizes), lazy load de activos no críticos | — |
| `image-dimension` | Declarar width/height o aspect-ratio para prevenir layout shift | CWV |
| `font-loading` | font-display: swap/optional para evitar FOIT; reservar espacio | MD |
| `font-preload` | Precargar solo fuentes críticas; no abusar de preload por variante | — |
| `critical-css` | Priorizar CSS del contenido visible (inline o carga temprana) | — |
| `lazy-loading` | Lazy load de componentes no hero vía import dinámico / división por ruta | — |
| `bundle-splitting` | Dividir código por ruta/funcionalidad (React Suspense / Next.js dynamic) para reducir carga inicial y TTI | — |
| `third-party-scripts` | Scripts de terceros async/defer; auditar y eliminar innecesarios | MD |
| `reduce-reflows` | Evitar lecturas/escrituras frecuentes del layout; agrupar lecturas DOM luego escrituras | — |
| `content-jumping` | Reservar espacio para contenido asíncrono (CLS) | CWV |
| `lazy-load-below-fold` | loading="lazy" para imágenes debajo del pliegue y media pesado | — |
| `virtualize-lists` | Virtualizar listas con 50+ items | — |
| `main-thread-budget` | Trabajo por frame bajo ~16ms (60fps); tareas pesadas fuera del hilo principal | HIG, MD |
| `progressive-loading` | Skeleton screens / shimmer en lugar de spinners bloqueantes >1s | HIG |
| `input-latency` | Latencia de entrada bajo ~100ms para taps/scrolleo | MD |
| `tap-feedback-speed` | Feedback visual dentro de 100ms del tap | HIG |
| `debounce-throttle` | Debounce/throttle en eventos de alta frecuencia (scroll, resize, input) | — |
| `offline-support` | Mensajería de estado offline y fallback básico (PWA/móvil) | — |
| `network-fallback` | Modos degradados para redes lentas (menor resolución, menos animaciones) | — |

## 4. Selección de Estilo — ALTO

Anti-patrones clave: mezclar plano y skeuomorphic aleatoriamente; emoji como iconos.

| ID | Regla | Fuente |
|----|-------|--------|
| `style-match` | Coincidir estilo con tipo de producto (usar `--design-system`) | — |
| `consistency` | Mismo estilo en todas las páginas | — |
| `no-emoji-icons` | Iconos SVG (Heroicons, Lucide), no emojis | — |
| `color-palette-from-product` | Paleta del producto/industria (`--domain color`) | — |
| `effects-match-style` | Sombras, blur y radio alineados con el estilo elegido (glass/flat/clay) | — |
| `platform-adaptive` | Respetar modismos de plataforma (iOS HIG vs Material): navegación, controles, tipografía, movimiento | HIG, MD |
| `state-clarity` | Estados hover/pressed/disabled visualmente distintos manteniendo el estilo | MD |
| `elevation-consistent` | Escala de elevación/sombra consistente para cards, sheets, modales | MD |
| `dark-mode-pairing` | Diseñar variantes claro/oscuro juntas (marca, contraste, estilo) | HIG, MD |
| `icon-style-consistent` | Un conjunto/lenguaje visual de iconos (grosor de trazo, radio) en todo el producto | — |
| `system-controls` | Preferir controles nativos del sistema; personalizar solo si el branding lo requiere | HIG |
| `blur-purpose` | Blur para indicar descarte de fondo (modales, sheets), no decoración | HIG |
| `primary-action` | Un solo CTA principal por pantalla; secundarias subordinadas | HIG |

## 5. Layout y Responsive — ALTO

Anti-patrones clave: scroll horizontal; containers con px fijos; deshabilitar zoom.

| ID | Regla | Fuente |
|----|-------|--------|
| `viewport-meta` | width=device-width initial-scale=1 (nunca deshabilitar zoom) | WCAG |
| `mobile-first` | Diseñar primero para móvil, luego escalar a tablet y escritorio | — |
| `breakpoint-consistency` | Breakpoints sistemáticos (375 / 768 / 1024 / 1440) | — |
| `readable-font-size` | Mínimo 16px texto cuerpo en móvil (evita auto-zoom de iOS) | — |
| `line-length-control` | Móvil 35-60 caracteres/línea; escritorio 60-75 | — |
| `horizontal-scroll` | Sin scroll horizontal en móvil; el contenido debe caber en viewport | — |
| `spacing-scale` | Sistema de espaciado incremental 4pt/8dp | MD |
| `touch-density` | Espaciado cómodo para táctil: ni apretado ni propenso a errores | MD |
| `container-width` | Max-width consistente en escritorio (max-w-6xl / 7xl) | — |
| `z-index-management` | Escala de z-index por capas (0 / 10 / 20 / 40 / 100 / 1000) | — |
| `fixed-element-offset` | Navbar/barra inferior fija reserva padding seguro para contenido | — |
| `scroll-behavior` | Evitar scrolls anidados que interfieran con la experiencia principal | — |
| `viewport-units` | Preferir min-h-dvh sobre 100vh en móvil | — |
| `orientation-support` | Layout legible y operable en landscape | HIG |
| `content-priority` | Contenido principal primero en móvil; plegar/ocultar secundario | — |
| `visual-hierarchy` | Jerarquía por tamaño, espaciado y contraste — no solo color | — |

## 6. Tipografía y Color — MEDIO

Anti-patrones clave: texto <12px en cuerpo; gris-sobre-gris; hex raw en componentes.

| ID | Regla | Fuente |
|----|-------|--------|
| `line-height` | 1.5-1.75 para texto cuerpo | — |
| `line-length` | 65-75 caracteres por línea | — |
| `font-pairing` | Coincidir personalidades de fuente título/cuerpo | — |
| `font-scale` | Escala tipográfica consistente (12 14 16 18 24 32) | — |
| `contrast-readability` | Texto oscuro sobre fondos claros (slate-900 sobre blanco) | — |
| `text-styles-system` | Sistema de tipos de plataforma: iOS 11 Dynamic Type / Material 5 roles (display, headline, title, body, label) | HIG, MD |
| `weight-hierarchy` | Bold títulos (600-700), Regular cuerpo (400), Medium etiquetas (500) | MD |
| `color-semantic` | Tokens semánticos (primary, secondary, error, surface, on-surface), no hex raw | MD |
| `color-dark-mode` | Modo oscuro: variantes desaturadas/más claras, no colores invertidos; probar contraste por separado | HIG, MD |
| `color-accessible-pairs` | Par frente/fondo 4.5:1 (AA) o 7:1 (AAA); verificar con herramientas | WCAG, MD |
| `color-not-decorative-only` | Color funcional (rojo error, verde éxito) incluye icono/texto | HIG, MD |
| `truncation-strategy` | Preferir wrapping; al truncar usar ellipsis + tooltip/expand | HIG |
| `letter-spacing` | Respetar letter-spacing por defecto de plataforma; evitar tracking ajustado en cuerpo | HIG, MD |
| `number-tabular` | Cifras tabulares/monoespaciadas para datos, precios y temporizadores (prevenir layout shift) | — |
| `whitespace-balance` | Espacio en blanco para agrupar relacionados y separar secciones; evitar desorden | HIG |

## 7. Animación — MEDIO

Anti-patrones clave: animación solo decorativa; animar width/height; sin reduced-motion.

| ID | Regla | Fuente |
|----|-------|--------|
| `duration-timing` | 150-300ms micro-interacciones; transiciones complejas ≤400ms; evitar >500ms | MD |
| `transform-performance` | Solo transform/opacity; no animar width/height/top/left | — |
| `loading-states` | Skeleton o progreso cuando la carga exceda 300ms | — |
| `excessive-motion` | Animar 1-2 elementos clave por vista como máximo | — |
| `easing` | ease-out entrada, ease-in salida; evitar linear en transiciones UI | MD |
| `motion-meaning` | Toda animación expresa relación causa-efecto, no decoración | HIG |
| `state-transition` | hover/active/expanded/collapsed/modal se animan suavemente | — |
| `continuity` | Transiciones de página mantienen continuidad espacial (elemento compartido, deslizamiento direccional) | HIG |
| `parallax-subtle` | Parallax con moderación; respetar reduced-motion; no desorientar | HIG |
| `spring-physics` | Preferir curvas físicas/spring sobre linear o cubic-bezier | HIG |
| `exit-faster-than-enter` | Salidas ~60-70% de la duración de entrada | MD |
| `stagger-sequence` | Escalonar 30-50ms por item; evitar revelaciones todo-a-la-vez o lentas | MD |
| `shared-element-transition` | Transiciones de elemento compartido/hero entre pantallas | MD, HIG |
| `interruptible` | Tap/gesto cancela la animación en curso inmediatamente | HIG |
| `no-blocking-animation` | Nunca bloquear entrada durante animación; UI interactiva | HIG |
| `fade-crossfade` | Crossfade para reemplazo de contenido en el mismo contenedor | MD |
| `scale-feedback` | Escala sutil (0.95-1.05) al presionar cards/botones; restaurar al soltar | HIG, MD |
| `gesture-feedback` | Drag/swipe/pinch con respuesta visual en tiempo real siguiendo el dedo | MD |
| `hierarchy-motion` | Dirección de translate/scale expresa jerarquía: entrar desde abajo = más profundo | MD |
| `motion-consistency` | Tokens de duración/easing unificados globalmente | — |
| `opacity-threshold` | Elementos en fade no permanecen bajo opacidad 0.2; o desvanecen completo o visibles | — |
| `modal-motion` | Modales/sheets animan desde su fuente de activación (scale+fade o slide-in) | HIG, MD |
| `navigation-direction` | Avanzar anima izquierda/arriba; retroceder derecha/abajo; lógica consistente | HIG |
| `layout-shift-avoid` | Animaciones no causan reflow/CLS; usar transform para posición | CWV |

## 8. Formularios y Feedback — MEDIO

Anti-patrones clave: placeholder como etiqueta; errores solo al inicio; abrumar al inicio.

| ID | Regla | Fuente |
|----|-------|--------|
| `input-labels` | Etiqueta visible por cada input (no solo placeholder) | WCAG |
| `error-placement` | Error debajo del campo relacionado | MD |
| `submit-feedback` | Carga → estado éxito/error al enviar | MD |
| `required-indicators` | Marcar campos obligatorios (asterisco) | — |
| `empty-states` | Mensaje útil y acción cuando no hay contenido | MD |
| `toast-dismiss` | Auto-descartar toasts en 3-5s | — |
| `confirmation-dialogs` | Confirmar antes de acciones destructivas | HIG |
| `input-helper-text` | Texto de ayuda persistente debajo de inputs complejos | MD |
| `disabled-states` | Opacidad reducida (0.38-0.5) + cambio de cursor + atributo semántico | MD |
| `progressive-disclosure` | Revelar opciones complejas progresivamente; no abrumar al inicio | HIG |
| `inline-validation` | Validar al blur (no al keystroke); error solo tras terminar de escribir | MD |
| `input-type-keyboard` | Tipos semánticos (email, tel, number) para teclado móvil correcto | HIG, MD |
| `password-toggle` | Toggle mostrar/ocultar contraseña | MD |
| `autofill-support` | autocomplete / textContentType para autocompletar | HIG, MD |
| `undo-support` | Deshacer acciones destructivas o masivas (toast "Deshacer eliminar") | HIG |
| `success-feedback` | Confirmar acciones completadas con feedback visual breve | MD |
| `error-recovery` | Errores incluyen ruta de recuperación (reintentar, editar, ayuda) | HIG, MD |
| `multi-step-progress` | Indicador de paso/barra de progreso; permitir navegación atrás | MD |
| `form-autosave` | Auto-guardar borradores en formularios largos | HIG |
| `sheet-dismiss-confirm` | Confirmar antes de descartar sheet/modal con cambios sin guardar | HIG |
| `error-clarity` | Error indica causa + cómo solucionarlo (no solo "Entrada inválida") | HIG, MD |
| `field-grouping` | Agrupar campos relacionados (fieldset/legend o agrupación visual) | MD |
| `read-only-distinction` | Solo-lectura visual y semánticamente distinto de deshabilitado | MD |
| `focus-management` | Tras error de envío, auto-enfocar primer campo inválido | WCAG, MD |
| `error-summary` | Múltiples errores: resumen al inicio con enlaces a cada campo | WCAG |
| `touch-friendly-input` | Altura de input móvil ≥44px | HIG |
| `destructive-emphasis` | Acciones destructivas con color de peligro semántico, separadas de primarias | HIG, MD |
| `toast-accessibility` | Toasts no roban foco; aria-live="polite" | WCAG |
| `aria-live-errors` | Errores con región aria-live o role="alert" | WCAG |
| `contrast-feedback` | Estados error/éxito cumplen 4.5:1 | WCAG, MD |
| `timeout-feedback` | Timeout muestra feedback claro con opción de reintentar | MD |

## 9. Patrones de Navegación — ALTO

Anti-patrones clave: nav sobrecargada; retroceso roto; sin deep links.

| ID | Regla | Fuente |
|----|-------|--------|
| `bottom-nav-limit` | Nav inferior máximo 5 items con etiquetas+iconos | MD |
| `drawer-usage` | Drawer/sidebar para navegación secundaria, no acciones primarias | MD |
| `back-behavior` | Retroceso predecible y consistente; preservar scroll/estado | HIG, MD |
| `deep-linking` | Pantallas clave alcanzables vía deep link/URL | HIG, MD |
| `tab-bar-ios` | iOS: Tab Bar inferior para nivel superior | HIG |
| `top-app-bar-android` | Android: Top App Bar con icono de navegación para estructura primaria | MD |
| `nav-label-icon` | Items con icono Y etiqueta; solo icono perjudica descubribilidad | MD |
| `nav-state-active` | Ubicación actual resaltada (color, peso, indicador) | HIG, MD |
| `nav-hierarchy` | Navegación primaria vs secundaria claramente separadas | MD |
| `modal-escape` | Modales/sheets con indicador claro de cierre; swipe-down para descartar | HIG |
| `search-accessible` | Búsqueda fácilmente alcanzable; consultas recientes/sugeridas | MD |
| `breadcrumb-web` | Web: breadcrumbs para jerarquías de 3+ niveles | MD |
| `state-preservation` | Retroceso restaura scroll, estado de filtro e input | HIG, MD |
| `gesture-nav-support` | Soportar gestos de sistema (swipe-back iOS, predictive back Android) sin conflicto | HIG, MD |
| `tab-badge` | Badges con moderación (no leído/pendiente); limpiar tras visitar | HIG, MD |
| `overflow-menu` | Desbordes: menú overflow/más en lugar de apretujar | MD |
| `bottom-nav-top-level` | Nav inferior solo para nivel superior; nunca anidar sub-navegación | MD |
| `adaptive-navigation` | ≥1024px sidebar; pantallas pequeñas nav inferior/superior | MD |
| `back-stack-integrity` | Nunca restablecer silenciosamente la pila de navegación ni saltar al inicio | HIG, MD |
| `navigation-consistency` | Ubicación de navegación idéntica en todas las páginas | — |
| `avoid-mixed-patterns` | No mezclar Tab + Sidebar + Bottom Nav en el mismo nivel jerárquico | — |
| `modal-vs-navigation` | Modales no para flujos de navegación primarios; rompen la ruta del usuario | HIG |
| `focus-on-route-change` | Tras transición de página, mover foco al contenido principal | WCAG |
| `persistent-nav` | Navegación principal accesible desde páginas profundas | HIG, MD |
| `destructive-nav-separation` | Acciones peligrosas (eliminar cuenta, cerrar sesión) separadas de items normales | HIG, MD |
| `empty-nav-state` | Destino no disponible: explicar por qué, no ocultar silenciosamente | MD |

## 10. Gráficos y Datos — BAJO

Anti-patrón clave: depender solo del color para transmitir información.

| ID | Regla | Fuente |
|----|-------|--------|
| `chart-type` | Tipo de gráfico según datos (tendencia→línea, comparación→barra, proporción→pie/donut) | — |
| `color-guidance` | Paletas accesibles; evitar rojo/verde para daltónicos | WCAG, MD |
| `data-table` | Alternativa de tabla accesible; gráficos solos no son amigables con lectores | WCAG |
| `pattern-texture` | Suplementar color con patrones/texturas/formas | WCAG, MD |
| `legend-visible` | Leyenda siempre visible, cerca del gráfico | MD |
| `tooltip-on-interact` | Tooltips al hover (web) o tap (móvil) con valores exactos | HIG, MD |
| `axis-labels` | Ejes con unidades y escala legible; evitar etiquetas truncadas/rotadas en móvil | — |
| `responsive-chart` | Gráficos refluyen/se simplifican en pantallas pequeñas | — |
| `empty-data-state` | Estado vacío significativo ("Sin datos aún" + orientación) | MD |
| `loading-chart` | Skeleton/shimmer mientras cargan datos; no marcos de ejes vacíos | — |
| `animation-optional` | Animación de entrada respeta prefers-reduced-motion; datos legibles de inmediato | HIG |
| `large-dataset` | 1000+ puntos: agregar/muestrear; drill-down en lugar de renderizar todo | MD |
| `number-formatting` | Formato locale-aware de números/fechas/monedas | HIG, MD |
| `touch-target-chart` | Elementos interactivos ≥44pt o expandibles al tocar | HIG |
| `no-pie-overuse` | Evitar pie/donut >5 categorías; cambiar a barras | — |
| `contrast-data` | Líneas/barras vs fondo ≥3:1; etiquetas de datos ≥4.5:1 | WCAG |
| `legend-interactive` | Leyendas cliqueables para alternar series | MD |
| `direct-labeling` | Conjuntos pequeños: etiquetar valores directamente en el gráfico | — |
| `tooltip-keyboard` | Tooltip alcanzable por teclado, no solo hover | WCAG |
| `sortable-table` | Ordenamiento de tablas con aria-sort | WCAG |
| `axis-readability` | Marcas de eje espaciadas; auto-omitir en pantallas pequeñas | — |
| `data-density` | Limitar densidad por gráfico; dividir si es necesario | — |
| `trend-emphasis` | Enfatizar tendencias sobre decoración; sin gradientes/sombras pesadas | — |
| `gridline-subtle` | Cuadrícula bajo contraste (gray-200) para no competir con datos | — |
| `focusable-elements` | Elementos interactivos navegables por teclado | WCAG |
| `screen-reader-summary` | Resumen de texto o aria-label con la idea clave del gráfico | WCAG |
| `error-state-chart` | Falla de carga: error con acción de reintentar, no gráfico roto/vacío | — |
| `export-option` | Productos data-heavy: exportación CSV/imagen | — |
| `drill-down-consistency` | Drill-down con ruta de retorno clara y breadcrumb de jerarquía | — |
| `time-scale-clarity` | Series de tiempo: etiquetar granularidad (día/semana/mes) y permitir cambio | — |

---

## Apéndice A: Reglas comunes para UI profesional (Apps)

Cuestiones frecuentemente pasadas por alto que hacen que la UI se vea poco profesional. Alcance: UI de Apps (iOS/Android/React Native/Flutter), no patrones de interacción web-escritorio.

### Iconos y elementos visuales

| Regla | Estándar | Evitar | Por qué importa |
|-------|----------|--------|-----------------|
| Sin emoji como iconos estructurales | Iconos vectoriales (Lucide, react-native-vector-icons, @expo/vector-icons) | Emojis para navegación, configuración o controles | Dependen de la fuente, inconsistentes entre plataformas, no tematizables |
| Activos solo vectoriales | SVG o iconos de plataforma que escalan y soportan theming | PNG raster borrosos/pixelados | Escalabilidad, nitidez y adaptación claro/oscuro |
| Estados de interacción estables | Transiciones de color/opacidad/elevación sin cambiar límites del layout | Transformaciones que desplazan contenido o vibran | Estabilidad y calidad percibida en móvil |
| Logotipos de marca correctos | Activos oficiales y guías de uso (espaciado, color, espacio limpio) | Adivinar rutas, recolorizar, modificar proporciones | Cumplimiento legal/de plataforma |
| Tamaño de icono consistente | Tokens (icon-sm, icon-md = 24pt, icon-lg) | Valores arbitrarios 20/24/28pt mezclados | Ritmo y jerarquía visual |
| Consistencia de trazo | Grosor uniforme por capa visual (1.5px o 2px) | Mezclar grosores arbitrarios | Cohesión y pulido percibido |
| Relleno vs contorno | Un estilo de icono por nivel de jerarquía | Mezclar relleno y contorno en el mismo nivel | Claridad semántica y coherencia |
| Objetivo táctil mínimo | 44x44pt de área interactiva (hitSlop si el icono es menor) | Iconos pequeños sin área expandida | Accesibilidad de plataforma |
| Alineación de iconos | Alineados a línea base del texto, padding consistente | Iconos desalineados o espaciado inconsistente | Equilibrio visual |
| Contraste de iconos | WCAG: 4.5:1 pequeños, 3:1 glifos UI grandes | Iconos de bajo contraste | Accesibilidad en ambos modos |

### Interacción (App)

| Regla | Hacer | No hacer |
|-------|-------|----------|
| Feedback al tap | Ripple/opacidad/elevación en 80-150ms | Sin respuesta visual al tap |
| Timing de animación | Micro-interacciones 150-300ms con easing nativo | Instantáneas o >500ms |
| Foco de accesibilidad | Orden de foco del lector de pantalla = orden visual; etiquetas descriptivas | Controles sin etiqueta o foco confuso |
| Estado deshabilitado | Semánticas disabled, énfasis reducido, sin acción al tap | Controles que parecen tappables pero no hacen nada |
| Objetivo táctil mínimo | ≥44x44pt (iOS) / ≥48x48dp (Android); expandir área de impacto | Targets minúsculos o solo-icono sin padding |
| Conflictos de gestos | Un gesto primario por región; sin conflictos anidados tap/drag | Gestos superpuestos que causan acciones accidentales |
| Controles nativos semánticos | Primitivas nativas (Button, Pressable) con roles de accesibilidad | Contenedores genéricos como controles primarios |

### Contraste modo claro/oscuro

| Regla | Hacer | No hacer |
|-------|-------|----------|
| Superficie (claro) | Cards separadas del fondo con opacidad/elevación suficiente | Superficies demasiado transparentes |
| Texto (claro) | Contraste cuerpo ≥4.5:1 sobre superficies claras | Gris de bajo contraste |
| Texto (oscuro) | Primario ≥4.5:1 y secundario ≥3:1 en superficies oscuras | Texto que se mezcla con el fondo |
| Bordes y divisores | Visibles en ambos temas | Bordes que desaparecen en un modo |
| Paridad de estados | pressed/focused/disabled distinguibles en ambos temas | Estados definidos para un solo tema |
| Theming por tokens | Tokens semánticos mapeados por tema | Hex hardcodeados por pantalla |
| Scrim modal | Scrim 40-60% negro para aislar primer plano | Scrim débil con fondo compitiendo |

### Layout y espaciado

| Regla | Hacer | No hacer |
|-------|-------|----------|
| Áreas seguras | Respetar safe areas en headers fijos, tab bars y CTA | UI fija bajo notch, barra de estado o área de gestos |
| Barras del sistema | Espaciado para barras de estado/navegación e indicador de gestos | Contenido tappable chocando con cromo del SO |
| Ancho consistente | Ancho predecible por clase de dispositivo | Anchos arbitrarios entre pantallas |
| Ritmo 8dp | Sistema 4/8dp para padding/gaps/secciones | Incrementos aleatorios |
| Medida de texto | Texto extenso legible en dispositivos grandes | Párrafos de borde a borde en tablets |
| Jerarquía de espaciado | Niveles claros (16/24/32/48) por jerarquía | Espaciado inconsistente entre niveles similares |
| Gutters adaptativos | Insets horizontales mayores en anchos grandes y landscape | Mismo gutter estrecho en todos los tamaños |
| Scroll y elementos fijos | Insets de contenido para listas bajo barras fijas | Contenido scrollable oscurecido por headers/footers |

---

## Apéndice B: Checklist pre-entrega para Apps

Alcance: UI de Apps (iOS/Android/React Native/Flutter). Para el checklist web ver SKILL.md.

### Calidad visual
- [ ] No se usan emojis como iconos (SVG en su lugar)
- [ ] Iconos de una familia y estilo consistente
- [ ] Activos de marca oficiales con proporciones y espacio limpio correctos
- [ ] Estados presionados no desplazan límites del layout ni vibran
- [ ] Tokens de tema semánticos consistentes (sin colores hardcodeados por pantalla)

### Interacción
- [ ] Todo elemento tappable da feedback claro al presionar (ripple/opacidad/elevación)
- [ ] Objetivos táctiles ≥44x44pt iOS / ≥48x48dp Android
- [ ] Micro-interacciones 150-300ms con easing nativo
- [ ] Estados deshabilitados visualmente claros y no interactivos
- [ ] Orden de foco del lector de pantalla = orden visual; etiquetas descriptivas
- [ ] Regiones de gestos sin interacciones anidadas/conflictivas (tap/drag/back-swipe)

### Modo claro/oscuro
- [ ] Contraste texto primario ≥4.5:1 en ambos modos
- [ ] Contraste texto secundario ≥3:1 en ambos modos
- [ ] Divisores/bordes y estados distinguibles en ambos modos
- [ ] Scrim modal/drawer 40-60% negro
- [ ] Ambos temas probados antes de entrega (no inferidos de uno)

### Layout
- [ ] Safe areas respetadas en headers, tab bars y CTA inferiores
- [ ] Contenido scrollable no oculto tras barras fijas/sticky
- [ ] Verificado en teléfono pequeño, grande y tablet (retrato + paisaje)
- [ ] Insets/gutters adaptados por tamaño y orientación
- [ ] Ritmo 4/8dp en componente, sección y página
- [ ] Medida de texto extenso legible en dispositivos grandes

### Accesibilidad
- [ ] Imágenes/iconos significativos con etiquetas de accesibilidad
- [ ] Campos de formulario con etiquetas, pistas y errores claros
- [ ] El color no es el único indicador
- [ ] Reduced motion y Dynamic Type soportados sin rotura de layout
- [ ] Traits/roles/estados (selected, disabled, expanded) se anuncian correctamente
