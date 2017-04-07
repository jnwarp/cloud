cloud9
======

Install NodeJS
```bash
sudo apt-get install build-essential libssl-dev
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash
```

Install Cloud9
```bash
git clone git://github.com/c9/core.git ~/.c9sdk
cd ~/.c9sdk
scripts/install-sdk.sh
```

Start Cloud9
```bash
node ~/.c9sdk/server.js -w /home/james/ -p 8080 -a :
```
