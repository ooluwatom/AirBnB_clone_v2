#!/usr/bin/env bash
# Bash script to set up server file system for deployment

# TO install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

# To configure file system
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# To set permissions
sudo chown -R ubuntu:ubuntu /data/

# To configure nginx
sudo sed -i '44i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# To restart web server
sudo service nginx restart
