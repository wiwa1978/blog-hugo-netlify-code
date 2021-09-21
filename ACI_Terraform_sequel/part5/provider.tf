terraform {
  required_providers {
    aci = {
      source  = "CiscoDevNet/aci"
    }
  }
}

provider "aci" {
  username = "apic:amslab\\\\wauterw"
  password = "C!sco12345"
  url      = "https://10.61.124.32"
  insecure = true
}
