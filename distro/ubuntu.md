[Ubuntu 16.04](https://github.com/jnwarp/cloud/)
================================================

Basic Setup
-----------

Software: apt-get
```bash
sudo apt-get install git curl vim zsh screenfetch gnupg-curl ranger htop ufw fail2ban
```

/etc/timezone
```
America/New_York
```


Security
--------

SSH: /etc/ssh/sshd_config
```
PermitRootLogin no
PasswordAuthentication no
AuthorizedKeysFile      %h/.ssh/authorized_keys
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
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
```
