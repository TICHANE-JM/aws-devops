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
* Lien GitHub pour le modèle Terraform pour le premier projet : https://raw.githubusercontent.com/TICHANE-JM/aws-devops/Partie4/master/firstproject/ec2.tf
* Lien GitHub pour le modèle Terraform pour le deuxième projet : https://raw.githubusercontent.com/TICHANE-JM/aws-devops/Partie4/master/secondproject/helloworldec2.tf
* Lien Github pour le modèle Terraform pour le troisième projet : https://raw.githubusercontent.com/TICHANE-JM/aws-devops/Partie4/master/thirdproject/helloworldansible.tf
* Lien Github pour le modèle Terraform pour le quatrième projet : https://raw.githubusercontent.com/TICHANE-JM/aws-devops/Partie4/master/fourthproject/helloworldansiblepull.tf

## Qu'est-ce que Terraform ?

Terraform est un logiciel IaC open source lancé en juillet 2014 par une société nommée HashiCorp. C'est la même société qui a produit des outils tels que Vagrant, Packer et Vault. Terraform a été publié sous la licence publique Mozilla (MPL) version 2.0. Le code source de Terraform est disponible sur GitHub à l'adresse https://github.com/hashicorp/terraform. Tout le monde peut utiliser ce code source et contribuer au développement de Terraform.

Terraform permet aux utilisateurs de définir une infrastructure de centre de données dans un langage de configuration de haut niveau appelé HashiCorp Configuration Language (HCL). HashiCorp fournit également la version Enterprise de Terraform, qui est fournie avec une prise en charge supplémentaire. De nombreuses fonctionnalités sont disponibles avec Terraform, ce qui en fait un outil d'orchestration d'infrastructure de haut niveau parfait. Il a les caractéristiques suivantes :

* Il a des étapes d'installation très simples et minimales.
* Il a une approche déclarative pour écrire des modèles Terraform.
* Il est disponible en tant qu'offre open source et entreprise.
* Il a une idempotence, ce qui signifie que les modèles Terraform fournissent le même résultat chaque fois que vous les appliquez dans votre environnement.
* Il correspond parfaitement à presque toutes les principales plates-formes cloud disponibles telles que AWS, Azure, GCP, OpenStack, DigitalOcean, etc. Reportez-vous à https://www.terraform.io/docs/providers/ pour plus de détails.

### Cependant, Terraform n'est pas :

* Un outil de gestion de configuration comme Puppet, Chef, Ansible ou SaltStack. Vous pouvez installer des programmes ou des logiciels légers pour expédier certains fichiers de configuration importants dans vos instances, mais lorsqu'il s'agit de déployer et d'orchestration d'applications plus complexes, vous devez utiliser des outils de configuration comme ceux répertoriés dans la section précédente.
* Un outil de bas niveau comme Boto pour AWS.

## Premiers pas avec Terraform

Ici, nous nous concentrerons sur Terraform open-source. Nous allons démontrer la configuration complète de Terraform sur la machine CentOS 7.x que nous avons utilisée dans les chapitres précédents. HashiCorp ne fournit pas de packages natifs pour les systèmes d'exploitation, donc Terraform est distribué sous la forme d'un binaire unique, emballé dans une archive ZIP.

Configurons Terraform sur notre serveur CentOS. Suivez ces étapes:
1. Il faut télécharger les binaires Terraform depuis le site officiel : https://www.terraform.io/downloads.html. Dans notre cas, nous utiliserons Linux 64 bits :
```
# curl -O https://releases.hashicorp.com/terraform/0.11.8/terraform_0.11.8_linux_amd64.zip

# ls -lrt terraform_0.11.8_linux_amd64.zip
-rw-r--r--.   1    root    root   17871447  Jun   30   16:40    terraform_0.11.8_linux_amd64.zip
```

2. Décompressez le fichier `.zip` Terraform extrait. Vous devez installer le package de décompression s'il n'est pas déjà présent :

```
$ yum -y install unzip
$ echo $PATH
$ unzip terraform_0.11.8_linux_amd64.zip -d /usr/bin/
```
Cela extraira le binaire Terraform dans `/usr/bin`, qui est disponible dans la variable d'environnement PATH pour vos systèmes Linux.
3. Enfin, vérifiez la version installée de Terraform. La dernière version du logiciel Terraform disponible au moment de la rédaction est la suivante :
```
$ terraform -v
Terraform v0.11.8
```
Comme vous pouvez le constater, la configuration de Terraform ne prend que quelques minutes et ses fichiers binaires sont très légers. Nous sommes maintenant prêts à utiliser l'environnement Terraform pour le provisionnement des services AWS.

## Terraform et AWS pour le provisionnement automatisé
Comme mentionné précédemment, Terraform prend en charge plusieurs fournisseurs tels qu'AWS, Azure et GCP pour l'orchestration d'infrastructure de haut niveau. Dans cette étude, nous n'utiliserons que la plateforme AWS. Comme nous l'avons vu dans la partie précédente, __Déploiement de votre première application Web__, nous pouvons déployer des services de calcul ou n'importe quel service AWS en utilisant deux modes :
* Console de gestion AWS
* **Interface de ligne de commande** AWS (CLI)

## Déploiement à l'aide d'AWS Management Console
Ici, nous nous concentrerons sur le déploiement du service de calcul AWS comme nous l'avons fait précédemment. Le déploiement d'instances AWS à l'aide d'AWS Management Console est assez simple. Suivez les étapes ci-dessous :

