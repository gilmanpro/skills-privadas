# Diferencias con wget y conversión a curl

Usar cuando el usuario llegue con un comando `wget` que quiere convertir a `curl`, o dude de si la tarea corresponde a cada herramienta.

## curl vs wget

| Característica | curl | wget |
|----------------|------|------|
| Recursivo | ❌ No (intencional) | ✅ Sí |
| Pipes a stdout | ✅ Por defecto | ⚠️ Con `-O -` |
| Múltiples protocolos | ✅ 30+ esquemas | ⚠️ HTTP/HTTPS/FTP |
| Uploads | ✅ PUT, POST, multipart | ⚠️ Limitado |
| Pipes stdin → POST | ✅ `-d @-` | ❌ |
| Configuración | `.curlrc` | `.wgetrc` |
| Rango de bytes | ✅ `-r` | ⚠️ Limitado |
| En scripts | ✅ Diseñado para esto | ✅ También |

## Conversión rápida wget → curl

- `wget URL` → `curl -O URL`
- `wget -O file URL` → `curl -o file URL`
- `wget --header "X: y" URL` → `curl -H "X: y" URL`
- `wget --post-data "a=b" URL` → `curl -d "a=b" URL`

Para scraping recursivo, wget sigue siendo la herramienta adecuada: curl no descargará sitios.
