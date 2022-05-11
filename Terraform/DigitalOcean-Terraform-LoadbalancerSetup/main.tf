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
  resources   = digitalocean_droplet.server[*].urn
}

resource "digitalocean_droplet" "server" {
  count = var.amount

  name = format("%s-%s", var.name, "${count.index + 1}")

  image  = var.image
  size   = "s-2vcpu-2gb"
  region = var.region
  ssh_keys = [
    data.digitalocean_ssh_key.terraform.id
  ]

  tags = [format("%s-%s", var.name, "${count.index + 1}")]

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


  # Install software
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
resource "digitalocean_tag" "webserver" {
  count = var.amount
  name  = "server-${count.index}"
}


resource "digitalocean_loadbalancer" "public" {
  name   = "lbdigitalocean"
  region = var.region

  forwarding_rule {
    entry_port     = 80
    entry_protocol = "http"

    target_port     = 80
    target_protocol = "http"
  }

  healthcheck {
    port     = 22
    protocol = "tcp"
  }

  droplet_ids = digitalocean_droplet.server[*].id
}

resource "digitalocean_firewall" "web" {
  name        = "Test"
  droplet_ids = digitalocean_droplet.server[*].id

  inbound_rule {
    protocol   = "tcp"
    port_range = "80"
    //source_addresses   = [digitalocean_loadbalancer.public.id]
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "22"
    source_addresses = ["0.0.0.0/0"]
  }

  inbound_rule {
    protocol         = "icmp"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }


  outbound_rule {
    protocol              = "tcp"
    port_range            = "1-65535"
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }

  outbound_rule {
    protocol              = "icmp"
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }
}

output "droplet_ip_address" {
  value = digitalocean_droplet.server.*.ipv4_address
}

output "loadbalancer_ip_address" {
  value = digitalocean_loadbalancer.public.ip
}



resource "digitalocean_record" "www" {
  domain = data.digitalocean_domain.server.id
  type   = "A"
  name   = digitalocean_loadbalancer.public.name
  value  = digitalocean_loadbalancer.public.ip
}

