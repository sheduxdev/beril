terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

resource "aws_s3_bucket" "reports" {
  bucket = "beril-lab-reports"
  acl    = "public-read"
}

resource "aws_security_group" "web" {
  name = "beril-lab-web"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_instance" "main" {
  engine               = "postgres"
  instance_class       = "db.t3.micro"
  username             = "beril"
  password             = "beril-lab-password"
  publicly_accessible  = true
  skip_final_snapshot  = true
}

resource "aws_iam_policy" "deploy" {
  name = "beril-lab-deploy"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "*"
      Resource = "*"
    }]
  })
}
