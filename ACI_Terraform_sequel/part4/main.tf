module "tenant_1" {
  source                =   "./modules/aci_tenant"
  tenant_name           =   var.tenants["tenant1_name"]
  tenant_description    =   var.tenants["tenant1_description"]
}

module "tenant_2" {
  source                =   "./modules/aci_tenant"
  tenant_name           =   var.tenants["tenant2_name"]
  tenant_description    =   var.tenants["tenant2_description"]
}

module "vrf_1" {
  source        =   "./modules/aci_vrf"
  tenant        =   module.tenant_1.tenant
  vrf_name      =   var.vrfs["vrf_1_name"]
}

module "vrf_2" {
  source        =   "./modules/aci_vrf"
  tenant        =   module.tenant_2.tenant
  vrf_name      =   var.vrfs["vrf_2_name"]
}

module "app_1" {
  source        =   "./modules/aci_ap"
  tenant        =   module.tenant_1.tenant
  ap_name       =   var.aps["application_profile_1_name"]
}

module "app_2" {
  source        =   "./modules/aci_ap"
  tenant        =   module.tenant_2.tenant
  ap_name       =   var.aps["application_profile_2_name"]
}

module "bd_1" {
  source        =   "./modules/aci_bd"
  tenant        =   module.tenant_1.tenant
  vrf           =   module.vrf_1.vrf
  bd_name       =   var.bds["bd_1_name"]
}

module "bd_2" {
  source        =   "./modules/aci_bd"
  tenant        =   module.tenant_2.tenant
  vrf           =   module.vrf_2.vrf
  bd_name       =   var.bds["bd_2_name"]
}
