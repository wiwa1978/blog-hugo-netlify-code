resource "aci_tenant" "tenant_1" {
  name = var.aci_tenant_1_name
}

resource "aci_tenant" "tenant_2" {
  name = var.aci_tenant_2_name
}

resource "aci_application_profile" "ap_1" {
  tenant_dn = aci_tenant.tenant_1.id
  name      = var.application_profile_1_name
}

resource "aci_application_profile" "ap_2" {
  tenant_dn = aci_tenant.tenant_2.id
  name      = var.application_profile_2_name
}

resource "aci_vrf" "vrf_1" {
  tenant_dn = aci_tenant.tenant_1.id
  name      = var.vrf_1_name
}

resource "aci_vrf" "vrf_2" {
  tenant_dn = aci_tenant.tenant_2.id
  name      = var.vrf_2_name
}

resource "aci_bridge_domain" "bd_1" {
  tenant_dn          = aci_tenant.tenant_1.id
  name               = var.bd_1_name
  relation_fv_rs_ctx = aci_vrf.vrf_1.id
}

resource "aci_bridge_domain" "bd_2" {
  tenant_dn          = aci_tenant.tenant_2.id
  name               = var.bd_2_name
  relation_fv_rs_ctx = aci_vrf.vrf_2.id
}