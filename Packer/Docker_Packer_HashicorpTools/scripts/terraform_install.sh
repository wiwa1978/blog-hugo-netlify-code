#!/bin/env bash

#export DEBIAN_FRONTEND=noninteractive
echo 'Performing apt updates ...'
apt -y update
apt -y dist-upgrade
apt -y upgrade
echo 'Installing general tools ...'
apt-get install wget unzip mkisofs -y
echo 'Installing Terraform ...'
wget --quiet https://releases.hashicorp.com/terraform/1.1.8/terraform_1.1.8_linux_arm64.zip && unzip terraform_1.1.8_linux_arm64.zip && mv terraform /usr/local/bin

