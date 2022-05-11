module "ubuntu-server" {
    source = "./modules/server"

    for_each = var.servers

    name           =       each.value.name
    image          =       each.value.image
    environment    =       each.value.environment
    tag            =       each.key
    domain_name    =       var.domain_name
    region         =       each.value.region
    ssh_key        =       var.ssh_key
}

module "terraform-project" {
    source = "./modules/project" 

    project_name   =       var.project_name
    # resources      =       [format("do:droplet:%s",module.ubuntu-server.droplet_id)]
    resources      =       values(module.ubuntu-server)[*].droplet_urn
}

module "server-record" {
    source = "./modules/record"

    count = length(module.ubuntu-server)

    domain_name    =       var.domain_name
    name           =       values(module.ubuntu-server)[count.index].droplet_name
    value          =       values(module.ubuntu-server)[count.index].droplet_ip_address
}
