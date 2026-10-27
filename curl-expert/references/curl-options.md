# Referencia completa de opciones de curl

Catálogo organizado por categoría, basado en `curl --manual` (man page v8.21.1).

## Convenciones

- `[OPC]` indica opcional
- `<VAL>` indica valor obligatorio
- `bool` indica opción booleana (sin valor)
- Las opciones marcadas con **(G)** son **globales** (sobreviven a `--next`)

## Opciones globales (G)

Estas opciones mantienen su valor entre URLs separadas por `--next`:

- `--fail-early` - Salir al primer error
- `--libcurl <file>` - Escribir código C usando libcurl
- `--parallel`, `--parallel-immediate`, `--parallel-max`, `--parallel-max-host`
- `--progress-bar` (`-#`)
- `--rate <max/s>` - Tasa máxima de transferencia
- `--show-error` (`-S`)
- `--stderr <file>` - Redirigir stderr
- `--styled-output` - Salida con estilos/color
- `--trace`, `--trace-ascii`, `--trace-config`, `--trace-ids`, `--trace-time`
- `--verbose` (`-v`)

## URLs

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `--url <url>` | string | URL alternativa (útil en config files) |
| `-:` / `--next` | bool | Reset state para siguiente URL |
| `-g` / `--globoff` | bool | Desactivar globbing `{}` y `[]` |
| `--expand-url <url>` | string | URL con expansión de variables `{{var}}` |
| `--url-query <data>` | string | Añadir query string a URL |

### Múltiples URLs: --next y --parallel

`--next` (`-:`) resetea el estado de opciones entre URLs. `-Z` / `--parallel` (opción global) transfiere varias URLs en paralelo.

```bash
# HEAD seguido de GET
curl -I https://example.com --next https://example.com

# Login → dashboard reusando cookie jar entre peticiones
curl -c jar -d "user=a&pass=b" https://example.com/login --next -b jar https://example.com/dashboard

# Descargar múltiples archivos en paralelo
curl -Z -O "https://example.com/file[1-100].txt"
# Limitar concurrencia: --parallel-max 5
```

## Salida y archivos

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `-o` / `--output <file>` | file | Guardar a archivo (en lugar de stdout) |
| `-O` / `--remote-name` | bool | Usar nombre remoto como nombre local |
| `--remote-name-all` | bool | Aplicar `-O` a TODAS las URLs |
| `-J` / `--remote-header-name` | bool | Usar `Content-Disposition` filename |
| `--output-dir <dir>` | dir | Directorio base para `-O` |
| `--create-dirs` | bool | Crear directorios locales automáticamente |
| `--create-file-mode <mode>` | octal | Permisos al crear (default 0644) |
| `-D` / `--dump-header <file>` | file | Guardar headers |
| `-c` / `--cookie-jar <file>` | file | Guardar cookies (Netscape format) |
| `-w` / `--write-out <format>` | format | Variables de post-transferencia |
| `--write-out <format>` | format | Idem (forma larga) |
| `--xattr` | bool | Guardar metadata en xattr (file modification) |
| `--remove-on-error` | bool | Borrar archivo si la transferencia falla |
| `--skip-existing` | bool | No sobrescribir archivos existentes |
| `--no-clobber` | bool | No sobrescribir (`-O`) |
| `-#` / `--progress-bar` (G) | bool | Barra de progreso en lugar del medidor |
| `--no-progress-meter` | bool | Ocultar medidor |
| `-R` / `--remote-time` | bool | Poner timestamp del servidor al archivo |

