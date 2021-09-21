resource "aci_tenant" "this" {
  name = var.tenant_name
  description = var.tenant_description
}
