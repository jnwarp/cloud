Backup Target
-------------

```bash
ssh-keygen -t rsa -b 4096 -C "root@vega.jnwarp.com"
```

/root/vega-backup.sh
```bash
#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin:/snap/bin

# prepare backups of wordpress and the mysql database
cd /root
automysqlbackup
tar -czf vega-wordpress.tar.gz /var/www/* /var/lib/automysqlbackup/latest/*

# encrypt backups
gpg --passphrase-file vega-backup.password -c --cipher-algo AES256 -o vega-wordpress-`date +%F`.tar.gz.gpg vega-wordpress.tar.gz

# save backups on remote server
scp vega-wordpress-`date +%F`.tar.gz.gpg vega@star.jnwarp.com:vega-wordpress-`date +%F`.tar.gz.gpg

# clean up old files
rm vega-wordpress.tar.gz
rm vega-wordpress-`date +%F`.tar.gz.gpg
```

Backup Destination
------------------