## HTTP - Peticiones

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `-X` / `--request <method>` | string | Forzar método HTTP |
| `-d` / `--data <data>` | data | POST urlencoded (también `@file`, `@-` stdin) |
| `--data-raw <data>` | data | `-d` sin interpretar `@` |
| `--data-binary <data>` | data | POST preservando newlines |
| `--data-urlencode <data>` | data | POST con URL-encoding |
| `--data-ascii <data>` | data | Alias de `--data` |
| `-F` / `--form <name=content>` | data | POST multipart (también `@file`, `<file`, `;type=`) |
| `--form-string <string>` | string | `-F` sin interpretar caracteres especiales. Si el valor viene del usuario, un `@` malicioso se interpretaría como path de archivo |
| `--form-escape` | bool | Escapar valores de form |
| `-G` / `--get` | bool | Convertir `-d` a GET con query string |
| `-I` / `--head` | bool | Solo HEAD request |
| `-T` / `--upload-file <file>` | file | PUT (también `-T -` para stdin) |
| `--upload-flags <flags>` | string | Flags para SFTP/SCP |
| `--json <data>` | data | POST JSON (atajo para `-d` + Content-Type). Requiere curl 7.82+ |
| `--url-query <data>` | data | Añadir a query string |
| `--compressed` | bool | Pedir respuesta comprimida |
| `--compressed-ssh` | bool | Compresión SSH (SCP/SFTP) |
| `-r` / `--range <range>` | range | Rango de bytes |
| `-C` / `--continue-at <offset>` | offset | Reanudar (`-C -` auto) |
| `-e` / `--referer <URL>` | URL | Header `Referer` |
| `-A` / `--user-agent <string>` | string | Header `User-Agent` |
| `-H` / `--header <line>` | string | Añadir/modificar header (repetible) |
| `-b` / `--cookie <data\|file>` | string/file | Cookie o archivo |
| `--cookie-jar <file>` | file | Ver "Salida" |
| `-j` / `--junk-session-cookies` | bool | Ignorar session cookies al cargar |
| `-L` / `--location` | bool | Seguir redirects (3xx) |
| `--location-trusted` | bool | Como `-L` pero envía auth también a otros hosts |
| `--max-redirs <n>` | int | Máximo de redirects (default 50) |
| `--post301`, `--post302`, `--post303` | bool | Mantener método en esos redirects |
| `--request-target <path>` | string | Path personalizado (proxy) |
| `--proto-default <scheme>` | string | Si la URL no tiene esquema |
| `--proto <list>` | string | Permitir solo estos protocolos |
| `--proto-redir <list>` | string | Limitar protocolos en redirects |

## HTTP - Respuesta

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `-i` / `--include` | bool | Incluir headers HTTP en la salida |
| `--show-headers` | bool | Idem (forma larga) |
| `-s` / `--silent` | bool | Silenciar medidor y errores |
| `-S` / `--show-error` (G) | bool | Mostrar errores con `-s` |
| `--fail` (`-f`) | bool | Fallar en HTTP >= 400 (sin output del body) |
| `--fail-with-body` | bool | Fallar en HTTP >= 400 pero mostrar body |
| `--fail-early` (G) | bool | Salir al primer error (sin paralelo) |
| `--max-filesize <bytes>` | bytes | Abortar si descarga > size |

## Autenticación

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `-u` / `--user <user:pass>` | string | Credenciales (`:pass` opcional → prompt) |
| `--anyauth` | bool | Negociar el más seguro |
| `--basic` | bool | Forzar Basic |
| `--digest` | bool | Forzar Digest |
| `--ntlm` | bool | Forzar NTLM |
| `--ntlm-wb` | bool | NTLM con Winbind |
| `--negotiate` | bool | SPNEGO/Kerberos |
| `--delegation <LEVEL>` | string | Kerberos delegation (none/policy/always) |
| `--oauth2-bearer <token>` | string | OAuth2 Bearer |
| `--aws-sigv4 <provider[:reg[:svc]]>` | string | AWS SigV4 |
| `--sasl-authzid <id>` | string | AuthzID SASL |
| `--sasl-ir` | bool | Initial response SASL |
| `-n` / `--netrc` | bool | Usar `.netrc` (required) |
| `--netrc-optional` | bool | Usar `.netrc` (opcional) |
| `--netrc-file <file>` | file | Path personalizado a `.netrc` |
| `--login-options <opts>` | string | Opciones de login (IMAP, POP3, SMTP) |

