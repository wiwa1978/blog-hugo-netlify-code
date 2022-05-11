output "droplet_ip_address" {
  value = digitalocean_droplet.server.ipv4_address
}


output "droplet_id" {
  value = digitalocean_droplet.server.id
}

output "droplet_name" {
    value = digitalocean_droplet.server.name
}


output "droplet_urn" {
  value = digitalocean_droplet.server.urn
}
