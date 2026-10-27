# Sintaxis de URLs en curl

curl sigue "RFC 3986 plus" - es decir, RFC 3986 con algunas extensiones pragmáticas.

## Estructura de una URL

```
[scheme][//][userinfo@]hostname[:port][/path][?query][#fragment]
```

Ejemplo completo:
```
https://user:password@www.example.com:443/path/to/file?key=value#section
└─┬──┘  └┬┘ └────┬────┘ └─┬─┘ └──┬──┘ └─┬─┘ └──┬──┘ └──┬──┘
scheme   //  userinfo    host   port   path   query  fragment
```

## Componentes

### Scheme (esquema)

Define el protocolo. Case-insensitive.

Esquemas soportados para transferencias:
- `dict`, `file`, `ftp`, `ftps`, `gopher`, `gophers`, `http`, `https`
- `imap`, `imaps`, `ldap`, `ldaps`, `mqtt`, `pop3`, `pop3s`
- `rtsp`, `smb`, `smbs`, `smtp`, `smtps`, `telnet`, `tftp`
- `ws`, `wss`

Esquemas para proxies:
- `http`, `https`, `socks4`, `socks4a`, `socks5`, `socks5h`, `socks`

### Userinfo (usuario:contraseña)

⚠️ **Desaconsejado**: la contraseña va en texto plano.

```bash
# NO recomendado (visible en logs)
curl https://user:pass@example.com/

# Mejor: -u
curl -u user:pass https://example.com/

# O netrc
curl -n https://example.com/
```

### Hostname

Puede ser:
- Nombre de dominio: `www.example.com`
- IPv4: `192.168.1.1` (acepta formatos octal, hex, parciales)
- IPv6: `[2001:db8::1]` (siempre con corchetes)
- Localhost: `localhost` (resuelve a 127.0.0.1 / ::1)

Libcurl rechaza hostnames con más de un punto final (ej: `example..com`).

### Puerto

1-65535. Si se omite, usa el default del esquema:
- HTTP: 80, HTTPS: 443
- FTP: 21, FTPS: 990
- SFTP/SCP: 22
- SMTP: 25, SMTPS: 465
- IMAP: 143, IMAPS: 993
- POP3: 110, POP3S: 995
- LDAP: 389, LDAPS: 636
- MQTT: 1883
- SMB: 445
- DICT: 2628
- TELNET: 23
- TFTP: 69
- GOPHER/GOPHERS: 70
- WS: 80, WSS: 443

```bash
# Puerto en URL
curl https://example.com:8443/

# Puerto vacío (usa default)
curl https://example.com:/
```

### Path

Por defecto, curl normaliza `/./` y `/..//` (per RFC 3986).

```bash
# Se normaliza a /api/users
curl https://example.com/api/../api/users
```

Con `--path-as-is`, NO se normaliza.

### Query string

`?key1=value1&key2=value2`. Caracteres especiales deben URL-encode.

```bash
# URL encoding manual
curl "https://api.example.com/search?q=hello%20world"

# Con --data-urlencode (en POST)
curl --data-urlencode "q=hello world" -G https://api.example.com/search

# --url-query añade a URL existente
curl "https://api.example.com/search" --url-query "q=hello world"
```

### Fragment

`#fragment` - generalmente ignorado por curl (se envía al server, pero el server no lo usa).

## Variaciones de curl vs specs

### Espacios

No permitidos en URLs. Deben ser URL-encoded (`%20`).

```bash
# MAL
curl "https://example.com/path with spaces"

# BIEN
curl "https://example.com/path%20with%20spaces"
```

Excepción: curl re-encodifica espacios en headers `Location:` de redirects.

### No-ASCII

Bytes fuera del rango ASCII son automáticamente percent-encoded.

```bash
# "café" → "caf%C3%A9"
curl "https://example.com/café"
```

### Múltiples slashes

RFC 3986 requiere `://` (dos slashes) tras el scheme. curl acepta 1, 2 o 3 slashes.

```bash
# Todos válidos en curl
curl http:/example.com
curl http://example.com
curl http:///example.com
```

### Scheme-less (sin esquema)

curl "adivina" el esquema según el prefijo del hostname:

| Prefijo | Esquema asumido |
|---------|-----------------|
| `ftp.` | FTP |
| `dict.` | DICT |
| `ldap.` | LDAP |
| `imap.` | IMAP |
| `smtp.` | SMTP |
| `pop3.` | POP3 |
| otros | HTTP |

```bash
# Asume HTTP
curl www.example.com

# Asume FTP
curl ftp.example.com
```

### Globbing letters

`{...}` y `[...]` son interpretadas como globbing en la línea de comandos:

```bash
# Globbing
curl "https://example.com/file[1-10].txt"
curl "https://example.com/{a,b,c}.jpg"

# Desactivar globbing
curl -g "https://example.com/path[a-b]"  # o --globoff
```

#### Globbing avanzado

```bash
# Con padding de ceros
curl -O "https://example.com/file[001-100].txt"

# Secuencia alfabética
curl -O "https://example.com/file[a-z].txt"

# Con step (1, 11, 21, ...)
curl -O "https://example.com/file[1-100:10].txt"

# Combinar patrones en una misma URL
curl -O "https://example.com/archive[1996-1999]/vol[1-4]/part{a,b,c}.html"
```

