locals {
  script_directory = "${path.module}/scripts/"
}

data "digitalocean_ssh_key" "terraform" {
  name = var.ssh_key
}

data "digitalocean_domain" "server" {
  name = var.domain_name
}

resource "digitalocean_tag" "webserver" {
    name = "web"
}

resource "digitalocean_record" "www" {
  domain    = data.digitalocean_domain.server.id
  type      = "A"
  name      = digitalocean_droplet.server.name
  value     = digitalocean_droplet.server.ipv4_address
}

resource "digitalocean_project" "terraform_project" {
  name        = var.project_name
  environment = var.environment
  resources   = [digitalocean_droplet.server.urn]
}

resource "digitalocean_droplet" "server" {
    name    = var.name
    image   = var.image
    size    = "s-2vcpu-2gb"
    region  = var.region
    ssh_keys = [
      data.digitalocean_ssh_key.terraform.id
    ]
    tags   = [digitalocean_tag.webserver.id, var.tag]   

  # Create directories for deployment scripts
  provisioner "remote-exec" {
    inline = [
      "mkdir -p  /tmp/scripts/",
    ]

    connection {
      type        = "ssh"
      user        = "root"
      private_key = file("ssh_keys/${var.ssh_key}")
      host        = digitalocean_droplet.server.ipv4_address
    }
  }

  # Copy  Scripts
  provisioner "file" {
    source      = "${local.script_directory}/"
    destination = "/tmp/scripts/"

    connection {
      type        = "ssh"
      user        = "root"
      private_key = file("ssh_keys/${var.ssh_key}")
      host        = digitalocean_droplet.server.ipv4_address
    }
  }

  provisioner "remote-exec" {
    inline = [
      "bash /tmp/scripts/software_install.sh"
    ]

    connection {
      type        = "ssh"
      user        = "root"
      private_key = file("ssh_keys/${var.ssh_key}")
      host        = digitalocean_droplet.server.ipv4_address
    }
  }
}

