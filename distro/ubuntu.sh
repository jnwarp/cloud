#!/bin/bash

## Basic Setup
sudo apt-get install git curl vim zsh screenfetch gnupg-curl ranger htop ufw fail2ban
echo "America/New_York" > /etc/timezone

## Security
sed -i '
s/.*PermitRootLogin.*/PermitRootLogin no/
s/.*PasswordAuthentication.*/PasswordAuthentication no/
s/.*AuthorizedKeysFile.*/AuthorizedKeysFile %h\/.ssh\/authorized_keys/
' /etc/ssh/sshd_config

echo "
[DEFAULT]
# 34 days
bantime  = 3000000

# 10 hours
findtime = 36000

[ssh]
enabled = true

[ssh-ddos]
enabled  = true
" > /etc/fail2ban/jail.local

r="Unattended-Upgrade::Allowed-Origins{
        "${distro_id}:${distro_codename}";
        "${distro_id}:${distro_codename}-security";
        "${distro_id}:${distro_codename}-updates";
};"

sed -i '
s/(Unattended-Upgrade)((.|\n)*?)(};)/$r/
' sshd_config
