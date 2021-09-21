resource "aci_vrf" "this" {
  tenant_dn = var.tenant.id
  name      = var.vrf_name
}
