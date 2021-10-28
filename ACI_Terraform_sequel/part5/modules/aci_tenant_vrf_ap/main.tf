resource "aci_tenant" "this" {
  name = var.tenant_name
  description = var.tenant_description
}

resource "aci_vrf" "this" {
  tenant_dn = aci_tenant.this.id
  name      = var.vrf_name
}

resource "aci_application_profile" "this" {
  tenant_dn = aci_tenant.this.id
  name      = var.ap_name
}

