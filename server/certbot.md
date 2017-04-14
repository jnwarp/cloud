Certbot
=======

Install Certbot
```bash
apt-get install letsencrypt
#letsencrypt certonly --rsa-key-size 4096 --standalone -d jnwarp.com -d vega.jnwarp.com

# run this command at the end
#openssl dhparam -out /etc/letsencrypt/dhparam.pem

# get certificate in server configuration
#sudo wget -O /etc/letsencrypt/chain.pem "https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem"
```

*/root/certbot-renew.sh*
```
#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
systemctl stop nginx
letsencrypt renew --rsa-key-size 4096 --standalone
systemctl start nginx
```

crontab -e
```bash
echo "# m h  dom mon dow   command"
echo "20 3 * * * /root/certbot-renew.sh"
echo ""
echo "Copy the above output into the next screen."
read -r -p "Press enter to continue..." key
crontab -e
```
