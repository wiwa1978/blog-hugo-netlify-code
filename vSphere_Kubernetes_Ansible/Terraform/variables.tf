variable "vsphere_server" {
  default = "10.x.y.z"
}

variable "vsphere_user" {
  default = "administrator@vsphere.local"
}

variable "vsphere_password" {
  default = "***"
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

variable "server1_name" {
  default = "wauterw-k8s-master"
}

variable "server2_name" {
  default = "wauterw-k8s-worker01"
}

variable "server3_name" {
  default = "wauterw-k8s-worker02"
}

variable "server1_address" {
  default = "10.16.2.236"
}

variable "server2_address" {
  default = "10.16.2.237"
}

variable "server3_address" {
  default = "10.16.2.238"
}

variable "gateway" {
  default = "10.16.2.254"
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