1. Connectez-vous à votre AWS Management Console à l'adresse https://console.aws.amazon.com ou utilisez votre compte d'utilisateur IAM pour vous connecter. Nous avons créé un compte utilisateur IAM Dans la partie 2, __Déploiement de votre première application Web__ à l'adresse `https://AWS-account-ID-oralias.signin.aws.amazon.com/console`.
2. Sélectionnez l'onglet Services, puis EC2 dans la section Calcul, puis cliquez sur le bouton Lancer l'instance.
3. Sur l'écran suivant, recherchez et sélectionnez **Amazon Machine Image (AMI)**. Ici, nous utilisons `ami-cfe4b2b0`, qui est Amazon Linux AMI.
4. Sélectionnez le type `t2.micro` à l'étape Choisir un type d'instance et cliquez sur le bouton Suivant : Configurer les détails de l'instance.
5. Acceptez les paramètres par défaut et cliquez sur le bouton Suivant : Ajouter un stockage.
6. Encore une fois, acceptez le paramètre par défaut pour le stockage et cliquez sur le bouton Suivant : Ajouter des balises suivi du bouton Suivant : Configurer le groupe de sécurité.
7. Ici, sélectionnez le groupe de sécurité que vous avez créé dans la partie 2, __Déploiement de votre première application Web__, qui dans mon cas est `sg-01864b4c`, comme illustré dans la capture d'écran suivante :

