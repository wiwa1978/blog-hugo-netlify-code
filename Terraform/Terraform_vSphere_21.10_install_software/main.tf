#===============================================================================
# vSphere Provider
#===============================================================================

provider "vsphere" {
  vsphere_server       =    var.VAR_VSPHERE_SERVER
  user                 =    var.VAR_VSPHERE_USERNAME
  password             =    var.VAR_VSPHERE_PASSWORD
  allow_unverified_ssl =    true
}

#===============================================================================
# vSphere Data
#===============================================================================

module "ubuntu-server" {
  source = "./modules/ubuntu-server"

  # Define vSphere variables
  vsphere_datacenter    =   var.VAR_VSPHERE_DATACENTER
  vsphere_cluster       =   var.VAR_VSPHERE_CLUSTER
  vsphere_vm_datastore  =   var.VAR_VSPHERE_VM_DATASTORE
  vsphere_network       =   var.VAR_VSPHERE_NETWORK

#===============================================================================
# vSphere Resources
#===============================================================================

  name                      =       var.vm_name
  vm_template_name          =       var.vm_template
  network_ip                =       var.network_ip
  network_mask              =       var.network_mask
  network_gateway           =       var.network_gateway
  dns_server                =       var.dns_server

  cpu_count                 =       var.cpu_count
  memory_count              =       var.memory_count

  #ssh_key_file              =       format("%s/%s",var.ssh_key_directory, var.ssh_key_name)

  ssh_key_directory         =       var.ssh_key_directory
  ssh_key_name              =       var.ssh_key_name

  vm_username               =       var.vm_username
  vm_password               =       var.vm_password

}                                     