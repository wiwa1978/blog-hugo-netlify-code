provider "digitalocean"{
  token = var.do_token
}

resource "digitalocean_droplet" "myserver" {
   count = var.number_servers
   name = "server-${count.index}"
   image = "ubuntu-18-04-x64"
   size = "1gb"
   region = var.region
   ssh_keys = [
        var.ssh_fingerprint
   ]
   tags   = ["${digitalocean_tag.webserver.id}"]  
}

resource "digitalocean_tag" "webserver" {
    name = "webserver"
}