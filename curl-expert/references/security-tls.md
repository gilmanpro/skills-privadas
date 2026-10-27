# Seguridad y TLS en curl

Guía completa sobre TLS, certificados, CA stores y verificación de servidores.

## ⚠️ Regla de oro: NUNCA uses `-k` (`--insecure`) en producción

`-k` deshabilita la verificación del certificado del servidor. Esto significa que un atacante puede hacer MITM (Man-in-the-Middle) sin que curl lo detecte.

```bash
# MAL (excepto en dev/testing local)
curl -k https://self-signed.local

# BIEN
curl https://self-signed.local --cacert my-ca.pem
```

## Verificación por defecto

Por defecto, curl:

1. Verifica la cadena de confianza del certificado del servidor contra la CA store local
2. Verifica que el certificado fue emitido para el hostname correcto (SAN/CN)
3. Verifica la firma criptográfica
4. (Si el backend lo soporta) Verifica que no esté revocado (CRL/OCSP)

Si cualquiera falla, curl rechaza la conexión con error.

## CA Store (almacén de certificados raíz)

### Por defecto, ¿dónde busca las CAs?

Depende de cómo fue compilado curl:

| Backend TLS | CA Store por defecto |
|-------------|----------------------|
| OpenSSL, BoringSSL, LibreSSL, wolfSSL | Archivo: `CURL_CA_BUNDLE` o compilado en |
| GnuTLS | Archivo |
| Schannel (Windows) | Windows certificate store (nativa) |
| Apple SecTrust | macOS Keychain (nativa) |
| Rustls | Mozilla bundle (Linux) o nativa (otros) |

### Opciones de configuración de CA store

```bash
# CA bundle personalizado
curl --cacert /path/to/ca-bundle.crt https://example.com

# Directorio de CAs (debe estar hasheado con c_rehash para OpenSSL)
curl --capath /path/to/ca-dir/ https://example.com

# CA store del sistema operativo
curl --ca-native https://example.com

# Combinar nativo + custom
curl --ca-native --cacert my-certs.pem https://example.com
```

### Variables de entorno

```bash
# Unix
export CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_DIR=/etc/ssl/certs

# Windows: busca curl-ca-bundle.crt en:
#   1. Application directory
#   2. Current working directory
#   3. System directory
#   4. Windows directory
#   5. PATH
```

### En Windows

Si curl fue construido con Schannel, usa el Windows certificate store (nativo, recomendado). Si usa OpenSSL:

```bash
# Buscar bundle
curl -v https://example.com 2>&1 | grep "CAfile:"
# Típicamente: C:\Program Files\curl\ssl\curl-ca-bundle.crt
```

Para usar el CA store de Windows con OpenSSL:
```bash
curl --ca-native https://example.com
```

## Certificados de cliente

curl puede autenticarse ante el servidor con un certificado de cliente.

```bash
# PEM (cert + key en archivos separados)
curl --cert client.pem --key client.key https://example.com

# PEM combinado (cert y key en el mismo archivo)
curl --cert combined.pem https://example.com

# PEM con passphrase
curl --cert combined.pem:myPassphrase https://example.com

# PKCS#12 / PFX
curl --cert client.p12:p12password --cert-type P12 https://example.com

# PKCS#11 (token hardware)
curl --cert "pkcs11:manufacturer-id=..." https://example.com

# Windows certificate store (Schannel)
curl --cert "CurrentUser\MY\thumbprint" https://example.com
```

## Credenciales

Guarda credenciales en `.netrc` con permisos 600 y léelas con `--netrc` / `-n` (o `--netrc-file <file>` para una ruta personalizada). **Nunca** pases credenciales en la línea de comandos (`-u user:pass`): quedan visibles en la lista de procesos (`ps`).

## Versiones de TLS

```bash
# Forzar versión específica
curl --tlsv1.0 URL   # TLS 1.0 (deprecado)
curl --tlsv1.1 URL   # TLS 1.1 (deprecado)
curl --tlsv1.2 URL   # TLS 1.2 (default en muchos casos)
curl --tlsv1.3 URL   # TLS 1.3 (más nuevo y rápido)

# Versión máxima permitida
curl --tls-max 1.3 https://example.com

# Debug de TLS handshake
curl -v https://example.com 2>&1 | grep -A 3 "TLS handshake"
```

### Cuál usar

- **TLS 1.3**: más rápido (1-RTT vs 2-RTT), más seguro, default moderno
- **TLS 1.2**: compatible con casi todo
- **TLS 1.0/1.1**: ❌ deprecados, no usar

## Cipher suites

```bash
# TLS 1.2 y anteriores
curl --ciphers "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256" https://example.com

# TLS 1.3 (diferente sintaxis)
curl --tls13-ciphers "TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256" https://example.com
```

Por defecto, curl usa los cipher suites que el backend TLS considere seguros. Personalizar solo si hay problemas de compatibilidad con servidores legacy.

### Curvas EC

```bash
curl --curves X25519:P-256:P-384 https://example.com
```

## Certificate Status / OCSP Stapling

```bash
# Verificar status del cert del servidor (OCSP stapling)
curl --cert-status https://example.com

# Skip revocation check (Schannel only)
curl --ssl-no-revoke https://example.com

# Best-effort revocation (no falla si no se puede verificar)
curl --ssl-revoke-best-effort https://example.com
```

## Pinning (HPKP-style)

Pinear la clave pública del servidor. Si cambia, curl rechaza la conexión.

