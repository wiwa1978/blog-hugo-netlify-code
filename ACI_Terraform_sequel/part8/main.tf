module "tenantvrfap" {
  source              =   "./modules/aci_tenant_vrf_ap"

  for_each            =   var.tenants

  tenant_name         =   each.value.tenant_name
  tenant_description  =   each.value.tenant_description
  vrfs                =   var.vrfs[each.key]
  aps                 =   var.aps[each.key]

}

module "bd" {
  source        =   "./modules/aci_bd"

  for_each      =   var.bds

  tenant        =   module.tenantvrfap[each.value.tenant].tenant
  //vrf           =   module.tenantvrfap[each.value.vrf].vrf
  
  bds           =   var.bds[each.key]

}


