Shell In A Box
==============

```bash
sudo apt install shellinabox
```

/etc/default/shellinabox
```
SHELLINABOX_ARGS="--no-beep --localhost-only"
```

/etc/nginx/sites-available/jnwarp.com.conf
```
	location /shell/ {
		rewrite ^/shell/(.*) /$1 break;
		proxy_pass https://127.0.0.1:4200;
		proxy_read_timeout 90;
	}
```
