[Ubuntu 18.04](https://github.com/jnwarp/cloud/)
================================================

Basic Setup
-----------

Software: apt-get
```bash
apt-get update
apt-get upgrade -y
apt-get install curl fail2ban git htop libpam-google-authenticator python ranger screenfetch ufw vim zsh ssh unattended-upgrades links tmux -y
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

Two Factor Authentication
```bash
# create two factor code
runuser -l james -c 'google-authenticator'

# move two factor to secret directory
mkdir -p /var/lib/google-authenticator/
mv /home/james/.google_authenticator /var/lib/google-authenticator/james
chown root:root /var/lib/google-authenticator/*
```

/etc/pam.d/sshd*
```
#@include common-auth
auth [success=1 default=ignore] pam_succeed_if.so user notingroup sudo
auth required pam_google_authenticator.so user=root secret=/var/lib/google-authenticator/${USER}
```

/etc/ssh/sshd_config
```
PermitRootLogin no
ChallengeResponseAuthentication yes
PasswordAuthentication no
AuthorizedKeysFile %h/.ssh/authorized_keys
AuthenticationMethods publickey,keyboard-interactive
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
