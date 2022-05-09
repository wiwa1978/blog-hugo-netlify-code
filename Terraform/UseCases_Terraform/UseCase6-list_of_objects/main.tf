data "digitalocean_ssh_key" "terraform" {
  name = var.ssh_key
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
  count = length(var.projects)

  name = var.projects[count.index].name
  description = var.projects[count.index].description
  purpose = var.projects[count.index].purpose
  environment = var.projects[count.index].environment
}

output "droplet_ip_addresses" {
  value = values(digitalocean_droplet.server)[*].ipv4_address
}

output "project_names" {
  value = digitalocean_project.project[*].name
}


