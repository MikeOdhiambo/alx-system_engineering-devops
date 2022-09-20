# Puppet automate creating a custom HTTP header response.

exec { 'http config':
  provider => shell,
  command  => 'sudo apt-get update -y && sudo apt-get install -y nginx && echo "Hello World!" > /var/www/html/index.html && sed -i '/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;' /etc/nginx/sites-available/default && echo "Ceci n'est pas une page" > /usr/share/nginx/html/custom_404.html && sed -i '/listen 80 default_server;/a error_page 404 /custom_404.html;\nlocation = /custom_404.html {\nroot /usr/share/nginx/html; \ninternal;\n}' /etc/nginx/sites-available/default && sudo service nginx restart',
}
