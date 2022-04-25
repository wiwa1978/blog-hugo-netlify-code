locals {
  script_directory = "${path.module}/scripts/"
}

# ssh_key_file_private will contain: ssh_keys/ed25519_git
locals {
  ssh_key_file_private = format("%s/%s",var.ssh_key_directory, var.ssh_key_name)
}

# ssh_key_file_public will contain: ssh_keys/ed25519_git.pub
locals {
  ssh_key_file_public = format("%s/%s%s",var.ssh_key_directory, var.ssh_key_name, ".pub")
}


#===============================================================================
# vSphere Data
#===============================================================================

data "vsphere_datacenter" "datacenter" {
  name = var.vsphere_datacenter
}

data "vsphere_network" "network" {
  name          = var.vsphere_network
  datacenter_id = data.vsphere_datacenter.datacenter.id
}


data "vsphere_compute_cluster" "cluster" {
  name          = var.vsphere_cluster
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_datastore" "datastore" {
  name          = var.vsphere_vm_datastore
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

data "vsphere_virtual_machine" "template" {
  name          = var.vm_template_name
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

#===============================================================================
# vSphere Resources
#===============================================================================

resource "vsphere_virtual_machine" "vm" {
  name             = var.name
  resource_pool_id = data.vsphere_compute_cluster.cluster.resource_pool_id
  datastore_id     = data.vsphere_datastore.datastore.id
  
  num_cpus         = coalesce(var.cpu_count, data.vsphere_virtual_machine.template.num_cpus)
  memory           = coalesce(var.memory_count, data.vsphere_virtual_machine.template.memory)
  guest_id         = data.vsphere_virtual_machine.template.guest_id
  scsi_type        = data.vsphere_virtual_machine.template.scsi_type

  network_interface {
    network_id   = data.vsphere_network.network.id
    adapter_type = data.vsphere_virtual_machine.template.network_interface_types[0]
  }

  disk {
    label            = "disk0"
    size             = data.vsphere_virtual_machine.template.disks.0.size
    eagerly_scrub    = data.vsphere_virtual_machine.template.disks.0.eagerly_scrub
    thin_provisioned = data.vsphere_virtual_machine.template.disks.0.thin_provisioned
  }

  clone {
    template_uuid = data.vsphere_virtual_machine.template.id

    customize {
      linux_options {
        host_name = var.name
        domain    = "localhost.domain"
      }
      network_interface {
        ipv4_address = var.network_ip
        ipv4_netmask = var.network_mask
      }
      ipv4_gateway    = var.network_gateway
      dns_suffix_list = [var.dns_domain]
      dns_server_list = [var.dns_server]
    }
  }



  # Copy ssh_keys
  provisioner "file" {
    source      = var.ssh_key_directory
    destination = format("%s/%s", "/tmp/", var.ssh_key_directory)

    connection {
      type     = "ssh"
      user     = "ubuntu"
      password = "ubuntu"
      host     = var.network_ip
    }
  }


  provisioner "remote-exec" {
    inline = [
      "sudo useradd -s /bin/bash -m -p $(perl -e 'print crypt($ARGV[0], \"password\")' ${var.vm_password}) ${var.vm_username}",
      "sudo mkdir -p /home/${var.vm_username}/.ssh",
      "sudo touch /home/${var.vm_username}/.ssh/authorized_keys",
      "sudo echo $(cat /tmp/${local.ssh_key_file_public}) > authorized_keys", 
      "sudo mv authorized_keys /home/${var.vm_username}/.ssh", 
      "sudo echo $(cat /tmp/${local.ssh_key_file_public}) > id_ed25519.pub",
      "sudo mv id_ed25519.pub /home/${var.vm_username}/.ssh",
      "sudo echo $(cat /tmp/${local.ssh_key_file_private}) > id_ed25519",
      "sudo mv id_ed25519 /home/${var.vm_username}/.ssh",
      "sudo chown -R ${var.vm_username}:${var.vm_username} /home/${var.vm_username}/.ssh",
      "sudo chmod 700 /home/${var.vm_username}/.ssh",
      "sudo chmod 600 /home/${var.vm_username}/.ssh/authorized_keys",
      "sudo chmod 644 /home/${var.vm_username}/.ssh/id_ed25519.pub",
      "sudo chmod 600 /home/${var.vm_username}/.ssh/id_ed25519",
      "sudo usermod -aG sudo ${var.vm_username}",
      "sudo groupadd docker",
      "sudo usermod -aG docker ${var.vm_username}",
      "sudo usermod -aG adm ${var.vm_username}",
      "echo '${var.vm_username} ALL=(ALL) NOPASSWD:ALL' | sudo tee -a /etc/sudoers.d/${var.vm_username}",
    ]
  
    connection {
      type     = "ssh"
      user     = "ubuntu"
      password = "ubuntu"
      host     = var.network_ip
    }
  }

  # Create directories for deployment scripts
  provisioner "remote-exec" {
    inline = [
      "mkdir -p  ~${var.vm_username}/scripts/",
    ]

    connection {
      type        = "ssh"
      user        = var.vm_username
      private_key = file("./${local.ssh_key_file_private}")
      host        = var.network_ip
    }
  }

  # Copy  Scripts
  provisioner "file" {
    source      = "${local.script_directory}/"
    destination = "scripts/"

    connection {
      type        = "ssh"
      user        = var.vm_username
      private_key = file("./${local.ssh_key_file_private}")
      host        = var.network_ip
    }
  }

  # Run install nginx script
  provisioner "remote-exec" {
    inline = [
      "cd scripts",
      "bash ./02_install_nginx.sh"
    ]

    connection {
      type        = "ssh"
      user        = var.vm_username
      private_key = file("./${local.ssh_key_file_private}")
      host        = var.network_ip
    }
  }

  # Run install docker script
  provisioner "remote-exec" {
    inline = [
      "cd scripts",
      "bash ./03_install_docker.sh"
    ]

    connection {
      type        = "ssh"
      user        = var.vm_username
      private_key = file("./${local.ssh_key_file_private}")
      host        = var.network_ip
    }
  }
   # Install Docker through Ansible

  provisioner "local-exec" {
      command = "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u ${var.vm_username} -i ${var.network_ip},  ${local.script_directory}/04_docker_playbook.yaml --private-key=${local.ssh_key_file_private}"
  
    }





}