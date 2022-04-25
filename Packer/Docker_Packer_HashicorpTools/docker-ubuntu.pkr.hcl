packer {
  required_plugins {
    docker = {
      version = ">= 1.0.1"
      source  = "github.com/hashicorp/docker"
    }
  }
}

source "docker" "ubuntu" {
  image  = "ubuntu:bionic"
  commit = true
}

build {
  name = "hashicorp-tools"
  sources = [
    "source.docker.ubuntu"
  ]

  // provisioner "shell" {
  //   inline = [
  //     "apt-get -y update",
  //     "apt-get install wget unzip mkisofs -y",
  //   ]
  // }

  // provisioner "shell" {
  //   inline = [
  //     <<EOF
  //     wget --quiet https://releases.hashicorp.com/packer/1.8.0/packer_1.8.0_linux_amd64.zip \
  //         && unzip packer_1.8.0_linux_amd64.zip \
  //         && mv packer /usr/local/bin
  //     EOF
  //   ]
  // }
  provisioner "shell" {
    inline = [
      "mkdir /tmp/scripts"
    ]
  }

  provisioner "file" {
    source      = "scripts/packer_install.sh"
    destination = "/tmp/scripts/packer_install.sh"
  }

  provisioner "shell" {
    inline = [
      "bash /tmp/scripts/packer_install.sh"
      
    ]
  }

  provisioner "file" {
    source      = "scripts/terraform_install.sh"
    destination = "/tmp/scripts/terraform_install.sh"
  }

  provisioner "shell" {
    inline = [
      "bash /tmp/scripts/terraform_install.sh"
    ]
  }


  post-processors {
    post-processor "docker-tag" {
      repository = var.docker_repo
      tags       = ["0.1.1"]
    }

    post-processor "docker-push" {
      login          = true
      login_username = var.docker_username
      login_password = var.docker_password
    }

  }



}



