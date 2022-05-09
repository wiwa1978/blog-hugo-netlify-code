data "digitalocean_ssh_key" "terraform" {
  name = var.ssh_key
}

resource "digitalocean_droplet" "server" {

    count = length(var.servers)

    name    =  var.servers[count.index].name
    image   =  var.servers[count.index].image
    size    =  var.servers[count.index].size
    region  =  var.servers[count.index].region
    ssh_keys = [
      data.digitalocean_ssh_key.terraform.id
    ]
    tags   = var.servers[count.index].tags
}

output "droplet_ip_addresses" {
  value = digitalocean_droplet.server[*].ipv4_address
}

