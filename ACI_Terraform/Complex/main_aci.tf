provider "aci" {
    username = var.aci_user
    password = var.aci_password
    url      = var.apic_ip
    insecure = true
}

resource "aci_tenant" "tenant" {
  name        = var.aci_tn
  description = "Tenant {var.aci_tn} created by terraform"
}

resource "aci_bridge_domain" "bd" {
  tenant_dn  = aci_tenant.tenant.id
  name       = var.aci_bd
}
resource "aci_subnet" "subnet" {
  bridge_domain_dn  = aci_bridge_domain.bd.id
  ip                = var.aci_subnet
  scope             = var.aci_subnet_type
}

resource "aci_filter" "filter" {
    tenant_dn   = aci_tenant.tenant.id
    name        = var.aci_filter
}

resource "aci_filter_entry" "filter_entry" {
    filter_dn     = aci_filter.filter.id
    name          = var.aci_filter_entry
    d_from_port   = var.aci_filter_port_from
    d_to_port     = var.aci_filter_port_to
    ether_t       = "ipv4"
    prot          = "tcp"
}

resource "aci_contract" "contract" {
    tenant_dn   = aci_tenant.tenant.id
    name        = var.aci_contract
}

resource "aci_contract_subject" "contract_subject" {
    contract_dn   = aci_contract.contract.id
    name          = var.contract_subject
}

resource "aci_application_profile" "ap" {
  tenant_dn  = aci_tenant.tenant.id
  name = var.aci_ap
}

resource "aci_application_epg" "epg" {
  count = length(var.aci_epgs)
  application_profile_dn  = aci_application_profile.ap.id
  name                    =  var.aci_epgs[count.index]
  relation_fv_rs_bd       = aci_bridge_domain.bd.name
  relation_fv_rs_cons     = [aci_contract.contract.name]
}

