# Troubleshooting de curl

Guía para diagnosticar y resolver problemas comunes con curl.

## Diagnóstico progresivo

### Nivel 1: Verbose básico

```bash
curl -v https://example.com
```

Muestra:
- DNS lookup y resolución
- Conexión TCP
- TLS handshake (si aplica)
- Request headers
- Response headers
- SSL info
- Tiempos parciales

### Nivel 2: Trace completo a archivo

```bash
curl --trace-ascii debug.txt https://example.com
```

Muestra TODO byte-a-byte. Para análisis profundo.

### Nivel 3: Trace con tiempo e IDs

```bash
curl --trace-ascii debug.txt --trace-time --trace-ids https://example.com
```

Añade timestamps y IDs de transfer/connection (útil con `--parallel`).

### Nivel 4: Comparar con navegador

1. Abre DevTools en el navegador (F12) → Network
2. Reproduce la acción
3. Click derecho → "Copy as cURL" (Chrome/Edge) o "Copy" → "Copy as cURL" (Firefox)
4. Ejecuta el comando copiado

### Nivel 5: Captura con tcpdump/Wireshark

```bash
# Capturar todo el tráfico a un host
sudo tcpdump -i any host example.com -w capture.pcap
```

Para HTTPS, usa `SSLKEYLOGFILE` para descifrar (solo debug local).

## Problemas comunes

### 🔴 "SSL certificate problem"

**Diagnóstico**:
```bash
curl -v https://example.com 2>&1 | grep -i "ssl\|tls\|verify\|cert"
```

**Causas y soluciones**:

| Mensaje | Causa | Solución |
|---------|-------|----------|
| "unable to get local issuer certificate" | CA no conocida | Actualizar `--cacert` o usar `--ca-native` |
| "certificate has expired" | Cert expirado | Verificar fecha del sistema, esperar renovación |
| "self-signed certificate" | Cert autofirmado | Agregar a CA store o usar `--cacert` |
| "hostname mismatch" | Cert no es para este dominio | Usar el dominio correcto, `--resolve` |
| "revoked" | Cert revocado | Server debe renovar cert |

**Fix rápido (desarrollo)**:
```bash
# Temporal - NO producción
curl -k https://example.com

# Permanente - actualizar CA bundle
curl --cacert /path/to/ca.pem https://example.com
```

### 🔴 "Could not resolve host"

**Diagnóstico**:
```bash
curl -v https://example.com 2>&1 | grep -i "resolve\|dns"
nslookup example.com
```

**Causas**:
- DNS no funciona
- Hostname mal escrito
- Sin conectividad a Internet
- DNS over HTTPS no funciona (en algunos backends)

**Soluciones**:
```bash
# Usar IP directa
curl https://93.184.216.34/

# Forzar DNS
curl --doh-url https://1.1.1.1/dns-query https://example.com

# IPv4 forzado
curl -4 https://example.com
```

### 🔴 "Connection refused"

**Diagnóstico**:
```bash
curl -v telnet://example.com:443  # o el puerto correspondiente
```

**Causas**:
- Server no está corriendo
- Puerto incorrecto
- Firewall bloqueando
- Server bind a localhost solamente

**Soluciones**:
```bash
# Verificar puerto
nc -zv example.com 443

# Otro puerto
curl https://example.com:8443/

# IPv6 vs IPv4
curl -4 https://example.com
curl -6 https://example.com
```

### 🔴 "Connection timed out"

**Diagnóstico**:
```bash
curl -v --connect-timeout 5 https://example.com
```

**Causas**:
- Firewall corporativo
- Red inestable
- Server muy lento
- IP bloqueada geográficamente

**Soluciones**:
```bash
# Timeout más largo
curl --connect-timeout 30 --max-time 60 https://example.com

# Vía proxy
curl -x http://proxy:8080 https://example.com

# Vía VPN (si está disponible)
```

### 🔴 HTTP 401 Unauthorized

**Diagnóstico**:
```bash
curl -v -u user:pass https://example.com 2>&1 | grep -i "auth\|www-auth"
```

**Causas y soluciones**:

