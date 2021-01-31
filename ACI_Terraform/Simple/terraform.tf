terraform {
  backend "s3" {
    bucket = "be.wymedia.terraform"
    key    = "terraform/state"
    region = "eu-west-1"
  }
}