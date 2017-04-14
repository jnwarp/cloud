Shell In A Box
==============

```bash
apt install shellinabox
```

*/etc/default/shellinabox*
```
# Should shellinaboxd start automatically
SHELLINABOX_DAEMON_START=1

# TCP port that shellinboxd's webserver listens on
SHELLINABOX_PORT=4200

# Parameters that are managed by the system and usually should not need
# changing:
# SHELLINABOX_DATADIR=/var/lib/shellinabox
# SHELLINABOX_USER=shellinabox
# SHELLINABOX_GROUP=shellinabox

# Any optional arguments (e.g. extra service definitions).  Make sure
# that that argument is quoted.
#
#   Beeps are disabled because of reports of the VLC plugin crashing
#   Firefox on Linux/x86_64.
SHELLINABOX_ARGS="--no-beep --localhost-only"
```

!/etc/nginx/sites-available/jnwarp.com.conf
```
	location /shell/ {
		rewrite ^/shell/(.*) /$1 break;
		proxy_pass https://127.0.0.1:4200;
		proxy_read_timeout 90;
	}
```
