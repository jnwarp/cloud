MySQL
=====

Install
```bash
sudo apt-get install mysql-server
sudo mysql_secure_installation
```

/etc/mysql/mysql.conf.d/mysqld.cnf
```
# listen on all ip addresses
bind-address            = 0.0.0.0

ssl-ca=/etc/mysql/chain.pem
ssl-cert=/etc/mysql/fullchain.pem
ssl-key=/etc/mysql/privkey.pem
```

/root/renew.sh
```bash
#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# renew https certificates
letsencrypt renew --rsa-key-size 4096 --standalone

# copy tls keys to usable location
openssl rsa -in /etc/letsencrypt/live/rel.jnwarp.com/privkey.pem -out /etc/mysql/privkey.pem
chown mysql:mysql /etc/mysql/*.pem
chmod og-rwx /etc/mysql/*.pem
chmod u+rwx /etc/mysql/*.pem

# restart mysql
systemctl restart mysql.service
```

crontab -e
```
# m h  dom mon dow   command
20 3 * * * /root/certbot-renew.sh
```

Firewall
```bash
ufw allow 3306
```
