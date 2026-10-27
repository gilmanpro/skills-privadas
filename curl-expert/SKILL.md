---
name: curl-expert
description: "Experto en curl: construye y depura peticiones HTTP/HTTPS desde terminal (GET/POST/PUT, headers, autenticacion, cookies, TLS/SSL, proxies, WebSocket, FTP/SFTP, HTTP/2-3) y las integra en scripts bash/PowerShell. Usar SIEMPRE que el usuario mencione curl, peticiones HTTP por linea de comandos, pruebas de APIs REST, descargas por URL, o quiera convertir un comando wget a curl."
---

# curl-expert

## Cuándo usar esta skill
Usa esta skill para construir, ejecutar o depurar comandos curl.
Aplica a peticiones HTTP/REST, descargas, uploads, autenticación, sesiones con cookies, TLS/SSL, proxies y protocolos como FTP/SFTP.
No aplica para scraping recursivo (usa wget) ni para lógica de aplicación fuera de curl.

## Sintaxis básica
Ejecuta `curl [opciones] URL`.
Usa comillas dobles en URLs con `[]`, `{}`, `?`, `&`, `#`, espacios o caracteres especiales para evitar expansión de shell.
Cada opción que no sea URL debe empezar con `-` o `--`.
Separa múltiples URLs con `--next` (`-:`) para resetear el estado entre peticiones.

## Opciones esenciales
Usa estas opciones para cubrir el 90% de los casos comunes.

### HTTP, salida y body
| Opción | Uso |
|--------|-----|
| `-o file` / `-O` | Guardar salida en archivo o con nombre remoto. |
| `-L` | Seguir redirecciones 3xx. |
| `-s` / `-S` | Silenciar progreso (`-s`) pero mostrar errores (`-S`). |
| `-v` | Verbose: ver request/response/timing. |
| `-I` / `-i` | Solo headers (`-I`) o headers + body (`-i`). |
| `-H "K: V"` | Añadir header personalizado. |
| `-A "UA"` / `-e "URL"` | User-Agent y Referer. |
| `-d "k=v"` / `--json '{...}'` | Enviar body urlencoded o JSON. |
| `-F "name=@file"` | Enviar multipart/form-data. |
| `-T file` | Subir archivo vía PUT/FTP/SFTP. |

### Autenticación, red y TLS
| Opción | Uso |
|--------|-----|
| `-u user:pass` / `-H "Authorization: Bearer ..."` | Autenticación Basic o Bearer. |
| `-b file` / `-c file` | Leer/escribir cookies. |
| `-x proxy:port` / `-U user:pass` | Proxy y credenciales de proxy. |
| `--connect-timeout N` / `-m N` | Timeouts de conexión y total. |
| `--retry N` | Reintentos ante errores transitorios. |
| `-k` / `--cacert file` | Desactivar verificación TLS (solo dev) o usar CA personalizada. |

## Ejemplos comunes
Prueba estos patrones antes de opciones más complejas.

```bash
curl -sS -o /dev/null -w "%{http_code} %{time_total}s" https://api.example.com/health
curl --json '{"name":"x"}' -H "Authorization: Bearer $TOKEN" https://api.example.com/items
curl -L -c jar.txt -b jar.txt -d "user=admin&pass=secret" https://example.com/login
```

## Depuración básica
Aplica este orden para diagnosticar problemas rápidamente.

1. Ejecuta `curl -v URL` para ver DNS, TCP, TLS, headers y códigos HTTP.
2. Usa `curl -i URL` si necesitas ver headers de respuesta junto al body.
3. Guarda un trace completo con `curl --trace-ascii debug.txt URL`.
4. Mide timing con `-w "%{time_namelookup} %{time_connect} %{time_appconnect} %{time_starttransfer} %{time_total}"`.
5. Compara con el navegador copiando el request como cURL desde DevTools.

## Referencias
Consulta los archivos de `references/` para opciones avanzadas y casos específicos.

- `references/curl-options.md` — catálogo completo de opciones.
- `references/protocols.md` — HTTP/2, HTTP/3, FTP, SFTP, SCP, WebSocket, MQTT, IMAP, SMTP, etc.
- `references/security-tls.md` — certificados, CA bundles, versiones TLS, pinning.
- `references/cookies.md` — motor de cookies, login con sesión, formato Netscape.
- `references/output-vars.md` — variables de `--write-out` para scripts y monitoring.
- `references/url-syntax.md` — sintaxis de URLs, globbing, encoding.
- `references/troubleshooting.md` — diagnóstico de errores comunes.
- `references/wget-to-curl.md` — tabla de diferencias curl vs wget y recetas de conversión. Cargar si el usuario menciona wget o quiere convertir comandos.
- `references/config-env.md` — archivo `.curlrc`, variables de entorno de proxy y reglas de sintaxis general. Cargar para configuración persistente o proxies por env vars.
