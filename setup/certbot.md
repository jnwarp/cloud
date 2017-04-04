Certbot
=======

Install Certbot
```bash
sudo apt-get install letsencrypt
sudo letsencrypt certonly --rsa-key-size 4096 --standalone -d jnwarp.com -d vega.jnwarp.com

sudo openssl dhparam -out /etc/letsencrypt/dhparam.pem 4096
#sudo wget -O /etc/letsencrypt/chain.pem "https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem"
```

/root/certbot-renew.sh
```bash
#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
letsencrypt renew --rsa-key-size 4096 --standalone
```

crontab -e
```
# m h  dom mon dow   command
20 3 * * * /root/certbot-renew.sh
```
