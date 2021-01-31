resource "aci_tenant" "Tenant_TF_Demo" {
  name        = var.aci_tenant
  description = "Tenant created by TF"
}

resource "aci_vrf" "VRF_TF_Demo" {
  tenant_dn = aci_tenant.Tenant_TF_Demo.id
  name      = var.aci_vrf
}

resource "aci_bridge_domain" "BD_TF_Demo" {
  tenant_dn          = aci_tenant.Tenant_TF_Demo.id
  name               = var.aci_bd
  description        = "BD created by TF"
  relation_fv_rs_ctx = aci_vrf.VRF_TF_Demo.name
}