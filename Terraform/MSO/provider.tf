terraform {
  required_providers {
    mso = {
      source  = "ciscodevnet/mso"
      version = "0.1.5"
    }
  }
}

provider "mso" {
  username = var.username
  password = var.password
  url      = var.url
  insecure = true
}