⚠️ **Siempre cita URLs con globbing en la shell** (corchetes y llaves son especiales).

## Comportamiento específico por esquema

### FTP

Path es relativo al directorio del usuario, no al root.

```bash
# README en home dir
curl ftp://user:pass@ftp.example.com/README

# Path absoluto (root del server) - doble slash
curl ftp://user:pass@ftp.example.com//etc/file
```

### FILE

Solo ciertos hostnames permitidos:
- `localhost`
- `127.0.0.1`
- (vacío)

```bash
# Válido
curl file:///etc/hostname
curl file://localhost/etc/hostname

# Inválido
curl file://example.com/etc/hostname
```

En Windows, soporta `file:///C:/path` con drive letter.

### IMAP

El path es muy rico: mailbox, UID, SECTION, PARTIAL, etc.

```bash
# Listar buzones
imap://user:pass@mail.example.com

# Listar INBOX
imap://user:pass@mail.example.com/INBOX

# Fetch mensaje por UID
imap://user:pass@mail.example.com/INBOX/;UID=1

# Validar UIDVALIDITY
imap://user:pass@mail.example.com/INBOX;UIDVALIDITY=50/;UID=2

# Fetch texto
imap://user:pass@mail.example.com/INBOX/;UID=3;SECTION=TEXT

# Bytes parciales
imap://user:pass@mail.example.com/INBOX/;UID=4;PARTIAL=0.1024

# Buscar
imap://user:pass@mail.example.com/INBOX?TEXT%20%22foo%20bar%22
```

### LDAP

Path = DN, attributes, scope, filter, extensions, separados por `?`:

```bash
# Búsqueda simple
ldap://ldap.example.com/o=My%20Org

# Solo atributo
ldap://ldap.example.com/o=My%20Org?postalAddress

# Active Directory
ldap://ldap.example.com/?rootDomainNamingContext
```

### SMB

Path incluye share y path:

```bash
# Formato: smb://[domain;]user:pass@server/share/path
curl -u "user:pass" smb://server/share/file.txt
```

⚠️ Solo SMBv1 (inseguro).

### SCP/SFTP

Path absoluto o `~/` para home:

```bash
# Absoluto
curl sftp://server/etc/passwd

# Relativo al home
curl sftp://server/~/documents/file.txt
```

### SMTP

Path = hostname a presentar al server (HELO/EHLO):

```bash
smtp://smtp.example.com  # usa hostname local
smtp://smtp.example.com/my-hostname.example.com  # usa este
```

## URL y variables de entorno

```bash
# NO_PROXY: lista de hosts que no usan proxy
export NO_PROXY="localhost,127.0.0.1,.local,.example.com"
# El punto inicial ".example.com" incluye subdominios

# http_proxy (Unix-style)
export http_proxy="http://proxy.example.com:8080"
```

## Path encoding

curl normaliza algunas secuencias percent-encoded a mayúsculas:

```bash
# %2f → %2F
curl https://example.com/%2f
```

Con `--path-as-is`, NO normaliza.

## Caracteres reservados (RFC 3986)

Caracteres que DEBEN URL-encode en una URL:

| Caracteres | Motivo |
|------------|--------|
| Espacio | Delimitador |
| `< > " ` | Delimitadores URL/HTML |
| `{ } \| \\ ^` ` | Inseguros o especiales |
| `[ ]` | Usados para IPv6/globbing |
| `?` | Inicio de query |
| `#` | Inicio de fragment |
| `%` | Inicio de encoding |
| `&` | Separador de query params |

## URL completa vs `-d -G` (query string)

```bash
# Opción 1: URL completa (URL-encode manual)
curl "https://api.example.com/search?q=hello%20world&page=1"

# Opción 2: -G convierte -d a query string (auto-encoding)
curl -G --data-urlencode "q=hello world" --data-urlencode "page=1" https://api.example.com/search
```

Ambas son equivalentes. La opción 2 es más legible y evita errores de encoding.

## Errores comunes

### "URL using bad/illegal format or missing URL"

Causas:
- Espacios sin codificar
- Caracteres especiales sin codificar
- Falta el scheme

```bash
# MAL
curl https://example.com/path with spaces

# BIEN
curl "https://example.com/path%20with%20spaces"
```

### "Protocol 'xyz' not supported or disabled in libcurl"

El scheme no está compilado en esta build de curl.

```bash
# Ver esquemas soportados
curl --version
# Última línea: "Protocols: dict file ftp ftps ..."
```

### Globbing no deseado

```bash
# MAL: la shell puede expandir las llaves
curl https://example.com/{a,b,c}.txt

# BIEN: comillas
curl "https://example.com/{a,b,c}.txt"

# O desactivar globbing de curl
curl -g "https://example.com/{a,b,c}.txt"
```

### IPv6 con corchetes

Los corchetes `[ ]` son especiales en la shell y para globbing.

```bash
# Comillas siempre
curl "https://[2001:db8::1]/"

# Con --globoff si hay [] en la URL
curl -g "https://[2001:db8::1]/"
```
