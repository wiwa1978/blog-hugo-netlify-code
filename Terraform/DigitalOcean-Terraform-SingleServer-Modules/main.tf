module "ubuntu-server" {
    source = "./modules/server"

    name           =       var.name
    image          =       var.image
    environment    =       var.environment
    tag            =       var.tag
    domain_name    =       var.domain_name
    region         =       var.region
    ssh_key        =       var.ssh_key
    project_name   =       var.project_name
}

output "droplet_ip_address" {
  value = module.ubuntu-server.droplet_ip_address
}