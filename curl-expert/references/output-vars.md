# Variables de output (`--write-out` / `-w`)

La opción `-w` / `--write-out` permite extraer información estructurada sobre una transferencia, ideal para scripts y monitoreo.

## Sintaxis

```bash
curl -w "FORMATO" URL
```

Donde `FORMATO` es texto literal con placeholders `%{variable}`. Puedes usar `\n` para newlines y otros escapes.

## Variables disponibles

### Básicas / respuesta HTTP

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `%{http_code}` | Código HTTP de la última response | `200`, `404`, `503` |
| `%{response_code}` | Igual a `http_code` (alias) | - |
| `%{content_type}` | Content-Type de la response | `application/json` |
| `%{http_connect}` | Código HTTP del CONNECT (proxy) | `200` |
| `%{http_version}` | Versión HTTP usada | `2`, `3` |
| `%{header_json}` | Todos los headers de la response en JSON | objeto |
| `%{ssl_verify_result}` | Resultado de la verificación TLS | `0` (ok), `21` (revoked) |
| `%{num_redirects}` | Cantidad de redirects seguidos | `2` |
| `%{redirect_url}` | URL del último redirect | - |

### Tamaño y transferencia

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `%{size_download}` | Bytes descargados | `12345` |
| `%{size_upload}` | Bytes subidos | `1024` |
| `%{size_header}` | Bytes de headers de response | `256` |
| `%{size_request}` | Bytes de headers de request | `180` |
| `%{speed_download}` | Velocidad de descarga (B/s) | `1234567` |
| `%{speed_upload}` | Velocidad de subida (B/s) | `98765` |
| `%{size_header}` | Bytes de headers | `256` |
| `%{request_size}` | Total bytes de la request | `512` |
| `%{num_headers}` | Número de headers en la response | `12` |

### Tiempos (en segundos)

| Variable | Descripción |
|----------|-------------|
| `%{time_total}` | Tiempo total de la transferencia |
| `%{time_namelookup}` | Tiempo de DNS lookup |
| `%{time_connect}` | Tiempo de conexión TCP (incluye DNS) |
| `%{time_appconnect}` | Tiempo hasta handshake completo (TLS/SSH/QUIC) |
| `%{time_pretransfer}` | Tiempo hasta que la transferencia está por iniciar (incluye TLS) |
| `%{time_starttransfer}` | Tiempo hasta el primer byte de la response |
| `%{time_redirect}` | Tiempo total gastado en redirects |

> **Nota**: Los tiempos se acumulan. `time_connect` = DNS + TCP. `time_appconnect` = `time_connect` + TLS/QUIC.

### Red

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `%{remote_ip}` | IP del servidor remoto | `93.184.216.34` |
| `%{remote_port}` | Puerto del servidor remoto | `443` |
| `%{local_ip}` | IP local (cliente) | `192.168.1.100` |
| `%{local_port}` | Puerto local (cliente) | `54321` |
| `%{primary_ip}` | IP primaria del host | - |
| `%{primary_port}` | Puerto primario | - |
| `%{dns_resolution}` | Tiempo de DNS | `0.023` |
| `%{scheme}` | Esquema de la URL | `HTTPS` |
| `%{url_effective}` | URL final (post-redirects) | - |

### Conexión / TLS

| Variable | Descripción |
|----------|-------------|
| `%{num_connects}` | Número de conexiones nuevas |
| `%{num_retries}` | Número de reintentos |
| `%{ssl_verify_result}` | TLS verify result code |
| `%{ssl_engines}` | Lista de engines SSL |
| `%{applcon_time}` | (legacy) = `time_appconnect` |
| `%{redirect_time}` | (legacy) = `time_redirect` |
| `%{pretransfer_time}` | (legacy) = `time_pretransfer` |
| `%{starttransfer_time}` | (legacy) = `time_starttransfer` |

### Otros

| Variable | Descripción |
|----------|-------------|
| `%{filename_effective}` | Path final del archivo guardado |
| `%{exitcode}` | Código de salida del proceso |
| `%{errormsg}` | Mensaje de error (si hubo) |
| `%{json}` | Output en JSON (con `-w "%{json}"`) |
| `%{certs}` | Cadena de certificados del server (PEM completo) |
| `%{ftp_entry_path}` | Path de entrada FTP |
| `%{proxy_ssl_verify_result}` | TLS verify result del proxy |
| `%{remote_ip}` | IP del server final |
| `%{proxy_ip}` | IP del proxy |
| `%{proxy_port}` | Puerto del proxy |
| `%{proxy_ssl_verify_result}` | TLS verify result del proxy |
| `%{url_effective}` | URL final |
| `%{onerror}` | Si ocurrió error, imprime el resto del formato |

## Ejemplos prácticos

### Monitoreo de tiempo de respuesta

```bash
curl -s -o /dev/null \
  -w "HTTP: %{http_code} | Total: %{time_total}s | TTFB: %{time_starttransfer}s\n" \
  https://api.example.com
```

Output:
```
HTTP: 200 | Total: 0.234s | TTFB: 0.123s
```

### Timing desglosado completo

