packer {
  required_plugins {
    digitalocean = {
      version = ">= 1.0.0"
      source  = "github.com/hashicorp/digitalocean"
    }
  }
}


source "digitalocean" "droplet" {
  api_token    = var.api_key
  image        = "ubuntu-21-10-x64"
  region       = "ams3"
  size         = "512mb"
  droplet_name = "packer"
  ssh_username = "root"
  snapshot_name= "packer_wim"
}

build {
  sources = ["source.digitalocean.droplet"]

  provisioner "file" {
    source      = "scripts/software_install.sh"
    destination = "/tmp/software_install.sh"
  }

  provisioner "shell" {
    inline = [
      "chmod +x /tmp/software_install.sh",
      "/tmp/software_install.sh"
    ]
  }
}