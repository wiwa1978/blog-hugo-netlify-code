output "droplet_ip_address" {
  value = digitalocean_droplet.server.ipv4_address
}