variable "aci_tenant_1_name" {
  type = string
}

variable "aci_tenant_2_name" {
  type = string

  validation {
    condition     = length(var.aci_tenant_2_name) > 5 && substr(var.aci_tenant_2_name, 0, 6) == "Tenant"
    error_message = "The tenant name must be larger than 5 characters and starting with \"Tenant\"."
  }
}

variable "application_profile_1_name" {
  type = string
}

variable "application_profile_2_name" {
  type = string
}

variable "vrf_1_name" {
  type = string
}

variable "vrf_2_name" {
  type = string
}

variable "bd_1_name" {
  type = string
}

variable "bd_2_name" {
  type = string
}