variable "ec2_region" {
  default = "eu-west-1"
}

variable "ec2_image" {
  default = "ami-00035f41c82244dab"
}

variable "ec2_instance_type" {
  default = "t2.medium"
}

variable "ec2_keypair" {
  default = "AWS-Cisco"
}

variable "ec2_tags" {
  default = "Kubernetes"
}

variable "ec2_count" {
  default = "3"
}

