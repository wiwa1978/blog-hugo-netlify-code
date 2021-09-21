resource "aci_application_profile" "this" {
  tenant_dn = var.tenant.id
  name      = var.ap_name
}

