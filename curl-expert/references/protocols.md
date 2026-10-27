# Protocolos soportados por curl

curl soporta más de 30 protocolos/esquemas. Aquí los detalles de cada uno.

## HTTP / HTTPS (los más comunes)

### Métodos

curl selecciona el método según las opciones:
- Sin opciones de envío → **GET**
- `-d` / `--data` / `-F` / `--form` → **POST**
- `-I` / `--head` → **HEAD**
- `-T` / `--upload-file` → **PUT**
- `-X <METHOD>` → fuerza el método (pero no cambia el comportamiento; ver abajo)

**Importante**: `-X POST` no convierte un GET a POST. Solo cambia el verbo pero curl no envía body. Para enviar POST real usa `-d` o `-F` (con o sin `-X POST`).

### HTTP/0.9, 1.0, 1.1, 2, 3

- HTTP/0.9: respuestas sin headers (legacy)
- HTTP/1.0: simple, sin keepalive
- HTTP/1.1: estándar, con chunked, keepalive, etc.
- HTTP/2: binario, multiplexado, server push, header compression (HPACK)
- HTTP/3: sobre QUIC (UDP), 0-RTT posible

### Selección de versión

```bash
curl --http1.0 URL              # Forzar HTTP/1.0
curl --http1.1 URL              # Forzar HTTP/1.1
curl --http2 URL                # Negociar HTTP/2 vía ALPN (TLS)
curl --http2-prior-knowledge URL  # HTTP/2 sin TLS (cleartext, h2c)
curl --http3 URL                # HTTP/3 con fallback
curl --http3-only URL           # Solo HTTP/3
```

### HTTP/2 features

- Multiplexado: múltiples requests en una conexión
- Server push: servidor puede enviar recursos adicionales
- Header compression: HPACK
- Stream prioritization

### HTTP/3 (QUIC)

**Estado**: experimental en algunos backends (quiche), estable con ngtcp2.

```bash
# Solo HTTP/3
curl --http3-only https://example.com

# HTTP/3 con fallback
curl --http3 https://example.com

# HTTP/3 con upgrade via Alt-Svc
curl --alt-svc altsvc.cache https://example.com
```

**HTTPS eyeballing** (similar a IPv4/v6 happy eyeballs):
- Hard timeout (default 200ms): abrir TLS/TCP en paralelo
- Soft timeout (default 100ms): empezar paralelo si no hay data aún
- Transferencia falla solo si AMBOS (HTTP/3 y HTTP/1-2) fallan

Configurable con `--happy-eyeballs-timeout-ms <ms>`.

### HTTPS / TLS

```bash
# Verificar (default)
curl https://secure.example.com

# Skip verificación (PELIGROSO, solo dev)
curl -k https://self-signed.local

# CA personalizada
curl --cacert my-ca.pem https://example.com

# Cert de cliente
curl --cert client.pem --key client.key https://example.com

# Forzar TLS 1.3
curl --tlsv1.3 https://example.com
```

### Cookies

Ver `cookies.md` para detalles.

### HTTP Authentication

| Método | Descripción | Default |
|--------|-------------|---------|
| Basic | Base64(user:pass), sin encriptación adicional | ✅ (default) |
| Digest | Hash-based, más seguro que Basic | `--digest` |
| NTLM | Windows authentication | `--ntlm` |
| Negotiate (SPNEGO) | Kerberos | `--negotiate` |
| Bearer | OAuth2 token | `--oauth2-bearer` |
| AWS SigV4 | AWS API | `--aws-sigv4` |

```bash
# Auto-negociar el más seguro
curl --anyauth -u user:pass https://example.com
```

## FTP / FTPS

File Transfer Protocol clásico. curl puede actuar como cliente FTP completo.

### Modos de conexión

- **Activo** (PORT): servidor se conecta al cliente (problemático con NAT/firewalls)
- **Pasivo** (PASV): cliente se conecta al servidor (default, recomendado)

### FTPS (FTP over SSL/TLS)

Dos variantes:
- **Implícito** (raro): `ftps://` (puerto 990)
- **Explícito** (recomendado): `ftp://` + `--ssl-reqd` (puerto 21)

