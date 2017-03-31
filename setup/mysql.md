MySQL
=======

```bash
sudo apt-get install mariadb-server
sudo mysql_secure_installation
```

/etc/mariadb/mariadb.conf.d/50-server.cnf
```
# listen on all ip addresses
bind-address            = 0.0.0.0
```
