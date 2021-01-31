variable "vsphere_server" {
  default = "10.16.2.99"
}

variable "vsphere_user" {
  default = "administrator@vsphere.local"
}

variable "vsphere_password" {
  default = "---"
}

variable "vsphere_datacenter" {
  default = "SaS-DC"
}

variable "vsphere_datastore" {
  default = "datastore-UCS-POD1-2"
}

variable "vsphere_compute_cluster" {
  default = "SaS-Cluster"
}

variable "vsphere_template" {
  default = "ubuntu-1604-server-template"
}

variable "folder" {
  default = "wauterw"
}

variable "aci_vm1_name" {
  default = "ACI1-ACI"
}

variable "aci_vm2_name" {
  default = "ACI2-ACI"
}

variable "aci_vm1_address" {
  default = "10.16.100.10"
}

variable "aci_vm2_address" {
  default = "10.16.100.11"
}

variable "gateway" {
  default = "10.16.100.1"
}

variable "dns_list" {
  default = "10.9.15.1"
}

variable "dns_search" {
  default = "cisco.com"
}

variable "domain_name" {
  default = "cisco.com"
}

