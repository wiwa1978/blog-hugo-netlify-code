resource "aws_instance" "OneServer" {
  ami           = var.ec2_image
  instance_type = var.ec2_instance_type
  key_name      = var.ec2_keypair
  count         = var.ec2_count
  tags = {
    Name = var.ec2_tags
  }
}

output "instance_ip_addr" {
  value       = aws_instance.OneServer.*.private_ip
  description = "The private IP address of the main server instance."
}

output "instance_ips" {
  value = aws_instance.OneServer.*.public_ip
}