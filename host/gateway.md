gateway
=======

Basic Setup: [Ubuntu 16.04](https://github.com/jnwarp/cloud/blob/master/distro/ubuntu.md)
------------

User Accounts
```bash
userdel -r ubuntu
passwd -l root
```

/etc/update-motd.d/00-header
```
printf "\n ██████╗  █████╗ ████████╗███████╗██╗    ██╗ █████╗ ██╗   ██╗\n██╔════╝ ██╔══██╗╚══██╔══╝██╔════╝██║    ██║██╔══██╗╚██╗ ██╔╝\n██║  ███╗███████║   ██║   █████╗  ██║ █╗ ██║███████║ ╚████╔╝ \n██║   ██║██╔══██║   ██║   ██╔══╝  ██║███╗██║██╔══██║  ╚██╔╝  \n╚██████╔╝██║  ██║   ██║   ███████╗╚███╔███╔╝██║  ██║   ██║   \n ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   \n\n"
```

*/etc/hostname*
```
gateway
```

/etc/hosts*
```
127.0.0.1 gateway
```

*/etc/network/interfaces.d/60-cloud-init-ipv6.cfg*
```
auto eth0
iface eth0 inet6 dhcp
```

[Certbot](https://github.com/jnwarp/cloud/blob/master/setup/certbot.md)
---------

[Nginx](https://github.com/jnwarp/cloud/blob/master/setup/nginx.md)
-------

*/etc/nginx/sites-available/jnwarp.com.conf*
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

Enabling `jnwarp.com`
```bash
ln -s /etc/nginx/sites-available/jnwarp.com.conf /etc/nginx/sites-enabled/jnwarp.com.conf
```

[ShellInABox](https://github.com/jnwarp/cloud/blob/master/setup/shellinabox.md)
-------------

[Cloud9](https://github.com/jnwarp/cloud/blob/master/setup/cloud9.md)
--------
