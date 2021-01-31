provider "aci" {
  username = var.apic_username
  password = var.apic_password
  url      = var.apic_server
  insecure = true
}

resource "aci_tenant" "Tenant_TF" {
  name        = var.aci_tenant
  description = "Tenant created by TF"
}

resource "aci_vrf" "VRF_TF" {
  tenant_dn          = aci_tenant.Tenant_TF.id
  name               = var.aci_vrf
  description        = "VRF created by TF"
  bd_enforced_enable = false
}

resource "aci_bridge_domain" "BD_TF" {
  tenant_dn          = aci_tenant.Tenant_TF.id
  name               = var.aci_bd
  description        = "BD created by TF"
  relation_fv_rs_ctx = aci_vrf.VRF_TF.name
}

resource "aci_subnet" "Subnet_BD" {
  bridge_domain_dn = aci_bridge_domain.BD_TF.id

  #name             = "Subnet"
  ip = var.aci_bd_subnet
}

resource "aci_application_profile" "AppProfile_TF" {
  tenant_dn   = aci_tenant.Tenant_TF.id
  name        = var.aci_app_profile
  description = "App profile created by TF"
}

resource "aci_application_epg" "EPG_TF_1" {
  application_profile_dn = aci_application_profile.AppProfile_TF.id
  name                   = var.aci_epg_1
  description            = "EPG created by TF"
  relation_fv_rs_bd      = aci_bridge_domain.BD_TF.name
  relation_fv_rs_dom_att = [var.vmm_domain]
  relation_fv_rs_cons    = [aci_contract.Contract_EPG1_EPG2.name]
}

resource "aci_application_epg" "EPG_TF_2" {
  application_profile_dn = aci_application_profile.AppProfile_TF.id
  name                   = var.aci_epg_2
  description            = "EPG created by TF"
  relation_fv_rs_bd      = aci_bridge_domain.BD_TF.name
  relation_fv_rs_dom_att = [var.vmm_domain]
  relation_fv_rs_prov    = [aci_contract.Contract_EPG1_EPG2.name]
}

resource "null_resource" "delay" {
  provisioner "local-exec" {
    command = "sleep 5"
  }

  triggers = {
    "epg1" = aci_application_epg.EPG_TF_1.id
    "epg2" = aci_application_epg.EPG_TF_2.id
  }
}

resource "aci_contract" "Contract_EPG1_EPG2" {
  tenant_dn   = aci_tenant.Tenant_TF.id
  name        = "Contract_EPG1_EPG2"
  description = "Contract created by TF"
}

resource "aci_contract_subject" "Contract_Subject" {
  contract_dn                  = aci_contract.Contract_EPG1_EPG2.id
  name                         = var.aci_contract_subject
  relation_vz_rs_subj_filt_att = [aci_filter.Filter_Allow_HTTPS.name, aci_filter.Filter_Allow_ICMP.name]
}

resource "aci_filter" "Filter_Allow_HTTPS" {
  tenant_dn = aci_tenant.Tenant_TF.id
  name      = var.aci_filter_allow_https
}

resource "aci_filter" "Filter_Allow_ICMP" {
  tenant_dn = aci_tenant.Tenant_TF.id
  name      = var.aci_filter_allow_icmp
}

resource "aci_filter_entry" "Filter_Entry_HTTPS" {
  name        = var.aci_filter_entry_https
  filter_dn   = aci_filter.Filter_Allow_HTTPS.id
  ether_t     = "ip"
  prot        = "tcp"
  d_from_port = "https"
  d_to_port   = "https"
  stateful    = "yes"
}

resource "aci_filter_entry" "Filter_Entry_ICMP" {
  name      = var.aci_filter_entry_icmp
  filter_dn = aci_filter.Filter_Allow_ICMP.id
  ether_t   = "ip"
  prot      = "icmp"
  stateful  = "yes"
}

