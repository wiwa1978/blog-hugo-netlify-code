variable "tenants" { 
  type = map(object({
    tenant_name          =  string
    tenant_description   =  string
  }))
}

variable "vrfs" {
  type = map(map(object({
    vrf_name          =  string
  })))
}

variable "aps" {
  type = map(map(object({
    ap_name          =  string
  })))
}

variable "bds" {
  type = map(object({
    bd_name         = string
    vrf             = string
    tenant          = string
  }))
}
