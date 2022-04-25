#===============================================================================
# vSphere Provider
#===============================================================================

variable "VAR_VSPHERE_SERVER" {
  description = "Name or IP of the vSphere vCenter"
  type        = string
}

variable "VAR_VSPHERE_USERNAME" {
  description = "vSphere vCenter username"
  type        = string
}

variable "VAR_VSPHERE_PASSWORD" {
  description = "vSphere vCenter passwor"
  type        = string
  sensitive   = true
}


#===============================================================================
# vSphere Data
#===============================================================================

variable "VAR_VSPHERE_DATACENTER" {
  description = "vCenter Datacenter in which the VMs will be deployed"
  type        = string
}

variable "VAR_VSPHERE_CLUSTER" {
  description = "vCenter Cluster on which the VMs will be deployed (Optional parameter, leave empty if not used)"
  type        = string
}

variable "VAR_VSPHERE_VM_DATASTORE" {
  description = "vCenter Datastore that will be used by the VMs"
  type        = string
}

variable "VAR_VSPHERE_NETWORK" {
  description = "vCenter Port-Group that will be used by the VMs"
  type        = string
}


#===============================================================================
# vSphere Resources
#===============================================================================


variable "vm_name" {
  description = "Name for the VM getting deployed"
  type        = string
}

variable "vm_template" {
  description = "Name of the template for the server "
  type        = string
}

variable "network_ip" {
  description = "IP address for the VM getting deployed"
  type        = string
}

variable "network_mask" {
  description = "Network mask for the VM getting deployed"
  type        = number
}

variable "network_gateway" {
  description = "Network GW for the VM getting deployed"
  type        = string
}

variable "dns_server" {
  description = "DNS server for the VM getting deployed"
  type        = string
}

variable "cpu_count" {
  description = "Amount of CPUs for the VM getting deployed"
  type        = number
}

variable "memory_count" {
  description = "Amount of memory for the VM getting deployed"
  type        = number
}
