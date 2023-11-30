package { 'nginx':
  ensure => 'present',
}

# Install nginx
exec { 'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}

# Write index.html
exec { 'Hello World!':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

# Redirect
exec { 'Add redirect configuration':
  command  => 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \\/redirect_me {\\n\\t\\treturn 301 https:\\/\\/www.youtube.com\\/;\\n\\t}/" /etc/nginx/sites-available/default',
  provider => shell,
}

# Restart the server
exec { 'Restart NGINX':
  command  => 'sudo service nginx restart',
  provider => shell,
}
