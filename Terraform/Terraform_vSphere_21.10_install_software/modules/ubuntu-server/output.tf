output "vm_name" {
  description = "Server VM Name"
  value       = vsphere_virtual_machine.vm.*.name
}

output "ip_address" {
  description = "Server IP Address"
  value       = var.network_ip
}