```bash
curl -s -o /dev/null \
  -w "DNS:    %{time_namelookup}s\n\
Connect: %{time_connect}s\n\
TLS:     %{time_appconnect}s\n\
TTFB:    %{time_starttransfer}s\n\
Total:   %{time_total}s\n" \
  https://example.com
```

Output:
```
DNS:    0.012s
Connect: 0.045s
TLS:     0.089s
TTFB:    0.156s
Total:   0.234s
```

### Output en JSON (para parsing)

```bash
curl -s -o /dev/null -w "%{json}" https://api.example.com | jq
```

Output:
```json
{
  "url_effective": "https://api.example.com/",
  "http_code": 200,
  "response_code": 200,
  "http_connect": 0,
  "time_total": 0.234,
  "time_namelookup": 0.012,
  "time_connect": 0.045,
  "time_appconnect": 0.089,
  "time_pretransfer": 0.092,
  "time_starttransfer": 0.156,
  "time_redirect": 0,
  "size_download": 1256,
  "size_upload": 0,
  "size_header": 256,
  "size_request": 180,
  "speed_download": 5367,
  "speed_upload": 0,
  "num_connects": 1,
  "num_redirects": 0,
  "remote_ip": "93.184.216.34",
  "remote_port": 443,
  "local_ip": "192.168.1.100",
  "local_port": 54321,
  "scheme": "HTTPS",
  ...
}
```

### Verificar si un sitio está disponible (script)

```bash
#!/bin/bash
URL="https://api.example.com/health"

response=$(curl -s -o /dev/null -w "%{http_code}|%{time_total}" --max-time 10 "$URL")
http_code=$(echo "$response" | cut -d'|' -f1)
time_total=$(echo "$response" | cut -d'|' -f2)

if [ "$http_code" = "200" ]; then
  echo "OK: $URL responded in ${time_total}s"
  exit 0
else
  echo "FAIL: $URL returned HTTP $http_code"
  exit 1
fi
```

### Test de velocidad de descarga

```bash
curl -s -o /dev/null \
  -w "Downloaded: %{size_download} bytes in %{time_total}s\nSpeed: %{speed_download} B/s\n" \
  https://speed.cloudflare.com/__down?bytes=10000000
```

### Monitoreo de varios endpoints

```bash
for url in https://api1.example.com https://api2.example.com https://api3.example.com; do
  curl -s -o /dev/null \
    -w "$url: %{http_code} (%{time_total}s)\n" \
    "$url"
done
```

### Información de conexión de red

```bash
curl -s -o /dev/null \
  -w "Resolved IP: %{remote_ip}:%{remote_port}\nLocal socket: %{local_ip}:%{local_port}\nProtocol: HTTP/%{http_version}\nTLS verify: %{ssl_verify_result}\n" \
  https://example.com
```

### Verificar velocidad y disponibilidad simultáneamente

```bash
result=$(curl -s -o /dev/null \
  -w "%{http_code}:%{time_total}:%{speed_download}" \
  --max-time 30 \
  https://example.com/big-file.zip)

http_code=$(echo "$result" | cut -d: -f1)
time=$(echo "$result" | cut -d: -f2)
speed=$(echo "$result" | cut -d: -f3)

echo "HTTP $http_code, took ${time}s, ${speed} B/s"
```

### Capturar solo el código HTTP

```bash
status=$(curl -s -o /dev/null -w "%{http_code}" URL)
case $status in
  200) echo "OK";;
  404) echo "Not found";;
  5*) echo "Server error: $status";;
  *) echo "Other: $status";;
esac
```

## Output en JSON vs texto

```bash
# Texto plano con formato
curl -w "Code: %{http_code}\nTime: %{time_total}\n" URL

# JSON completo
curl -w "%{json}" URL

# Mezclar (concatenación)
curl -w "Status: %{http_code} | JSON: %{json}\n" URL
```

## Formato personalizado con colores/estilos

```bash
# -w con secuencia ANSI (requiere --styled-output o terminal)
curl -s -o /dev/null \
  --styled-output \
  -w "Status: \e[32m%{http_code}\e[0m | Time: \e[33m%{time_total}s\e[0m\n" \
  URL
```

## Variables especiales

### `%{onerror}`

Imprime el resto del formato SOLO si hubo error:

```bash
curl -s -w "OK: %{http_code}%{onerror}|ERROR: %{errormsg}" URL
```

### `%{header_json}`

Headers de la response en JSON:

```bash
curl -s -o /dev/null -w "%{header_json}" URL | jq '.date, ."content-type"'
```

## Tips y trucos

1. **`%{time_total}` incluye todo** (DNS + TCP + TLS + TTFB + download)
2. **`%{time_connect}` incluye DNS** (DNS + TCP)
3. **Para TTFB real, usa `time_starttransfer`** (time-to-first-byte)
4. **Para benchmark, repite N veces y promedia** (curl tiene varianza de un solo request)
5. **`-o /dev/null` silencia el body** pero mantiene la transferencia
6. **Combina con `-s` y `-S`**: `-s` silencia errores, `-S` los muestra
7. **`%{json}` es excelente para parsing** con `jq` o similar
8. **`%{onerror}` evita formato condicional complejo**
