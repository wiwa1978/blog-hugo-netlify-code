#!/bin/env bash

#export DEBIAN_FRONTEND=noninteractive
echo "Configuring users"
sudo adduser ubuntu --gecos "First Last,RoomNumber,WorkPhone,HomePhone" --disabled-password
echo "ubuntu:ubuntu" | sudo chpasswd

echo 'Performing apt updates ...'
sudo apt -y update
echo 'Installing net-tools ...'
sudo apt install -y net-tools
echo 'Installing nginx ...'
sudo apt install -y nginx
echo 'Changing default nginx page ...'
echo 'Servername:' > /var/www/html/index.html
echo $(uname -n) '<br>' >> /var/www/html/index.html
echo 'IP address:' >> /var/www/html/index.html
echo $(ip route get 8.8.8.8 | sed -n '/src/{s/.*src *\([^ ]*\).*/\1/p;q}') >> /var/www/html/index.html
echo 'Restarting nginx ...'
sudo service nginx restart