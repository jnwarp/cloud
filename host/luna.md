reliant
=======

Basic Setup: [Ubuntu 16.04](https://github.com/jnwarp/cloud/blob/master/distro/ubuntu.md)
------------

User Accounts
```bash
userdel -r ubuntu
passwd -l root
```

/etc/update-motd.d/00-header*
```
printf "\n██╗     ██╗   ██╗███╗   ██╗ █████╗ \n██║     ██║   ██║████╗  ██║██╔══██╗\n██║     ██║   ██║██╔██╗ ██║███████║\n██║     ██║   ██║██║╚██╗██║██╔══██║\n███████╗╚██████╔╝██║ ╚████║██║  ██║\n╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝\n\n"
```

/etc/hostname
```
luna
```

/etc/hosts
```
127.0.0.1 luna
```

/etc/network/interfaces.d/60-cloud-init-ipv6.cfg
```
auto eth0
iface eth0 inet6 dhcp
```

[Certbot](https://github.com/jnwarp/cloud/blob/master/setup/certbot.md)
---------

[Nginx](https://github.com/jnwarp/cloud/blob/master/setup/nginx.md)
-------
