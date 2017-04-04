Nginx
=====

Nginx: /etc/nginx/nginx.conf
```
worker_processes auto;
worker_rlimit_nofile 8192;

events {
        worker_connections 8000;
}

http {
        ##
        # Basic Settings
        ##
        sendfile on;
        tcp_nopush on;
        keepalive_timeout 20s
        client_max_body_size 2m;

        ##
        # SSL Settings
        ##
        ssl_protocols TLSv1.2;
        ssl_ecdh_curve secp384r1;
        ssl_dhparam ssl/dhparam.pem;
        ssl_ciphers AES256+EECDH:AES256+EDH:!aNULL;
        ssl_prefer_server_ciphers on;
        ssl_stapling on;
        ssl_stapling_verify on;
        ssl_session_cache shared:SSL:30m;
        ssl_session_timeout 30m;
        resolver 8.8.4.4 8.8.8.8;

        ##
        # Gzip Settings
        ##

        gzip on;
        gzip_comp_level 5;
        gzip_min_length 256;
        gzip_proxied any;
        gzip_vary on;
        gzip_disable "msie6";

        gzip_types
          application/atom+xml
          application/javascript
          application/json
          application/ld+json
          application/manifest+json
          application/rss+xml
          application/vnd.geo+json
          application/vnd.ms-fontobject
          application/x-font-ttf
          application/x-web-app-manifest+json
          application/xhtml+xml
          application/xml
          font/opentype
          image/bmp
          image/svg+xml
          image/x-icon
          text/cache-manifest
          text/css
          text/plain
          text/vcard
          text/vnd.rim.location.xloc
          text/vtt
          text/x-component
          text/x-cross-domain-policy;
        # text/html is always compressed by gzip module
}
```

/etc/nginx/sites-available/andrewregan.me.conf
```
server {
        listen 80;
        listen [::]:80;

        server_name .andrewregan.me;

        return 301 https://$host$request_uri;
}

server {
        listen 443 ssl;
        listen [::]:443 ssl;

        root /var/www/andrewregan.me/src;

        index index.html;

        server_name andrewregan.me;

        location ~* .(woff|eot|ttf|svg|mp4|webm|jpg|jpeg|png|gif|ico|css|js)$ {
                expires 30d;
        }

        location / {
                try_files $uri $uri/ =404;
        }

        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
        add_header X-Frame-Options DENY;
        add_header X-Content-Type-Options nosniff;

        ssl_certificate /etc/letsencrypt/live/andrewregan.me/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/andrewregan.me/privkey.pem;
        ssl_trusted_certificate /etc/letsencrypt/live/andrewregan.me/chain.pem;
}

server {
        listen 443 ssl;
        listen [::]:443 ssl;

        server_name www.andrewregan.me;

        return 301 https://andrewregan.me$request_uri;

        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
        add_header X-Frame-Options DENY;
        add_header X-Content-Type-Options nosniff;

        ssl_certificate /etc/letsencrypt/live/andrewregan.me/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/andrewregan.me/privkey.pem;
        ssl_trusted_certificate /etc/letsencrypt/live/andrewregan.me/chain.pem;
}
```

```bash
sudo ln -s /etc/nginx/sites-available/andrewregan.me.conf /etc/nginx/sites-enabled/andrewregan.me.conf
sudo git clone https://github.com/jnwarp/andrewregan.me /var/www/andrewregan.me/
```

/etc/nginx/sites-available/jnwarp.com.conf
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

        server_name jnwarp.com;

        return 302 https://twitter.com/jnwarp;

        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
        add_header X-Frame-Options DENY;
        add_header X-Content-Type-Options nosniff;

        ssl_certificate /etc/letsencrypt/live/jnwarp.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/jnwarp.com/privkey.pem;
        ssl_trusted_certificate /etc/letsencrypt/live/jnwarp.com/chain.pem;
}

server {
        listen 443 ssl;
        listen [::]:443 ssl;

        server_name www.jnwarp.com vega.jnwarp.com;

        return 301 https://jnwarp.com$request_uri;

        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
        add_header X-Frame-Options DENY;
        add_header X-Content-Type-Options nosniff;

        ssl_certificate /etc/letsencrypt/live/jnwarp.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/jnwarp.com/privkey.pem;
        ssl_trusted_certificate /etc/letsencrypt/live/jnwarp.com/chain.pem;
}

