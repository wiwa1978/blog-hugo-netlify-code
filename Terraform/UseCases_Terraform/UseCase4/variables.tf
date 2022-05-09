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
    type = map(object({
        size = string,
        image = string,
        region = string
        tags = list(string)
    }))
}