## Proxy

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `-x` / `--proxy <[proto://]host:port>` | string | Configurar proxy |
| `--proxy1.0 <host:port>` | string | Proxy HTTP/1.0 |
| `--preproxy <[proto://]host:port>` | string | Proxy solo para pre-TRANSFER |
| `--socks4 <host:port>` | string | SOCKS4 |
| `--socks4a <host:port>` | string | SOCKS4a (resolución remota) |
| `--socks5 <host:port>` | string | SOCKS5 (resolución local) |
| `--socks5-hostname <host:port>` | string | SOCKS5h (resolución remota) |
| `--socks5-gssapi` / `--socks5-gssapi-service` / `--socks5-gssapi-nec` | bool/string | SOCKS5 con GSSAPI |
| `--socks5-basic` | bool | SOCKS5 con Basic auth |
| `-U` / `--proxy-user <user:pass>` | string | Auth del proxy |
| `--proxy-anyauth` | bool | Negociar auth del proxy |
| `--proxy-basic` | bool | Forzar Basic en proxy |
| `--proxy-digest` | bool | Forzar Digest en proxy |
| `--proxy-negotiate` | bool | SPNEGO/Kerberos en proxy |
| `--proxy-ntlm` | bool | NTLM en proxy |
| `--proxy-header <line>` | string | Header extra al proxy |
| `--proxy-http2` | bool | HTTP/2 con proxy |
| `-p` / `--proxytunnel` | bool | Tunneling (no proxy para CONNECT) |
| `--noproxy <list>` | string | Hosts sin proxy |

## TLS / SSL

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `-k` / `--insecure` | bool | **NO** verificar certificado del servidor |
| `--cacert <file>` | file | CA bundle personalizado |
| `--capath <dir>` | dir | Directorio de CAs |
| `--ca-native` | bool | CA store del sistema |
| `--dump-ca-embed <file>` | file | Extraer CA embebido |
| `--proxy-cacert`, `--proxy-capath`, `--proxy-ca-native`, `--proxy-insecure` | - | TLS para proxy |
| `-E` / `--cert <cert[:pass]>` | file | Certificado de cliente |
| `--cert-type <type>` | string | PEM, DER, P12, ENG, PROV |
| `--key <key>` | file | Clave privada |
| `--key-type <type>` | string | Tipo de clave |
| `--pass <phrase>` | string | Passphrase de clave privada |
| `--proxy-cert`, `--proxy-key`, `--proxy-key-type`, `--proxy-pass` | - | TLS de proxy |
| `--cert-status` | bool | Verificar status (OCSP stapling) |
| `--doh-cert-status` | bool | OCSP stapling para DNS-over-HTTPS |
| `--doh-insecure` | bool | Skip verify DNS-over-HTTPS |
| `--doh-url <URL>` | URL | Resolver DoH |
| `--ciphers <list>` | string | Cipher suites TLS 1.2- |
| `--tls13-ciphers <list>` | string | Cipher suites TLS 1.3 |
| `--curves <list>` | string | Curvas EC (X25519, P-256, etc.) |
| `--tlsv1.0` / `--tlsv1.1` / `--tlsv1.2` / `--tlsv1.3` | bool | Forzar versión TLS |
| `--tlsv1` (`-1`) | bool | TLS 1.x (≥1.0) |
| `--tls-max <version>` | string | Versión máxima |
| `--ssl` / `--ssl-reqd` | bool | Forzar SSL/TLS (FTPS) |
| `-2` / `--sslv2` / `-3` / `--sslv3` | bool | SSLv2/v3 (inseguros) |
| `--ssl-allow-beast` | bool | Permitir BEAST attack |
| `--ssl-no-revoke` | bool | Skip revocation check (Schannel) |
| `--ssl-revoke-best-effort` | bool | Revocación con fallback |
| `--ssl-auto-client-cert` | bool | Auto-selección de cert de cliente |
| `--ssl-sessions <file>` | file | Reusar sesiones TLS |
| `--pinnedpubkey <hashes>` | string | Pinning de clave pública |
| `--proxy-pinnedpubkey` | string | Pinning para proxy |
| `--tls-earlydata <bytes>` | int | TLS 1.3 early data (0-RTT) |
| `--tlsauthtype <type>` | string | SRP type |
| `--tlsuser <user>` | string | TLS user (SRP) |
| `--tlspassword <pass>` | string | TLS password (SRP) |
| `--ech <config>` | string | Encrypted Client Hello |
| `--false-start` | bool | TLS False Start |
| `--ssl-sessions` | file | Cache de sesiones TLS |
| `--engine <name>` | string | OpenSSL engine |
| `--egd-file <file>` | file | Entropy Gathering Daemon socket |
| `--random-file <file>` | file | Random data (legacy) |