server {
        listen 443 ssl;
        listen [::]:443 ssl;

        server_name rat.jnwarp.com;

        root /var/www/rat/html;
        access_log /var/www/rat/access_log;
        error_log /var/www/rat/error_log;

        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
        add_header X-Frame-Options DENY;
        add_header X-Content-Type-Options nosniff;

        ssl_certificate /etc/letsencrypt/live/jnwarp.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/jnwarp.com/privkey.pem;
        ssl_trusted_certificate /etc/letsencrypt/live/jnwarp.com/chain.pem;
}
```

```bash
sudo ln -s /etc/nginx/sites-available/jnwarp.com.conf /etc/nginx/sites-enabled/jnwarp.com.conf
```

/etc/nginx/sites-available/jameswarp.com.conf
```
server {
        listen 80;
        listen [::]:80;

        server_name .jameswarp.com;

        return 301 https://$host$request_uri;
}

server {
        listen 443 ssl;
        listen [::]:443 ssl;

    	root /var/www/jameswarp.com;
        index index.php index.html index.htm;

        server_name jameswarp.com;

        location / {
            try_files $uri $uri/ /index.php$is_args$args;
        }

        location ~ \.php$ {
            include snippets/fastcgi-php.conf;
            fastcgi_pass unix:/run/php/php7.0-fpm.sock;
        }

        location ~ /\.ht {
            deny all;
        }
        
        location = /favicon.ico { log_not_found off; access_log off; }
        location = /robots.txt { log_not_found off; access_log off; allow all; }
        location ~* \.(css|gif|ico|jpeg|jpg|js|png)$ {
            expires max;
            log_not_found off;
        }

        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
        add_header X-Frame-Options DENY;
        add_header X-Content-Type-Options nosniff;

        ssl_certificate /etc/letsencrypt/live/jameswarp.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/jameswarp.com/privkey.pem;
        ssl_trusted_certificate /etc/letsencrypt/live/jameswarp.com/chain.pem;
}

server {
        listen 443 ssl;
        listen [::]:443 ssl;

        server_name www.jameswarp.com;

        return 301 https://jameswarp.com$request_uri;

        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
        add_header X-Frame-Options DENY;
        add_header X-Content-Type-Options nosniff;

        ssl_certificate /etc/letsencrypt/live/jameswarp.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/jameswarp.com/privkey.pem;
        ssl_trusted_certificate /etc/letsencrypt/live/jameswarp.com/chain.pem;
}
```

```bash
sudo ln -s /etc/nginx/sites-available/jameswarp.com.conf /etc/nginx/sites-enabled/jameswarp.com.conf
```

/var/www/html/robots.txt
```
User-agent: *
Disallow: /
```


Wordpress
---------

Software: apt-get
```bash
# mysql
sudo apt-get install mysql-server automysqlbackup
sudo mysql_secure_installation

# php
sudo apt-get install php-fpm php-mysql php-curl php-gd php-mcrypt php-xmlrpc
```

AutoMySQLBackup: /etc/default/automysqlbackup
```
LATEST=yes
```

PHP: /etc/php/7.0/fpm/php.ini
```
cgi.fix_pathinfo=0
```

Wordpress: sudo -i
```bash
cd /tmp
curl -O https://wordpress.org/latest.tar.gz
tar xzvf latest.tar.gz
cp /tmp/wordpress/wp-config-sample.php /tmp/wordpress/wp-config.php
mkdir /tmp/wordpress/wp-content/upgrade
sudo cp -a /tmp/wordpress/. /var/www/jameswarp.com/
sudo chown -R www-data:www-data /var/www/jameswarp.com/
sudo find /var/www/jameswarp.com -type d -exec chmod g+s {} \;
sudo chmod g+w /var/www/jameswarp.com/wp-content
sudo chmod -R g+w /var/www/jameswarp.com/wp-content/themes
sudo chmod -R g+w /var/www/jameswarp.com/wp-content/plugins
```

Wordpress: mysql
```bash
mysql -u root -p
```

```mysql
CREATE DATABASE wordpress DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
GRANT ALL ON wordpress.* TO 'wordpress'@'localhost' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
EXIT;
```

Wordpress: /var/www/html/wp-config.php
```bash


# place output into file below
curl -s https://api.wordpress.org/secret-key/1.1/salt/
```

```
define('DB_NAME', 'wordpress');
define('DB_USER', 'wordpress');
define('DB_PASSWORD', 'change the password');

define('FS_METHOD', 'direct');

define('AUTH_KEY',         'put your unique phrase here');
define('SECURE_AUTH_KEY',  'put your unique phrase here');
define('LOGGED_IN_KEY',    'put your unique phrase here');
define('NONCE_KEY',        'put your unique phrase here');
define('AUTH_SALT',        'put your unique phrase here');
define('SECURE_AUTH_SALT', 'put your unique phrase here');
define('LOGGED_IN_SALT',   'put your unique phrase here');
define('NONCE_SALT',       'put your unique phrase here');
```
