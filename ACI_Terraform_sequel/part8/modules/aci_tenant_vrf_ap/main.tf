resource "aci_tenant" "this" {
  name = var.tenant_name
  description = var.tenant_description
}

resource "aci_vrf" "this" {
  for_each = var.vrfs

  tenant_dn = aci_tenant.this.id
  name      = var.vrfs[each.key].vrf_name
}

resource "aci_application_profile" "this" {
  for_each = var.aps
  
  tenant_dn = aci_tenant.this.id
  name      = var.aps[each.key].ap_name
}

