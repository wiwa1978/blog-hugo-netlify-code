provider "vsphere" {
  user                 = var.vsphere_user
  password             = var.vsphere_password
  vsphere_server       = var.vsphere_server
  allow_unverified_ssl = true
}

data "vsphere_datacenter" "dc" {
  name = var.vsphere_datacenter
}

data "vsphere_network" "vm1_net" {
  name          = "VM Network"
  datacenter_id = data.vsphere_datacenter.dc.id
}

data "vsphere_network" "vm2_net" {
  name          = "VM Network"
  datacenter_id = data.vsphere_datacenter.dc.id
}

data "vsphere_network" "vm3_net" {
  name          = "VM Network"
  datacenter_id = data.vsphere_datacenter.dc.id
}

data "vsphere_datastore" "ds" {
  name          = var.vsphere_datastore
  datacenter_id = data.vsphere_datacenter.dc.id
}

data "vsphere_compute_cluster" "cl" {
  name          = var.vsphere_compute_cluster
  datacenter_id = data.vsphere_datacenter.dc.id
}

data "vsphere_virtual_machine" "template" {
  name          = var.vsphere_template
  datacenter_id = data.vsphere_datacenter.dc.id
}

resource "vsphere_virtual_machine" "server1" {
  count            = 1
  name             = var.server1_name
  resource_pool_id = data.vsphere_compute_cluster.cl.resource_pool_id
  datastore_id     = data.vsphere_datastore.ds.id

  num_cpus  = 2
  memory    = 4096
  guest_id  = data.vsphere_virtual_machine.template.guest_id
  scsi_type = data.vsphere_virtual_machine.template.scsi_type

  disk {
    label            = "disk0"
    size             = data.vsphere_virtual_machine.template.disks[0].size
    thin_provisioned = data.vsphere_virtual_machine.template.disks[0].thin_provisioned
  }

  folder = var.folder

  network_interface {
    network_id   = data.vsphere_network.vm1_net.id
    adapter_type = data.vsphere_virtual_machine.template.network_interface_types[0]
  }

  clone {
    linked_clone  = "false"
    template_uuid = data.vsphere_virtual_machine.template.id

    customize {
      linux_options {
        host_name = var.server1_name
        domain    = var.domain_name
      }

      network_interface {
        ipv4_address = var.server1_address
        ipv4_netmask = "24"
      }

      ipv4_gateway    = var.gateway
      dns_server_list = [var.dns_list]
      dns_suffix_list = [var.dns_search]
    }
  }
}

resource "vsphere_virtual_machine" "server2" {
  count            = 1
  name             = var.server2_name
  resource_pool_id = data.vsphere_compute_cluster.cl.resource_pool_id
  datastore_id     = data.vsphere_datastore.ds.id

  num_cpus = 2
  memory   = 4096
  guest_id = data.vsphere_virtual_machine.template.guest_id

  scsi_type = data.vsphere_virtual_machine.template.scsi_type

  disk {
    label            = "disk0"
    size             = data.vsphere_virtual_machine.template.disks[0].size
    thin_provisioned = data.vsphere_virtual_machine.template.disks[0].thin_provisioned
  }

  folder = var.folder

  network_interface {
    network_id   = data.vsphere_network.vm2_net.id
    adapter_type = data.vsphere_virtual_machine.template.network_interface_types[0]
  }

  clone {
    linked_clone  = "false"
    template_uuid = data.vsphere_virtual_machine.template.id

    customize {
      linux_options {
        host_name = var.server2_name
        domain    = var.domain_name
      }

      network_interface {
        ipv4_address = var.server2_address
        ipv4_netmask = "24"
      }

      ipv4_gateway    = var.gateway
      dns_server_list = [var.dns_list]
      dns_suffix_list = [var.dns_search]
    }
  }
}

resource "vsphere_virtual_machine" "server3" {
  count            = 1
  name             = var.server3_name
  resource_pool_id = data.vsphere_compute_cluster.cl.resource_pool_id
  datastore_id     = data.vsphere_datastore.ds.id

  num_cpus = 2
  memory   = 4096
  guest_id = data.vsphere_virtual_machine.template.guest_id

  scsi_type = data.vsphere_virtual_machine.template.scsi_type

  disk {
    label            = "disk0"
    size             = data.vsphere_virtual_machine.template.disks[0].size
    thin_provisioned = data.vsphere_virtual_machine.template.disks[0].thin_provisioned
  }

  folder = var.folder

  network_interface {
    network_id   = data.vsphere_network.vm3_net.id
    adapter_type = data.vsphere_virtual_machine.template.network_interface_types[0]
  }

  clone {
    linked_clone  = "false"
    template_uuid = data.vsphere_virtual_machine.template.id

    customize {
      linux_options {
        host_name = var.server3_name
        domain    = var.domain_name
      }

      network_interface {
        ipv4_address = var.server3_address
        ipv4_netmask = "24"
      }

      ipv4_gateway    = var.gateway
      dns_server_list = [var.dns_list]
      dns_suffix_list = [var.dns_search]
    }
  }
}