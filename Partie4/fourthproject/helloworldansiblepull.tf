# Configuration du fournisseur pour AWS
provider "aws" {
  region     = "us-east-1"
}

# Configuration des ressources pour AWS
resource "aws_instance" "myserver" {
  ami = "ami-cfe4b2b0"
  instance_type = "t2.micro"
  key_name = "EffectiveDevOpsAWS"
  vpc_security_group_ids = ["sg-01864b4c"]

  tags {
    Name = "helloworld"
  }

# Approvisionnement pour l'application du playbook Ansible en mode Pull
  provisioner "remote-exec" {
    connection {
      user = "ec2-user"
      private_key = "${file("/root/.ssh/EffectiveDevOpsAWS.pem")}"
    }
    inline = [
      "sudo yum install --enablerepo=epel -y ansible git",
      "sudo ansible-pull -U https://github.com/yogeshraheja/ansible helloworld.yml -i localhost",
    ]
  }
  
}

# Adresse IP de l'instance EC2 nouvellement créée
output "myserver" {
 value = "${aws_instance.myserver.public_ip}"
}
