provider "aws" {
  region = "us-east-1"
}

data "aws_ami" "latest_amazon_linux" {
  owners      = ["amazon"]
  most_recent = true
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}
resource "aws_ecr_repository" "webapp-ecr" {
  name = "webapp-ecr"
}

resource "aws_ecr_repository" "database-ecr" {
  name = "database-ecr"
}

resource "aws_instance" "webapp_instance" {
  ami                  = data.aws_ami.latest_amazon_linux.id
  instance_type        = "t2.micro"
  subnet_id            = aws_subnet.public_subnet.id
  iam_instance_profile = "LabInstanceProfile"
  security_groups      = [aws_security_group.sg_hafees.id]
  key_name             = aws_key_pair.my_key.key_name

  tags = {
    Name = "webapp-server"
  }
}

resource "aws_key_pair" "my_key" {
  key_name   = "assignmentkey"
  public_key = file("assignmentkey.pub")
}

