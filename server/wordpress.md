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

/etc/default/automysqlbackup
```
LATEST=yes
```

/etc/php/7.0/fpm/php.ini
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
