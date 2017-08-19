Nginx
=====

Install Nginx
```bash
apt install nginx
```

*/etc/nginx/nginx.conf*
```
user www-data;
worker_processes auto;
worker_rlimit_nofile 8192;
pid /run/nginx.pid;

events {
	worker_connections 8000;
	# multi_accept on;
}

http {

	##
	# Basic Settings
	##
	sendfile on;
	tcp_nopush on;
	tcp_nodelay on;
	keepalive_timeout 20s;
	types_hash_max_size 2048;
	client_max_body_size 2m;
	# server_tokens off;

	# server_names_hash_bucket_size 64;
	# server_name_in_redirect off;

	include /etc/nginx/mime.types;
	default_type application/octet-stream;

	##
	# SSL Settings
	##
	ssl_protocols TLSv1.2;
	ssl_ecdh_curve secp384r1;
	ssl_dhparam /etc/nginx/ssl/dhparam.pem;
	ssl_ciphers AES256+EECDH:AES256+EDH:!aNULL;
	ssl_prefer_server_ciphers on;
	ssl_stapling on;
	ssl_stapling_verify on;
	ssl_session_cache shared:SSL:30m;
	ssl_session_timeout 30m;
	resolver 8.8.4.4 8.8.8.8;

	##
	# Logging Settings
	##
	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;

	##
	# Gzip Settings
	##
	gzip on;
	gzip_disable "msie6";
	gzip_vary on;
	gzip_proxied any;
	gzip_comp_level 5;
	gzip_min_length 256;
	# gzip_buffers 16 8k;
	# gzip_http_version 1.1;
	gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;


	##
	# Virtual Host Configs
	##
	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
}


#mail {
#	# See sample authentication script at:
#	# http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
# 
#	# auth_http localhost/auth.php;
#	# pop3_capabilities "TOP" "USER";
#	# imap_capabilities "IMAP4rev1" "UIDPLUS";
# 
#	server {
#		listen     localhost:110;
#		protocol   pop3;
#		proxy      on;
#	}
# 
#	server {
#		listen     localhost:143;
#		protocol   imap;
#		proxy      on;
#	}
#}

```

*/var/www/html/robots.txt*
```
User-agent: *
Disallow: /
```
