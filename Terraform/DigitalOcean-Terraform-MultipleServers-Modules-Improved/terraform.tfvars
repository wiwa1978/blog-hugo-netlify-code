do_token        =       "dop_v1_***"
domain_name     =       "wimwauters.com"
ssh_key         =       "key_digitalocean_2020"
project_name    =       "Project Terraform"
servers = {
    server1 = {
        name  = "server1",
        image = "ubuntu-21-10-x64"
        region = "ams3",
        environment = "development"
    },
    server2 = {
        name  = "server2",
        image = "ubuntu-20-04-x64"
        region = "lon1",
        environment = "staging"
    } 
}