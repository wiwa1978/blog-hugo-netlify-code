data "digitalocean_ssh_key" "terraform" {
  name = var.ssh_key
}

data "digitalocean_domain" "server" {
  name = var.domain_name
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
}

# Give the project the name of the server
resource "digitalocean_project" "project" {
  for_each = var.projects

  name = each.value.name
  description = each.value.description
  purpose = each.value.purpose
  environment = each.value.environment

  resources = values(digitalocean_droplet.server)[*].urn
}

resource "digitalocean_record" "www" {
  count = length(digitalocean_droplet.server)

  domain    = data.digitalocean_domain.server.id
  type      = "A"
  name      = values(digitalocean_droplet.server)[count.index].name
  value     = values(digitalocean_droplet.server)[count.index].ipv4_address
}



output "droplet_ip_addresses" {
  value = values(digitalocean_droplet.server)[*].ipv4_address
}

output "project_names" {
  value = values(digitalocean_project.project)[*].name
}


