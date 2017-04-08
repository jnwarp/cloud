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
gpg --passphrase=`cat vega-backup.password` -c --cipher-algo AES256 -o vega-wordpress-`date +%F`.tar.gz.gpg vega-wordpress.tar.gz

# save backups on remote server
scp vega-wordpress-`date +%F`.tar.gz.gpg vega@star.jnwarp.com:vega-wordpress-`date +%F`.tar.gz.gpg

# clean up old files
rm vega-wordpress.tar.gz
rm vega-wordpress-`date +%F`.tar.gz.gpg
```

Backup Destination
------------------

```bash
useradd vega
mkdir /home/vega
chown vega:vega /home/vega -R
```

/root/backup-lock.sh
```bash
#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin:/snap/bin

# prevent users from reading or changing backups
chown root:root /home/vega/*.gpg -R
chmod og-rwx /home/vega/*.gpg

chown root:root /home/gateway/*.gpg -R
chmod og-rwx /home/gateway/*.gpg
```

Decrypt Backup
--------------
```bash
gpg --output vega-backup.tar.gz --decrypt vega-backup-2017-04-08.tar.gz.gpg
```
