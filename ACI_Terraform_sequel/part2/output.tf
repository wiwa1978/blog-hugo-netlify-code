output "tenant1" {
    description = "Tenant 1 name"
    value   =  aci_tenant.tenant_1.name
}

output "tenant2" {
    description = "Tenant 2 name"
    value   =  aci_tenant.tenant_2.name
}

output "ap1" {
    description = "Application Profile 1 name"
    value   =  aci_application_profile.ap_1.name
}

output "ap2" {
    description = "Application Profile 2 name"
    value   =  aci_application_profile.ap_2.name
}

output "vrf1" {
    description = "VRF 1 name"
    value   =  aci_vrf.vrf_1.name
}

output "vrf2" {
    description = "VRF 2 name"
    value   =  aci_vrf.vrf_2.name
}

output "bd1" {
    description = "BD 1 name"
    value   =  aci_bridge_domain.bd_1.name
}

output "bd2" {
    description = "BD 2 name"
    value   =  aci_bridge_domain.bd_2.name
}
