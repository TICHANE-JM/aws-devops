# Infrastructure en tant que code avec Terraform

Dans la [Partie 3](https://github.com/TICHANE-JM/aws-devops/blob/main/Traiter_votre_infra_comme_du_code.md), __Traiter votre infrastructure comme du code__ , nous nous sommes familiarisés avec AWS CloudFormation et Ansible. Nous avons créé un modèle CloudFormation pour créer un environnement EC2 et y avons déployé une application Web HelloWorld. Faisant un pas de plus dans le monde de l'automatisation, nous avons ensuite introduit l'outil de gestion de configuration **Ansible**. Nous avons appris comment Ansible s'occupe du déploiement et de l'orchestration des applications afin que les modèles CloudFormation restent propres et confinés jusqu'au provisionnement. Cette approche est bien acceptée par les géants de la technologie en ce qui concerne le cloud AWS, mais lorsque nous parlons d'environnements hétérogènes où nous avons plusieurs plates-formes cloud telles qu'AWS, Azure, Google cloud, OpenStack et VMware, le service CloudFormation, car il est un service natif AWS, n'est pas applicable.

Par conséquent, nous avons besoin d'une solution alternative qui nous aidera non seulement à fournir des services de calcul, mais également d'autres services cloud natifs sans trop d'effort. Évidemment, cela est possible en utilisant des scripts complexes et ingérables de manière impérative, mais on finirait par rendre les environnements encore plus complexes. Nous avons besoin d'une solution qui gardera l'environnement hétérogène simple et gérable, avec une approche déclarative qui suit les directives recommandées concernant l'utilisation de l'**infrastructure en tant que code (IaC)**. Cette solution est **Terraform**, un outil pour créer, modifier et versionner l'infrastructure de manière sûre et efficace.

Dans cette partie, nous aborderons les sujets suivants :
* Qu'est-ce que Terraform ?
* Créer un référentiel Terraform
* Intégration d'AWS, Terraform et Ansible

## Les pré-requis techniques
Les exigences techniques sont les suivantes :
* AWS Console
* Git
* GitHub
* Terraform
* Ansible

Les sites Web suivants fournissent de plus amples informations sur Terraform :
* Terraform official website for product information: https://terraform.io
* Terraform pris en charge fournit des détails : https://www.terraform.io/docs/providers/
* Détails du langage de configuration HashiCorp : https://github.com/hashicorp/hcl
* Lien GitHub pour le modèle Terraform pour le premier projet : https://raw.githubusercontent.com/TICHANE-JM/aws-devops/master/firstproject/ec2.tf
* Lien GitHub pour le modèle Terraform pour le deuxième projet : https://raw.githubusercontent.com/TICHANE-JM/aws-devops/master/secondproject/helloworldec2.tf
* Lien Github pour le modèle Terraform pour le troisième projet : https://raw.githubusercontent.com/TICHANE-JM/aws-devops/master/thirdproject/helloworldansible.tf
* Lien Github pour le modèle Terraform pour le quatrième projet : https://raw.githubusercontent.com/TICHANE-JM/aws-devops/master/fourthproject/helloworldansiblepull.tf