```bash
# FTP simple
curl ftp://ftp.example.com/pub/

# Con autenticación
curl -u user:pass ftp://ftp.example.com/

# Listar directorio
curl --list-only ftp://ftp.example.com/dir/

# Descargar
curl -O ftp://ftp.example.com/path/file.zip

# Subir
curl -T localfile.zip -u user:pass ftp://ftp.example.com/upload/

# FTPS explícito
curl --ssl-reqd -u user:pass ftp://secure.example.com/file

# FTPS implícito
curl -u user:pass ftps://secure.example.com/file

# Crear directorios remotos
curl --ftp-create-dirs -T local.txt ftp://ftp.example.com/new/dir/file.txt

# Append (no overwrite)
curl -T appendfile -a ftp://ftp.example.com/file.txt

# Comando pre-transfer
curl -Q "DELE oldfile" ftp://ftp.example.com/
```

### PATH en FTP

La ruta es relativa al directorio home del usuario, NO al root:
```bash
# Archivo README en home dir
curl ftp://user:pass@ftp.example.com/README

# Root absoluto (con // extra)
curl ftp://user:pass@ftp.example.com//absolute/path/README
```

### Modos de operación FTP

- **multicwd** (default): cambia a cada directorio
- **singlecwd**: cambia al dir raíz una vez
- **nocwd**: usa CWD para navegación

Configurable con `--ftp-method`.

## SFTP (SSH File Transfer Protocol)

Transferencia de archivos sobre SSH. **No es FTP sobre SSH** (eso es SFTP=SSH File Transfer, no FTPS).

```bash
# Listar directorio home
curl sftp://user@server.example.com/

# Directorio específico (absoluto en el server)
curl sftp://user@server.example.com/home/user/documents/

# Path relativo al home
curl -u user sftp://server.example.com/~/file.txt

# Descargar
curl -u user sftp://server.example.com/path/file.txt -o local.txt

# Subir
curl -T local.txt -u user sftp://server.example.com/path/

# Con clave SSH
curl -u user --key ~/.ssh/id_ed25519 sftp://server.example.com/

# Con clave y passphrase
curl -u user --key ~/.ssh/id_rsa --pass "myPassphrase" sftp://server.example.com/

# Con clave pública explícita (si curl no la extrae)
curl -u user --key ~/.ssh/id_rsa --pubkey ~/.ssh/id_rsa.pub sftp://server.example.com/
```

### Host key verification

```bash
# Verificar SHA256 del host pub key
curl --hostpubsha256 "abc123..." sftp://server.example.com/

# O MD5 (legacy)
curl --hostpubmd5 "abc123..." sftp://server.example.com/
```

⚠️ curl NO usa `known_hosts` por defecto. Usa `--hostpubsha256` o `--hostpubmd5` para verificación manual.

## SCP (Secure Copy Protocol sobre SSH)

```bash
# Descargar
curl -u user: --key ~/.ssh/id_rsa scp://server.example.com/~/file.txt

# Subir
curl -T local.txt -u user --key ~/.ssh/id_rsa scp://server.example.com/~/path/

# Path absoluto (no relativo al home)
curl -u user scp://server.example.com//etc/passwd
```

Nota: En SCP, `~/` indica home dir del usuario en el server. Sin `~`, el path es absoluto.

## SMB / SMBS (Server Message Block)

Samba / Windows file sharing. **Solo SMB v1** (limitación importante).

```bash
# Formato: smb://[domain;][user[:password]@]server/share/path

# Descargar
curl -u "user:pass" smb://server.example.com/share/file.txt

# Con dominio Windows
curl -u "DOMAIN\user:pass" smb://server.example.com/share/file.txt

# Subir
curl -T localfile.txt -u "user:pass" smb://server.example.com/share/

# SMBS (sobre TLS)
curl -u "user:pass" smbs://server.example.com/share/file.txt
```

⚠️ SMBv1 es inseguro. Usar solo en LANs confiables.

## LDAP / LDAPS

Lightweight Directory Access Protocol.

```bash
# Búsqueda LDAP
curl "ldap://ldap.example.com/o=My%20Organization"

# Solo atributo específico
curl "ldap://ldap.example.com/o=My%20Organization?postalAddress"

# Con autenticación
curl -u user:pass "ldap://ldap.example.com/o=My%20Organization?sub?mail=*"

# LDAPS (TLS)
curl -u user:pass "ldaps://ldap.example.com/o=Org??sub?mail=*"
```

Formato URL LDAP: `ldap://host:port/dn?attributes?scope?filter?extensions`