## HTTP/2 y HTTP/3

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `--http0.9` | bool | Permitir HTTP/0.9 responses |
| `--http1.0` (`-0`) | bool | Forzar HTTP/1.0 |
| `--http1.1` | bool | Forzar HTTP/1.1 |
| `--http2` | bool | Negociar HTTP/2 vía ALPN |
| `--http2-prior-knowledge` | bool | HTTP/2 sin TLS (h2c) |
| `--http3` | bool | HTTP/3 con fallback a HTTP/1-2 |
| `--http3-only` | bool | Solo HTTP/3 (falla si no) |
| `--alt-svc <file>` | file | Alt-Svc cache |
| `--no-alpn` | bool | Disable ALPN |
| `--no-npn` | bool | Disable NPN (legacy) |
| `--happy-eyeballs-timeout-ms <ms>` | int | Timeout fallback HTTP/3 (default 200) |

## Red y conexión

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `--interface <name\|ip>` | string | Interfaz de red de salida |
| `-4` / `--ipv4` | bool | Forzar IPv4 |
| `-6` / `--ipv6` | bool | Forzar IPv6 |
| `--ip-tos <value>` | string | IP Type of Service |
| `--vlan-priority <num>` | int | VLAN priority |
| `--local-port <range>` | string | Rango de puertos locales (ej: 1000-2000) |
| `--abstract-unix-socket <path>` | path | Unix socket abstracto (sin red) |
| `--unix-socket <path>` | path | Unix socket (HTTP local) |
| `--dns-interface <if>` | string | Interfaz para DNS |
| `--dns-ipv4-addr <ip>` | IP | IPv4 para DNS |
| `--dns-ipv6-addr <ip>` | IP | IPv6 para DNS |
| `--dns-servers <list>` | string | Servidores DNS |
| `--connect-timeout <seconds>` | float | Timeout de conexión (default 0=∞) |
| `-m` / `--max-time <seconds>` | float | Timeout total (default 0=∞) |
| `--expect100-timeout <seconds>` | float | Timeout para HTTP 100-continue |
| `--keepalive-time <seconds>` | int | TCP keepalive (default 60) |
| `--keepalive-cnt <num>` | int | TCP keepalive probes (default 9) |
| `--no-keepalive` | bool | Disable TCP keepalive |
| `--tcp-nodelay` | bool | TCP_NODELAY (disable Nagle) |
| `--tcp-fastopen` | bool | TCP Fast Open |
| `--mptcp` | bool | Multipath TCP (Linux) |
| `--resolve <host:port:addr>` | string | DNS override (repetible) |
| `--connect-to <h1:p1:h2:p2>` | string | Redirigir conexión (repetible) |
| `--service-name <name>` | string | SNI personalizado |
| `--proxy-service-name <name>` | string | SNI para proxy |

