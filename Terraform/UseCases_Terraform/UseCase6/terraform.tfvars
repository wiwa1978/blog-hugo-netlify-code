do_token    = "dop_v1_***"
domain_name = "wimwauters.com"
ssh_key     = "key_digitalocean_2020"
servers = {
  server1 = {
    size        = "s-2vcpu-2gb"
    image       = "ubuntu-21-10-x64"
    region      = "ams3",
    environment = "development"
    tags        = ["web", "development"]
  },
  server2 = {
    size        = "s-2vcpu-2gb"
    image       = "ubuntu-20-04-x64"
    region      = "lon1",
    environment = "staging"
    tags        = ["web", "staging"]
  }

}
projects = ["Project Development", "Project Staging"]