- `dn`: Distinguished Name
- `attributes`: separados por coma
- `scope`: `base`, `one`, `sub`
- `filter`: filtro de búsqueda

## MQTT

Message Queuing Telemetry Transport - protocolo IoT pub/sub.

```bash
# Suscribirse a un topic (download)
curl mqtt://broker.example.com/topic/sensor/temperature

# Publicar en un topic (upload)
curl -T payload.txt mqtt://broker.example.com/topic/sensor/temperature

# Especificar versión MQTT
curl mqtt://broker.example.com/topic?version=5
```

⚠️ MQTT sobre TLS **no soportado aún** (limitante de curl).

## IMAP / IMAPS

Internet Message Access Protocol - leer correo.

```bash
# Listar buzones del usuario
curl imap://user:pass@mail.example.com

# Listar mensajes del INBOX
curl imap://user:pass@mail.example.com/INBOX

# Fetch mensaje específico por UID
curl imap://user:pass@mail.example.com/INBOX/;UID=1

# Fetch texto del mensaje 3
curl imap://user:pass@mail.example.com/INBOX/;UID=3;SECTION=TEXT

# Buscar
curl imap://user:pass@mail.example.com/INBOX?SUBJECT%20hello
```

Ver URL syntax para opciones IMAP completas.

## POP3 / POP3S

Post Office Protocol - descargar correo.

```bash
# Listar mensajes
curl pop3://user:pass@mail.example.com

# Descargar mensaje 1
curl pop3://user:pass@mail.example.com/1

# POP3S (TLS)
curl pop3s://user:pass@mail.example.com
```

## SMTP / SMTPS

Simple Mail Transfer Protocol - enviar correo.

```bash
# Enviar correo (asume stream local RFC 5322)
curl smtp://smtp.example.com --mail-from from@example.com --mail-rcpt to@example.com -T email.txt

# Con autenticación
curl -u user:pass smtp://smtp.example.com --mail-from from@example.com --mail-rcpt to@example.com -T email.txt

# SMTPS (TLS, puerto 465)
curl smtps://smtp.example.com ...

# Con STARTTLS (puerto 587)
curl --ssl-reqd smtp://smtp.example.com:587 ...
```

## Telnet

Sesión telnet interactiva.

```bash
# Conectar
curl telnet://server.example.com

# Con opciones de negociación
curl -t TTYPE=vt100 telnet://server.example.com
```

curl lee stdin y envía al server, lo que recibe lo muestra en stdout.

## DICT

Protocolo de diccionario.

```bash
# Buscar palabra
curl dict://dict.org/m:curl

# Definir palabra
curl dict://dict.org/d:curl

# Alias: m=match, find; d=define, lookup
curl dict://dict.org/find:curl
```

## TFTP

Trivial File Transfer Protocol - muy simple, sin autenticación.

```bash
# Descargar
curl tftp://server.example.com/file

# Subir
curl -T local.txt tftp://server.example.com/file
```

## FILE

Archivos locales (en el mismo equipo).

```bash
# Leer archivo
curl file:///etc/hostname

# Escribir archivo (con -T)
curl -T local.txt file:///tmp/upload.txt
```

⚠️ Solo hostnames `localhost`, `127.0.0.1` o vacío. Por seguridad.

## Gopher / Gophers

Protocolo Gopher (legacy). Útil para tests o protocolos restringidos sobre HTTP.

```bash
curl gopher://gopher.example.com/0/path/to/resource
curl gophers://gopher.example.com/0/path
```

## WebSocket (ws:// / wss://)

⚠️ **Estado**: experimental. Solo soportado en libcurl API, no totalmente expuesto en la línea de comandos.

```bash
# Comando (experimental)
curl --include --no-buffer \
  --header "Connection: Upgrade" \
  --header "Upgrade: websocket" \
  --header "Sec-WebSocket-Version: 13" \
  --header "Sec-WebSocket-Key: $(head -c 16 /dev/urandom | base64)" \
  https://echo.websocket.org
```

Mejor uso: a través de libcurl programáticamente.

## RTSP (Real Time Streaming Protocol)

Para streaming de medios (cámaras, audio/video).

```bash
curl rtsp://camera.example.com/stream
```

Solo RTSP 1.0.

## SSH (sin sub-protocolo)

No confundir: `ssh://` no es un esquema soportado directamente. Usa `sftp://` o `scp://`.
