variable "apic_server" {
  default = "https://10.16.2.1"
}

variable "apic_username" {
  default = "admin"
}

variable "apic_password" {
  default = "---"
}

variable "aci_tenant" {
  default = "Tenant_test_123"
}

variable "aci_vrf" {
  default = "VRF_TF"
}

variable "aci_bd" {
  default = "BD_TF"
}

variable "aci_bd_subnet" {
  default = "10.16.100.1/24"
}

variable "aci_app_profile" {
  default = "AppProfile_TF"
}

variable "aci_epg_1" {
  default = "EPG_TF_1"
}

variable "aci_epg_2" {
  default = "EPG_TF_2"
}

variable "aci_contract_subject" {
  default = "Subject_TF"
}

variable "aci_filter_allow_https" {
  default = "allow_https"
}

variable "aci_filter_allow_icmp" {
  default = "allow_icmp"
}

variable "aci_filter_entry_https" {
  default = "https"
}

variable "aci_filter_entry_icmp" {
  default = "icmp"
}

variable "provider_profile_dn" {
  default = "uni/vmmp-VMware"
}

variable "vmm_domain" {
  default = "uni/vmmp-VMware/dom-dvs-demo-dynamic"
}