## Transferencia y rendimiento

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `--limit-rate <speed>` | string | Velocidad máxima (K, M) |
| `-Y` / `--speed-limit <bytes>` | int | Velocidad mínima |
| `-y` / `--speed-time <seconds>` | int | Tiempo para `--speed-limit` |
| `--rate <max/s>` | int | Tasa global de transferencias |
| `--max-filesize <bytes>` | bytes | Tamaño máximo descargable |
| `--max-time <seconds>` | float | Tiempo total máximo |
| `--retry <num>` | int | Reintentos en error transient |
| `--retry-all-errors` | bool | Reintentar en TODOS los errores |
| `--retry-connrefused` | bool | Reintentar en ECONNREFUSED |
| `--retry-delay <seconds>` | float | Delay entre reintentos (default 1) |
| `--retry-max-time <seconds>` | float | Tiempo total para reintentos |
| `-z` / `--time-cond <time>` | string | Condicional por tiempo (con `-` invierte) |
| `--etag-compare <file>` | file | Hacer request solo si ETag difiere |
| `--etag-save <file>` | file | Guardar ETag del response |

## Cookies (resumen)

Ver `cookies.md` para más detalles.

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `-b` / `--cookie <data\|file>` | string/file | Cookies a enviar (o archivo a leer) |
| `-c` / `--cookie-jar <file>` | file | Guardar cookies tras transferencia |
| `-j` / `--junk-session-cookies` | bool | Ignorar session cookies al cargar |
| `--cookie <empty>` | - | Activar motor de cookies sin enviar ninguna |

## FTP

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `-P` / `--ftp-port <addr>` | string | Address para PORT (`:`, `-`, IP, interface) |
| `--ftp-pasv` | bool | Usar PASV (default) |
| `--ftp-skip-pasv-ip` | bool | Ignorar IP en respuesta PASV |
| `--ftp-method <method>` | string | multicwd, singlecwd, nocwd |
| `--ftp-create-dirs` | bool | Crear directorios remotos |
| `--ftp-account <data>` | string | Cuenta FTP |
| `--ftp-alternative-to-user <cmd>` | string | Comando alternativo al USER |
| `-Q` / `--quote <cmd>` | string | Comando FTP a enviar (antes de transfer) |
| `--disable-eprt` | bool | Disable EPRT |
| `--disable-epsv` | bool | Disable EPSV |
| `--ftp-pret` | bool | PRET command |
| `--ftp-ssl-ccc` | bool | CCC tras auth |
| `--ftp-ssl-ccc-mode <mode>` | string | Modo CCC (active/passive) |
| `--ftp-ssl-control` | bool | SSL en control connection |
| `-a` / `--append` | bool | Append en upload (FTP/SFTP) |
| `-l` / `--list-only` | bool | Listar solo nombres (FTP) |

## SSH / SFTP / SCP

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `--key <file>` | file | Clave privada SSH |
| `--key-type <type>` | string | Tipo de clave |
| `--pass <phrase>` | string | Passphrase de la clave |
| `--pubkey <file>` | file | Clave pública (si curl no la extrae) |
| `--hostpubmd5 <md5>` | string | MD5 esperado de host pub key |
| `--hostpubsha256 <hash>` | string | SHA256 esperado de host pub key |
| `--krb <level>` | string | Kerberos (FTP) |
| `-2` / `--sslv2` | - | (En SSH: SSHv2) |
| `--ssh-compressed` / `--compressed-ssh` | bool | Compresión SSH |

## Mail (IMAP, POP3, SMTP)

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `-M` / `--manual` | bool | Mostrar manual completo |
| `--mail-from <addr>` | string | Remitente (SMTP) |
| `--mail-rcpt <addr>` | string | Destinatario (SMTP) (repetible) |
| `--mail-rcpt-allowfails` | bool | Permitir que algunos RCPT fallen |
| `--mail-auth <auth>` | string | Auth string (SMTP) |

