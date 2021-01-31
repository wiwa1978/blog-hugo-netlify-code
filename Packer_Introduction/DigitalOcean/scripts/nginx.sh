#!/bin/bash
apt-get update -y
apt-get upgrade -y

apt-get install -y nginx

systemctl enable nginx
systemctl start nginx