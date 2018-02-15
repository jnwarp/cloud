challenger
==========

Basic Setup: [Ubuntu 16.04](https://github.com/jnwarp/cloud/blob/master/distro/ubuntu.md)
------------

User Accounts
```bash
userdel -r ubuntu
passwd -l root
```

/etc/update-motd.d/00-header
```
printf "         Welcome to Challenger, the\n  ███████╗██████╗  ██████╗████████╗███████╗\n  ██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝\n  █████╗  ██████╔╝██║        ██║   █████╗  \n  ██╔══╝  ██╔══██╗██║        ██║   ██╔══╝  \n  ██║     ██████╔╝╚██████╗   ██║   ██║     \n  ╚═╝     ╚═════╝  ╚═════╝   ╚═╝   ╚═╝     \n       server for the college of IST!\n\n"
```

/etc/hostname
```
challenger
```

/etc/hosts
```
127.0.0.1 localhost challenger
```
