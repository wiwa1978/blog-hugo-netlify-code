#!/bin/env bash

#export DEBIAN_FRONTEND=noninteractive
echo "Configuring users"
sudo adduser ubuntu --gecos "First Last,RoomNumber,WorkPhone,HomePhone" --disabled-password
echo "ubuntu:ubuntu" | sudo chpasswd

echo 'Performing apt updates ...'
sudo apt -y update
sudo apt -y dist-upgrade
sudo apt -y upgrade
echo 'Installing net-tools ...'
sudo apt install -y net-tools
echo 'Installing nginx ...'
sudo apt install -y nginx