#!/bin/env bash

#export DEBIAN_FRONTEND=noninteractive
echo 'Performing apt updates ...'
sudo apt -y update
sudo apt -y dist-upgrade
sudo apt -y upgrade
echo 'Installing net-tools ...'
sudo apt install -y net-tools
echo 'Installing nginx ...'
sudo apt install -y nginx