# Configuración persistente y entorno de curl

## Archivo de configuración `.curlrc`

curl lee su archivo de configuración al arrancar (desactivable con `-q` / `--disable`).

Ubicaciones:
- Unix: `~/.curlrc`
- Windows: `%USERPROFILE%\_curlrc` o `%APPDATA%\_curlrc`
- Override con `CURL_HOME/.curlrc`
- O con `--config <file>` (o `-K`); `-K -` lee la config de stdin

Formato (`clave = valor`, un archivo admite tanto la forma larga sin guiones como la corta):

```
# Comentarios con #
# Sin guiones para opciones largas
user-agent = "Mozilla/5.0 ..."
proxy = http://proxy.example.com:8080
-m 1800
# Opciones con valor con espacios entre comillas
header = "Accept: application/json"
```

## Variables de entorno

| Variable | Descripción |
|----------|-------------|
| `http_proxy` / `HTTP_PROXY` | Proxy para HTTP |
| `HTTPS_PROXY` | Proxy para HTTPS |
| `FTP_PROXY` | Proxy para FTP |
| `ALL_PROXY` | Proxy general |
| `NO_PROXY` | Lista de hosts que NO usan proxy |
| `CURL_CA_BUNDLE` | Path a CA bundle personalizado |
| `SSL_CERT_FILE` / `SSL_CERT_DIR` | CA certs (OpenSSL) |
| `http_proxy` (minúsculas) | Solo usado por curl/scripts específicos; `HTTP_PROXY` es el estándar cross-platform |

## Reglas de sintaxis general

- Puedes especificar **múltiples URLs** en la misma línea (se procesan secuencialmente).
- Las opciones con un guion corto (`-d`) aceptan el valor con o sin espacio.
- Las opciones largas (`--data`) requieren espacio entre opción y valor.
- Opciones booleanas se desactivan con `--no-<opción>` (ej: `--no-keepalive`).