## Variables y expansión (8.3.0+)

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `--variable <name=content>` | string | Definir variable |
| `--variable <name@file>` | file | Definir desde archivo |
| `--variable <name@->` | stdin | Definir desde stdin |
| `--variable <%ENV_VAR>` | env | Importar env var (falla si no existe) |
| `--variable <%ENV_VAR=default>` | env | Importar con default |
| `--expand-url <url>` | string | URL con `{{var}}` |
| `--expand-data <data>` | data | Body con `{{var}}` |
| `--expand-header <line>` | string | Header con `{{var}}` |
| `--expand-variable <name=...>` | string | Definir variable expandida |
| (con `-K -` para leer config de stdin) | | |

**Funciones de transformación** (con `:` después de `{{var}}`):
- `trim` - Quitar espacios al inicio/final
- `json` - Escapar como string JSON
- `url` - URL-encode
- `b64` - Base64 encode
- `64dec` - Base64 decode

## Debugging y tracing

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `-v` / `--verbose` (G) | bool | Verbose |
| `--trace <file>` (G) | file | Trace completo (binario) |
| `--trace-ascii <file>` (G) | file | Trace completo en ASCII |
| `--trace-config <string>` (G) | string | Configurar qué tracear |
| `--trace-ids` (G) | bool | IDs de transfer/connection |
| `--trace-time` (G) | bool | Timestamps en trace |
| `-s` / `--silent` | bool | Silenciar |
| `-S` / `--show-error` (G) | bool | Mostrar errores con `-s` |
| `--styled-output` (G) | bool | Salida con color |
| `--stderr <file>` (G) | file | Redirigir stderr |

## Config files

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `-K` / `--config <file>` | file | Leer opciones de archivo (`-` para stdin) |
| `-q` / `--disable` | bool | No leer `.curlrc` |

## Otros

| Opción | Tipo | Descripción |
|--------|------|-------------|
| `--libcurl <file>` (G) | file | Escribir código C usando libcurl |
| `--aws-sigv4` | string | AWS Signature v4 (ya cubierto) |
| `--curves` | string | Curvas EC (ya cubierto) |
| `--metalink` | bool | Procesar archivo metalink |
| `--crlf` | bool | Convertir LF a CRLF en upload |
| `-B` / `--use-ascii` | bool | ASCII mode (FTP/SMTP) |
| `-t` / `--telnet-option <opt=val>` | string | Opción telnet |
| `--tftp-blksize <value>` | int | Tamaño bloque TFTP |
| `--tftp-no-options` | bool | TFTP sin options request |
| `--haproxy-protocol` | bool | Enviar HAProxy PROXY protocol |
| `--haproxy-clientip <ip>` | IP | Client IP en HAProxy PROXY |
| `--ipfs-gateway <URL>` | URL | IPFS gateway |
| `--disallow-username-in-url` | bool | Rechazar user:pass en URL |
| `-V` / `--version` | bool | Mostrar versión y protocolos |
| `-h` / `--help` | bool | Ayuda de categorías de opciones |
| `--help <category>` | string | Ayuda de categoría específica |

## Categorías para `--help <category>`

- `auth` - Autenticación
- `connection` - Conexión
- `curl` - El comando curl
- `dns` - DNS
- `file` - File:// URLs
- `ftp` - FTP
- `http` - HTTP y HTTPS
- `imap` - IMAP
- `ldap` - LDAP
- `output` - Output
- `pop3` - POP3
- `post` - POST
- `proxy` - Proxy
- `scp` - SCP
- `sftp` - SFTP
- `smtp` - SMTP
- `telnet` - TELNET
- `tftp` - TFTP
- `tls` - TLS
- `upload` - Upload
- `verbose` - Verbose/debug
- `websocket` - WebSocket

Ejemplo: `curl --help http`
