variable "docker_repo" {
  type      = string
  default   = "wiwa1978/hashicorp-tools"
  sensitive = true
}

variable "docker_username" {
  type      = string
  default   = "wiwa1978"
  sensitive = true
}

variable "docker_password" {
  type      = string
  default   = "***"
  sensitive = true
}
