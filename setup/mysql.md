MySQL
=====

```bash
sudo apt-get install mysql-server
sudo mysql_secure_installation
openssl rsa -in /etc/letsencrypt/live/rel.jnwarp.com/privkey.pem -out /etc/mysql/privkey.pem
```

/etc/mysql/mysql.conf.d/mysqld.cnf
```
# listen on all ip addresses
bind-address            = 0.0.0.0

ssl-ca=chain.pem
ssl-cert=fullchain.pem
ssl-key=privkey.pem
```
