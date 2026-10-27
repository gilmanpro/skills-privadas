# Resumen rapido — clpctl v2

Vista de todos los comandos de la CLI de CloudPanel v2. Los **root commands** se ejecutan como root (o `sudo`); los **Site User commands** como usuario del sitio (via SSH: `john@server`).

## Root commands (`clpctl`)

| Comando | Descripcion |
|---|---|
| `cloudflare:update:ips` | Actualiza IPs de Cloudflare (cron diario 6 AM) |
| `cloudpanel:enable:basic-auth` | Activa Basic Auth en puerto 8443 |
| `cloudpanel:disable:basic-auth` | Desactiva Basic Auth en puerto 8443 |
| `db:show:master-credentials` | Muestra credenciales maestras de BD |
| `db:add` | Crea nueva base de datos |
| `db:export` | Exporta BD a dump (`.sql` o `.sql.gz`) |
| `db:import` | Importa dump a BD |
| `lets-encrypt:install:certificate` | Emite e instala certificado SSL gratuito |
| `site:add:nodejs` | Anade sitio Node.js |
| `site:add:static` | Anade sitio HTML estatico |
| `site:add:php` | Anade sitio PHP con vhost template |
| `site:add:python` | Anade sitio Python |
| `site:add:reverse-proxy` | Anade reverse proxy |
| `site:install:certificate` | Instala certificado SSL desde archivos |
| `site:delete` | Elimina un sitio |
| `user:add` | Anade usuario (admin/site-manager/user) |
| `user:delete` | Elimina un usuario |
| `user:list` | Lista todos los usuarios |
| `user:reset:password` | Resetea contrasena de usuario |
| `user:disable:mfa` | Desactiva 2FA de un usuario |
| `vhost-templates:import` | Importa/actualiza templates (cron diario) |
| `vhost-templates:list` | Lista templates disponibles |
| `vhost-template:add` | Anade template personalizado |
| `vhost-template:delete` | Elimina template personalizado |
| `vhost-template:view` | Muestra contenido de un template |

## Site User commands (`clpctl`)

| Comando | Descripcion |
|---|---|
| `system:permissions:reset` | Resetea permisos de archivos/directorios |
| `db:export` | Exporta BD del sitio |
| `db:import` | Importa dump a BD del sitio |
| `varnish-cache:purge` | Purga Varnish Cache (todo/tags/URL) |

## Flags comunes

| Flag | Proposito |
|---|---|
| `--domainName` | Dominio del sitio |
| `--siteUser` | Usuario del sitio |
| `--siteUserPassword` | Contrasena del usuario del sitio |
| `--force` | Forzar accion sin confirmacion |
| `--file` | Ruta al archivo (dump, template) |
| `--databaseName` | Nombre de la base de datos |

> Para los parametros obligatorios/opcionales exactos de cada comando, ver [parametros.md](parametros.md).
