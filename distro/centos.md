[Centos 8](https://github.com/jnwarp/cloud/)
============================================

Basic Setup
-----------

Software: dnf
```bash
dnf update
dnf upgrade -y
dnf install -y epel-release

dnf update
dnf upgrade -y
dnf install -y curl fail2ban git htop vim zsh dnf-automatic tmux python2
```

Users: james
```bash
# add user and grant sudo permissions
adduser james; gpasswd -a james wheel

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
ChallengeResponseAuthentication no
PasswordAuthentication no
AuthorizedKeysFile .ssh/authorized_keys
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

*/etc/dnf/automatic.conf*
```
apply_updates = yes
emit_via = stdio
```

Security: dnf-automatic
```bash
systemctl enable --now dnf-automatic-notifyonly.timer
```
