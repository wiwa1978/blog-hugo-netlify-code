resource "aci_bridge_domain" "this" {
  for_each = var.bds
  
  tenant_dn          = var.tenant.id
  name               = each.value.bd_name
  
  relation_fv_rs_ctx = each.value.vrf.id
}

