[Ubuntu 16.04](https://github.com/jnwarp/cloud/)
================================================

Basic Setup
-----------

Software: apt-get
```bash
sudo apt-get update; sudo apt-get install curl fail2ban git gnupg-curl htop libpam-google-authenticator python ranger screenfetch ufw vim zsh
```

Users: james
```bash
adduser james; gpasswd -a james sudo
```

```bash
# clone dotfiles
git clone https://github.com/jnwarp/dotfiles ~/.dotfiles

# dotbot install
~/.dotfiles/install
```

Timezone
```bash
sudo rm /etc/localtime
sudo ln -s /usr/share/zoneinfo/US/Eastern /etc/localtime
```


Security
--------

Two Factor Authentication
```bash
google-authenticator
```

/etc/pam.d/sshd
```
#@include common-auth
auth required pam_google_authenticator.so nullok
```

SSH: /etc/ssh/sshd_config
```
PermitRootLogin no
ChallengeResponseAuthentication yes
PasswordAuthentication no
AuthorizedKeysFile      %h/.ssh/authorized_keys
AuthenticationMethods publickey,keyboard-interactive
```

Fail2ban: /etc/fail2ban/jail.local
```
[DEFAULT]
# 34 days
bantime  = 3000000

# 10 hours
findtime = 36000

[ssh]
enabled = true

[ssh-ddos]
enabled  = true
```

Updates: /etc/apt/apt.conf.d/50unattended-upgrades
```
Unattended-Upgrade::Allowed-Origins {
        "${distro_id}:${distro_codename}";
        "${distro_id}:${distro_codename}-security";
        "${distro_id}:${distro_codename}-updates";
};

Unattended-Upgrade::AutoFixInterruptedDpkg "true";
Unattended-Upgrade::Remove-Unused-Dependencies "true";
Unattended-Upgrade::Automatic-Reboot "true";
Unattended-Upgrade::Automatic-Reboot-Time "01:00";
```

```bash
sudo dpkg-reconfigure --priority=low unattended-upgrades
```

Uncomplicated Firewall
```bash
sudo ufw allow 22
sudo ufw enable
```