![image](https://user-images.githubusercontent.com/107214400/176898693-e6ad74d7-ef93-4437-8c3e-474d7a4b3b76.png)

8. Maintenant, cliquez sur le bouton Réviser et lancer. Ignorez les avertissements qui s'affichent et appuyez sur le bouton Lancer.
9. Sélectionnez la paire de clés, qui dans mon cas est `aws-devops`. Cliquez sur le bouton Lancer des instances.

En quelques minutes, votre instance AWS sera opérationnelle. Une fois le serveur démarré, connectez-vous au serveur à partir de votre instance locale, qui est CentOS dans mon cas. Suivez le processus suivant pour déployer l'application Hello World manuellement et vérifiez-la localement ou depuis le navigateur :
```
$ ssh -i ~/.ssh/aws-devops.pem ec2-user@34.201.116.2 (remplacez cette IP par votre IP publique AWS)

$ sudo yum install --enablerepo=epel -y nodejs
$ sudo wget https://raw.githubusercontent.com/TICHANE-JM/aws-devops/master/Partie2/helloworld.js -O /home/ec2-utilisateur/helloworld.js
$ sudo wget https://raw.githubusercontent.com/TICHANE-JM/aws-devops/master/Partie2/helloworld.conf -O /etc/init/helloworld.conf
$ sudo start helloworld

$ curl http://34.201.116.2:3000/
Hello World
```
> N'oubliez pas de résilier l'instance à partir d'AWS Management Console une fois que vous avez terminé le test.

Le processus de résiliation est également très simple. Sélectionnez l'instance créée, cliquez sur le menu déroulant Actions, suivi de l'option État de l'instance, puis cliquez sur Terminer.

```
$ aws ec2 run-instances --instance-type t2.micro 
    --key-name aws-devops 
    --security-group-ids sg-01864b4c 
    --image-id ami-cfe4b2b0
$ aws ec2 describeinstances --instance-ids i-0eb05adae2bb760c6 
    --query "Reservations[*].Instances[*].PublicDnsName"
$ ssh -i ~/.ssh/aws-devops.pem ec2-user@ec2-18-234-227-160.compute-1.amazonaws.com
$ sudo yum install --enablerepo=epel -y nodejs
$ sudo wget https://raw.githubusercontent.com/TICHANE-JM/aws-devops/master/Partie2/helloworld.js -O /home/ec2-user/helloworld.js
$ sudo wget https://raw.githubusercontent.com/TICHANE-JM/aws-devops/master/Partie2/helloworld.conf -O /etc/init/helloworld.conf
$ sudo start helloworld
$ curl http://ec2-18-234-227-160.compute-1.amazonaws.com:3000
Hello World
```
N'oubliez pas de résilier l'instance à l'aide de `aws ec2 terminate-instances --instance-ids <AWS INSTANCE ID>` une fois que vous avez terminé les tests.

## Création de notre référentiel Terraform

Nous avons maintenant examiné deux modes de création d'instances AWS EC2 : à l'aide d'AWS Management Console et à l'aide de l'AWS CLI. Celles-ci peuvent être automatisées à l'aide du service cloud natif d'AWS appelé modèle CloudFormation, comme nous l'avons vu dans la [Partie 3](https://github.com/TICHANE-JM/aws-devops/blob/main/Traiter_votre_infra_comme_du_code.md), __Traiter votre infrastructure comme du code__. Cela ne s'applique qu'à une utilisation avec le cloud AWS. Dans ce chapitre, nous obtiendrons les mêmes résultats de provisionnement d'instances AWS à l'aide de Terraform. Reportez-vous à https://www.terraform.io/intro/vs/cloudformation.html pour comprendre les différences entre Terraform et CloudFormation.

Créons un référentiel dédié dans notre compte GitHub et commençons notre voyage avec Terraform. Une fois connecté à GitHub, créez un nouveau référentiel pour les modèles Terraform en suivant les étapes ci-dessous :

1. Dans votre navigateur, ouvrez https://github.com/new.
2. Appelez le nouveau référentiel `aws-devops`

![image](https://user-images.githubusercontent.com/107214400/176903193-aa198b22-eddf-4d60-8ec6-8ef890bdec46.png)

3. Cochez la case Initialiser ce référentiel avec un fichier README.
4. Enfin, cliquez sur le bouton Créer un référentiel.
5. Une fois votre référentiel créé, vous souhaiterez le cloner sur votre système. Pour ce faire, vous devez avoir installé Git. Si vous n'avez pas encore Git, recherchez sur Google des instructions sur la façon de l'installer pour votre système d'exploitation. Pour CentOS, il vous suffit d'exécuter `yum -y install git` car le package Git fait désormais partie de la distribution Linux :

```
$ git clone https://github.com/<your_github_username>/DevopsTeraformAWS
```
Maintenant que le référentiel est cloné, il est temps de commencer à développer des modèles Terraform. Allez dans le référentiel `DevopsTeraformAWS` et créez un répertoire nommé `firstproject` :
```
$ cd EffectiveDevOpsTerraform
$ mkdir firstproject
$ cd firstproject
```

## Premier modèle Terraform pour le provisionnement d'instance AWS
Terraform est utilisé pour créer, gérer et mettre à jour des ressources d'infrastructure telles que des machines virtuelles, des instances cloud, des machines physiques, des conteneurs et bien plus encore. Presque tous les types d'infrastructure peuvent être représentés en tant que ressource dans Terraform. Nous allons créer une ressource à l'étape suivante. Avant cela, nous devons comprendre les __fournisseurs Terraform__, qui sont chargés de comprendre les interactions API et d'exposer les ressources. Un fournisseur peut être IaaS (comme AWS, GCP, etc.), PaaS (comme Heroku) ou SaaS (comme DNSimple). Le fournisseur est la première section avec laquelle nous devons démarrer nos modèles Terraform. Avant d'utiliser Terraform pour créer une instance, nous devons configurer le fournisseur AWS. C'est le premier morceau de code que nous allons écrire dans notre modèle.

Les modèles sont écrits dans un langage spécial appelé HCL. Plus de détails sur HCL peuvent être trouvés sur https://github.com/hashicorp/hcl. Vous pouvez également écrire vos modèles en JSON, mais nous utiliserons HCL ici. Les fichiers de modèle Terraform doivent avoir l'extension .tf, qui signifie fichier Terraform. Créons notre premier modèle, `ec2.tf` :
```
provider "aws" {
access_key = "<YOUR AWS ACCESS KEY>"
secret_key = "<YOUR AWS SECRET KEY>"
region = "us-east-1"
}
```
Visitez https://www.terraform.io/docs/providers/aws/index.html pour explorer plus d'options sur le fournisseur AWS.

Ce type de déclaration pour les fournisseurs dans Terraform est appelé configuration de fournisseurs à l'aide d'informations d'identification statiques. Ce n'est pas un moyen sûr de déclarer les fournisseurs ; il existe d'autres options dans Terraform, telles que les variables d'environnement, les fichiers de variables Terraform, les fichiers d'informations d'identification natifs AWS (`~/.aws/credentials`), etc., pour stocker les fournisseurs avec des informations sensibles.

> Ne poussez pas votre clé d'accès AWS ou votre clé secrète sur GitHub ou tout autre site Web public. Cela permettra aux pirates de pirater votre compte AWS.

Avant de continuer, nous devons installer le plug-in ou réinitialiser les plug-ins liés à AWS pour Terraform. Nous n'avons pas besoin de faire grand-chose ici; le fichier configuré avec les plugins du `provider` effectuera cette tâche pour nous.

Exécutez la commande suivante :
```
# terraform init

**Initializing provider plugins...**
- checking for available provider plugins on https://releases.hashicorp.com...
- Downloading plugin for provider "aws" (1.36.0) ...

The following providers do not have any version constrints in configuration, so the latest version was installed.

To prevent automatic upgrades to new major versions that may contain breaking changes, it is recommended to add version = "..." constraints to the corresponding provider blocks in configuration, with the constraint strings suggested below.

* provider.aws: version ="~> 1.36"

**Terraform has been successfully initialized!**

You may now begin working with Terraform. Try running "terraform plan" to see any changes that are required for your infrastructure. All terraform commands should not work.

Il you ever set or change modules or backend configuration for Terraform, rerun this command to reinitialize your working directory. If you forger, other commands will detect it and remind you to do so if necessary.
```
La prochaine étape consiste à configurer notre infrastructure. C'est là que nous commençons à développer le fichier `ec2.tf` avec les ressources Terraform. Les ressources sont des composants de votre infrastructure. Ils peuvent être aussi complexes qu'un serveur virtuel complet doté de plusieurs autres services, ou aussi simples qu'un enregistrement DNS. Chaque ressource appartient à un fournisseur et le type de la ressource est suffixé par le nom du fournisseur. La configuration d'une ressource, appelée bloc de `resource`, prend la forme suivante :

```
resource "provider-name_resource-type" "resource-name" {
parameter_name = “parameter_value”
parameter_name = “parameter_value”
.
.
}
```
Dans notre cas, nous devons créer une instance EC2. La ressource `aws_instance` dans Terraform est responsable de cette tâche. Pour créer une instance, nous devons définir au moins deux paramètres : `ami` et `instance_type`. Ces deux paramètres sont obligatoires, alors que les autres sont facultatifs. Pour obtenir une liste et une description de tous les paramètres de ressource aws_instance, consultez le site Web suivant : https://www.terraform.io/docs/providers/aws/r/instance.html.

Dans notre cas, nous allons créer une instance avec les mêmes détails avec lesquels nous avons créé et testé l'instance à l'aide d'AWS Management Console et de l'utilitaire AWS CLI. Nous avons `ami-cfe4b2b0` comme AMI et `t2.micro` comme type d'instance. àws-devops` est le nom de clé que nous avons créé dans le passé et `sg-01864b4c` est notre groupe de sécurité. Nous étiquetons également l'instance avec le nom `helloworld` pour une reconnaissance facile. Il convient de mentionner que, comme tout autre langage de script ou d'automatisation, vous pouvez ajouter des commentaires dans le modèle Terraform avec le signe #. Notre dossier complet devrait maintenant ressembler à ceci :
```
# Provider Configuration for AWS
provider "aws" {
access_key = “<YOUR AWS ACCESS KEY>"
secret_key = "<YOUR AWS SECRET KEY>"
region = "us-east-1"
}
# Resource Configuration for AWS
resource "aws_instance" "myserver" {
ami = "ami-cfe4b2b0"
instance_type = "t2.micro"
key_name = "EffectiveDevOpsAWS"
vpc_security_group_ids = ["sg-01864b4c"]
tags {
Name = "helloworld"
}
}
```
Le fichier créé devrait ressembler au fichier sur le site Web suivant : https://github.com/TICHANE-JM/DevopsTeraformAWS/tree/main/firstproject .

Commençons par valider le modèle Terraform pour nous assurer qu'il ne contient aucune erreur de syntaxe. Terraform dispose d'un utilitaire de `terraform validate` dédié, qui vérifie la syntaxe du modèle Terraform et nous fournit les résultats s'il y a des erreurs de syntaxe qui nécessitent notre attention :
```
$ terraform validate
```
Comme il n'y a pas de sortie, cela signifie que notre modèle Terraform est exempt d'erreurs de syntaxe. Il est temps d'effectuer un essai pour voir ce que ce modèle va exécuter. Il s'agit juste d'un test de fumée pour savoir quelles modifications ou implémentations seront effectuées par le modèle que nous avons créé. Cette étape dans Terraform est connue sous le nom de **plan** :
```
[root@tichanejm firstproject]# terraform plan Refreshing Terraform state in-memory prior to plan...
The refreshed state will be used to calculate this plan, but will not be persisted to local or remote state storage.

------------------------------------------------------------------------

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
    + create

Terraform will perform the following actions:

    + aws_instance.myserver
    id: <computed>
    ami: "ami-cfe4b2b0"
    arn: <computed>
    associate_public_ip_address: <computed>
    availability_zone: <computed>
    cpu_core_count: <computed>
    cpu_threads_per_core: <computed>
    ebs_block_device.#: <computed>
    ephemeral_block_device.#: <computed>
    get_password_data: "false"
    instance_state: <computed>
    instance_type: "t2.micro"
    ipv6_address_count: <computed>
    ipv6_addresses.#: <computed>
    key_name: "EffectiveDevOpsAWS"
    network_interface.#: <computed>
    network_interface_id: <computed>
    password_data: <computed>
    placement_group: <computed>
    primary_network_interface_id: <computed>
    private_dns: <computed>
    private_ip: <computed>
    public_dns: <computed>
    public_ip: <computed>
    root_block_device.#: <computed>
    security_groups.#: <computed>
    source_dest_check: "true"
    subnet_id: <computed>
    tags.%: "1"
    tags.Name: "helloworld"
    tenancy: <computed>
    volume_tags.%: <computed>
    vpc_security_group_ids.#: "1"
    vpc_security_group_ids.1524136243: "sg-01864b4c"
    
Plan: 1 to add, 0 to change, 0 to destroy.

------------------------------------------------------------------------
```
Ici, nous n'avons pas spécifié de paramètre `-out` pour enregistrer ce plan, donc Terraform ne peut pas garantir que ces actions seront exactement exécutées si `terraform apply` est exécuté par la suite :
```
[root@tichanejm firstproject]#
```
Notre étape de planification indique les mêmes paramètres que nous voulons dans l'exécution réelle lors de la création de notre instance. Encore une fois, ne vous confondez pas avec les paramètres `<computed>`, cela signifie simplement que leur valeur sera attribuée lors de la création des ressources.

Exécutons maintenant notre plan pour de vrai et voyons comment un modèle Terraform peut être utilisé pour créer une instance AWS avec les paramètres de ressource définis. Terraform le fait à l'aide de l'utilitaire `terraform apply` et vous pouvez considérer cette étape comme une **application**. Une fois que vous avez exécuté `terraform apply`, il vous demandera votre approbation par défaut pour confirmation. Tapez `yes` pour lancer la création de la ressource.

Si vous souhaitez ignorer cette approbation interactive du plan avant de l'appliquer, utilisez l'option `--auto-approve` avec la commande `terraform apply` :
```
[root@tichanejm firstproject]# terraform apply

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
    + create
    
Terraform will perform the following actions:

  + aws_instance.myserver
    id: <computed>
    ami: "ami-cfe4b2b0"
    arn: <computed>
    associate_public_ip_address: <computed>
    availability_zone: <computed>
    cpu_core_count: <computed>
    cpu_threads_per_core: <computed>
    ebs_block_device.#: <computed>
    ephemeral_block_device.#: <computed>
    get_password_data: "false"
    instance_state: <computed>
    instance_type: "t2.micro"
    ipv6_address_count: <computed>
    ipv6_addresses.#: <computed>
    key_name: "aws-devops"
    network_interface.#: <computed>
    network_interface_id: <computed>
    password_data: <computed>
    placement_group: <computed>
    primary_network_interface_id: <computed>
    private_dns: <computed>
    private_ip: <computed>
    public_dns: <computed>
    public_ip: <computed>
    root_block_device.#: <computed>
    security_groups.#: <computed>
    source_dest_check: "true"
    subnet_id: <computed>
    tags.%: "1"
    tags.Name: "helloworld"
    tenancy: <computed>
    volume_tags.%: <computed>
    vpc_security_group_ids.#: "1"
    vpc_security_group_ids.1524136243: "sg-01864b4c"

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.
  
  Enter a value: yes
  
  aws_instance.myserver: Creating...
    ami: "" => "ami-cfe4b2b0"
    arn: "" => "<computed>"
    associate_public_ip_address: "" => "<computed>"
    availability_zone: "" => "<computed>"
    cpu_core_count: "" => "<computed>"
    cpu_threads_per_core: "" => "<computed>"
    ebs_block_device.#: "" => "<computed>"
    ephemeral_block_device.#: "" => "<computed>"
    get_password_data: "" => "false"
    instance_state: "" => "<computed>"
    instance_type: "" => "t2.micro"
    ipv6_address_count: "" => "<computed>"
    ipv6_addresses.#: "" => "<computed>"
    key_name: "" => "aws-devops"
    network_interface.#: "" => "<computed>"
    network_interface_id: "" => "<computed>"
    password_data: "" => "<computed>"
    placement_group: "" => "<computed>"
    primary_network_interface_id: "" => "<computed>"
    private_dns: "" => "<computed>"
    private_ip: "" => "<computed>"
    public_dns: "" => "<computed>"
    public_ip: "" => "<computed>"
    root_block_device.#: "" => "<computed>"
    security_groups.#: "" => "<computed>"
    source_dest_check: "" => "true"
    subnet_id: "" => "<computed>"
    tags.%: "" => "1"
    tags.Name: "" => "helloworld"
    tenancy: "" => "<computed>"
    volume_tags.%: "" => "<computed>"
    vpc_security_group_ids.#: "" => "1"
    vpc_security_group_ids.1524136243: "" => "sg-01864b4c"
aws_instance.myserver: Still creating... (10s elapsed)
aws_instance.myserver: Still creating... (20s elapsed)
aws_instance.myserver: Creation complete after 22s (ID: i-dd8834ca)

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
[root@tichanejm firstproject]#
```
Confirmons l'instance nouvellement créée à partir de notre console AWS pour nous assurer que l'instance `helloworld` a été créée par le modèle Terraform :

![image](https://user-images.githubusercontent.com/107214400/176911251-46f0e758-3949-45b5-a6bb-40349592bc21.png)

Terraform ne s'est pas contenté de créer une instance et de l'oublier. En fait, Terraform enregistre en fait tout ce qu'il sait sur les ressources (dans notre cas, l'instance) dans un fichier spécial, appelé **fichier d'état** dans Terraform. Dans ce fichier, Terraform stocke l'état de toutes les ressources qu'il a créées. Il est enregistré dans le même répertoire où le modèle Terraform est présent et avec l'extension `.tfstate`. Le format du fichier d'état est un format JSON simple :
```
[root@tichanejm firstproject]# cat terraform.tfstate
{
    "version": 3,
    "terraform_version": "0.11.8",
    "serial": 1,
    "lineage": "9158b0ed-754a-e01e-094e-6b0827347950",
    "modules": [
        {
            "path": [
                "root"
            ],
            "outputs": {},
            "resources": {
                "aws_instance.myserver": {
                    "type": "aws_instance",
                    "depends_on": [],
                    "primary": {
                        "id": "i-dd8834ca",
                        "attributes": {
                              "ami": "ami-cfe4b2b0",
                              "arn": "arn:aws:ec2:us-east-1:094507990803:instance/i-dd8834ca",
                              "associate_public_ip_address": "true",
                              "availability_zone": "us-east-1b",
                              "cpu_core_count": "1",
                              "cpu_threads_per_core": "1",
                              "credit_specification.#": "1",
                              "credit_specification.0.cpu_credits": "standard",
                              "disable_api_termination": "false",
                              "ebs_block_device.#": "0",
                              "ebs_optimized": "false",
                              "ephemeral_block_device.#": "0",
                              "get_password_data": "false",
                              "iam_instance_profile": "",
                              "id": "i-dd8834ca",
                              "instance_state": "running",
                              "instance_type": "t2.micro",
                              "ipv6_addresses.#": "0",
                              "key_name": "aws-devops",
                              "monitoring": "false",
                              "network_interface.#": "0",
                              "network_interface_id": "eni-b0683ee7",
                              "password_data": "",
                              "placement_group": "",
                              "primary_network_interface_id": "eni-b0683ee7",
                              "private_dns": "ip-172-31-74-203.ec2.internal",
                              "private_ip": "172.31.74.203",
                              "public_dns": "ec2-52-70-251-228.compute-1.amazonaws.com",
                              "public_ip": "52.70.251.228",
                              "root_block_device.#": "1",
                              "root_block_device.0.delete_on_termination": "true",
                              "root_block_device.0.iops": "100",
                              "root_block_device.0.volume_id": "vol-024f64aa1bb805237",
                              "root_block_device.0.volume_size": "8",
                              "root_block_device.0.volume_type": "gp2",
                              "security_groups.#": "1",
                              "security_groups.2004290681": "HelloWorld",
                              "source_dest_check": "true",
                              "subnet_id": "subnet-658b6149",
                              "tags.%": "1",
                              "tags.Name": "helloworld",
                              "tenancy": "default",
                              "volume_tags.%": "0",
                              "vpc_security_group_ids.#": "1",
                              "vpc_security_group_ids.1524136243": "sg-01864b4c"
                          },
                          "meta": {
                                "e2bfb730-ecaa-11e6-8f88-34363bc7c4c0": {
                                    "create": 600000000000,
                                    "delete": 1200000000000,
                                    "update": 600000000000
                                },
                                "schema_version": "1"
                           },
                            "tainted": false
                      },
                      "deposed": [],
                      "provider": "provider.aws"
                  }
            },
            "depends_on": []
        }
    ]
  } 
[root@tichanejm firstproject]#
```
La particularité de Terraform est que vous pouvez lire cette sortie JSON dans un format lisible par l'homme à l'aide de la commande `terraform show` :

```
[root@tichanejm firstproject]# terraform show
aws_instance.myserver:
  id = i-dd8834ca
  ami = ami-cfe4b2b0
  arn = arn:aws:ec2:us-east-1:094507990803:instance/i-dd8834ca
  associate_public_ip_address = true
  availability_zone = us-east-1b
  cpu_core_count = 1
  cpu_threads_per_core = 1
  credit_specification.# = 1
  credit_specification.0.cpu_credits = standard
  disable_api_termination = false
  ebs_block_device.# = 0
  ebs_optimized = false
  ephemeral_block_device.# = 0
  get_password_data = false
  iam_instance_profile =
  instance_state = running
  instance_type = t2.micro
  ipv6_addresses.# = 0
  key_name = aws-devops
  monitoring = false
  network_interface.# = 0
  network_interface_id = eni-b0683ee7
  password_data =
  placement_group =
  primary_network_interface_id = eni-b0683ee7
  private_dns = ip-172-31-74-203.ec2.internal
  private_ip = 172.31.74.203
  public_dns = ec2-52-70-251-228.compute-1.amazonaws.com
  public_ip = 52.70.251.228
  root_block_device.# = 1
  root_block_device.0.delete_on_termination = true
  root_block_device.0.iops = 100
  root_block_device.0.volume_id = vol-024f64aa1bb805237
  root_block_device.0.volume_size = 8
  root_block_device.0.volume_type = gp2
  security_groups.# = 1
  security_groups.2004290681 = HelloWorld
  source_dest_check = true
  subnet_id = subnet-658b6149
  tags.% = 1
  tags.Name = helloworld
  tenancy = default
  volume_tags.% = 0
  vpc_security_group_ids.# = 1
  vpc_security_group_ids.1524136243 = sg-01864b4c
  
[root@tichanejm firstproject]#
```

Jusqu'ici, nous avons créé un modèle Terraform, l'avons validé pour nous assurer qu'il n'y a pas d'erreurs de syntaxe, avons effectué un test de fumée sous la forme d'un `terraform plan`, puis avons finalement appliqué notre modèle Terraform à l'aide de `terraform apply` pour créer des ressources.

La question qui reste est de savoir __comment supprimer ou détruire toutes les ressources créées par le modèle Terraform ?__ Avons-nous besoin de rechercher et de supprimer des ressources les unes après les autres ? La réponse est non, cela sera également pris en charge par Terraform. En se référant au fichier d'état créé par Terraform lors de la phase **d'application (apply)**, toutes les ressources créées par Terraform peuvent être détruites à l'aide de la simple commande `terraform destroy` du répertoire `template` :
```
[root@tichanejm firstproject]# terraform destroy
aws_instance.myserver: Refreshing state... (ID: i-dd8834ca)

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
    - destroy
    
Terraform will perform the following actions:

    - aws_instance.myserver
    
    
Plan: 0 to add, 0 to change, 1 to destroy.

Do you really want to destroy all resources?
    Terraform will destroy all your managed infrastructure, as shown above.
    There is no undo. Only 'yes' will be accepted to confirm.
    
Enter a value: yes

aws_instance.myserver: Destroying... (ID: i-dd8834ca)
aws_instance.myserver: Still destroying... (ID: i-dd8834ca, 10s elapsed)
aws_instance.myserver: Still destroying... (ID: i-dd8834ca, 20s elapsed)
aws_instance.myserver: Still destroying... (ID: i-dd8834ca, 30s elapsed)
aws_instance.myserver: Still destroying... (ID: i-dd8834ca, 40s elapsed)
aws_instance.myserver: Still destroying... (ID: i-dd8834ca, 50s elapsed)
aws_instance.myserver: Destruction complete after 1m0s

Destroy complete! Resources: 1 destroyed.

[root@tichanejm firstproject]#
```

Vérifiez votre console AWS pour vous assurer que l'instance est dans un état résilié.
> Vérifiez la commande `terraform show` maintenant. Il doit être vide car aucune de vos ressources ne sera disponible.

## Un deuxième template Terraform pour déployer une application Hello World

Allez dans le référentiel [DevopsTeraformAWS](https://github.com/TICHANE-JM/DevopsTeraformAWS) et créez un répertoire appelé second projet :
```
$ mkdir secondproject
$ cd secondproject
```
Maintenant que nous avons créé notre instance EC2 avec le modèle Terraform dans la section précédente, nous sommes prêts à étendre le provisionnement de notre application Web Hello World. Nous allons utiliser **Terraform Provisioner** pour recréer la pile Hello World que nous avons précédemment créée en utilisant le champ `UserDatablock` de CloudFormation dans la partie 2, __Déployer votre première application Web__ et en utilisant les rôles Ansible dans la partie 3, __Traiter votre infrastructure comme du code__. Si vous vous souvenez, le champ `UserData` ressemblait à peu près à ceci :
```
yum install --enablerepo=epel -y nodejs
wget https://raw.githubusercontent.com/TICHANE-JM/aws-devops/master/Partie2/helloworld
wget https://raw.githubusercontent.com/TICHANE-JM/aws-devops/master/Partie2/helloworld
start helloworld
```
Vous observerez qu'il existe trois types d'opérations différentes pour le déploiement de notre application web Hello World. Tout d'abord, nous préparons le système pour exécuter notre application. Pour ce faire, dans notre exemple, nous installons simplement le package Node.js. Ensuite, nous copions les différentes ressources nécessaires au fonctionnement de l'application. Dans notre cas, ces ressources incluent le code JavaScript et la configuration de démarrage. Enfin, nous commençons le service.

Afin de déployer notre application Web Hello World, nous devons introduire **Terraform Provisioner**. Les approvisionneurs dans Terraform sont des blocs de configuration disponibles pour plusieurs ressources qui vous permettent d'effectuer des actions après la création de la ressource. Il est principalement utilisé pour les instances EC2. Les provisionneurs sont principalement utilisés comme étapes de **post-construction** pour installer des applications légères ou des agents de gestion de la configuration tels que des **agents Puppet** ou des **chefs-clients**. Ils peuvent même être utilisés pour exécuter des outils de gestion de configuration tels que des **playbooks**, des **modules Puppet**, des **cookbooks Chef** ou des **formules Salt**. Dans la section suivante, nous verrons quelques exemples d'utilisation de Terraform avec Ansible.

Créons le modèle Terraform `helloworldec2.tf` pour créer l'instance, puis introduisons le bloc `provisioner` avec `remote-exec` pour établir une connexion avec l'instance nouvellement créée et téléchargeons et déployons l'application Hello World par-dessus. Notre modèle Terraform terminé devrait ressembler à ceci :

```
# Provider Configuration for AWS
provider "aws" {
    access_key = "<YOUR AWS ACCESS KEY>"
    secret_key = "<YOUR AWS SECRET KEY>"
    region = "us-east-1"
}
# Resource Configuration for AWS
resource "aws_instance" "myserver" {
    ami = "ami-cfe4b2b0"
    instance_type = "t2.micro"
    key_name = "EffectiveDevOpsAWS"
    vpc_security_group_ids = ["sg-01864b4c"]
    tags {
        Name = "helloworld"
    }
# Helloworld Appication code
    provisioner "remote-exec" {
      connection {
        user = "ec2-user"
        private_key = "${file("/root/.ssh/aws-devops.pem")}"
      }
      inline = [
        "sudo yum install --enablerepo=epel -y nodejs",
        "sudo wget https://raw.githubusercontent.com/TICHANE-JM/aws-devops/master/Partie2/
        "sudo wget https://raw.githubusercontent.com/TICHANE-JM/aws-devops/master/Chapter02/
        "sudo start helloworld",
      ]
    }
}
```
Le fichier créé doit ressembler au fichier sur : https://github.com/TICHANE-JM/DevopsTeraformAWS/blob/main/secondproject/helloworldec2.tf

Comme nous créons le modèle Terraform dans un nouveau répertoire, `secondproject`, nous devons installer le plug-in ou réinitialiser les plug-ins liés à AWS pour Terraform. Le fichier configuré avec la section `provider` effectuera cette tâche pour nous :
```
$ terraform init
```
Il est maintenant temps de valider le fichier de modèle Terraform pour vous assurer qu'il ne contient aucune erreur de syntaxe. Une fois la vérification réussie, exécutez la commande `plan` suivie de l'exécution complète du modèle à l'aide de la commande `terraform apply` :
```
$ terraform validate
$ terraform plan
$ terraform apply
```
Notre modèle Terraform a été exécuté avec succès. Nous avons provisionné notre instance EC2 et déployé notre application Web Hello World. Trouvons l'adresse IP publique de l'instance en exécutant la commande `terraform show` suivie de la commande `curl` pour nous assurer que l'application s'est correctement déployée :

```
$ terraform show | grep -i public_ip
$ curl <PUBLIC_IP>:3000
```
Le résultat de l'exécution des commandes précédentes est le suivant :
```
[root@tichanejm secondproject]# terraform show | grep -i public_ip
  associate_public_ip_address = true
  public_ip = 34.238.157.112
[root@tichanejm secondproject]#
[root@tichanejm secondproject]# curl 34.238.157.112:3000
Hello World
```
Vérifions également les sorties d'application de notre navigateur, comme indiqué dans la capture d'écran suivante :

![image](https://user-images.githubusercontent.com/107214400/176919143-c93e2996-9241-44ea-a756-65ac81a2c1e5.png)

Nous avons maintenant déployé avec succès notre application Web Hello World en utilisant la puissance de Terraform. Une fois que vous l'avez testé, assurez-vous de supprimer toutes les ressources créées avant de passer à la section suivante. Exécutez la commande `terraform destroy`, qui se chargera de supprimer toutes les ressources créées en se référant au fichier d'état Terraform.

Exécutez la commande suivante :
```
$ terraform destroy
```

## Intégration d'AWS, Terraform et Ansible
Dans les sections précédentes, nous avons vu comment provisionner une instance vanilla à l'aide de Terraform. Nous avons ensuite appris à provisionner une instance EC2 vanille et à exécuter des **post-builds** à l'aide de l'approvisionneur `remote-exec`. Maintenant, nous allons voir comment Terraform peut être intégré à Ansible pour effectuer des tâches de gestion de configuration. Nous allons envisager deux scénarios différents. Dans le premier scénario, nous provisionnerons une instance EC2 et exécuterons Ansible en mode **push**, qui est le principal moyen d'utiliser Ansible pour effectuer l'automatisation. Dans le deuxième scénario, nous provisionnerons une instance EC2 et exécuterons Ansible en mode **pull** en utilisant l'approche `ansible pull`.

## Terraform avec Ansible en utilisant une approche push

Allez dans le référentiel `DevopsTeraformAWS` et créez un répertoire nommé `thirdproject` :
```
$ mkdir thirdproject
$ cd thirdproject
```
Dans cet exemple, nous utiliserons les pratiques recommandées pour créer des modèles Terraform. Nous supprimerons d'abord notre AWS `access_key` et notre AWS `secret_key` de notre modèle Terraform. Nous avons AWS CLI installé sur notre système, ce qui signifie que nous avons déjà configuré ce système pour parler à notre compte AWS. Si nous n'avons pas déjà installé AWS CLI, nous utiliserons `aws configure` pour l'installer. Cela créera un fichier `credentials` dans le répertoire `/root/.aws`, qui contiendra nos clés d'accès et secrètes AWS. Nous allons tirer parti de ce fichier pour notre modèle Terraform et utiliser les mêmes informations d'identification pour créer des ressources mplate et utiliser les mêmes informations d'identification pour créer des ressources sur notre compte AWS :
```
[root@tichanejm thirdproject]# cat /root/.aws/credentials
[default]
aws_access_key_id = <YOUR AWS SECRET KEY>
aws_secret_access_key = <YOUR AWS SECRET KEY>
[root@tichanejm thirdproject]#
```
Il est maintenant temps de commencer à écrire notre modèle Terraform `helloworldansible.tf`. Dans ce cas, nous provisionnerons une instance EC2 et attendrons que les services SSH apparaissent en vérifiant la connexion à l'aide du fournisseur `remote-exec`. Nous utiliserons ensuite le provisionneur `local-exec` pour créer l'inventaire avec la nouvelle adresse IP et y exécuterons les playbooks Ansible à l'aide du modèle push principal en exécutant `ansible-playbook` localement à partir du système.

> À l'intérieur des provisionneurs (et uniquement à l'intérieur des provisionneurs), nous pouvons utiliser un mot-clé spécial, self, pour accéder aux attributs d'une ressource en cours de provisionnement.

Nous utilisons également un autre bloc dans notre code, appelé bloc `output`. Les Outputs vous permettent de renvoyer les données du modèle Terraform après son application, à l'aide de la commande Terraform `output` :

```
# Configuration du fournisseur pour AWS
  provider "aws" {
    region = "us-east-1"
}
# Resource Configuration for AWS
resource "aws_instance" "myserver" {
  ami = "ami-cfe4b2b0"
  instance_type = "t2.micro"
  key_name = "aws-devops"
  vpc_security_group_ids = ["sg-01864b4c"]
  tags {
    Name = "helloworld"
  }
# Approvisionnement pour l'application du playbook Ansible
  provisioner "remote-exec" {
    connection {
    user = "ec2-user"
    private_key = "${file("/root/.ssh/aws-devops.pem")}"
    }
  }
  provisioner "local-exec" {
    command = "sudo echo '${self.public_ip}' > ./myinventory",
  }
  provisioner "local-exec" {
    command = "sudo ansible-playbook -i myinventory --private-key=/root/.ssh/EffectiveDevOpsAWS.pem helloworld.}
  }
# Adresse IP de l'instance EC2 nouvellement créée
output "myserver" {
  value = "${aws_instance.myserver.public_ip}"
}
```
Le fichier créé devrait ressembler au fichier sur : [https://raw.githubusercontent.com/TICHANE-JM/EffectiveDevOpsTerraform/master/thirdproject/helloworldansible.tf.](https://github.com/TICHANE-JM/DevopsTeraformAWS/blob/main/thirdproject/helloworldansible.tf)

Nous appellerons le rôle `helloworld` dans notre playbook `helloworld.yml` Ansible pour déployer l'application web Hello World :
```
---
- hosts: all
    become: yes
    roles:
        - helloworld
```
Le fichier de configuration Ansible `ansible.cfg` devrait ressembler à ceci. Il doit pointer vers le fichier `myinventory` qui est présent dans notre structure de répertoires `thirdproject` :
```
[defaults]
inventory = $PWD/myinventory
roles_path = ./roles
remote_user = ec2-user
become = True
become_method = sudo
become_user = root
nocows = 1
host_key_checking = False
```
Le projet complet devrait ressembler au fichier sur : https://github.com/TICHANE-JM/DevopsTeraformAWS/blob/main/thirdproject

Comme nous avons créé un nouveau répertoire, thirdproject, nous devons à nouveau installer le plugin ou réinitialiser les plugins liés à AWS pour Terraform. Le fichier configuré avec la section fournisseur effectuera cette tâche pour nous :
```
$ terraform init
```
Il est maintenant temps de valider le fichier de modèle Terraform pour vous assurer qu'il ne contient aucune erreur de syntaxe. Une fois la vérification réussie, exécutez le plan suivi de l'exécution réelle à l'aide de terraform apply :
```
$ terraform validate
$ terraform plan
$ terraform apply
```
Les sorties affichent clairement les journaux du playbook Ansible et renvoient le bloc de sortie avec l'adresse IP publique. Utilisons cette adresse IP publique pour vérifier le déploiement de l'application :
```
$ curl 54.85.107.87:3000
```
Le résultat de l'exécution de la commande précédente est le suivant :
```
# [root@tichanejm thirdproject]# curl 54.85.107.87:3000
Hello world
```
Vérifions les sorties de l'application depuis le navigateur, comme illustré dans la capture d'écran suivante :

![image](https://user-images.githubusercontent.com/107214400/176997035-88ec9edd-5ccf-4e84-96ba-48ee9fe84920.png)

Une fois le déploiement réussi, exécutez `terraform destroy` pour nettoyer les ressources créées :
```
$ terraform destroy
```

## Terraform avec Ansible en utilisant l'approche basée sur l'extraction

214








