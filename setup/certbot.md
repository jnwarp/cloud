Certbot
=======

Install Certbot
```bash
sudo apt-get install letsencrypt
sudo letsencrypt certonly --rsa-key-size 4096 --standalone -d jnwarp.com -d vega.jnwarp.com

sudo openssl dhparam -out /etc/letsencrypt/dhparam.pem 4096
sudo wget -O /etc/letsencrypt/chain.pem "https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem"
```
