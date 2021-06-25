terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.37.0"
    }
  }
}

provider "aws" {
   region = "eu-west-1"
}

module "webserver" {
    source = "./modules/ec2"

    servername = "Testserver-Terraform"
    instance_type = "t3.micro"
}

