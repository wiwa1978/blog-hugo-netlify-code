output "tenants" {
    value   =   { for p in sort(keys(var.tenants)) : p => module.tenant[p].tenant.name }
}

output "vrfs" {
    value   =   { for p in sort(keys(var.tenants)) : p => module.vrf[p].vrf.name }
}

output "aps" {
    value   =   { for p in sort(keys(var.tenants)) : p => module.app[p].applicationprofile.name }
}

output "bds" {
    value   =   { for p in sort(keys(var.tenants)) : p => module.bd[p].bridge_domain.name }
}
