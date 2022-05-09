data "digitalocean_ssh_key" "terraform" {
  name = var.ssh_key
}

resource "digitalocean_droplet" "server" {

    count = length(var.servers)

    name    =  values(var.servers)[count.index]["name"]
    image   =  values(var.servers)[count.index]["image"]
    size    =  values(var.servers)[count.index]["size"]
    region  =  values(var.servers)[count.index]["region"]
    ssh_keys = [
      data.digitalocean_ssh_key.terraform.id
    ]
    tags   = var.servers[format("server%s", count.index+1)]["tags"]
}

output "droplet_ip_addresses" {
  value = digitalocean_droplet.server[*].ipv4_address
}


