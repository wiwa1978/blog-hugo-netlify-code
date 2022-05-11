module "ubuntu-server" {
    source = "./modules/server"

    name           =       var.name
    image          =       var.image
    environment    =       var.environment
    tag            =       var.tag
    domain_name    =       var.domain_name
    region         =       var.region
    ssh_key        =       var.ssh_key
}

module "terraform-project" {
    source = "./modules/project"

    project_name   =       var.project_name
    #resources      =       [format("do:droplet:%s",module.ubuntu-server.droplet_id)]
    resources      =       [module.ubuntu-server.droplet_urn]
}

module "server-record" {
    source = "./modules/record"

    domain_name    =       var.domain_name
    name           =       module.ubuntu-server.droplet_name
    value          =       module.ubuntu-server.droplet_ip_address
}