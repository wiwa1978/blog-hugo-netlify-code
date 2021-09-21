module "tenantvrfap" {
  source              =   "./modules/aci_tenant_vrf_ap"

  for_each            =   var.tenants

  tenant_name         =   each.value.tenant_name
  tenant_description  =   each.value.tenant_description
  vrf_name            =   var.vrfs[each.key].vrf_name
  ap_name             =   var.aps[each.key].ap_name

}

module "bd" {
  source        =   "./modules/aci_bd"

  for_each      =   var.tenants

  tenant        =   module.tenantvrfap[each.key].tenant
  vrf           =   module.tenantvrfap[each.key].vrf
  
  bd_name       =   var.bds[each.key].bd_name
}


