# Context7 — CLI `ctx7` (documentación actualizada)

Context7 indexa documentación oficial y actualizada de librerías/frameworks (con versiones específicas) y la expone a agentes de IA. El método recomendado en esta skill es la **CLI oficial `ctx7`** — ver https://context7.com/docs/clients/cli. Su uso evita **recomendaciones desactualizadas o alucinadas** (ej.: recomendar un middleware que ya no existe, un header obsoleto, o payloads para APIs que cambiaron).

## Cuándo usarlo

- Antes de emitir recomendaciones de hardening (security headers, auth, middleware, deserialización, rate limiting) → verifica contra las docs de la **versión instalada** en el proyecto.
- Al auditar dependencias → confirma la versión actual, prácticas recomendadas y cambios de seguridad entre versiones.
- Al revisar implementaciones de auth (JWT, OAuth, sesiones, MFA) → verifica el patrón recomendado actual del framework.
- Para construir POCs/payloads → consulta las docs de la versión exacta del objetivo.
- Para validar que un hallazgo sigue siendo válido en la versión actual del framework.

## Instalación (no requiere instalación para usos puntuales)

Requiere Node.js 18+.

```bash
# Sin instalar nada — útil para usos puntuales
npx ctx7 --help
npx ctx7 library react

# O instalación global para uso frecuente
npm install -g ctx7
ctx7 --version
```

## Setup del agente (una sola vez)

`ctx7 setup` ofrece dos modos: **MCP** o **CLI + Skills**. Esta skill usa el modo CLI + Skills (instala una skill `docs` que guía al agente con `ctx7 library` y `ctx7 docs`, sin MCP):

```bash
npx ctx7 setup --cli --universal    # global (~/.agents/skills)
npx ctx7 setup --cli --project      # solo para el proyecto actual
npx ctx7 setup --cli --yes          # sin confirmaciones
npx ctx7 setup --cli --api-key TU_API_KEY   # sin flujo OAuth interactivo
npx ctx7 remove --cli               # desinstalar el setup
```

## Flujo de uso — 2 pasos

### Paso 1 — `ctx7 library`: resolver el ID de la librería

Siempre pasa una `query` describiendo lo que intentas hacer: rankea resultados y desambigua nombres compartidos entre paquetes.

```bash
npx ctx7 library express "security headers helmet"
npx ctx7 library nextjs "how to set up app router with middleware"
npx ctx7 library prisma "one-to-many relations with cascade delete"
```

Cada resultado incluye: **Library ID** (formato `/org/project` — es lo que se pasa a `ctx7 docs`), nº de code snippets indexados, reputación de la fuente (High/Medium/Low/Unknown), benchmark score y versiones disponibles (`/org/project/version`). El mejor match suele ser el de nombre más cercano, más snippets y mejor reputación.

### Paso 2 — `ctx7 docs`: consultar documentación

```bash
npx ctx7 docs /expressjs/express "how to set security headers with helmet"
npx ctx7 docs /vercel/next.js "middleware that redirects unauthenticated users"
npx ctx7 docs /prisma/prisma "row level security with prisma client extensions"

# Versión específica (si el hallazgo depende de la versión instalada)
npx ctx7 docs /expressjs/express/v4.18.2 "secure session and cookie configuration"
npx ctx7 docs /vercel/next.js/v15.1.8 "route protection with middleware"

# JSON para scripting
npx ctx7 docs /expressjs/express "rate limiting" --json
```

Reglas:
- Los IDs **siempre empiezan con `/`**: `npx ctx7 docs express "auth"` falla; usa el ID completo devuelto por `ctx7 library`.
- Consultas específicas y en inglés dan mejores resultados que palabras sueltas: `"How to set up authentication with JWT in Express.js"` > `"auth"`.
- La salida es limpia cuando no hay TTY (pipes): `npx ctx7 docs /facebook/react "useEffect cleanup" | head -50`.
- El output incluye code snippets (con lenguaje) e info snippets (prose con breadcrumb).

## Autenticación

```bash
npx ctx7 login              # abre el navegador (--no-browser imprime la URL)
npx ctx7 whoami             # estado del login
npx ctx7 logout
export CONTEXT7_API_KEY=tu_key   # para CI/scripts, salta el login interactivo
```

- `ctx7 library` y `ctx7 docs` **funcionan sin login**; el login sube los rate limits.
- `ctx7 setup` requiere login salvo que se pase `--api-key`.
- Deshabilitar telemetría: `CTX7_TELEMETRY_DISABLED=1`.

## HTTP API como alternativa (curl)

Sin instalar nada; sin API key hay rate limits bajos, con `Authorization: Bearer $CONTEXT7_API_KEY` (de context7.com/dashboard) son más altos.

```bash
# Buscar librería
curl -s "https://context7.com/api/v2/libs/search?libraryName=express&query=security%20headers" \
  -H "Authorization: Bearer $CONTEXT7_API_KEY" | jq '.results[0]'

# Obtener contexto de docs
curl -s "https://context7.com/api/v2/context?libraryId=/expressjs/express&query=how%20to%20set%20security%20headers" \
  -H "Authorization: Bearer $CONTEXT7_API_KEY" | jq '.infoSnippets[].content'

# Versión pineada
curl -s "https://context7.com/api/v2/context?libraryId=/expressjs/express/v4.18.2&query=helmet%20configuration" \
  -H "Authorization: Bearer $CONTEXT7_API_KEY"
```

Formato de `libraryId`: `/org/repo` (GitHub), `/org/repo/v1.2.3` o `/org/repo@v1.2.3` (versión), `/packages/<name>` (npm). El ID de una librería es la URL de su página en context7.com.

**Códigos de error útiles:** `401` API key inválida (empieza con `ctx7sk`) · `404` librería inexistente · `429` rate limit (respetar `Retry-After`) · `301` la librería se movió (`redirectUrl` en el body).

## Flujo de uso en una auditoría

```
1. Extraer dependencias y versiones del proyecto (package.json, requirements.txt, go.mod, pom.xml)
2. Para cada dependencia crítica (web framework, auth lib, ORM, parser):
     npx ctx7 library <lib> "<pregunta>"
     npx ctx7 docs /org/repo "secure configuration for version X"
3. Contrastar la configuración ACTUAL del proyecto con la recomendada:
     - headers faltantes, middleware de auth mal colocado, parser inseguro, etc.
4. Para hallazgos de versión: consultar docs de la versión exacta (pin /org/repo/vX.Y.Z) y el changelog
5. Si no está indexado → fetch de la doc oficial (ej. https://docs.example.com/llms.txt si existe)
```

## Reglas

- Pregunta específica y en inglés suele devolver mejores resultados que una palabra suelta.
- Siempre indica la versión cuando el hallazgo dependa de ella (pin `/org/repo/vX.Y.Z`).
- No sustituye a la verificación empírica: las docs validan la *recomendación*, los tests/curl validan el *comportamiento*.
- Al citar docs en el informe (`security/report.md`), incluye la URL de la fuente para trazabilidad.
