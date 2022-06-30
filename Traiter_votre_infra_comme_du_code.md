# Traiter votre infrastructure comme du code

Dans le chapitre précédent, nous nous sommes familiarisés avec AWS. Nous avons également créé une instance EC2 et y avons déployé une application Web Hello World. Cependant, pour y arriver, nous avons dû passer par un certain nombre d'étapes pour configurer l'instance et ses groupes de sécurité. Comme nous l'avons fait de manière très manuelle à l'aide de l'interface de ligne de commande, les étapes que nous avons suivies ne seront ni réutilisables ni auditables, comme vous vous en souviendrez peut-être dans le premier chapitre lors de la mise en œuvre des meilleures pratiques DevOps. Deux concepts clés sur lesquels vous devez vous appuyer aussi souvent que possible sont le contrôle de source (contrôle de version) et l'automatisation. Dans ce chapitre, nous allons explorer comment appliquer ces principes à notre infrastructure.

Dans un environnement cloud, où presque tout est abstrait et servi par l'intermédiaire de ressources virtuelles, il est facile d'imaginer que du code puisse décrire la topologie d'un réseau et la configuration d'un système. Pour passer par cette transformation, nous découvrirons deux concepts clés dans une organisation DevOps efficace. Le premier est communément appelé **Infrastructure as Code (IAC)**. C'est le processus de description de toutes vos ressources virtuelles sous forme de codes. Ces ressources peuvent inclure des serveurs virtuels, des équilibreurs de charge, du stockage, la couche réseau, etc. Le deuxième concept, très proche de l'IAC, se concentre davantage sur la configuration du système et s'appelle la **gestion de la configuration**. Grâce aux systèmes de gestion de la configuration, les développeurs et les administrateurs système ont la possibilité d'automatiser la configuration du système d'exploitation, l'installation des packages et même le déploiement des applications.

Passer par cette transformation est une étape cruciale pour toute organisation axée sur DevOps. En ayant le code pour décrire les différentes ressources et leurs configurations, nous pourrons utiliser les mêmes outils et processus que nous utilisons lors du développement d'applications. Nous serons en mesure d'utiliser le contrôle des sources et d'apporter de petites modifications à des branches individuelles, ainsi que de soumettre des demandes d'extraction, de suivre les processus de révision standard et enfin, de tester les modifications avant qu'elles ne soient appliquées à notre environnement de production. Cela nous donnera plus de clarté, de responsabilité et de vérifiabilité pour les changements d'infrastructure. De ce fait, nous pourrons également gérer un parc de ressources beaucoup plus important sans nécessairement avoir besoin de plus d'ingénieurs ou sans passer beaucoup plus de temps à exploiter toutes les ressources. Cela ouvrira également la porte à une automatisation plus poussée, comme nous le verrons avec le déploiement continu dans la partie , __Ajout de l'intégration continue et du déploiement continu__. Dans ce chapitre, nous aborderons les sujets suivants :
* Gérer votre infrastructure avec CloudFormation
* Ajout d'un système de gestion de configuration

## Les pré-requis techniques

Les exigences techniques pour ce chapitre sont les suivantes :
* AWS Console
* AWS CloudFormation
* AWS CloudFormation Designer
* CloudFormer
* Troposphere
* Git
* GitHub
* Ansible

Les liens GitHub pour trouver les codes dans ce chapitre sont les suivants :
https://github.com/TICHANE-JM/aws-devops/blob/main/Partie3/EffectiveDevOpsTemplates/ansiblebase-cf-template.py
https://github.com/TICHANE-JM/aws-devops/blob/main/Partie3/EffectiveDevOpsTemplates/helloworld-cf-template-part-1.py
https://github.com/TICHANE-JM/aws-devops/blob/main/Partie3/EffectiveDevOpsTemplates/helloworld-cf-template.py
https://github.com/TICHANE-JM/aws-devops/tree/main/Partie3/ansible

## Gérer votre infrastructure avec CloudFormation

CloudFormation introduit une nouvelle façon de gérer les services et leurs configurations. Grâce à la création de fichiers JSON ou YAML, CloudFormation vous permet de décrire l'architecture AWS que vous souhaitez construire. Une fois vos fichiers créés, vous pouvez simplement les télécharger sur CloudFormation, qui les exécutera, et créera ou mettra à jour automatiquement vos ressources AWS. La plupart des outils et services gérés par AWS sont pris en charge. Vous pouvez obtenir la liste complète sur http://amzn.to/1Odslix. Dans ce chapitre, nous n'examinerons que l'infrastructure que nous avons construite jusqu'à présent, mais nous ajouterons plus de ressources dans les chapitres suivants. Après un bref aperçu de la structure de CloudFormation, nous allons créer une pile de listes minimale pour recréer l'application Web Hello World de la partie 2, [Déploiement de votre première application Web](https://github.com/TICHANE-JM/aws-devops#d%C3%A9ploiement-de-votre-premi%C3%A8re-application-web). Après cela, nous verrons deux autres options pour créer des modèles CloudFormation : le concepteur, qui vous permet de modifier visuellement votre modèle dans une interface graphique Web, et CloudFormer, un outil permettant de générer des modèles à partir d'une infrastructure existante.

## Premiers pas avec CloudFormation
Comme vous vous en doutez, vous pouvez accéder à CloudFormation via la console AWS à l'adresse https://console.aws.amazon.com/cloudformation, ou en utilisant la ligne de commande suivante :

```
$ aws cloudformation help # pour la liste des options
```
Le service est organisé autour du concept de stacks. Chaque pile décrit généralement un ensemble de ressources AWS et leur configuration afin de démarrer une application. Lorsque vous travaillez avec CloudFormation, vous passez la plupart de votre temps à modifier ces modèles. Il existe différentes manières de commencer l'édition proprement dite des modèles. L'un des moyens les plus simples consiste à modifier les modèles existants. AWS a un certain nombre d'exemples bien écrits disponibles sur http://amzn.to/27cHmrb. Au niveau le plus élevé, les modèles sont structurés comme suit :

```
{
"AWSTemplateFormatVersion" : "version date", "Description" : "Description", "Resources" : { },
"Parameters" : { },
"Mappings" : { },
"Conditions" : { },
"Metadata" : { },
"Outputs" : { }
}
```
La section `AWSTemplateFormatVersion` est actuellement toujours `2010-09-09` et cela représente la version du langage de modèle utilisé. Cette version est actuellement la seule valeur valide. La section `Description` est là pour vous permettre de résumer ce que fait le modèle. La section `Ressources` décrit quels services AWS seront instanciés et quelles sont leurs configurations. Lorsque vous lancez un modèle, vous avez la possibilité de fournir des informations supplémentaires à CloudFormation, telles que la paire de clés SSH à utiliser. Par exemple, si vous souhaitez accorder un accès SSH à vos instances EC2, ce type d'informations va dans la section `Paramètres`. La section `Mappings` est utile lorsque vous essayez de créer un modèle plus générique.

Vous pouvez, par exemple, définir quelle **Amazon Machine Image (AMI)** utiliser pour une région donnée, afin que le même modèle puisse être utilisé pour démarrer une application dans cette région AWS. La section `Conditions` vous permet d'ajouter une logique conditionnelle à vos autres sections (instructions if, opérateurs logiques, etc.), tandis que la section `Metadata` vous permet d'ajouter des informations plus arbitraires à vos ressources. Enfin, la section `Outputs` permet d'extraire et d'imprimer des informations utiles en fonction de l'exécution de votre template, comme par exemple l'adresse IP du serveur EC2 créé. En plus de ces exemples, AWS fournit également quelques outils et services autour de la création de modèles CloudFormation. Le premier outil que vous pouvez utiliser pour créer vos modèles s'appelle CloudFormation Designer.

