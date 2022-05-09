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



resource "digitalocean_project" "project_development" {
  for_each = {
    for key, value in var.projects : key => value
    if value.environment == "Development"
  }

  name        = each.value.name
  description = each.value.description
  purpose     = each.value.purpose
  environment = each.value.environment

  resources = [for key, value in var.servers : digitalocean_droplet.server[key].urn
      if value.project == "Development"
  ]
}

resource "digitalocean_project" "project_staging" {
  for_each = {
    for key, value in var.projects : key => value
    if value.environment == "Staging"
  }

  name        = each.value.name
  description = each.value.description
  purpose     = each.value.purpose
  environment = each.value.environment

  resources = [for key, value in var.servers : digitalocean_droplet.server[key].urn
    if value.project == "Staging"
  ]
}


output "droplet_ip_addresses" {
  value = values(digitalocean_droplet.server)[*].ipv4_address
}

output "project_names_development" {
  value = values(digitalocean_project.project_development)[*].name
}

output "project_names_staging" {
  value = values(digitalocean_project.project_staging)[*].name
}



// servers = {
//   server1 = {
//     name   = "Server1"
//     project = "Development"
//   },
//   server2 = {
//     name   = "Server2"
//     project = "Staging"
//   }
// }

// projects = {
//   project1 = {
//     name        = "Project Development"
//     environment = "Development"
//   },
//   project2 = {
//     name        = "Project Staging"
//     environment = "Staging"
//   }
// }


// projects = {
//   project1 = {
//     name        = "Project Development"
//     environment = "Development"
//     servers = {
//       server1 = {
//         name   = "Server1"
//         project = "Development"
//       }
//     }
//   },
//   project2 = {
//     name        = "Project Staging"
//     environment = "Staging"
//     servers = {
//       server2 = {
//         name   = "Server2"
//         project = "Staging"
//       }
//     }
//   }
// }
