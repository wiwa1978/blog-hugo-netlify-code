data "digitalocean_domain" "server" {
  name = var.domain_name
}

resource "digitalocean_record" "www" {
  domain    = data.digitalocean_domain.server.id
  type      = "A"
  name      = var.name
  value     = var.value
}
