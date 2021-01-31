
variable "aci_tn" {
  default = "EC_Demo_Terraform"
}

variable "aci_bd" {
  default = "EC_Demo_Terraform_BD"
}

variable "aci_subnet" {
  default = "10.0.0.254/24"
}

variable "aci_subnet_type" {
  default = "public"
}

variable "aci_ap" {
  default = "Production"
}

variable "aci_filter_entry" {
  default = "HTTP"
}

variable "aci_filter" {
  default = "HTTP"
}

variable "contract_subject" {
  default = "HTTP"
}

variable "aci_filter_port_from" {
  default = "80"
}

variable "aci_filter_port_to" {
  default = "80"
}


variable "aci_contract" {
  default = "HTTP"
}

variable "aci_epgs" {
  default = ["Frontend", "Middleware", "Databases"]
}