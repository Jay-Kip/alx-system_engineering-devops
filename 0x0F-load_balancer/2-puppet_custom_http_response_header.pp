#!/bin/bash

# Install Nginx
sudo apt update
sudo apt install -y nginx

# Retrieve the hostname
hostname=$(hostname)

# Configure Nginx to add custom header
sudo bash -c "cat > /etc/nginx/conf.d/custom-header.conf" <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;
    add_header X-Served-By $hostname;

    location / {
        # Your other Nginx configuration directives
    }
}
EOF

# Restart Nginx
sudo systemctl restart nginx
