[Ubuntu 20.04](https://github.com/jnwarp/cloud/)
================================================

Basic Setup
-----------

Software: apt-get
```bash
apt-get update
apt-get upgrade -y
apt-get install curl fail2ban git htop python ranger screenfetch ufw vim zsh ssh unattended-upgrades links tmux -y
```

Users: james
```bash
# add user and grant sudo permissions
adduser james; gpasswd -a james sudo

# clone dotfiles
runuser -l james -c 'git clone https://github.com/jnwarp/dotfiles ~/.dotfiles'

# dotbot install
runuser -l james -c '~/.dotfiles/install'
```

Timezone
```bash
rm /etc/localtime
ln -s /usr/share/zoneinfo/US/Eastern /etc/localtime
```


Security
--------

/etc/ssh/sshd_config
```
PermitRootLogin no
PasswordAuthentication no
AuthorizedKeysFile %h/.ssh/authorized_keys
AuthenticationMethods publickey
```

*/etc/fail2ban/jail.local*
```
[DEFAULT]
# 34 days
bantime = 3000000

# 10 hours
findtime = 36000

[sshd]
enabled = true

[sshd-ddos]
enabled = true
```

/etc/apt/apt.conf.d/50unattended-upgrades
```
Unattended-Upgrade::AutoFixInterruptedDpkg "true";
Unattended-Upgrade::Remove-Unused-Dependencies "true";
Unattended-Upgrade::Automatic-Reboot "true";
Unattended-Upgrade::Automatic-Reboot-Time "01:00";
```

Unattended Upgrades
```bash
sudo dpkg-reconfigure --priority=low unattended-upgrades
```

Uncomplicated Firewall
```bash
sudo ufw allow 22
sudo ufw enable
```
