resource "aci_bridge_domain" "this" {
  tenant_dn          = var.tenant.id
  name               = var.bd_name
  relation_fv_rs_ctx = var.vrf.id
}

