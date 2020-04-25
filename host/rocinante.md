rocinante
=========

Basic Setup: CentOS 8
------------

[Certbot](https://github.com/jnwarp/cloud/blob/master/setup/certbot.md)
---------

[Nginx](https://github.com/jnwarp/cloud/blob/master/setup/nginx.md)
-------

*/etc/nginx/sites-available/mistystep.com*
```
server {
    listen 80;
    listen [::]:80;

    server_name mistystep.com;

    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;

    server_name mistystep.com;

    root /var/www/mistystep.com;
    index index.html;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;

    ssl_certificate /etc/letsencrypt/live/mistystep.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/mistystep.com/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/mistystep.com/chain.pem;
}
```

*/etc/nginx/sites-available/superevil.site*
```
server {
    listen 80;
    listen [::]:80;

    server_name superevil.site;

    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;

    server_name superevil.site;

    root /var/www/superevil.site;
    index index.html;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;

    ssl_certificate /etc/letsencrypt/live/superevil.site/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/superevil.site/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/superevil.site/chain.pem;
}
```

```
server {
    listen 80;
    listen [::]:80;

    server_name .jnwarp.com;

    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;

    server_name gate.jnwarp.com;

    root /var/www/html;
    index index.html;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;

    ssl_certificate /etc/letsencrypt/live/gate.jnwarp.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/gate.jnwarp.com/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/gate.jnwarp.com/chain.pem;
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;

    server_name code.jnwarp.com;

    location / {
        auth_basic "Restricted Content";
        auth_basic_user_file /etc/nginx/.htpasswd;
        rewrite ^/(.*) /$1 break;
        proxy_pass http://127.0.0.1:8080;
        proxy_read_timeout 90;
    }

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;

    ssl_certificate /etc/letsencrypt/live/gate.jnwarp.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/gate.jnwarp.com/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/gate.jnwarp.com/chain.pem;
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;

    server_name shell.jnwarp.com;

    location / {
        rewrite ^/(.*) /$1 break;
        proxy_pass https://127.0.0.1:4200;
        proxy_read_timeout 90;
    }

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;

    ssl_certificate /etc/letsencrypt/live/gate.jnwarp.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/gate.jnwarp.com/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/gate.jnwarp.com/chain.pem;
}
```

Enabling `mistystep.com`
```bash
chcon -Rt httpd_sys_content_t /var/www/mistystep.com
ln -s /etc/nginx/sites-available/mistystep.com /etc/nginx/sites-enabled/mistystep.com
```

Enabling `superevil.site`
```bash
chcon -Rt httpd_sys_content_t /var/www/superevil.site
ln -s /etc/nginx/sites-available/superevil.site /etc/nginx/sites-enabled/superevil.site
```
