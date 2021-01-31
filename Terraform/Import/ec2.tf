provider "aws" {
  access_key = "***"
  secret_key = "***"
  region     = "eu-west-3"
}

resource "aws_instance" "import_ec2" {
  ami           = var.aws_ami
  instance_type = var.instance_type
  key_name      = var.key_name
  tags = {
    name    =   "imported-instance"
  }
}
