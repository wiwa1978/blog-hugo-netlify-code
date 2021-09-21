output "tenant1" {
    description = "Tenant 1 name"
    value   =   module.tenant_1.tenant.name
}

output "tenant2" {
    description = "Tenant 2 name"
    value   =   module.tenant_2.tenant.name
}

output "ap1" {
    description = "Application Profile 1 name"
    value   =  module.app_1.applicationprofile.name
}

output "ap2" {
    description = "Application Profile 2 name"
    value   =  module.app_2.applicationprofile.name
}

output "vrf1" {
    description = "VRF 1 name"
    value   =  module.vrf_1.vrf.name
}

output "vrf2" {
    description = "VRF 2 name"
    value   =  module.vrf_2.vrf.name
}

output "bd1" {
    description = "BD 1 name"
    value   =  module.bd_1.bridge_domain.name
}

output "bd2" {
    description = "BD 2 name"
    value   =  module.bd_2.bridge_domain.name
}