variable "version" {
  description = "VM version"
  default     = "0.1.0"
}

variable "vm_name_prefix" {
  default = "Ubuntu_22_04_Wim"
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

variable "boot_command" {
  default = [
    "c<wait>",
    "linux /casper/vmlinuz autoinstall ds=\"nocloud-net;seedfrom=http://{{.HTTPIP}}:{{.HTTPPort}}/\" ---",
    "<enter><wait>",
    "initrd /casper/initrd",
    "<enter><wait>",
    "boot",
    "<enter>"
  ]
}

variable "iso_checksum" {
  default = "sha256:39fdd5f7e868ab7981b492a8887dbaec85acf798b209162a37893cb4b209a26b" # 22.04
}

variable "iso_urls" {
  default = ["https://releases.ubuntu.com/22.04/ubuntu-22.04-beta-live-server-amd64.iso"] # 22.04
}

variable "http_directory" {
  default = "http"
}