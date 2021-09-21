resource "aci_bridge_domain" "this" {
  for_each = var.bds
  
  tenant_dn          = var.tenant.id
  name               = var.bds[each.key].bd_name
  
  //relation_fv_rs_ctx = var.bds[each.key].vrf
}

