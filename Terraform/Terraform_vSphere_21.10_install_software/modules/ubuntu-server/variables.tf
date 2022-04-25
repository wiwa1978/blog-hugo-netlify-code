#===============================================================================
# vSphere Data
#===============================================================================

variable "vsphere_datacenter" {
  description = "vCenter Datacenter in which server will be deployed"
  type        = string
}

variable "vsphere_network" {
  description = "vCenter Port-Group that will be used by the server"
  type        = string
}

variable "vsphere_cluster" {
  description = "vCenter Cluster on which the server will be deployed"
  type        = string
}

variable "vsphere_vm_datastore" {
  description = "vCenter Datastore that will be used by the server"
  type        = string
}


#===============================================================================
# vSphere Resources
#===============================================================================


variable "name" {
  description = "Name of the server"
  type        = string
}

variable "vm_template_name" {
  description = "Name of the VM the server will be cloned from"
  type        = string
}


variable "cpu_count" {
  description = "vCPU count for the server"
  type        = number
  default     = null
}

variable "memory_count" {
  description = "Memory count for the server"
  type        = number
  default     = null
}

variable "network_ip" {
  description = "IP Address of the server (excluding the netmask)"
  type        = string
}

variable "network_mask" {
  description = "Netmask for the server"
  type        = number
}


variable "network_gateway" {
  description = "Default Gateway for the server"
  type        = string
}

variable "dns_server" {
  description = "DNS Server"
  type        = string
}

variable "dns_domain" {
  description = "DNS Search Domain"
  type        = string
  default     = "cisco.com"
}

// variable "ssh_key_file" {
//   description = "Name of the SSH key added onto the server upon instantiation"
//   type        = string
// }

variable "ssh_key_directory" {
  description = "Name of the SSH key added onto the server upon instantiation"
  type        = string
}

variable "ssh_key_name" {
  description = "Name of the SSH key added onto the server upon instantiation"
  type        = string
}

variable "vm_username" {
  description = "Name of the additional user"
  type        = string
}

variable "vm_password" {
  description = "Password of the additional user"
  type        = string
}
