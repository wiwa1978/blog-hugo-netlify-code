locals {
  script_directory = "${path.module}/scripts/"
}

data "digitalocean_ssh_key" "terraform" {
  name = var.ssh_key
}

data "digitalocean_domain" "server" {
  name = var.domain_name
}

resource "digitalocean_project" "terraform_project" {
  name        = var.project_name
  environment = "Development"
  resources   = values(digitalocean_droplet.server)[*].urn
}

resource "digitalocean_record" "www" {
  for_each = {
    for server in digitalocean_droplet.server : server.name => server
  }

  domain = data.digitalocean_domain.server.id
  type   = "A"
  name   = each.value.name
  value  = each.value.ipv4_address
}

resource "digitalocean_tag" "webserver" {
  name = "web"
}

resource "digitalocean_droplet" "server" {
  for_each = var.servers

  name   = each.key
  image  = each.value.image
  size   = each.value.size
  region = each.value.region
  ssh_keys = [
    data.digitalocean_ssh_key.terraform.id
  ]
  tags = each.value.tags

  # Create directories for deployment scripts
  provisioner "remote-exec" {
    inline = [
      "mkdir -p  /tmp/scripts/",
    ]

    connection {
      type        = "ssh"
      user        = "root"
      private_key = file("ssh_keys/${var.ssh_key}")
      host        = self.ipv4_address
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
      host        = self.ipv4_address
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
      host        = self.ipv4_address
    }
  }
}

output "droplet_ip_address" {
  value = values(digitalocean_droplet.server)[*].ipv4_address
}