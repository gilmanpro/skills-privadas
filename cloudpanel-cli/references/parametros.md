# Parametros obligatorios/opcionales por comando (clpctl v2)

Tablas de parametros de los comandos con mas flags. Todos se ejecutan como **root** (o `sudo`), salvo `system:permissions:reset` y `varnish-cache:purge`, que son **Site User Commands** (se ejecutan como usuario del sitio).

## db:add

```bash
clpctl db:add --domainName=www.domain.com --databaseName=my-database --databaseUserName=john --databaseUserPassword='!secretPassword!'
```

| Parametro | Obligatorio | Descripcion |
|---|---|---|
| `--domainName` | Si | Dominio del sitio asociado |
| `--databaseName` | Si | Nombre de la base de datos |
| `--databaseUserName` | Si | Usuario de la BD |
| `--databaseUserPassword` | Si | Contrasena del usuario |

## site:add:nodejs

```bash
clpctl site:add:nodejs --domainName=www.domain.com --nodejsVersion=22 --appPort=3000 --siteUser=john --siteUserPassword='!secretPassword!'
```

| Parametro | Obligatorio | Descripcion |
|---|---|---|
| `--domainName` | Si | Dominio del sitio |
| `--nodejsVersion` | Si | Version de Node (22, 20, 18, 16, 14, 12) |
| `--appPort` | Si | Puerto de la aplicacion |
| `--siteUser` | Si | Usuario del sitio |
| `--siteUserPassword` | Si | Contrasena del usuario |

## site:add:php

```bash
clpctl site:add:php --domainName=www.domain.com --phpVersion=8.4 --vhostTemplate='Generic' --siteUser=john --siteUserPassword='!secretPassword!'
```

| Parametro | Obligatorio | Descripcion |
|---|---|---|
| `--domainName` | Si | Dominio del sitio |
| `--phpVersion` | Si | Version de PHP (ej. 8.4, 8.3, 8.2, 8.1, 8.0) |
| `--vhostTemplate` | Si | Nombre de la plantilla (ver `vhost-templates:list`) |
| `--siteUser` | Si | Usuario del sitio |
| `--siteUserPassword` | Si | Contrasena del usuario |

## site:install:certificate

```bash
clpctl site:install:certificate --domainName=www.domain.com --privateKey=/path/to/private.key --certificate=/path/to/certificate.crt --certificateChain=/path/to/chain.crt
```

| Parametro | Obligatorio | Descripcion |
|---|---|---|
| `--domainName` | Si | Dominio del sitio |
| `--privateKey` | Si | Ruta a la clave privada |
| `--certificate` | Si | Ruta al certificado |
| `--certificateChain` | No (opcional) | Ruta a la cadena de certificados |

> `--certificateChain` es **opcional**: se usa cuando el certificado necesita una cadena de intermedios (CA bundle).

## user:add

```bash
clpctl user:add --userName='john.doe' --email='john.doe@domain.com' --firstName='John' --lastName='Doe' --password='!password!' --role='user' --sites='domain.com,domain.io' --timezone='UTC' --status='1'
```

| Parametro | Obligatorio | Descripcion |
|---|---|---|
| `--userName` | Si | Nombre de usuario |
| `--email` | Si | Correo electronico |
| `--firstName` | Si | Nombre |
| `--lastName` | Si | Apellido |
| `--password` | Si | Contrasena |
| `--role` | Si | Rol: `admin`, `site-manager` o `user` |
| `--sites` | No (solo para `role=user`) | Lista de dominios separados por coma |
| `--timezone` | Si | Zona horaria (ej. `UTC`, `America/Panama`) |
| `--status` | Si | `1` = activo, `0` = inactivo |

Semantica de valores:

- `--status`: `1` deja el usuario **activo**, `0` **inactivo**.
- `--sites`: solo aplica cuando `--role='user'`; restringe al usuario a esos dominios.
- `--timezone`: zona horaria IANA; ejemplo tipico `America/Panama` (tambien `UTC`).

## system:permissions:reset (site user)

```bash
clpctl system:permissions:reset --directories=770 --files=660 --path=.
```

| Parametro | Obligatorio | Descripcion |
|---|---|---|
| `--directories` | Si | Permisos para directorios (octal) |
| `--files` | Si | Permisos para archivos (octal) |
| `--path` | Si | Ruta donde aplicar (`.` para el directorio actual) |

## varnish-cache:purge — valores de `--purge` (site user)

```bash
clpctl varnish-cache:purge --purge=all
```

| Valor | Descripcion |
|---|---|
| `all` | Purga toda la cache de Varnish |
| `tag1,tag2,...` | Purga tags especificos separados por coma |
| `'https://www.domain.com/site.html'` | Purga una URL especifica |