## Concepteur AWS CloudFormation
AWS CloudFormation Designer est un outil qui vous permet de créer et de modifier des modèles CloudFormation à l'aide d'une interface utilisateur graphique. Designer cache une grande partie de la complexité de l'édition d'un modèle CloudFormation à l'aide d'un éditeur de texte standard. Vous pouvez y accéder directement sur https://console.aws.amazon.com/cloudformation/designer, ou dans le tableau de bord CloudFormation après avoir cliqué sur le bouton Créer une pile, comme illustré ici :

![image](https://user-images.githubusercontent.com/107214400/176675817-b87bb9da-4ff2-4d7c-b8e3-0d20126f0190.png)

Le flux de travail est assez simple. Vous faites simplement glisser et déposez les ressources du menu de gauche dans un canevas.
Une fois vos ressources ajoutées, vous pouvez ensuite les connecter à d'autres ressources à l'aide des petits points entourant chaque icône de ressource. Dans l'exemple précédent, nous connectons une instance EC2 à son groupe de sécurité. Il existe un certain nombre de joyaux cachés qui peuvent vous aider lors de la conception de votre modèle. Vous pouvez cliquer avec le bouton droit sur les ressources et accéder directement à la documentation de la ressource CloudFormation comme suit :

![image](https://user-images.githubusercontent.com/107214400/176676185-1495c674-5963-4ca3-984c-795d963aae4e.png)

Lorsque vous faites glisser un point pour connecter deux ressources, un concepteur mettra en évidence les ressources compatibles avec cette connexion. L'éditeur dans la section inférieure du concepteur prend en charge la complétion automatique à l'aide de `Ctrl + barre d'espace` :

![image](https://user-images.githubusercontent.com/107214400/176676469-3e517327-c07f-4ef7-8086-96f286ea3524.png)

Une fois votre modèle terminé, vous pouvez simplement cliquer sur un bouton et passer de la conception de votre pile à son lancement. Le prochain outil que nous examinerons s'appelle **CloudFormer**.

## CloudFormer

CloudFormer est un outil qui vous permet de créer des modèles CloudFormation en consultant des ressources préexistantes. Si vous avez un ensemble de ressources que vous avez déjà créées de manière ad hoc, comme nous l'avons fait jusqu'à présent , vous pouvez utiliser CloudFormer pour les regrouper sous un nouveau modèle CloudFormation. Vous pouvez ensuite personnaliser ultérieurement le modèle généré par CloudFormer à l'aide d'un éditeur de texte ou même du concepteur CloudFormation, en l'adaptant à vos besoins. Contrairement à la plupart des outils et services AWS, CloudFormer n'est pas entièrement géré par AWS ; c'est un outil auto-hébergé que vous pouvez instancier à la demande à l'aide de CloudFormation. Pour ce faire, suivez les étapes indiquées :

1. Ouvrez https://console.aws.amazon.com/cloudformation dans votre navigateur.
2. Maintenant, faites défiler l'écran de la console AWS, sélectionnez Créer un modèle à partir de votre option Ressources existantes, puis cliquez sur le bouton Lancer CloudFormer.
3. Dans le menu déroulant Select a sample template, choisissez l'option CloudFormer et cliquez sur le bouton Next, comme illustré dans la capture d'écran suivante :

![image](https://user-images.githubusercontent.com/107214400/176677172-0417607b-b8d8-4da8-8a30-12935377b7d6.png)

4. Sur cet écran, en haut, vous pouvez fournir un nom de pile (n'hésitez pas à conserver le nom par défaut, AWSCloudFormer) et en bas, il vous est demandé de fournir trois paramètres supplémentaires, un nom d'utilisateur, un mot de passe et une sélection de VPC. Ce nom d'utilisateur et ce mot de passe seront utilisés plus tard pour se connecter à CloudFormer. Choisissez un nom d'utilisateur et un mot de passe, sélectionnez le VPC par défaut et cliquez sur le bouton Suivant.
5. Sur l'écran suivant, vous pouvez fournir des balises supplémentaires et des options plus avancées, mais nous continuerons simplement en cliquant sur le bouton Suivant.
6. Cela nous amène à la page de révision, où nous cocherons la case pour reconnaître que cela amènera AWS CloudFormation à créer des ressources IAM. Cliquez sur le bouton Créer.
7. Cela nous ramènera à l'écran principal de la console CloudFormation, où nous pouvons voir notre pile AWS CloudFormer en cours de création. Une fois que la colonne Status passe de CREATE_IN_PROGRESS à CREATE_COMPLETE, sélectionnez-la et cliquez sur l'onglet Outputs en bas. À ce stade, vous avez créé les ressources nécessaires pour utiliser CloudFormer. Pour créer une pile avec, procédez comme suit : dans l'onglet Outputs (qui illustre la section Outputs de CloudFormation), cliquez sur le lien URL du site Web. Cela ouvrira l'outil CloudFormer. Connectez-vous à l'aide du nom d'utilisateur et du mot de passe fournis à la quatrième étape de l'ensemble d'instructions précédent, et vous devriez voir quelque chose comme ce qui suit :

![image](https://user-images.githubusercontent.com/107214400/176677972-e5e0404a-d7cc-433d-b51d-1459fe2dbe86.png)

8. Sélectionnez la région AWS dans laquelle vous souhaitez créer le modèle, puis cliquez sur le bouton Créer un modèle. L'écran suivant apparaît alors :

![image](https://user-images.githubusercontent.com/107214400/176678219-31d237f2-27fd-46a9-a403-a363782158ca.png)

9. Suivez le workflow proposé par l'outil pour sélectionner les différentes ressources que vous souhaitez pour votre template CloudFormation, jusqu'à la dernière étape.
10. Au final, vous pourrez télécharger le modèle généré ou l'enregistrer directement dans S3.

Le modèle CloudFormation généré par CloudFormer nécessitera généralement un peu d'édition, car vous souhaiterez souvent créer une pile plus flexible avec des paramètres d'entrée et une section Sorties.

## Recréer notre exemple Hello World avec CloudFormation
Designer et CloudFormer sont deux outils très utiles lorsque vous êtes en train de concevoir votre infrastructure et d'essayer d'ajouter un contrôle de code source à votre conception. Cela dit, chaque fois que vous portez votre chapeau DevOps, c'est une autre histoire. L'utilisation de ces outils réduit considérablement la valeur ajoutée fournie par CloudFormation en utilisant le format JSON. Si vous avez eu l'occasion de lire certains des modèles disponibles ou d'essayer d'utiliser CloudFormer sur votre infrastructure existante, vous avez probablement remarqué que les modèles bruts CloudFormation ont tendance à être assez longs et à **ne pas se répéter (DRY)**.

Du point de vue DevOps, l'un des aspects les plus puissants de CloudFormation est la possibilité d'écrire du code pour générer dynamiquement ces modèles. Pour illustrer ce point, nous allons nous tourner vers Python et une bibliothèque appelée `troposphere` pour générer notre modèle Hello World CloudFormation.

> Il existe également un certain nombre d'outils plus avancés pour aider à la création de modèles CloudFormation. Si vous prévoyez d'utiliser d'autres services tiers en plus d'AWS, vous pouvez jeter un œil à Terraform de Hashicorp (disponible sur https://www.terraform.io), par exemple, qui gère un certain nombre d'autres fournisseurs de cloud et services en plus de CloudFormation.

## Utilisation de Troposphere pour créer un script Python pour notre modèle
Nous allons d'abord installer la bibliothèque de `troposphère`. Encore une fois, nous démontrons toutes les sorties d'une distribution Linux basée sur CentOS 7.x, mais le processus s'applique également à toutes les plates-formes prises en charge mentionnées. Voici la commande pour installer la bibliothèque de `troposphère` :

```
$ pip install troposphere
```
> Un problème connu avec Troposphere est la version mise à jour de `setuptools`. Si vous rencontrez le problème suivant, la solution consiste à mettre à niveau `setuptools` à l'aide de la commande `pip install -U setuptools`.

Une fois que vous avez exécuté la commande précédente, vous pouvez rencontrer l'erreur suivante :

```
....
setuptools_scm.version.SetuptoolsOutdatedWarning: your setuptools is too old (<12)
-----------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-install-pW4aV4/cfn-flip/
```
Afin de corriger l'erreur, vous pouvez exécuter la commande suivante :

```
$ pip install -U setuptools
Collecting setuptools
Downloading https://files.pythonhosted.org/packages/ff/f4/385715ccc461885f3cedf57a41ae3c12b5fec3f35cce4c8706b1a112a133/100% |████████████████████████████████| 573kB 22.2MB/s
Installing collected packages: setuptools
Found existing installation: setuptools 0.9.8
Uninstalling setuptools-0.9.8:
Successfully uninstalled setuptools-0.9.8
Successfully installed setuptools-40.0.0
```

Une fois l'installation terminée, vous pouvez alors créer un nouveau fichier appelé `helloworld-cf-template.py`.

Nous allons commencer notre fichier en important un certain nombre de définitions du module de `troposphère` comme suit :

```
"""Generating CloudFormation template."""
from troposphere import (
  Base64,
  ec2,
  GetAtt,
  Join,
  Output,
  Parameter,
  Ref,
  Template,
)
```
Nous allons également définir une première variable qui facilitera l'édition du code pour la suite du livre. En effet, nous allons créer de nouveaux scripts en nous appuyant sur ce modèle initial :

```
ApplicationPort = "3000"
```
Du point de vue du code, la première chose que nous allons faire est d'initialiser une variable Template. À la fin de notre script, le modèle contiendra la description complète de notre infrastructure et nous pourrons simplement imprimer sa sortie pour obtenir notre modèle CloudFormation :

```
t = Template()
```
Tout au long de ce livre, nous allons créer et exécuter plusieurs modèles CloudFormation simultanément. Pour nous aider à identifier ce qui se trouve dans une pile donnée, nous avons la possibilité de fournir une description. Après la création du modèle, ajoutez la description comme suit :

```
add_description("Effective DevOps in AWS: HelloWorld web application")
```
Lorsque nous avons lancé des instances EC2 à l'aide de l'interface de ligne de commande Web, nous avons sélectionné la paire de clés à utiliser pour obtenir un accès SSH à l'hôte. Afin de ne pas perdre cette capacité, la première chose que notre modèle aura est un paramètre pour offrir à l'utilisateur CloudFormation la possibilité de sélectionner la paire de clés à utiliser lors du lancement de l'instance EC2. Pour ce faire, nous allons créer un objet `Parameter` et l'initialiser en fournissant un identifiant, une description, un type de paramètre, une description du type de paramètre et une description de la contrainte pour aider à prendre la bonne décision lorsque nous lançons la pile. Pour que ce paramètre existe dans notre template final, nous utiliserons également la fonction `add_parameter()` définie dans la classe template :

```
t.add_parameter(Parameter(
"KeyPair",
Description="Nom d'une EC2 KeyPair existante vers SSH",
Type="AWS::EC2::KeyPair::KeyName",
ConstraintDescription="doit être le nom d'une EC2 KeyPair existante.",
))
```
La prochaine chose que nous allons examiner est le groupe de sécurité. Nous allons procéder exactement comme nous l'avons fait pour notre paramètre `KeyPair`. Nous voulons ouvrir `SSH/22` et `TCP/3000` au monde. Le port `3000` a été défini dans la variable `ApplicationPort` déclarée précédemment. De plus, cette fois, l'information définie n'est plus un paramètre comme avant, mais une ressource. Par conséquent, nous ajouterons cette nouvelle ressource en utilisant la fonction `add_resource()` comme suit :

```
t.add_resource(ec2.SecurityGroup(
    "SecurityGroup",
    GroupDescription="Allow SSH and TCP/{} access".format(ApplicationPort),
    SecurityGroupIngress=[
        ec2.SecurityGroupRule(
            IpProtocol="tcp",
            FromPort="22",
            ToPort="22",
            CidrIp="0.0.0.0/0",
        ),
        ec2.SecurityGroupRule(
            IpProtocol="tcp",
            FromPort=ApplicationPort,
            ToPort=ApplicationPort,
            CidrIp="0.0.0.0/0",
        ),
    ],
))
```
Dans notre prochaine section, nous remplacerons la nécessité de se connecter à notre instance EC2 et d'installer le fichier `helloworld.js` et ses scripts d'initialisation à la main. Pour ce faire, nous tirerons parti des fonctionnalités `UserData` proposées par EC2. Lorsque vous créez une instance EC2, le paramètre facultatif `UserData` vous permet de fournir un ensemble de commandes à exécuter une fois que la machine virtuelle est apparue (vous pouvez en savoir plus sur ce sujet à l'adresse http://amzn.to/1VU5b3s). L'une des contraintes du paramètre `UserData` est que le script doit être encodé en base64 pour être ajouté à notre appel API.

Nous allons créer un petit script pour reproduire les étapes que nous avons parcourues à la Partie 2, __Déployer votre première application Web__ . Ici, nous allons encoder, déployer notre première étape de déploiement d'application Web en base-64 et la stocker dans une variable appelée `ud`. Notez que l'installation de l'application dans le répertoire `home` d'`ec2-user` n'est pas très propre. Pour l'instant, nous essayons de rester cohérents avec ce que nous avons fait au Chapitre 2, Déployer votre première application Web. Nous corrigerons cela dans la partie 5, __Ajout de l'intégration continue et du déploiement continu__ , à mesure que nous améliorons notre système de déploiement :

```
ud = Base64(Join('\n', [
"#!/bin/bash",
"sudo yum install --enablerepo=epel -y nodejs",
"wget http://bit.ly/2vESNuc -O /home/ec2-user/helloworld.js",
"wget http://bit.ly/2vVvT18 -O /etc/init/helloworld.conf",
"start helloworld"
]))
```
Nous allons maintenant nous concentrer sur la ressource principale de notre modèle, qui est notre instance EC2. La création de l'instance nécessite de fournir un nom pour identifier la ressource, un ID d'image, un type d'instance, un groupe de sécurité, la paire de clés à utiliser pour l'accès SSH et les données de l'utilisateur. Afin de garder les choses simples, nous allons coder en dur l'ID AMI (`ami-cfe4b2b0`) et le type d'instance (`t2.micro`).

Les informations restantes nécessaires pour créer nos instances EC2 sont les informations du groupe de sécurité et le nom `KeyPair`, que nous avons collectés précédemment en définissant un paramètre et une ressource. Dans CloudFormation, vous pouvez faire référence à des sous-sections préexistantes de votre modèle en utilisant le mot-clé `Ref`. Dans Troposphere, cela se fait en appelant la fonction `Ref()`. Comme précédemment, nous ajouterons la sortie résultante à notre modèle à l'aide de la fonction `add_resource` :

```
...
t.add_resource(ec2.Instance(
    "instance",
    ImageId="ami-cfe4b2b0",
    InstanceType="t2.micro",
    SecurityGroups=[Ref("SecurityGroup")],
    KeyName=Ref("KeyPair"),
    UserData=ud,
))
...
```
Dans la dernière section de notre script, nous nous concentrerons sur la production de la section `Outputs` du modèle qui est remplie lorsque CloudFormation crée une pile. Cette sélection vous permet d'imprimer des informations utiles qui ont été calculées lors du lancement de la pile. Dans notre cas, il existe deux informations utiles : l'URL pour accéder à notre application Web et l'adresse IP publique de l'instance, afin que nous puissions nous y connecter en SSH si nous le souhaitons. Afin de récupérer ces informations, CloudFormation utilise la fonction `Fn::GetAtt`. Dans Troposphere, cela se traduit par la fonction `GetAtt()` :

```
...
t.add_output(Output(
    "InstancePublicIp",
    Description="Public IP of our instance.",
    Value=GetAtt("instance", "PublicIp"),
))
t.add_output(Output(
    "WebUrl",
    Description="Application endpoint",
    Value=Join("", [
        "http://", GetAtt("instance", "PublicDnsName"),
        ":", ApplicationPort
    ]),
))
...
```
À ce stade, nous pouvons faire en sorte que notre sortie de script soit le résultat final du modèle que nous avons généré :
```
print t.to_json()
```
The script is now complete. We can save this and quit our editor. The file created
should look like the file at the following link:
https://github.com/TICHANE-JM/aws-devops/blob/main/Partie3/EffectiveDevOpsTemplates/helloworld-cf-template-part-1.py

Nous pouvons maintenant exécuter notre script, lui donner les autorisations appropriées et générer le modèle CloudFormation en enregistrant la sortie de notre script dans un fichier comme suit :

```
$ python helloworld-cf-template.py > helloworld-cf.template
```
> `cloud-init` est un ensemble de scripts Python compatibles avec la plupart des distributions Linux et des fournisseurs de cloud. Cela complète le champ UserData en déplaçant la plupart des opérations standard, telles que l'installation de packages, la création de fichiers et l'exécution de commandes dans différentes sections du modèle. Ce livre ne couvre pas cet outil, mais si vos modèles CloudFormation reposent fortement sur le champ UserData, jetez-y un coup d'œil. Vous pouvez obtenir sa documentation sur http://bit.ly/1W6s96M.

## Créer la pile dans la console CloudFormation

À ce stade, nous pouvons lancer notre modèle en suivant les étapes suivantes :

1. Ouvrez la console Web CloudFormation dans votre navigateur avec le lien suivant : https://console.aws.amazon.com/cloudformation. Cliquez sur le bouton Créer une pile.
2. Sur l'écran suivant, nous allons télécharger notre modèle nouvellement généré, `helloworld-cf.template`, en sélectionnant Télécharger un modèle sur Amazon S3, puis en naviguant pour sélectionner notre fichier `helloworld-cf.template`.
3. Nous choisirons ensuite un nom de pile, tel que `HelloWorld`.
4. Après le nom de la pile, nous pouvons voir la section Paramètres de notre modèle en action. CloudFormation nous permet de choisir la paire de clés SSH à utiliser. Sélectionnez votre paire de clés à l'aide du menu déroulant.
5. Sur l'écran suivant, nous devons pouvoir ajouter des balises facultatives à nos ressources ; dans la section Avancé, nous pouvons voir comment nous pouvons potentiellement intégrer CloudFormation et SNS, prendre des décisions sur ce qu'il faut faire lorsqu'une panne ou un délai d'attente se produit, et même ajouter une politique de pile qui vous permet de contrôler qui peut modifier la pile, par exemple. Pour l'instant, nous allons simplement cliquer sur le bouton Suivant.
6. Cela nous amène à l'écran de révision où nous pouvons vérifier les informations sélectionnées et même estimer combien il en coûtera pour exécuter cette pile. Cliquez sur le bouton Créer.
7. Cela nous amènera à la console principale de CloudFormation. Sur cet écran, nous pouvons voir comment nos ressources sont créées dans l'onglet Événements.
8. Lorsque la création du modèle est terminée, cliquez sur les onglets Sorties, qui révéleront les informations que nous avons générées via la section Sorties de notre modèle, comme indiqué ici :

![image](https://user-images.githubusercontent.com/107214400/176697977-cc83f5a8-4ce1-423b-9408-90bf25c17d76.png)

9. Cliquez sur le lien dans la valeur de la clé WebUrl, ce qui ouvrira notre page Hello World.

## Ajout de notre modèle à un système de contrôle de code source

Maintenant que nous avons testé notre modèle et que nous savons qu'il fonctionne, nous allons le valider dans notre système de contrôle des sources. Cela nous permettra de garder une trace des changements, permettant de traiter notre code d'infrastructure au même standard que notre code d'application (plus à ce sujet dans la partie 5, __Ajouter l'intégration continue et le déploiement continu__ ).

Pour ce faire, nous allons nous appuyer sur Git. AWS dispose d'un service appelé AWS CodeCommit (http://amzn.to/2tKUj0n), qui vous permet de gérer facilement les référentiels Git. Cependant, comme ce service est beaucoup moins populaire que GitHub (https://github.com), nous utiliserons plutôt ce dernier. Si vous n'avez pas encore de compte GitHub, commencez par vous inscrire au service, c'est entièrement gratuit.

Une fois connecté à GitHub, créez un nouveau dépôt pour le modèle CloudFormation :

1. Dans votre navigateur, ouvrez https://github.com/new.
2. Appelez le nouveau référentiel comme suit : aws-devops.
3. Cochez la case Initialiser ce référentiel avec un fichier README.
4. Enfin, cliquez sur le bouton Créer un référentiel, comme illustré ici :

![image](https://user-images.githubusercontent.com/107214400/176702675-aa0c4489-4a52-4879-91c9-aae69b958ba3.png)

5. Une fois votre référentiel créé, vous souhaiterez le cloner sur votre ordinateur. Pour cela, vous devez avoir Git installé (recherchez sur Google des instructions sur la façon d'installer Git pour votre système d'exploitation si vous ne l'avez pas encore). Pour CentOS, il vous suffit d'exécuter `yum -y install git`, car le package Git fait désormais partie de la distribution Linux :

```
$ git clone https://github.com/<your_github_username>/aws-devops
```

6. Maintenant que le dépôt est cloné, nous allons y entrer et copier le modèle précédemment créé dans le nouveau dépôt GitHub :

```
$ cd aws-devops
$ cp <path_to_helloworld_template>/helloworld-cf-template.py .
```
7. Enfin, nous ajouterons et validerons ce nouveau fichier dans notre projet et le transmettrons à GitHub comme suit :

```
$ git add helloworld-cf-template.py
$ git commit -m "Adding helloworld Troposphere template"
$ git push
```

> **Monorepo versus multirepo :** lors de la gestion de votre code, il existe deux approches courantes pour organiser vos référentiels de code. Vous pouvez créer un référentiel pour chaque projet que vous avez ou décider de placer l'ensemble de votre code d'organisation sous un seul référentiel. Nous choisirons l'option la plus simple pour ce livre, qui est un référentiel par projet, mais avec les versions récentes de plusieurs projets open source, tels que Bazel de Google, Buck de Facebook ou Pants de Twitter, l'utilisation d'un monorepo devient très convaincante. option car elle évite de jongler entre plusieurs référentiels lors de modifications importantes simultanées de votre infrastructure et de vos services.

## Mise à jour de notre stack CloudFormation
L'un des principaux avantages de l'utilisation du modèle CloudFormation pour gérer nos ressources est que les ressources créées à partir de CloudFormation sont étroitement couplées à notre pile. Si nous voulons apporter une modification à notre pile, nous pouvons mettre à jour le modèle et appliquer la modification à notre pile CloudFormation existante. Voyons comment cela fonctionne.

### Mise à jour de notre script Python

Notre script `helloworld-cf-template.py` est assez basique. À ce stade, nous ne profitons de Python que pour utiliser la bibliothèque `troposphere` pour générer facilement une sortie JSON d'une manière plus agréable que si nous devions l'écrire à la main. Bien sûr, vous vous rendez peut-être déjà compte que nous effleurons à peine la surface de ce que nous pouvons faire lorsque nous avons la capacité d'écrire des scripts pour créer et gérer des infrastructures. La section suivante est un exemple simple qui nous permettra d'écrire quelques lignes supplémentaires de Python et d'illustrer le concept de mise à jour d'une pile CloudFormation, tout en tirant parti de davantage de services et de ressources externes.

Les groupes de sécurité que nous avons créés dans notre exemple précédent ouvrent deux ports au monde : `22` (SSH) et `3000` (le port d'application Web). Nous pourrions essayer de renforcer un aspect de notre sécurité en autorisant uniquement notre propre adresse IP à utiliser SSH. Cela signifie modifier les informations **IP CIDR (Classless Inter-Domain Routing)** dans notre script Python sur le groupe de sécurité qui gère le trafic du port 22. Il existe un certain nombre de services gratuits en ligne qui nous permettront de savoir quelle est notre adresse IP publique. Nous allons en utiliser un, disponible sur https://api.ipify.org. Nous pouvons le voir en action avec une simple commande `curl` :

```
$ curl https://api.ipify.org 54.164.95.231
```
Nous allons profiter de ce service dans notre script. L'une des raisons d'utiliser ce service particulier est qu'il a été empaqueté dans une bibliothèque Python. Vous pouvez en savoir plus à ce sujet sur https://github.com/rdegges/python-ipify. Vous pouvez d'abord installer cette bibliothèque comme suit :

```
$ pip install ipify
```
Si vous rencontrez des erreurs liées à pip, comme indiqué dans le bloc de code suivant, le correctif consisterait à rétrograder la version pip, à installer `ipify`, puis à mettre à niveau la version `pip` vers la dernière version :

```
Cannot uninstall 'requests'. It is a distutils installed project and thus we cannot accurately determ
```
L'erreur précédente peut être corrigée avec les commandes suivantes :

```
$ pip install --upgrade --force-reinstall pip==9.0.3
$ pip install ipify
$ pip install --upgrade pip
```
Notre script nécessite un CIDR. Afin de convertir notre adresse IP en CIDR, nous allons également installer une autre bibliothèque, appelée `ipaddress`. Le principal avantage de combiner ces bibliothèques est que nous n'avons pas à nous soucier de la gestion d'IPv4 par rapport à IPv6 :

```
$ pip install ipaddress
```
Une fois ces bibliothèques installées, rouvrez `helloworld-cf-template.py` dans votre éditeur. En haut de notre script, nous allons importer les bibliothèques, puis, après la définition de la variable `ApplicationPort`, nous définirons une nouvelle variable appelée `PublicCidrIp` et, en combinant les deux bibliothèques citées précédemment, nous pourrons extraire notre CIDR comme suit :

```
...
from ipaddress import ip_network
from ipify import get_ip
from troposphere import (
    Base64,
    ec2,
    GetAtt,
    Join,
    Output,
    Parameter,
    Ref,
    Template,
)
ApplicationPort = "3000"
PublicCidrIp = str(ip_network(get_ip()))
...
```
Enfin, nous pouvons modifier la déclaration CidrIp pour la règle de groupe SSH comme suit :

```
SecurityGroupIngress=[
        ec2.SecurityGroupRule(
        IpProtocol="tcp",
        FromPort="22",
        ToPort="22",
        CidrIp=PublicCidrIp,
    ),
....
  ]
```
Nous pouvons maintenant enregistrer ces modifications. Le fichier créé doit ressembler au fichier sur https://github.com/TICHANE-JM/aws-devops/blob/master/Partie3/EffectiveDevOpsTemplates/helloworld-cf-template.py

Nous pouvons maintenant générer une nouvelle commande `diff` pour vérifier visuellement le changement :

```
$ python helloworld-cf-template.py > helloworld-cf-v2.template
$ diff helloworld-cf-v2.template helloworld-cf.template
46c46
< "CidrIp": "54.164.95.231/32",
---
> "CidrIp": "0.0.0.0/0",
91a92
>$
```
Comme nous pouvons le voir, notre IP CIDR restreint maintenant correctement la connexion à notre IP. Nous pouvons maintenant appliquer ce changement.

### Mise à jour de notre pile

Après avoir généré le nouveau modèle JSON CloudFormation, nous pouvons accéder à la console CloudFormation et mettre à jour la pile comme suit :

1. Ouvrez la console Web CloudFormation dans votre navigateur à l'adresse https://console.aws.amazon.com/cloudformation.
2. Sélectionnez la pile `HelloWorld` que nous avons créée précédemment.
3. Cliquez sur le menu déroulant Actions, puis choisissez l'option Mettre à jour la pile.
4. Choisissez le fichier `helloworld-cf-v2`.template en cliquant sur le bouton Parcourir, en sélectionnant le fichier, puis en cliquant sur le bouton Suivant.
5. Cela nous amène à l'écran suivant qui nous permet de mettre à jour les détails de notre pile. Dans notre cas, rien n'a changé dans les paramètres, nous pouvons donc continuer en cliquant sur le bouton Suivant.
6. Dans l'écran suivant également, puisque nous voulons simplement voir l'effet de notre changement d'IP, nous pouvons cliquer sur le bouton Suivant :

![image](https://user-images.githubusercontent.com/107214400/176714152-d73fa7ad-1fba-434a-9382-e0c4618a57d0.png)

7.Cela nous amène à la page de révision, où, après quelques secondes, nous pouvons voir CloudFormation nous donner un aperçu de notre changement :

![image](https://user-images.githubusercontent.com/107214400/176714327-11866980-92d1-4e3a-b3e5-9ccf907edfd9.png)

8. Comme vous pouvez le voir, le seul changement sera une mise à jour du groupe de sécurité. Cliquez maintenant sur le bouton Mettre à jour. Cela nous ramènera au modèle CloudFormation, où nous verrons le changement appliqué.
9. Dans cet exemple particulier, AWS peut simplement mettre à jour le groupe de sécurité pour prendre en compte notre changement. Nous pouvons vérifier le changement en extrayant l'ID physique de la page de révision ou de l'onglet Ressources de la console :

```
$ aws ec2 describe-security-groups \
--group-names HelloWorld-SecurityGroup-1XTG3J074MXX
```

### Ensembles de modifications

Notre modèle ne comprend qu'un serveur Web et un groupe de sécurité qui fait de la mise à jour de CloudFormation une opération assez inoffensive. De plus, notre changement était assez trivial, car AWS pouvait simplement mettre à jour le groupe de sécurité existant, au lieu de devoir le remplacer. Comme vous pouvez l'imaginer, à mesure que l'architecture devient de plus en plus complexe, il en va de même pour le modèle CloudFormation. Selon la mise à jour que vous souhaitez effectuer, vous pouvez rencontrer des modifications inattendues lorsque vous examinez l'ensemble de modifications à l'étape finale de la mise à jour d'un modèle. AWS offre un moyen alternatif et plus sûr de mettre à jour les modèles ; cette fonctionnalité est appelée **ensembles de modifications** et est accessible depuis la console CloudFormation. Suivez cette procédure afin d'utiliser des ensembles de modifications pour examiner les mises à jour, suivies de l'exécution :
1. Ouvrez la console Web CloudFormation dans votre navigateur à l'adresse https://console.aws.amazon.com/cloudformation
2. Sélectionnez la pile `HelloWorld` que nous avons précédemment créée
3. Cliquez sur le menu déroulant Actions, puis cliquez sur l'option Créer un ensemble de modifications pour la pile actuelle

À partir de là, vous pouvez suivre les mêmes étapes que vous avez suivies pour créer une mise à jour simple dans la section __Mise à jour de notre pile__. La principale différence se produit sur le dernier écran, illustré ici :

![image](https://user-images.githubusercontent.com/107214400/176715447-6f1d1f4f-caf8-42da-b907-a8facd8dcec0.png)

Contrairement aux mises à jour régulières de la pile, les ensembles de modifications mettent fortement l'accent sur la possibilité d'examiner une modification avant de l'appliquer. Si vous êtes satisfait des modifications affichées, vous avez la possibilité d'exécuter la mise à jour. Enfin, lorsque vous utilisez un ensemble de modifications pour mettre à jour votre pile, vous pouvez facilement auditer les modifications récentes à l'aide de l'onglet Ensembles de modifications de votre pile dans la console CloudFormation. Enfin, nous allons valider les modifications apportées au script Troposphere avec la commande suivante :

```
$ git commit -am "Only allow ssh from our local IP"
$ git push
```
### Suppression de notre pile CloudFormation

Dans la dernière section, nous avons vu comment CloudFormation a pu mettre à jour les ressources au fur et à mesure que nous mettons à jour notre modèle. Il en va de même lorsque vous souhaitez supprimer une pile CloudFormation et ses ressources. En quelques clics, vous pouvez supprimer votre modèle et les différentes ressources qui ont été créées au moment du lancement. Du point de vue des meilleures pratiques, il est fortement recommandé de toujours utiliser CloudFormation pour apporter des modifications à vos ressources précédemment initialisées avec CloudFormation, y compris lorsque vous n'avez plus besoin de votre pile.

La suppression d'une pile est très simple et vous devez procéder comme suit :
1. Ouvrez la console Web CloudFormation dans votre navigateur à l'adresse https://console.aws.amazon.com/cloudformation
2. Sélectionnez la pile HelloWorld que nous avons créée précédemment
3. Cliquez sur le menu déroulant Actions, puis cliquez sur l'option Supprimer la pile

Comme toujours, vous pourrez suivre l'achèvement dans l'onglet Événements :

![image](https://user-images.githubusercontent.com/107214400/176716424-8cbef056-f097-41f8-bc37-4bd106a5f552.png)

CloudFormation occupe une place unique dans l'écosystème AWS. Aussi complexes soient-elles, la plupart des architectures peuvent être décrites et gérées via CloudFormation, ce qui vous permet de garder un contrôle étroit sur la création de vos ressources AWS. Bien que CloudFormation fasse un excellent travail de gestion de la création de ressources, cela ne facilite pas toujours les choses. C'est particulièrement le cas lorsque vous souhaitez apporter des modifications simples à des services tels que EC2. Étant donné que CloudFormation ne suit pas l'état des ressources une fois qu'elles sont lancées, le seul moyen fiable de mettre à jour une instance EC2 est, par exemple, de recréer une nouvelle instance et de l'échanger avec l'instance existante lorsqu'elle est prête. Cela crée en quelque sorte une conception immuable (en supposant que vous n'exécutez aucune commande supplémentaire lors de la création de l'instance). Cela peut être un choix d'architecture attrayant et, dans certains cas, cela peut vous prendre un long chemin, mais vous souhaiterez peut-être avoir la possibilité d'avoir des instances de longue durée là où vous le pouvez, car cela vous permet d'apporter des modifications rapidement et de manière fiable via un pipeline contrôlé, comme nous l'avons fait avec CloudFormation. C'est ce à quoi excellent les systèmes de gestion de configuration.

## Ajout d'un système de gestion de configuration
Les systèmes de gestion de configuration sont probablement les composants les plus connus des organisations classiques axées sur DevOps. Présents dans la plupart des entreprises (y compris sur le marché des entreprises), les systèmes de gestion de configuration remplacent rapidement les scripts Shell, Python et Perl développés en interne. Il existe de nombreuses raisons pour lesquelles les systèmes de gestion de la configuration devraient faire partie de votre environnement. L'une des raisons est qu'ils proposent des langages spécifiques à un domaine, ce qui améliore la lisibilité du code, et qu'ils sont adaptés aux besoins spécifiques qui surviennent dans les organisations lors de la configuration des systèmes. Cela se traduit par de nombreuses fonctionnalités intégrées utiles. De plus, les outils de gestion de configuration les plus courants ont une communauté d'utilisateurs importante et active, ce qui signifie souvent que vous pourrez trouver le code existant pour le système que vous essayez d'automatiser.

Certains des outils de gestion de configuration les plus populaires incluent **Puppet**, **Chef**, **SaltStack** et **Ansible**. Bien que toutes ces options soient assez bonnes, ce livre se concentrera sur Ansible, le plus simple des quatre outils mentionnés. Il existe un certain nombre de caractéristiques clés qui font d'Ansible une solution très populaire et facile à utiliser. Contrairement à d'autres systèmes de gestion de configuration, Ansible est conçu pour fonctionner sans serveur, démon ou base de données. Vous pouvez simplement conserver votre code dans le contrôle de code source et le télécharger sur l'hôte chaque fois que vous avez besoin de l'exécuter ou d'utiliser un mécanisme push via SSH. Le code d'automatisation que vous écrivez se trouve dans des fichiers statiques YAML, ce qui rend la courbe d'apprentissage beaucoup moins abrupte que certaines des autres alternatives qui utilisent Ruby ou un DSL spécifique. Afin de stocker nos fichiers de configuration, nous nous appuierons plutôt sur notre système de contrôle de version (dans notre cas, GitHub.) **AWS OpsWorks et son intégration Chef :** alors qu'Amazon n'a pas vraiment publié de service dédié à la gestion de la configuration, il prend en charge Chef et Marionnette au sein du service OpsWorks. Contrairement aux services que nous avons explorés jusqu'à présent , OpsWorks vise à être un __cycle de vie complet des applications, y compris l'approvisionnement des ressources, la gestion de la configuration, le déploiement des applications, les mises à jour logicielles, la surveillance et le contrôle d'accès__. Si vous êtes prêt à sacrifier une certaine flexibilité et un certain contrôle, OpsWorks peut être en mesure de gérer ce dont vous avez besoin pour exécuter une application Web simple. Vous pouvez en savoir plus à ce sujet sur http://amzn.to/1O8dTsn.

## Premiers pas avec Ansible

Commencez par installer Ansible sur votre ordinateur. Après cela, créez une instance EC2 qui nous permettra d'illustrer l'utilisation de base d'Ansible. Après cela, nous travaillerons à recréer l'application Hello World Node.js en créant et en exécutant ce qu'Ansible appelle un playbook. Nous verrons ensuite comment Ansible peut fonctionner en mode pull, qui offre une nouvelle approche du déploiement des changements. Enfin, nous envisagerons de remplacer le bloc `UserData` dans notre modèle CloudFormation par Ansible pour combiner les avantages de CloudFormation et de notre système de gestion de configuration.

> Ansible est assez facile à utiliser et bien documenté sur le Web. Ici on en en couvrira suffisamment pour vous aider à démarrer et à vous familiariser avec des configurations simples, telles que celle dont nous avons besoin dans nos exemples. Cependant, vous pourriez être intéressé à passer un peu plus de temps à apprendre Ansible afin d'être vraiment efficace avec lui.

### Installation d'Ansible sur votre ordinateur
Comme mentionné précédemment, Ansible est une application très simple avec très peu de dépendances. Vous pouvez installer Ansible sur votre ordinateur à l'aide du gestionnaire de packages de votre système d'exploitation ou via `pip`, car Ansible est écrit en Python. Nous présenterons toutes les sorties d'une distribution Linux basée sur CentOS 7.x, mais le processus s'applique de la même manière à toutes les plates-formes prises en charge. (Pour plus d'informations, reportez-vous au lien suivant afin de trouver et d'installer les binaires Ansible sur votre système d'exploitation : https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-the-control-machine .) La commande suivante installera un certain nombre de fichiers binaires, bibliothèques et modules Ansible :

```
$ yum install ansible
```
Notez qu'aucun démon ou base de données n'est installé à ce stade. En effet, par défaut, Ansible s'appuie sur des fichiers statiques et SSH pour s'exécuter. À ce stade, nous sommes prêts à utiliser Ansible :

```
$ ansible --version
    ansible 2.6.2
    config file = /etc/ansible/ansible.cfg
    configured module search path = [u'/root/.ansible/plugins/modules',
    u'/usr/share/ansible/plugins/modules']
    ansible python module location = /usr/lib/python2.7/sitepackages/
    ansible
    executable location = /bin/ansible
    python version = 2.7.5 (default, Aug 4 2017, 00:39:18) [GCC 4.8.5
    20150623 (Red Hat 4.8.5-16)]
```
### Créer notre terrain de jeu Ansible

Pour illustrer les fonctionnalités de base d'Ansible, nous allons commencer par relancer notre application Hello World.
Dans la section précédente, nous avons vu comment créer une pile à l'aide de l'interface Web. Comme vous vous en doutez, il est également possible de lancer une pile à l'aide de l'interface de ligne de commande. Allez dans le répertoire `aws-devops` où vous avez précédemment généré le fichier helloworld-cf-v2.template et exécutez la commande suivante :

```
$ aws cloudformation create-stack \
    --capabilities CAPABILITY_IAM \
    --stack-name ansible \
    --template-body file://helloworld-cf-v2.template \
    --parameters ParameterKey=KeyPair,ParameterValue=EffectiveDevOpsAWS
{
    "StackId": "arn:aws:cloudformation:us-east-
      1:094507990803:stack/ansible/bb29cb10-9bbe-11e8-9ee4-500c20fefad2"
}
```
Notre instance sera bientôt prête. Nous pouvons maintenant démarrer notre environnement en créant un espace de travail.

### Création de notre référentiel Ansible
Avec Ansible, notre premier objectif est de pouvoir exécuter des commandes sur des hôtes distants. Afin de le faire efficacement, nous devons configurer notre environnement local. Parce que nous ne voulons pas avoir à refaire ces étapes à plusieurs reprises, et parce que, finalement, nous voulons tout contrôler à la source, nous allons créer un nouveau dépôt Git. Pour ce faire, nous allons répéter les mêmes étapes que celles que nous avons utilisées lors de la création de notre référentiel `aws-devops`.
Une fois connecté à GitHub, créez un nouveau référentiel pour le modèle CloudFormation comme suit :

1. In your browser, open this link: https://github.com/new.
2. Give the new repository the name ansible, as shown here:

![image](https://user-images.githubusercontent.com/107214400/176720612-36663cb0-09f2-41b5-9852-a8d135f0d09c.png)

3. Cochez la case Initialiser ce référentiel avec un fichier README.
4. Enfin, cliquez sur le bouton Créer un référentiel.
5. Une fois votre dépôt créé, clonez-le sur votre ordinateur comme suit :

```
$ git clone https://github.com/<your_github_username>/ansible
```

6. Maintenant que le dépôt est cloné, nous allons y aller et copier le template créé précédemment dans le nouveau dépôt GitHub :

```
$ cd ansible
```
À sa base, Ansible est un outil qui peut exécuter des commandes à distance sur les hôtes de votre inventaire. L'inventaire peut être géré manuellement en créant un fichier INI où vous répertoriez tous vos hôtes et/ou IP. Il peut également être géré dynamiquement s'il peut interroger une API. Comme vous pouvez l'imaginer, Ansible est parfaitement capable de profiter de l'API AWS pour récupérer notre inventaire. Pour ce faire, nous allons télécharger un script Python à partir du référentiel officiel Ansible Git et donner les autorisations d'exécution comme suit :

```
$ curl -Lo ec2.py http://bit.ly/2v4SwE5
$ chmod +x ec2.py
```
Avant de pouvoir commencer à tester ce script Python, nous devons également lui fournir une configuration. Créez un nouveau fichier dans le même répertoire et appelez-le `ec2.ini`. Dans ce fichier, nous mettrons la configuration suivante :

```
[ec2]
regions = all
regions_exclude = us-gov-west-1,cn-north-1 destination_variable = public_dns_name vpc_destination_variable cache_path = ~/.ansible/tmp cache_max_age = 300
rds = False
```
Une fois ceci fait, vous pouvez enfin valider que l'inventaire fonctionne en exécutant le script `ec2.py` comme suit :

```
$ ./ec2.py
```
Cette commande doit renvoyer un grand JSON imbriqué des différentes ressources trouvées sur votre compte AWS. Parmi celles-ci se trouve l'adresse IP publique de l'instance EC2 que nous avons créée dans la section précédente. La dernière étape de notre démarrage consiste à configurer Ansible lui-même, de sorte qu'il sache comment obtenir l'inventaire de notre infrastructure ; quel utilisateur utiliser lorsqu'il essaie de se connecter en SSH à nos instances ; comment devenir une racine ; etc. Nous allons créer un nouveau fichier au même emplacement et l'appeler `ansible.cfg`. Son contenu doit être le suivant :

```
[defaults]
inventory = ./ec2.py
remote_user = ec2-user
become = True
become_method = sudo
become_user = root
nocows = 1
```
À ce stade, nous sommes prêts à commencer à exécuter les commandes Ansible. Ansible a quelques commandes et quelques concepts simples. Nous allons d'abord nous intéresser à la commande `ansible` et au concept de modules.

### Modules d'exécution
La commande ansible est la commande principale qui pilote l'exécution des différents modules sur les hôtes distants. Les modules sont des bibliothèques qui peuvent être exécutées directement sur des hôtes distants. Ansible est livré avec un certain nombre de modules, répertoriés sur http://bit.ly/24rU0yk. En plus des modules standard, vous pouvez également créer vos propres modules personnalisés à l'aide de Python. Ce sont les modules pour les cas d'utilisation et les technologies les plus courants. Le premier module que nous verrons est un module simple appelé ping, qui essaie de se connecter à un hôte et renvoie `pong` si l'hôte est utilisable.

> La documentation du module est également accessible à l'aide de la commande `ansible-doc`, illustrée ci-dessous :
> `$ ansible-doc <Module-Name>`
> `$ ansible-doc ping`
> Ici, ping est l'un des noms de module Ansible.

Lors de la création de notre section de terrain de jeu Ansible, nous avons créé une nouvelle instance EC2 à l'aide de CloudFormation. Jusqu'à présent, nous n'avons pas recherché l'adresse IP pour cela. En utilisant Ansible et le module `ping`, nous découvrirons ces informations. Comme mentionné précédemment, nous devons être dans le répertoire `ansible` pour exécuter la commande `ansible`. La commande est la suivante :

```
$ ansible --private-key ~/.ssh/aws-devops.pem ec2 -m ping
18.206.223.199 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```
Comme nous pouvons le voir, Ansible a pu trouver notre instance EC2 en interrogeant l'API AWS EC2. L'instance nouvellement créée est maintenant prête à être utilisée.

> Configuration de SSH : Comme Ansible s'appuie fortement sur SSH, il vaut la peine de consacrer un peu de temps à la configuration de SSH via le fichier $HOME/.ssh/config. Par exemple, vous pouvez utiliser les options suivantes pour éviter d'avoir à spécifier --private-key et -u dans l'exemple précédent :
> IdentityFile ~/.ssh/aws-devops.pem
> User ec2-user StrictHostKeyChecking no
> PasswordAuthentication no
> ForwardAgent yes
> Une fois configuré, vous n'aurez pas besoin de fournir l'option `--private-key` à Ansible.

### Exécuter des commandes arbitraires
La commande ansible peut également être utilisée pour exécuter des commandes arbitraires sur des serveurs distants. Dans l'exemple suivant, nous n'exécuterons la commande `df` que sur les hôtes correspondant à `18.206.223.*` pour leur adresse IP publique (vous devrez adapter cette commande pour qu'elle corresponde à l'adresse IP publique de votre instance, comme renvoyé dans la commande `ping` de l'exemple précédent ):

```
$ ansible --private-key ~/.ssh/aws-devops.pem '18.206.223.*' \
-a 'df -h'
18.206.223.199 | SUCCESS | rc=0 >>
Filesystem Size Used Avail Use% Mounted on
devtmpfs 484M 56K 484M 1% /dev
tmpfs 494M 0 494M 0% /dev/shm
/dev/xvda1 7.8G 1.1G 6.6G 15% /
```
Maintenant que nous avons une compréhension de base du fonctionnement d'Ansible, nous pouvons commencer à combiner les appels à différents modules Ansible à mettre en place pour l'automatisation. C'est ce qu'on appelle la création d'un **playbook**.

### Playbooks Ansible
Les playbooks sont les fichiers qui contiennent le langage de configuration, de déploiement et d'orchestration d'Ansible. En créant ces fichiers, vous définissez séquentiellement l'état de vos systèmes, de la configuration du système d'exploitation au déploiement et à la surveillance des applications. Ansible utilise YAML, qui est assez facile à lire. Pour cette raison, un moyen simple de démarrer avec Ansible, de la même manière que ce que nous avons fait avec CloudFormation, consiste à examiner quelques exemples dans le référentiel officiel Ansible GitHub, disponible sur https://github.com/ansible/ansible-examples. 

### Création d'un playbook
Ansible fournit un certain nombre de bonnes pratiques sur son site Web, disponible à l'adresse https://docs.ansible.com/ansible/latest/user_guide/index.html. Leur documentation met l'accent sur l'utilisation des rôles. Un moyen crucial d'organiser le contenu de votre playbook est la fonctionnalité d'organisation des rôles d'Ansible, qui est documentée dans le cadre de la page principale des playbooks. La création de rôles est un élément clé pour rendre le code Ansible suffisamment partageable et modulaire pour que vous puissiez réutiliser votre code dans les services et les playbooks. Pour démontrer une structure appropriée, nous allons créer un rôle que notre playbook appellera ensuite.

### Créer des rôles pour déployer et démarrer notre application Web
Nous allons utiliser des rôles pour recréer la pile Hello World que nous avons créée précédemment à l'aide du bloc `UserData` de CloudFormation. Si vous vous souvenez, la section UserData ressemblait à peu près à ceci :

```
yum install --enablerepo=epel -y nodejs
wget https://github.com/TICHANE-JM/aws-devops/blob/main/Partie2/helloworld.js -O /home/ec2-user/helloworld.js
wget https://github.com/TICHANE-JM/aws-devops/blob/main/Partie2/helloworld.conf -O /etc/init/helloworld.conf start helloworld
```
Vous remarquerez trois types d'opération différents dans le script précédent. Nous préparons d'abord le système pour exécuter notre application. Pour ce faire, dans notre exemple, nous installons simplement un package Node.js. Ensuite, nous copions les différentes ressources nécessaires au fonctionnement de l'application. Dans notre cas, il s'agit du code JavaScript et de la configuration parvenue. Enfin, nous commençons le service. Comme toujours lors de la programmation, il est important de garder le code DRY. Si le déploiement et le démarrage de notre application sont très spécifiques à notre projet Hello World, l'installation de Node.js ne l'est probablement pas. Afin de faire de l'installation de Node.js un morceau de code réutilisable, nous allons créer deux rôles : un pour installer Node.js et un pour déployer et démarrer l'application Hello World.

Par défaut, Ansible s'attend à voir les rôles dans un répertoire de `rôles` à la racine du référentiel Ansible. Donc, la première chose que nous devons faire est d'aller dans le répertoire `ansible` que nous avons créé dans la section __Création de notre référentiel Ansible__. Créez le répertoire des rôles à l'intérieur et placez-y les éléments suivants :

```
$ mkdir roles
$ cd roles
```
Nous pouvons maintenant créer nos rôles. Ansible a une commande ansible-galaxy qui peut être utilisée pour initialiser la création d'un rôle. Le premier rôle que nous examinerons est le rôle qui installera Node.js :
```
$ ansible-galaxy init nodejs
- nodejs was created successfully
```

> Comme mentionné brièvement, Ansible, comme la plupart des autres systèmes de gestion de configuration, dispose d'une solide communauté de support qui partage des rôles en ligne via https://galaxy.ansible.com/. En plus d'utiliser la commande `ansible-galaxy` pour créer le squelette de nouveaux rôles, vous pouvez également utiliser `ansible-galaxy` pour importer et installer des rôles pris en charge par la communauté.

Cela crée un répertoire `nodejs` et un certain nombre de sous-répertoires qui nous permettront de structurer les différentes sections de notre rôle. Nous entrerons dans ce répertoire avec la commande suivante :

```
$ cd nodejs
```
Le répertoire le plus important à l'intérieur du répertoire nodejs est celui appelé `tasks`. Lorsqu'Ansible exécute un playbook, il exécute le code présent dans le fichier `tasks/main.yml`. Ouvrez le fichier avec votre éditeur de texte préféré.

Lorsque vous ouvrez pour la première fois `tasks/main.yml`, vous verrez ce qui suit :

```
---
# tasks file for nodejs
```
L'objectif du rôle nodejs est d'installer Node.js et `npm`. Pour ce faire, nous procéderons de la même manière que nous l'avons fait avec le script UserData et utiliserons la commande `yum` pour effectuer ces tâches.

Lors de l'écriture d'une tâche dans Ansible, vous séquencez un certain nombre d'appels vers différents modules Ansible. Le premier module que nous allons examiner est un wrapper autour de la commande yum. La documentation à ce sujet est disponible sur http://bit.ly/28joDLe.
Cela nous permettra d'installer nos packages. Nous allons également introduire le concept de boucles. Puisque nous avons deux packages à installer, nous voudrons appeler le module yum deux fois. Nous utiliserons les `with_items` de l'opérateur. Tous les codes Ansible sont écrits en YAML, ce qui est très facile à démarrer et à utiliser. Après les trois tirets et commentaires initiaux, qui indiquent le début d'un fichier YAML, nous allons appeler le module `yum` afin d'installer nos packages :

```
---
# tasks file for nodejs
name: Installing node and npm yum:
name: "{{ item }}" enablerepo: epel state: installed
with_items:
nodejs
npm
```
Chaque fois qu'Ansible exécute ce playbook, il examine les packages installés sur le système. S'il ne trouve pas les packages `nodejs` ou `npm`, il les installera.

Your file should look like the example available at https://github.com/yogeshraheja/aws-devops/blob/master/Partie3/ansible/roles/nodejs/tasks/main.yml. This

Ce premier rôle est terminé. Pour les besoins , nous gardons le rôle très simple, mais vous pouvez imaginer comment, dans un environnement plus de type production, vous pourriez avoir un rôle qui installera des versions spécifiques de Node.js et npm, récupérera les binaires directement depuis https://nodejs.org/en/, et peut-être même installer des dépendances spécifiques. Notre prochain rôle sera dédié au déploiement et au démarrage de l'application Hello World que nous avons construite précédemment. Nous allons remonter d'un répertoire dans le répertoire des `rôles` et appeler `ansible-galaxy` une fois de plus :

```
$ cd ..
$ ansible-galaxy init helloworld
- helloworld was created successfully
```
Comme précédemment, nous allons maintenant entrer dans le répertoire helloworld nouvellement créé comme suit :
```
$ cd helloworld
```





