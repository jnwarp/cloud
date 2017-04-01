MySQL
=====

```bash
sudo apt-get install mysql-server
sudo mysql_secure_installation
```

/etc/mysql/mysql.conf.d/mysqld.cnf
```
# listen on all ip addresses
bind-address            = 0.0.0.0

ssl-ca=chain.pem
ssl-cert=fullchain.pem
ssl-key=privkey.pem
```
