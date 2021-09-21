terraform {
  required_providers {
    aci = {
      source  = "CiscoDevNet/aci"
    }
  }
}

provider "aci" {
  username = "apic:amslab\\\\wauterw"
  password = "***"
  url      = "***"
  insecure = true
}
