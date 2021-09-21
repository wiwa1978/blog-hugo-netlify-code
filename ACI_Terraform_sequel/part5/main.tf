module "tenant" {
  source        =   "./modules/aci_tenant"

  for_each     =    var.tenants

  tenant_name           =   each.value.tenant_name
  tenant_description    =   each.value.tenant_description
}

module "vrf" {
  source        =   "./modules/aci_vrf"

  for_each     =    var.tenants

  tenant        =   module.tenant[each.key].tenant
  vrf_name      =   var.vrfs[each.key].vrf_name
}

module "app" {
  source        =   "./modules/aci_ap"

  for_each     =    var.tenants

  tenant        =   module.tenant[each.key].tenant
  ap_name       =   var.aps[each.key].ap_name
}


module "bd" {
  source        =   "./modules/aci_bd"

  for_each     =    var.tenants

  tenant        =   module.tenant[each.key].tenant
  vrf           =   module.vrf[each.key].vrf
  
  bd_name       =   var.bds[each.key].bd_name
}