| Auth type | Comando |
|-----------|---------|
| Basic | `curl -u user:pass URL` |
| Bearer | `curl -H "Authorization: Bearer TOKEN" URL` |
| Digest | `curl --digest -u user:pass URL` |
| NTLM (Windows) | `curl --ntlm -u user:pass URL` |
| Negociar (Kerberos) | `curl --negotiate -u : URL` |
| Auto (mejor disponible) | `curl --anyauth -u user:pass URL` |
| Cookie-based | `curl -b cookies.txt URL` |

### 🔴 HTTP 403 Forbidden

**Causas comunes**:
- Falta User-Agent (algunos servers bloquean curl/bot)
- Falta Referer
- Bloqueo geográfico
- IP bloqueada
- Falta cookie/CSRF token

**Soluciones**:
```bash
# User-Agent de navegador
curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" URL

# Referer
curl -e "https://google.com" URL

# Todas las cookies + User-Agent + Referer
curl -b cookies.txt -A "Mozilla/5.0..." -e "https://referer.com" URL
```

### 🔴 HTTP 429 Too Many Requests

**Causa**: Rate limit.

**Soluciones**:
```bash
# Delay entre requests
sleep 2 && curl URL

# Limitar tasa
curl --rate 5/second URL  # máximo 5/seg

# Con reintentos
curl --retry 3 --retry-delay 5 URL

# User-Agent único (algunos sistemas lo rastrean)
curl -A "MyApp/1.0 (contact@example.com)" URL
```

### 🔴 Empty response / 0 bytes

**Diagnóstico**:
```bash
curl -v URL  # ver headers
curl -i URL  # mostrar headers + body
```

**Causas**:
- Server no envía body (HEAD, 204, 304)
- Error silencioso (con `-f`, body no se muestra en error)
- Redirección no seguida (sin `-L`)

**Soluciones**:
```bash
# Ver headers
curl -i URL

# No fallar en 4xx/5xx (mostrar body igualmente)
curl --fail-with-body URL

# Seguir redirects
curl -L URL
```

### 🔴 Transfer muy lento

**Diagnóstico**:
```bash
curl -v -o /dev/null -w "Speed: %{speed_download} B/s\n" URL
```

**Causas y soluciones**:

| Causa | Solución |
|-------|----------|
| Cuello de botella en red | Comprimir: `curl --compressed URL` |
| Server limita | Probar con HTTP/2 o HTTP/3: `curl --http2 URL` |
| Límites de MTU/TCP | `--tcp-nodelay` o `--tcp-fastopen` |
| No se reusan conexiones | Múltiples URLs en misma invocación |
| Transfer grande con overhead | `--range` para descargar por partes |

```bash
# Compresión
curl --compressed -o file URL

# HTTP/2 multiplex
curl --http2 -o file URL

# Múltiples URLs (connection reuse)
curl -O URL1 -O URL2 -O URL3

# Verificar velocidad teórica
curl -o /dev/null -w "Speed: %{speed_download} B/s\n" URL
```

### 🔴 "curl: (6) Could not resolve host" tras cambio de DNS

**Causa**: DNS cacheado.

**Solución**:
```bash
# Forzar nueva resolución
curl --resolve example.com:443:1.2.3.4 https://example.com/

# Limpiar cache de sistema
# Windows: ipconfig /flushdns
# macOS: sudo dscacheutil -flushcache
# Linux: sudo systemd-resolve --flush-caches
```

### 🔴 Caracteres raros en output

**Causa**: Encoding incorrecto.

**Soluciones**:
```bash
# Guardar con encoding correcto
curl URL | iconv -f latin1 -t utf-8

# Detectar encoding
curl URL | file -

# UTF-8 explícito
curl URL | iconv -f utf-8 -t utf-8//IGNORE
```

### 🔴 "curl: (23) Failed writing body"

**Causa**: Pipe cerrado prematuramente (ej: `head` corta el stream).

**Soluciones**:
```bash
# No usar head directamente
curl URL > file
curl -o file URL

# Si necesitas pipear
curl -s URL | head -n 10
# Ignorar el error (código 23 = SIGPIPE)
curl -s URL | head -n 10 2>/dev/null
# O
curl -sS URL | head -n 10 || true
```

### 🔴 "curl: (60) SSL certificate problem: unable to get local issuer certificate"

