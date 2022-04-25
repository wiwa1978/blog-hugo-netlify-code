#!/usr/bin/env bash

set -e

USERNAME="${1}"
PASSWORD="${2}"
SSH_KEYFILE_CONTENT_PUBLIC="${3}"
SSH_KEYFILE_CONTENT_PRIVATE="${4}"

"sudo useradd -s /bin/bash -m -p $(perl -e 'print crypt($ARGV[0], \"password\")' ${PASSWORD}) ${USERNAME}",
"sudo mkdir -p /home/${USERNAME}/.ssh",
"sudo touch /home/${USERNAME}/.ssh/authorized_keys",
"sudo echo $(cat /tmp/${SSH_KEYFILE_CONTENT_PUBLIC}) > authorized_keys", 
"sudo mv authorized_keys /home/${USERNAME}/.ssh", 
"sudo echo $(cat /tmp/${SSH_KEYFILE_CONTENT_PUBLIC}) > id_ed25519.pub",
"sudo mv id_ed25519.pub /home/${USERNAME}/.ssh",
"sudo echo $(cat /tmp/${SSH_KEYFILE_CONTENT_PRIVATE}) > id_ed25519",
"sudo mv id_ed25519 /home/${USERNAME}/.ssh",
"sudo chown -R ${USERNAME}:${USERNAME} /home/${var.vm_username}/.ssh",
"sudo chmod 700 /home/${USERNAME}/.ssh",
"sudo chmod 600 /home/${USERNAME}/.ssh/authorized_keys",
"sudo chmod 644 /home/${USERNAME}/.ssh/id_ed25519.pub",
"sudo chmod 600 /home/${USERNAME}/.ssh/id_ed25519",
"sudo usermod -aG sudo ${USERNAME}",
"sudo groupadd docker",
"sudo usermod -aG docker ${USERNAME}",
"sudo usermod -aG adm ${USERNAME}",
"echo '${USERNAME} ALL=(ALL) NOPASSWD:ALL' | sudo tee -a /etc/sudoers.d/${USERNAME}",