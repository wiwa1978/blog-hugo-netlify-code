#!/bin/env bash

#export DEBIAN_FRONTEND=noninteractive
echo 'Performing apt updates ...'
apt -y update
apt -y dist-upgrade
apt -y upgrade
echo 'Installing general tools ...'
apt-get install wget unzip mkisofs -y
echo 'Installing Packer ...'
wget --quiet https://releases.hashicorp.com/packer/1.8.0/packer_1.8.0_linux_amd64.zip && unzip packer_1.8.0_linux_amd64.zip && mv packer /usr/local/bin