```bash
# SHA256 del SubjectPublicKeyInfo (formato DER) o del certificado completo
curl --pinnedpubkey "sha256//base64encodedhash..." https://example.com

# Múltiples pins
curl --pinnedpubkey "sha256//hash1;sha256//hash2" https://example.com
```

Para obtener el hash:
```bash
# OpenSSL
openssl s_client -connect example.com:443 < /dev/null 2>/dev/null | \
  openssl x509 -pubkey -noout | \
  openssl pkey -pubin -outform der | \
  openssl dgst -sha256 -binary | \
  openssl enc -base64
```

## HTTPS Proxy

Si el proxy también usa HTTPS, las opciones TLS del proxy son **separadas**:

```bash
# Conexión al proxy: --proxy-insecure, --proxy-cacert
# Conexión al server final: --insecure, --cacert
curl --proxy https://proxy.example.com:443 \
     --proxy-cacert proxy-ca.pem \
     --cacert server-ca.pem \
     --proxy-user proxyuser:proxypass \
     https://target.example.com/
```

## Certificados autofirmados (desarrollo local)

```bash
# Opción 1: agregar al CA store del sistema
sudo cp my-dev-ca.crt /usr/local/share/ca-certificates/
sudo update-ca-certificates

# Opción 2: usar --cacert para este comando
curl --cacert my-dev-ca.crt https://dev.local

# Opción 3: variable de entorno
export CURL_CA_BUNDLE=/path/to/my-dev-ca.crt
curl https://dev.local
```

## Debugging TLS

```bash
# Ver handshake completo
curl -v https://example.com 2>&1 | grep -A 1 "SSL connection\|SSL certificate\|TLS\|Verify"

# Output típico útil:
# * TLSv1.3 (OUT), TLS handshake, Client hello (1):
# * TLSv1.3 (IN), TLS handshake, Server hello (2):
# * TLSv1.3 (IN), TLS handshake, Certificate (11):
# * TLSv1.3 (IN), TLS handshake, CERT verify (15):
# * TLSv1.3 (IN), TLS handshake, Finished (20):
# * SSL connection using TLS_AES_256_GCM_SHA384
# * SSL certificate verify ok.

# Test SSL detallado con openssl
openssl s_client -connect example.com:443 -servername example.com -showcerts

# Forzar versión TLS para debug
curl --tlsv1.2 -v https://example.com 2>&1 | grep "SSL\|TLS"
```

## Errores comunes y soluciones

### `SSL certificate problem: unable to get local issuer certificate`

El certificado del servidor está firmado por una CA que curl no conoce.

**Soluciones**:
1. Actualizar CA bundle: descargar versión reciente de https://curl.se/docs/caextract.html
2. Usar `--cacert` con la CA específica
3. Si el cert está en el sistema: `--ca-native` (o configurar `CURL_CA_BUNDLE`)

### `SSL certificate problem: certificate has expired`

El certificado del servidor expiró (o tu reloj está mal).

**Soluciones**:
1. Verificar fecha del sistema: `date`
2. Esperar renovación del cert (no es problema tuyo)
3. Si es dev local: regenerar cert

### `SSL: no alternative certificate type available`

curl no encuentra el cert de cliente correcto.

**Soluciones**:
1. Verificar formato (PEM, P12, etc.)
2. Verificar passphrase
3. Verificar permisos de lectura del archivo

### `gnutls_handshake() failed`

Problema en el handshake TLS (versión, ciphers, etc.).

**Soluciones**:
1. Probar con `--tlsv1.2` o `--tlsv1.3` explícito
2. Probar con `--ciphers` específico
3. Verificar que el server soporte TLS moderno
4. `curl -v` para ver el detalle

### `OpenSSL SSL_read: SSL_ERROR_SYSCALL`

Conexión interrumpida durante TLS.

**Soluciones**:
1. Verificar firewall
2. Probar con `--max-time` mayor
3. Verificar conectividad con `openssl s_client`

## HSTS (HTTP Strict Transport Security)

curl puede recordar HSTS y forzar HTTPS:

```bash
# Habilitar HSTS (recordar dominios HTTPS-only)
curl --hsts ~/.cache/curl/hsts.txt https://example.com

# Almacenar en el archivo especificado
curl --hsts /path/to/hsts.txt https://example.com
```

Una vez guardado, futuros requests al dominio serán forzados a HTTPS.

## Alt-Svc (HTTP/3 discovery)

```bash
# Permitir que curl descubra HTTP/3 via Alt-Svc
curl --alt-svc altsvc.cache https://curl.se

# Próxima request usará HTTP/3 si está disponible
curl --alt-svc altsvc.cache https://curl.se
```

## ECH (Encrypted Client Hello)

TLS 1.3 extension para cifrar el SNI (oculta qué dominio se visita).

```bash
curl --ech "cloudflare" https://example.com
```

(Soporte experimental; requiere TLS backend con soporte ECH).

## Resumen de buenas prácticas

1. ✅ Usa siempre HTTPS con verificación
2. ✅ Mantén el CA bundle actualizado
3. ✅ Prefiere TLS 1.3 / 1.2
4. ✅ Usa `--ca-native` en macOS/Windows
5. ✅ Para pinning: usa `--pinnedpubkey`
6. ✅ Habilita HSTS y Alt-Svc
7. ✅ Guarda credenciales en `.netrc` con permisos 600; nunca en la línea de comandos (visibles en `ps`)
8. ❌ NUNCA `-k` en producción
9. ❌ NUNCA `SSL_CERT_FILE=""` o equivalente
10. ⚠️ Cert pinning puede romper rotación de certs (úsalo con cuidado)
