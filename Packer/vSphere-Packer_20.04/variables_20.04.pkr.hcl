variable "version" {
  description = "VM version"
  default     = "0.1.0"
}

variable "vm_name_prefix" {
  default = "Ubuntu_20_04_Wim"
}

variable "vsphere_username" {
  description = "Username to authenticate to vsphere"
  default     = env("TF_VAR_VSPHERE_USERNAME")
}

variable "vsphere_password" {
  description = "Password to authenticate to vsphere"
  default     = env("TF_VAR_VSPHERE_PASSWORD")
  sensitive   = true
}

variable "vsphere_cluster" {
  description = "vsphere cluster to use for VM creation."
  default     = env("TF_VAR_VSPHERE_CLUSTER")
}

variable "vsphere_datacenter" {
  description = "vsphere datacenter to use for VM creation."
  default     = env("TF_VAR_VSPHERE_DATACENTER")
}

variable "vsphere_vm_datastore" {
  description = "vsphere datastore for VMs."
  default     = env("TF_VAR_VSPHERE_VM_DATASTORE")
}

variable "vsphere_server" {
  description = "vsphere server to build the VM on"
  default     = env("TF_VAR_VSPHERE_SERVER")
}

variable "vsphere_network" {
  description = "vsphere network for VM"
  default     = env("TF_VAR_VSPHERE_NETWORK")
}

variable "guest_os_type" {
  default = "ubuntu64Guest"
}

variable "insecure_connection" {
  default = "true"
}

variable "CPUs" {
  default = 4
}

variable "RAM" {
  default = 8192
}

variable "boot_wait" {
  default = "5s"
}

variable "common_data_source" {
  default = "http"
}


variable "boot_command" {
  default = [
      "<esc><esc><esc>",
      "<enter><wait>",
      "/casper/vmlinuz ",
      "root=/dev/sr0 ",
      "initrd=/casper/initrd ",
      "autoinstall ",
      "<enter>"
  ]
}

variable "iso_checksum" {
  default = "sha256:28ccdb56450e643bad03bb7bcf7507ce3d8d90e8bf09e38f6bd9ac298a98eaad"
}

variable "iso_urls" {
  default = ["https://releases.ubuntu.com/20.04/ubuntu-20.04.4-live-server-amd64.iso"] 
}

variable "http_directory" {
  default = "http"
}