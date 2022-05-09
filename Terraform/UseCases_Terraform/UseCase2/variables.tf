variable "do_token" {
     type = string
}
variable "domain_name" {     
    type = string
}
variable "ssh_key" {     
    type = string
}

variable "servers" {
    type = list(object({
        name  = string,
        size = string,
        image = string,
        region = string
        tags = list(string)
    }))
}
