# Vhost Template — Ejemplo Completo

La primera linea del template debe ser un comentario JSON con los metadatos de configuracion:

```json
#{"rootDirectory":"public","phpVersion":"8.4"}
```

- **`rootDirectory`**: Directorio raiz dentro del home del usuario (ej. `public`).
- **`phpVersion`**: Version de PHP por defecto.

## Ejemplo completo

```
#{"rootDirectory":"public","phpVersion":"8.4"}
server {
  listen 80;
  listen [::]:80;
  listen 443 ssl http2;
  listen [::]:443 ssl http2;
  {{ssl_certificate_key}}
  {{ssl_certificate}}
  {{server_name}}
  {{root}}

  {{nginx_access_log}}
  {{nginx_error_log}}

  if ($scheme != "https") {
    rewrite ^ https://$host$uri permanent;
  }

  location ~ /.well-known {
    auth_basic off;
    allow all;
  }

  {{settings}}

  try_files $uri $uri/ /index.php?$args;
  index index.php index.html;

  location ~ \.php$ {
    include fastcgi_params;
    fastcgi_intercept_errors on;
    fastcgi_index index.php;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    try_files $uri =404;
    fastcgi_read_timeout 3600;
    fastcgi_send_timeout 3600;
    fastcgi_param HTTPS $fastcgi_https;
    fastcgi_pass 127.0.0.1:{{php_fpm_port}};
    fastcgi_param PHP_VALUE "{{php_settings}}";
  }

  location ~* ^.+\.(css|js|jpg|jpeg|gif|png|ico|gz|svg|svgz|ttf|otf|woff|eot|mp4|ogg|ogv|webm|webp|zip|swf)$ {
    add_header Access-Control-Allow-Origin "*";
    expires max;
    access_log off;
  }

  if (-f $request_filename) {
    break;
  }
}
```

## Patron del directorio raiz generado

```
/home/$siteUser/htdocs/$domainName/$rootDirectory
```

Ejemplo con template `My Application` y sitio `www.domain.com`:
```
/home/custom-app/htdocs/www.domain.com/public
```
