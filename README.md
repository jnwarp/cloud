cloud configuration
===================

This repository hosts the configuration for my network of servers, use the links below to navigate.


### distro

- [Debian](https://github.com/jnwarp/cloud/distro/debian.md)


### setup

- [Nginx](https://github.com/jnwarp/cloud/setup/nginx.md)
- [World Community Grid](https://github.com/jnwarp/cloud/setup/boinc.md)

### server

- deviant
- proxima
- stargazer
- **vega**


---


proxima
-------

URLs to control RAT:
```
# recover-safe
https://rat.jnwarp.com/macbook-pro-2016.status

# recover
https://rat.jnwarp.com/macbook-pro-2016.sh

# logs
/var/www/rat/access_log
/var/www/rat/error_log
```

### Server Configuration

/etc/nginx/sites-enabled/jnwarp.com.conf
```
server {
        listen 443 ssl;
        listen [::]:443 ssl;

        server_name rat.jnwarp.com;

        root /var/www/rat/html;
        access_log /var/www/rat/access_log;
        error_log /var/www/rat/error_log;

        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
        add_header X-Frame-Options DENY;
        add_header X-Content-Type-Options nosniff;

        ssl_certificate /etc/letsencrypt/live/jnwarp.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/jnwarp.com/privkey.pem;
        ssl_trusted_certificate /etc/nginx/ssl/chain.pem;
}
```

### recover-safe

/var/root/recover-safe.sh
```bash
#!/bin/bash
PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
cd /var/root
curl https://rat.jnwarp.com/macbook-pro-2016.status > macbook-pro-2016.status
if grep -q reboot "macbook-pro-2016.status"; then
        echo "Rebooting into honeypot"
        shutdown -r now
else
        echo "Waiting..."
fi
```

#### sudo crontab -e
```
42 * * * * /var/root/recover-safe.sh > /var/root/recover-safe.log
```