Ya cubierto en `security-tls.md`. Resumen:

```bash
# 1. Usar CA bundle del sistema
curl --ca-native URL

# 2. CA bundle personalizado
curl --cacert /path/to/ca.pem URL

# 3. Variable de entorno
export CURL_CA_BUNDLE=/path/to/ca.pem

# 4. Solo desarrollo
curl -k URL
```

### 🔴 Server devuelve HTTP 301/302 y curl no sigue

**Causa**: Sin `-L`.

**Solución**:
```bash
curl -L URL
```

⚠️ Con `-L` y POST: el primer request es POST, los redirects subsiguientes son GET (RFC 7231).

Para forzar POST en 301/302/303:
```bash
curl -L --post301 URL
curl -L --post302 URL
curl -L --post303 URL
```

### 🔴 "Protocol 'http' not supported or disabled in libcurl"

curl no fue compilado con soporte HTTP (raro pero posible).

**Verificar**:
```bash
curl --version
# Última línea: Protocols: dict file ftp ftps ...
```

**Solución**: reinstalar curl con soporte HTTP (casi siempre está incluido).

## Debugging avanzado

### Capturar tráfico TLS decrypted

```bash
# Linux/macOS: usar SSLKEYLOGFILE con Firefox/Chrome
SSLKEYLOGFILE=/tmp/ssl.log curl --trace-ascii - https://example.com

# Luego abrir en Wireshark con ssl.log cargado
```

### Timing detallado

```bash
curl -s -o /dev/null \
  -w "\
DNS Lookup:    %{time_namelookup}s\n\
TCP Connect:   %{time_connect}s\n\
TLS/SSL:       %{time_appconnect}s\n\
Pre-transfer:  %{time_pretransfer}s\n\
TTFB:          %{time_starttransfer}s\n\
Total:         %{time_total}s\n" \
  https://example.com
```

### Ver qué headers del cliente envía

```bash
curl -v --trace-ascii - https://example.com 2>&1 | grep "^>"
```

### Ver qué headers del server devuelve

```bash
curl -v --trace-ascii - https://example.com 2>&1 | grep "^<"
```

### Detectar HTTP/2 vs HTTP/1.1

```bash
curl -v --http2 https://example.com 2>&1 | grep "using HTTP"
# Output: * Using HTTP/2
```

### Verificar soporte HTTP/3

```bash
curl --http3-only https://example.com  # falla si no soporta
```

### Test de CA bundle

```bash
# Ver qué CA bundle está usando
curl -v https://example.com 2>&1 | grep -i "cafile\|capath"

# Output típico:
# * CAfile: /etc/ssl/certs/ca-certificates.crt
# * CApath: /etc/ssl/certs
```

## Scripts de diagnóstico

### Test completo de un sitio

```bash
#!/bin/bash
URL=$1

echo "=== Testing $URL ==="
echo

echo "--- DNS ---"
nslookup $(echo $URL | sed 's|https\?://||;s|/.*||')

echo "--- Connectivity ---"
curl -s -o /dev/null -w "HTTP %{http_code} in %{time_total}s\n" --max-time 10 "$URL"

echo "--- TLS ---"
curl -v "$URL" 2>&1 | grep -E "SSL|TLS|Verify" | head -5

echo "--- HTTP version ---"
curl -v "$URL" 2>&1 | grep -E "Using HTTP|Server:" | head -3

echo "--- Redirect chain ---"
curl -L -s -o /dev/null -w "Final URL: %{url_effective}\nRedirects: %{num_redirects}\n" "$URL"

echo "--- Size ---"
curl -s -o /dev/null -w "Body size: %{size_download} bytes\n" "$URL"
```

Uso:
```bash
chmod +x test-url.sh
./test-url.sh https://example.com
```

## Recursos

- **Man page**: `man curl` o https://curl.se/docs/manpage.html
- **FAQ oficial**: https://curl.se/docs/faq.html
- **Bugs conocidos**: https://curl.se/docs/knownbugs.html
- **GitHub issues**: https://github.com/curl/curl/issues
- **Discord/Mailing lists**: https://curl.se/mail/
- **Everything curl book**: https://everything.curl.dev/
