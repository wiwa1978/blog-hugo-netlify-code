data "digitalocean_ssh_key" "terraform" {
  name = var.ssh_key
}

data "digitalocean_domain" "server" {
  name = var.domain_name
}



locals {
  all_servers = flatten([
    for project_key, project_value in var.projects : [
      for server_key, server_value in project_value.servers  : {
        project_key = project_key
        server_key = server_key
        name     = server_value["name"]
        image    = server_value["image"]
        size     = server_value["size"]
        region   = server_value["region"]
        tags     = server_value["tags"]
      }
    ]
  ])
}


resource "digitalocean_droplet" "server" {
 for_each = {
    for server in local.all_servers : server.server_key => server
  }
  
  name   = each.value.name
  image  = each.value.image
  size   = each.value.size
  region = each.value.region
  ssh_keys = [
    data.digitalocean_ssh_key.terraform.id
  ]
  tags = each.value.tags
}

resource "digitalocean_project" "project" {
  for_each = var.projects

  name        = each.key
  description = each.value.description
  purpose     = each.value.purpose
  environment = each.value.environment

  resources = [ for key, value in each.value.servers : digitalocean_droplet.server[key].urn]
  
}

resource "digitalocean_record" "www" {
  for_each = {
    for server in digitalocean_droplet.server : server.name => server
  }

  domain    = data.digitalocean_domain.server.id
  type      = "A"
  name      = each.value.name
  value     = each.value.ipv4_address
  // value     = each.value.droplet_ip_addresses
}


output "all_servers" {
  value = local.all_servers
}

output "droplet_ip_addresses" {
  value = values(digitalocean_droplet.server)[*].ipv4_address
}

output "project_names" {
  value = values(digitalocean_project.project)[*].name
}



