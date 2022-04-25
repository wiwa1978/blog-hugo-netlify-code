packer {
  required_plugins {
    vsphere = {
      version = ">= 0.0.1"
      source  = "github.com/hashicorp/vsphere"
    }
  }
}

locals {
  buildtime = formatdate("YYYY-MM-DD hh:mm ZZZ", timestamp())
}


source "vsphere-iso" "ubuntu" {
  username            = var.vsphere_username
  password            = var.vsphere_password
  vcenter_server      = var.vsphere_server
  cluster             = var.vsphere_cluster
  datacenter          = var.vsphere_datacenter
  datastore           = var.vsphere_vm_datastore
  guest_os_type       = var.guest_os_type
  insecure_connection = var.insecure_connection
  iso_checksum        = var.iso_checksum
  iso_urls            = var.iso_urls
  

  vm_name             = format("%s_%s", var.vm_name_prefix, var.version)
  CPUs                = var.CPUs
  RAM                 = var.RAM
  boot_wait           = var.boot_wait
  boot_command        = var.boot_command
  boot_order          = "disk,cdrom"
  remove_cdrom        = true
  notes                = "Built by HashiCorp Packer on ${local.buildtime}."

  cd_files = [
    "./http/meta-data",
    "./http/user-data"
  ]
  cd_label = "cidata"

  network_adapters {
    network      = var.vsphere_network
    network_card = "vmxnet3"
  }
  storage {
    disk_size             = 40960
    disk_thin_provisioned = true
  }

  ssh_username           = "ubuntu"
  ssh_password           = "ubuntu"
  ssh_timeout            = "30m"
  ssh_handshake_attempts = 60 # To allow for initial SSH failure during VM build

  convert_to_template = true
}

build {
  sources = [
    "source.vsphere-iso.ubuntu"
  ]

  provisioner "shell" {
    inline = [
      "mkdir /home/ubuntu/scripts"
    ]
  }

  provisioner "file" {
    source      = "scripts/fix_vm_customization_bug.sh"
    destination = "/home/ubuntu/scripts/fix_vm_customization_bug.sh"
  }

  provisioner "shell" {
    inline = [
      ". ./scripts/fix_vm_customization_bug.sh"
    ]
  }

  provisioner "file" {
    source      = "scripts/software_install.sh"
    destination = "/home/ubuntu/scripts/software_install.sh"
  }

  provisioner "shell" {
    inline = [
      ". ./scripts/software_install.sh"
    ]
  }
  
}

