# Remember to run Terraform with a tag -parallelism=1
data "mso_site" "site1" {
  name  = var.site1
}

resource "mso_tenant" "tenant1" {
  name         = var.tenant1
  display_name = var.tenant1
  description  = "Created by Terraform!"
  site_associations {
    site_id = data.mso_site.site1.id
  }
}

resource "mso_schema" "schema1" {
  name          = var.schema1
  template_name = var.template1
  tenant_id     = mso_tenant.tenant1.id
}

resource "mso_schema_site" "site1" {
  schema_id  = mso_schema.schema1.id
  site_id  = data.mso_site.site1.id
  template_name  = var.template1
}

resource "mso_schema_template_anp" "ap1" {
  schema_id    = mso_schema.schema1.id
  template     = var.template1
  name         = var.ap1
  display_name = var.ap1
}

resource "mso_schema_template_anp" "ap2" {
  schema_id    = mso_schema.schema1.id
  template     = var.template1
  name         = var.ap2
  display_name = var.ap2
}

resource "mso_schema_template_vrf" "vrf1" {
  schema_id    = mso_schema.schema1.id
  template     = var.template1
  name         = var.vrf1
  display_name = var.vrf1
  layer3_multicast= true
  vzany           = true
}

resource "mso_schema_template_bd" "bd1" {
  schema_id     = mso_schema.schema1.id
  template_name = var.template1
  name          = var.bd1
  display_name  = var.bd1
  vrf_name      = mso_schema_template_vrf.vrf1.name
}

resource "mso_schema_template_anp_epg" "epg1" {
  schema_id     = mso_schema.schema1.id
  template_name = var.template1
  anp_name      = mso_schema_template_anp.ap1.name
  name          = var.epg1
  bd_name       = mso_schema_template_bd.bd1.name
  vrf_name      = mso_schema_template_vrf.vrf1.name
  display_name  = var.epg1
}

resource "mso_schema_template_anp_epg" "epg2" {
  schema_id     = mso_schema.schema1.id
  template_name = var.template1
  anp_name      = mso_schema_template_anp.ap2.name
  name          = var.epg2
  bd_name       = mso_schema_template_bd.bd1.name
  vrf_name      = mso_schema_template_vrf.vrf1.name
  display_name  = var.epg2
}


resource "mso_schema_template_contract" "contract1" {
  schema_id     = mso_schema.schema1.id
  template_name = var.template1
  contract_name = var.contract_allow_all
  display_name  = var.contract_allow_all
  filter_type   = "bothWay"
  scope         = "context"
  filter_relationships = {
    filter_schema_id     = mso_schema.schema1.id
    filter_template_name = var.template1
    filter_name          = mso_schema_template_filter_entry.any.name
  }
  directives = ["none", "log"]
}


resource "mso_schema_template_filter_entry" "any" {
  schema_id          = mso_schema.schema1.id
  template_name      = var.template1
  name               = var.filter_any
  display_name       = var.filter_any
  entry_name         = "any"
  entry_display_name = "any"
  ether_type         = "ipv4"
  ip_protocol        = "tcp"
  destination_from   = "unspecified"
  destination_to     = "unspecified"
  source_from        = "unspecified"
  source_to          = "unspecified"
  arp_flag           = "unspecified"
}

resource "mso_schema_template_anp_epg_contract" "epg1_any" {
  schema_id         = mso_schema.schema1.id
  template_name     = var.template1
  anp_name          = mso_schema_template_anp.ap1.name
  epg_name          = mso_schema_template_anp_epg.epg1.name
  contract_name     = mso_schema_template_contract.contract1.contract_name
  relationship_type = "provider"
}

resource "mso_schema_template_anp_epg_contract" "epg2_any" {
  schema_id         = mso_schema.schema1.id
  template_name     = var.template1
  anp_name          = mso_schema_template_anp.ap2.name
  epg_name          = mso_schema_template_anp_epg.epg2.name
  contract_name     = mso_schema_template_contract.contract1.contract_name
  relationship_type = "consumer"
}

output "mso_tenant_name" {
  value = mso_tenant.tenant1.name
}

output "mso_schema_name" {
  value = mso_schema.schema1.name
}

output "mso_schema_template" {
  value = mso_schema.schema1.template_name
}

output "mso_schema_template_vrf" {
  value = mso_schema_template_vrf.vrf1.name
}

output "mso_schema_template_bd" {
  value = mso_schema_template_bd.bd1.name
}

output "mso_schema_template_anp1" {
  value = mso_schema_template_anp.ap1.name
}

output "mso_schema_template_anp2" {
  value = mso_schema_template_anp.ap2.name
}

output "mso_schema_template_anp_epg1" {
  value = mso_schema_template_anp_epg.epg1.name
}

output "mso_schema_template_anp_epg2" {
  value = mso_schema_template_anp_epg.epg2.name
}

output "mso_schema_template_contract" {
  value = mso_schema_template_contract.contract1.id
}

output "mso_schema_template_filter_entry" {
  value = mso_schema_template_filter_entry.any.id
}

output "mso_schema_template_anp_epg_contract_1" {
  value = mso_schema_template_anp_epg_contract.epg1_any.id
}

output "mso_schema_template_anp_epg_contract_2" {
  value = mso_schema_template_anp_epg_contract.epg2_any.id
}