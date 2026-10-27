# Validación de Endpoints con curl (AuthZ/AuthN)

Objetivo: verificar que los endpoints que **DEBEN requerir autenticación/autorización** la exigen de verdad, y que los públicos no filtran datos sensibles. Es la prueba nº 1 de **A01 Broken Access Control** (OWASP Top 10) y **API1 BOLA / API2 Broken Function Level Authorization** (OWASP API Top 10). 100% reproducible con curl, sin necesidad de Burp/ZAP.

## 1. Enumerar endpoints

| Fuente | Comando |
|--------|---------|
| Código del backend | `grep -rnE "(router|app)\.(get|post|put|patch|delete)\(" src/` (adaptar al framework) |
| OpenAPI/Swagger | `curl -s <url>/swagger.json \| jq '.paths \| keys'` — probar también `/openapi.json`, `/api-docs`, `/swagger-ui/`, `/v1/api-docs` |
| Bundles frontend | `grep -oE '"/api/[^"]+"' dist/*.js \| sort -u` (o `fetch\(|axios` para ver métodos) |
| Crawling pasivo | robots.txt, sitemap.xml, source maps (`*.js.map` revelan rutas y lógica) |
| Fuzzing | ffuf/gobuster contra rutas comunes de API: `/api/v1/users`, `/admin`, `/internal`, `/debug` |

## 2. Clasificar endpoints

| Clase | Esperado sin auth | Esperado con usuario normal |
|-------|-------------------|-----------------------------|
| Público (login, registro, health, docs) | 200 | 200 |
| Autenticado (cualquier sesión) | **401/403** | 200 |
| Admin / privilegiado | **401/403** | **403** |
| Interno (solo desde la red interna) | 401/403/404 | 404 (no debe existir en prod) |

## 3. Pruebas sin autenticación

```bash
# Estado y redirect (la base para toda la matriz)
curl -s -o /dev/null -w "%{http_code} %{redirect_url}\n" https://target.com/api/users

# Respuesta completa por si el código engaña (200 con HTML de login, etc.)
curl -s -i https://target.com/api/users | head -25

# Con cookie jar vacío (simula sesión inexistente)
curl -s -o /dev/null -w "%{http_code}\n" -b empty.txt -c cookies.txt https://target.com/api/users

# Sin token pero con headers "de confianza" que algunos proxies respetan mal
curl -s -o /dev/null -w "%{http_code}\n" -H "X-Forwarded-For: 127.0.0.1" https://target.com/api/admin
```

### Matriz de resultados (sin auth)

| Respuesta | Veredicto | Acción |
|-----------|-----------|--------|
| `200` + JSON/datos | **Critical** — Broken Access Control | Capturar evidencia, probar con más rutas |
| `200` + HTML de login genérico | Sospechoso | Revisar el body: ¿filtra datos? ¿es una SPA que cargará datos tras JS? |
| `302` a `/login` | OK aparente | Seguir el redirect (`-L`) y verificar que el body no contenga datos |
| `401` / `403` | OK | Correctamente protegido |
| `404` en ruta de admin | OK (o ruta renombrada — probar variantes) | — |

## 4. Pruebas con sesión de usuario con pocos privilegios

```bash
# 1. Login y guardar sesión
curl -s -c cookies.txt -H "Content-Type: application/json" \
  -d '{"user":"lowpriv","pass":"..."}' https://target.com/api/login

# 2. Endpoints admin con usuario normal → esperado 403
curl -s -o /dev/null -w "%{http_code}\n" -b cookies.txt https://target.com/api/admin/users

# 3. IDOR: recurso de otro usuario
curl -s -b cookies.txt https://target.com/api/orders/12345          # ¿dato de otro usuario?
curl -s -b cookies.txt "https://target.com/api/users?page=2&limit=1000"  # ¿paginación sin filtro de tenant?

# 4. Métodos alternativos (authz a veces solo en GET)
curl -s -o /dev/null -w "%{http_code}\n" -X PUT -b cookies.txt -d '{"role":"admin"}' https://target.com/api/users/me
curl -s -o /dev/null -w "%{http_code}\n" -X DELETE -b cookies.txt https://target.com/api/orders/999

# 5. Mass assignment (BOPLA)
curl -s -b cookies.txt -X PATCH -H "Content-Type: application/json" \
  -d '{"isAdmin":true,"balance":99999}' https://target.com/api/users/me

# 6. JWT débil (firmar con "none" o con el secreto "secret")
curl -s -H "Authorization: Bearer eyJhbGciOiJub25lIn0.eyJyb2xlIjoiYWRtaW4ifQ." https://target.com/api/admin
```

## 5. Detalles que importan

- **401 vs 403:** 401 = no autenticado; 403 = autenticado sin permiso. Un endpoint que da 403 sin token suele tener lógica de authz (pero verifica todos los métodos HTTP, no solo GET).
- **302 no es siempre OK:** algunos frameworks redirigen a login PERO responden el recurso en el body antes de redirigir. Usa `curl -s -i` y mira el body completo.
- **CORS:** `curl -s -I -H "Origin: https://evil.com" -H "Access-Control-Request-Method: GET" -X OPTIONS <url>` → si responde `Access-Control-Allow-Origin: https://evil.com` sin credenciales bien definidas, es hallazgo.
- **Rate limiting:** 10 requests seguidos → si no hay `429` ni `Retry-After`, anotar como Medium (A04).
- **Verbose/errores:** respuestas `500` con stack traces o `debug=true` en query params filtran internals.
- **HEAD vs GET:** a veces HEAD/OPTIONS no pasan por el middleware de auth: `curl -I` en endpoints protegidos.

## 6. Automatización

`scripts/endpoint-authz-check.sh` / `endpoint-authz-check.bat` — prueba una lista de endpoints (formato `METODO /ruta` por línea) sin auth y con token opcional, y genera `security/evidence/endpoint-authz.csv`:

```bash
echo "GET /api/users" | ./endpoint-authz-check.sh https://target.com
./endpoint-authz-check.sh https://target.com "$TOKEN" < endpoints.txt
```

## 7. Severidad sugerida

| Hallazgo | Severidad |
|----------|-----------|
| Endpoint autenticado responde 200 con datos sin token | Critical |
| Endpoint admin accesible con usuario normal | Critical |
| IDOR con datos sensibles de otros usuarios | Critical/High |
| IDOR con datos de bajo impacto | High/Medium |
| 302 a login con datos en el body | High |
| Ausencia de rate limiting en login/OTP | Medium |
| CORS permisivo | Medium |

## 8. Reporte

Cada hallazgo debe ir al informe `security/report.md` con: endpoint, método, petición curl de reproducción, respuesta observada vs esperada, severidad y recomendación (authz en cada handler, no solo en el router; middleware central; tests de integración que verifiquen 401/403).
