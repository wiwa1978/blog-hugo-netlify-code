
resource "digitalocean_project" "terraform_project" {
  name        = var.project_name
  resources   = var.resources
}
