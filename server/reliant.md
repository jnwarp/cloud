reliant
=======

Basic Setup: [Ubuntu 16.04](https://github.com/jnwarp/cloud/blob/master/distro/ubuntu.md)
------------

Users:
```bash
userdel -r ubuntu
passwd -l root
```

/etc/update-motd.d/00-header
```
printf "██████╗ ███████╗██╗     ██╗ █████╗ ███╗   ██╗████████╗\n██╔══██╗██╔════╝██║     ██║██╔══██╗████╗  ██║╚══██╔══╝\n██████╔╝█████╗  ██║     ██║███████║██╔██╗ ██║   ██║   \n██╔══██╗██╔══╝  ██║     ██║██╔══██║██║╚██╗██║   ██║   \n██║  ██║███████╗███████╗██║██║  ██║██║ ╚████║   ██║   \n╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   \n\n"
```

/etc/hostname
```
reliant
```

/etc/hosts
```
127.0.0.1 reliant
```

[Certbot](https://github.com/jnwarp/cloud/blob/master/setup/certbot.md)
---------

[MySQL](https://github.com/jnwarp/cloud/blob/master/setup/mysql.md)
-------
