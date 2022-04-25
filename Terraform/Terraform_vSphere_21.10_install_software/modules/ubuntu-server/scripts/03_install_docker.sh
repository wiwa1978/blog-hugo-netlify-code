#!/usr/bin/env bash

set -e

sudo apt update -y
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common python3-pip virtualenv python3-setuptools
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker