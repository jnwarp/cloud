cloud9
======

Install NodeJS
```bash
# download node version manager
sudo apt-get install build-essential libssl-dev
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash

# install the lts version
nvm install --lts
nvm use --lts
```

Install Cloud9
```bash
mkdir ~/.c9sdk
git clone git://github.com/c9/core.git ~/.c9sdk/c9sdk
~/.c9sdk/c9sdk/scripts/install-sdk.sh
```

/home/james/.c9sdk/process.yml
```yaml
apps:
  - script   : c9sdk/server.js
    watch    : true
    args     : "-w /home/james/ -p 8080 -a"
```

/home/james/.c9sdk/start_cloud9.sh
```bash
#!/bin/bash
PATH=/home/james/.nvm/versions/node/v6.10.2/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
cd /home/james/.c9sdk
pm2 start process.yml
```

/etc/nginx/sites-enabled/jnwarp.com.conf
```
location / {
    auth_basic "Restricted Content";
    auth_basic_user_file /etc/nginx/.htpasswd;
    rewrite ^/(.*) /$1 break;
    proxy_pass http://127.0.0.1:8080;
    proxy_read_timeout 90;
}
```

```bash
# password protect cloud9
sudo sh -c "echo -n 'james:' >> /etc/nginx/.htpasswd"
sudo sh -c "openssl passwd -apr1 >> /etc/nginx/.htpasswd"
```


Start Cloud9
------------
Using pm2
```bash
pm2 start ~/.c9sdk/process.yml
```

Manual
```bash
node ~/.c9sdk/server.js -w /home/james/ -p 8080 -a :
```