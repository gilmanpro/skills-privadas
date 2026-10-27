---
name: cloudpanel-cli
description: "Skill de la CLI de CloudPanel (clpctl) v2: actualizar IPs de Cloudflare, Basic Auth, bases de datos (crear/exportar/importar/credenciales), certificados Let's Encrypt, sitios PHP/Node.js/Static/Python/Reverse Proxy, usuarios admin/site-manager (listar, reset password, desactivar 2FA), vhost templates y comandos de site user (Varnish, permisos, export/import db). Activar SIEMPRE que el usuario mencione clpctl, CloudPanel o cualquier administracion de un servidor CloudPanel, aunque no nombre la CLI."
---

# cloudpanel-cli — clpctl v2

Guia de comandos de CloudPanel v2. Todos se ejecutan como **root** (o `sudo`), salvo los **Site User Commands** que se ejecutan como usuario del sitio.

## Cuándo usar

- Crear/modificar sitios (Node.js, PHP, Python, static, reverse proxy)
- Gestionar bases de datos, SSL, usuarios y permisos
- Configurar Cloudflare, Varnish cache y vhost templates
- Automatizar administración de servidores CloudPanel

> **Referencias:** [Root commands](https://www.cloudpanel.io/docs/v2/cloudpanel-cli/root-user-commands/) · [Site User](https://www.cloudpanel.io/docs/v2/cloudpanel-cli/site-user-commands/)

## Antes de empezar

1. Registrar el dominio y tener la IP del servidor
2. Configurar DNS: Registro A (`@` → IP) y www, CNAME (`*` → `@`) opcional
3. SSL: si usas Cloudflare con proxy (nube naranja), no necesitas Let's Encrypt. Si usas DNS-only, si.

## Puerto disponible (Node.js/Python/Proxy)

Los comandos `site:add:*` con `--appPort` necesitan un puerto libre. Reservalo ANTES de crear el sitio:

```bash
curl -s 'https://puertos-api.gilman.pro/api/ports/available?count=1'
# → {"from": 25095, "to": 25095, "count": 1}  → usa 25095 como --appPort
```

- `count=N` devuelve un rango consecutivo `from`–`to`; con `count=1` usa `from` como `--appPort`
- Si el primer request falla, reintenta (los puertos se reservan al solicitarlos); como respaldo usa el panel `https://puertos-disponibles.gilman.pro/`
- Verificar que la API responde: `curl -s https://puertos-api.gilman.pro/api/health` → `{"status": "ok"}`
- El escaneo cubre TCP LISTEN en 10001–65535, asi que el puerto devuelto esta libre

## Comandos por seccion

### 1. Cloudflare
```bash
clpctl cloudflare:update:ips   # Actualiza IPs de Cloudflare (cron diario 6 AM)
```

El comando actualiza el archivo `/etc/nginx/cloudflare/ips`. Si en la seguridad del sitio activaste la opcion **"Allow traffic from Cloudflare only"**, ese archivo se incluye en el vhost del sitio para restringir el trafico solo a las IPs de Cloudflare.

### 2. Basic Auth

Protege el panel de CloudPanel (puerto **8443**) con autenticacion basica HTTP como capa adicional de seguridad. Util cuando **no tienes una IP estatica** para cerrar el puerto.

```bash
clpctl cloudpanel:enable:basic-auth --userName=john.doe --password='password123'
clpctl cloudpanel:disable:basic-auth
```

### 3. Base de Datos
```bash
clpctl db:show:master-credentials                          # Ver credenciales maestras
clpctl db:add --domainName=www.domain.com --databaseName=my-db --databaseUserName=john --databaseUserPassword='!pass!'
clpctl db:export --databaseName=my-db --file=dump.sql.gz   # Exportar
clpctl db:import --databaseName=my-db --file=dump.sql.gz   # Importar (desde el dir del dump)
```

`db:show:master-credentials` muestra **Host**, **User Name**, **Password** y **Puerto** de la base de datos del servidor, con el comando listo para copiar y conectar. Salida tipica:

```
Host: 127.0.0.1
User Name: root
Password: ************
Port: 3306
```

En `db:export`, si el archivo termina en `.sql.gz` se comprime con **gzip automaticamente**; si termina en `.sql`, queda **sin comprimir**:

```bash
clpctl db:export --databaseName=my-db --file=dump.sql      # sin comprimir
```

### 4. Let's Encrypt
```bash
clpctl lets-encrypt:install:certificate --domainName=www.domain.com
clpctl lets-encrypt:install:certificate --domainName=www.domain.com --subjectAlternativeName=dom1.com,dom2.com
```
Si ingresas `www.domain.com`, emite certificado para `domain.com` y `www.domain.com`.

Asegurate de tener **registros DNS validos** apuntando al servidor para los dominios antes de emitir el certificado. `--subjectAlternativeName` es **opcional** e incluye dominios adicionales (SAN).

### 5. Sitios (Site)

| Tipo | Comando |
|------|---------|
| Node.js | `clpctl site:add:nodejs --domainName=www.dom.com --nodejsVersion=22 --appPort=3000 --siteUser=john --siteUserPassword='!pass!'` |
| Static | `clpctl site:add:static --domainName=www.dom.com --siteUser=john --siteUserPassword='!pass!'` |
| PHP | `clpctl site:add:php --domainName=www.dom.com --phpVersion=8.4 --vhostTemplate='Generic' --siteUser=john --siteUserPassword='!pass!'` |
| Python | `clpctl site:add:python --domainName=www.dom.com --pythonVersion=3.9 --appPort=8080 --siteUser=john --siteUserPassword='!pass!'` |
| Reverse Proxy | `clpctl site:add:reverse-proxy --domainName=www.dom.com --reverseProxyUrl='http://127.0.0.1:8000' --siteUser=john --siteUserPassword='!pass!'` |
| Cert SSL (archivo) | `clpctl site:install:certificate --domainName=www.dom.com --privateKey=/path/key --certificate=/path/cert --certificateChain=/path/chain` (opcional) |
| Eliminar | `clpctl site:delete --domainName=www.domain.com [--force]` |

**Versiones Node disponibles:** 22, 20, 18, 16, 14, 12 LTS. Gestionadas con [nvm](https://github.com/nvm-sh/nvm).

**Python:** en **Ubuntu 22.04** usa Python **3.10**, que es la version estandar del sistema.

**site:delete** pide confirmacion escribiendo `yes`; con `--force` se elimina sin confirmacion.

**Origen de los vhost templates:** los templates importados provienen del repositorio oficial [cloudpanel-io/vhost-templates](https://github.com/cloudpanel-io/vhost-templates/tree/master/v2), que se actualiza cada noche automaticamente.

### 6. Usuarios

```bash
# Admin (acceso total)
clpctl user:add --userName='john.doe' --email='john@dom.com' --firstName='John' --lastName='Doe' --password='!pass!' --role='admin' --timezone='UTC' --status='1'

# Site Manager (gestiona sitios)
clpctl user:add --userName='john.doe' --email='john@dom.com' --firstName='John' --lastName='Doe' --password='!pass!' --role='site-manager' --timezone='UTC' --status='1'

# User (restringido a sitios)
clpctl user:add --userName='john.doe' --email='john@dom.com' --firstName='John' --lastName='Doe' --password='!pass!' --role='user' --sites='dom.com,dom.io' --timezone='UTC' --status='1'

clpctl user:delete --userName='john.doe'
clpctl user:list
clpctl user:reset:password --userName=john.doe --password='!newPass!'
clpctl user:disable:mfa --userName=john.doe
```

**Semantica de valores:** `--status` `1` = activo / `0` = inactivo. `--sites` (dominios separados por coma) **solo aplica a `role=user`**. `--timezone` admite zonas como `UTC` o `America/Panama`. Tabla completa en `references/parametros.md`.

### 7. Vhost Templates

```bash
clpctl vhost-templates:import                    # Actualizar templates (cron diario)
clpctl vhost-templates:list                      # Listar templates disponibles
clpctl vhost-template:add --name='App' --file=/tmp/template.tpl   # Desde archivo
clpctl vhost-template:add --name='App' --file=https://gist.githubusercontent.com/swieczorek/1c344ca356118c45b7c1b7393cc00abc/raw/007ff01dff96978be65dca212990ac20f6fd16be/gistfile1.txt  # Desde URL
clpctl vhost-template:delete --name='App'
clpctl vhost-template:view --name='App'
```

**Estructura del template:** La primera linea debe ser un comentario JSON: `#{"rootDirectory":"public","phpVersion":"8.4"}`.
Para el ejemplo completo de template Nginx, lee `references/vhost-template-example.md`.

### 8. Site User Commands

Ejecutar como usuario del sitio (via SSH: `john@server`):

```bash
clpctl system:permissions:reset --directories=770 --files=660 --path=.
clpctl db:export --databaseName=my-db --file=dump.sql.gz
clpctl db:import --databaseName=my-db --file=dump.sql.gz
clpctl varnish-cache:purge --purge=all           # all | tags | URL
```

**Opciones de `--purge`:** `all` (toda la cache), `tag1,tag2` (tags especificos separados por coma), o una URL especifica entre comillas: `'https://www.domain.com/site.html'`.

En `db:export` / `db:import` el site user **solo puede exportar/importar sus propias bases de datos** (misma sintaxis que el comando root).

## Flags comunes

`--domainName`, `--siteUser`, `--siteUserPassword`, `--force`, `--file`, `--databaseName`

> **Documentacion oficial:** https://www.cloudpanel.io/docs/v2/cloudpanel-cli/root-user-commands/

## Referencias

- `references/parametros.md` — parametros obligatorios/opcionales por comando (usa esta tabla cuando necesites los flags **exactos** de un comando: db:add, site:add:nodejs, site:add:php, site:install:certificate, user:add, system:permissions:reset y las opciones de `--purge`)
- `references/resumen.md` — vista rapida de todos los comandos (25 root commands, 4 site user commands y flags comunes con su proposito)
- `references/vhost-template-example.md` — ejemplo completo de template Nginx
