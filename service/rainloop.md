```bash
# install dependencies
apt-get install unzip php-dom

# install rainloop into folder
cd /var/www
mkdir /var/www/rainloop
wget https://www.rainloop.net/repository/webmail/rainloop-latest.zip
unzip rainloop-latest.zip -d /var/www/rainloop

# restrict permissions
cd /var/www/rainloop
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;
chown -R www-data:www-data .
```

/etc/nginx/sites-enabled/jnwarp.com
```
server {
        listen 443 ssl;
        listen [::]:443 ssl;

        server_name mail.jnwarp.com;

        root /var/www/rainloop;

        location ^~ /data {
                deny all;
        }

        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
        add_header X-Frame-Options DENY;
        add_header X-Content-Type-Options nosniff;

        ssl_certificate /etc/letsencrypt/live/jnwarp.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/jnwarp.com/privkey.pem;
        ssl_trusted_certificate /etc/nginx/ssl/chain.pem;
}
```
