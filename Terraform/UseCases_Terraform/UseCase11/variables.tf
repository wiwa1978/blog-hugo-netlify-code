variable "do_token" {
  type = string
}
variable "domain_name" {
  type = string
}
variable "ssh_key" {
  type = string
}

variable "projects" {
  type = map(object({
    description = string,
    purpose     = string,
    environment = string,
    servers = map(object({
      name  = string
      size   = string,
      image  = string,
      region = string
      tags   = list(string)
    }))
  }))
}
