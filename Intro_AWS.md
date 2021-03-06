# EFFICACE AVEC AWS

Nous allons voir comment implémenter la livraison continue et l'intégration dans l'environnement AWS.

## Les différentes couches d'un Cloud
Le cloud computing est souvent décomposé en trois types de services différents,
généralement appelés modèles de service, comme suit :

* **Infrastructure en tant que service (IaaS) :**  c'est le bloc de construction fondamental,
au-dessus duquel tout ce qui concerne le cloud est construit. IaaS est généralement une
ressource informatique dans un environnement virtualisé. Cela offre une combinaison
de puissance de traitement, de mémoire, de stockage et de réseau. La plus commune des entités IaaS que vous trouverez sont les machines virtuelles (VM) et les équipements réseau, mais aussi les équilibreurs de charge ou les interfaces Ethernet virtuelles, mais aussi le stockage, tels que les périphériques de bloc. Cette couche est très proche du matériel, et offre toute la flexibilité que vous obtiendriez lors du déploiement de votre logiciel en dehors d'un cloud. Si vous avez de l'expérience avec les centres de données, cela s'appliquera également principalement à cette couche.
* **Plate-forme en tant que service (PaaS) :**  cette couche est l'endroit où les choses commencent à devenir vraiment intéressantes avec le cloud. Lors de la création d'une application, vous aurez probablement besoin d'un certain nombre de composants communs, tels qu'un magasin de données et une file d'attente. La couche PaaS fournit un certain nombre d'applications prêtes à l'emploi, pour vous aider à créer vos propres services sans vous soucier de l'administration et de l'exploitation de services tiers, tels que des serveurs de base de données.
* **Logiciel en tant que service (SaaS) :** cette couche est la cerise sur le gâteau. Semblable à la couche PaaS, vous avez accès à des services gérés, mais cette fois, ces services sont une solution complète dédiée à certains objectifs, tels que des outils de gestion ou de surveillance.

On va essayer de couvrir un bon nombre de services de type **PaaS** et **SaaS** . Lors de la création d'une application, s'appuyer sur ces services fait une grande différence par rapport à l'environnement plus traditionnel en dehors du cloud. Un autre élément clé du succès lors du déploiement ou de la migration vers une nouvelle infrastructure est l'adoption d'un état d'esprit DevOps.

## Déploiement dans AWS

AWS est à la pointe des fournisseurs de cloud. Lancé en 2006, avec SQS et EC2, Amazon est rapidement devenu le plus grand fournisseur d'IaaS. Ils ont la plus grande infrastructure et écosystème, avec des ajouts constants de nouvelles fonctionnalités et services. Ils ont dépassé le million de clients actifs. Au cours des dernières années, ils ont réussi à changer les mentalités sur le cloud, et le déploiement de nouveaux services est désormais la norme. L'utilisation des outils et services gérés d'AWS est un moyen d'améliorer considérablement votre productivité et de garder votre équipe allégée. Amazon écoute en permanence les commentaires de ses clients et observe les tendances du marché. Par conséquent, alors que le mouvement DevOps commençait à s'établir, Amazon a publié un certain nombre de nouveaux services adaptés à la mise en œuvre de certaines meilleures pratiques DevOps. On va voir comment ces services sont en synergie avec la culture DevOps.

## Comment profiter de l'écosystème AWS ?

Les services Amazon sont comme des pièces de Lego. Si vous pouvez imaginer votre produit final, vous pouvez explorer les différents services et commencer à les combiner, afin de créer la pile nécessaire pour créer rapidement et efficacement votre produit. Bien sûr, dans ce cas, le __si__ est un __gros si__ , et contrairement à Lego, comprendre ce que chaque pièce peut faire est beaucoup moins visuel et coloré. C'est pourquoi on va essayer d'être très pratique ; tout au long, nous allons prendre une application Web et la déployer comme si c'était notre produit principal. Vous verrez comment faire évoluer l'infrastructure qui la supporte, afin que des millions de personnes puissent l'utiliser, et aussi pour la rendre plus sécurisée. Et, bien sûr, nous le ferons en suivant les meilleures pratiques DevOps. En effectuant cet exercice, vous apprendrez comment AWS fournit un certain nombre de services et de systèmes gérés pour effectuer un certain nombre de tâches courantes, telles que l'informatique, la mise en réseau, l'équilibrage de charge, le stockage de données, la surveillance, la gestion par programme de l'infrastructure et du déploiement, la mise en cache et faire la queue.

## Comment AWS est-il en synergie avec une culture DevOps ?

Avoir une culture DevOps consiste à repenser la façon dont les équipes d'ingénierie travaillent ensemble, en cassant les silos de développement et d'exploitation et en apportant un nouvel ensemble d'outils, afin de mettre en œuvre les meilleures pratiques. AWS aide à accomplir cela de différentes manières. Pour certains développeurs, le monde des opérations peut être effrayant et déroutant, mais si vous voulez une meilleure coopération entre les ingénieurs, il est important d'exposer tous les aspects de l'exécution d'un service à l'ensemble de l'organisation d'ingénierie.

En tant qu'ingénieur d'exploitation, vous ne pouvez pas avoir une mentalité de gardien envers les développeurs. Au lieu de cela, il est préférable de les mettre à l'aise en accédant à la production et en travaillant sur la manière différente de démarrer avec cela dans la console AWS, comme suit : les composants de la plate-forme. Un bon moyen de démarrer avec ceci est dans la console AWS, comme suit :

![image](https://user-images.githubusercontent.com/107214400/176466969-c3811285-f3c8-426c-9e6a-b9c8e8d126e7.png)

Bien qu'un peu accablant, c'est toujours une bien meilleure expérience pour les personnes qui ne sont pas familiarisées avec la navigation sur cette interface Web, plutôt que de se référer à une documentation constamment obsolète, en utilisant SSH et des lectures aléatoires afin de découvrir la topologie et la configuration du service. Bien sûr, à mesure que votre expertise grandit et que votre application devient plus complexe, la nécessité de l'exploiter plus rapidement augmente et l'interface Web commence à montrer quelques faiblesses. Pour contourner ce problème, AWS propose une alternative très conviviale pour DevOps. Une API est accessible via un outil de ligne de commande et un certain nombre de SDK (y compris Java, JavaScript, Python, .NET, PHP, Ruby Go et C++). Ces SDK vous permettent d'administrer et d'utiliser les services gérés. Enfin, comme vous l'avez vu dans la section précédente, AWS propose un certain nombre de services qui correspondent aux méthodologies DevOps et nous permettront finalement de mettre en œuvre des solutions complexes en un rien de temps.

Certains des principaux services que vous utiliserez, au niveau informatique, sont Amazon **Elastic Compute Cloud (EC2)**, le service permettant de créer des serveurs virtuels. Plus tard, lorsque vous commencerez à étudier comment faire évoluer l'infrastructure, vous découvrirez Amazon EC2 Auto Scaling, un service qui vous permet de faire évoluer des pools sur des instances EC2, afin de gérer les pics de trafic et les pannes d'hôte. Vous explorerez également le concept de conteneurs avec Docker, via Amazon **Elastic Container Service (ECS)**. En plus de cela, vous créerez et déploierez votre application à l'aide d'AWS Elastic Beanstalk, avec lequel vous conservez un contrôle total sur les ressources AWS qui alimentent votre application ; vous pouvez accéder aux ressources sous-jacentes à tout moment. Enfin, vous créerez des fonctions sans serveur via AWS Lambda, pour exécuter du code personnalisé sans avoir à l'héberger sur nos serveurs. Pour mettre en place votre système d'intégration continue et de déploiement continu, vous vous appuierez sur les quatre services suivants :

* **AWS Simple Storage Service (S3) :**  C'est le service de magasin d'objets qui nous permettra de stocker nos artefacts
* **AWS CodeBuild :** Cela nous permettra de tester notre code
* **AWS CodeDeploy :** Cela nous permettra de déployer des artefacts sur nos instances EC2
* **AWS CodePipeline :** Cela nous permettra d'orchestrer la manière dont notre code est construit, testé et déployé dans tous les environnements

Pour tout surveiller et mesurer, vous vous fierez à **AWS CloudWatch**, et plus tard, à **ElasticSearch/Kibana**, pour collecter, indexer et visualiser les métriques et les journaux. Pour diffuser certaines de nos données vers ces services, vous comptez sur **AWS Kinesis**. Pour envoyer des alertes par e-mail et SMS, vous utiliserez le service **Amazon SNS**. Pour la gestion de l'infrastructure, vous vous fierez fortement à **AWS CloudFormation**, qui offre la possibilité de créer des modèles d'infrastructures. En fin de compte, alors que vous explorez les moyens de mieux sécuriser notre infrastructure, vous rencontrerez **Amazon Inspector** et **AWS Trusted Advisor** , et vous explorerez plus en détail les services IAM et VPC.

## Déploiement de votre première application Web

Dans le partie précédente, nous avons couvert une introduction générale au cloud, ses avantages et ce que signifie avoir une philosophie DevOps. AWS propose un certain nombre de services qui sont tous facilement accessibles via l'interface Web, l'interface de ligne de commande, divers SDK et les API. Dans ce chapitre, nous tirerons parti de l'interface Web et de l'interface de ligne de commande pour créer et configurer notre compte et créer un serveur Web pour héberger une simple application Hello World, le tout en quelques minutes.

Dans cette partie, nous aborderons les sujets suivants :
* Création et configuration de votre compte
* Faire tourner votre premier serveur Web

### Les pré-requis techniques

Les technologies et services utilisés sont les suivants :
* AWS Management Console
* AWS compute services
* AWS IAM
* AWS CLI setup
* JavaScript pour l'application Web
* GitHub pour du code prêt à l'emploi

Le liens GitHub pour le code est le suivant :
[https://github.com/TICHANE-JM/aws-devops/tree/main/Partie2]https://github.com/TICHANE-JM/aws-devops/tree/main/Partie2)

### Création et configuration de votre compte

Si vous n'êtes pas encore inscrit à AWS, il est temps de le faire.

#### S'enregistrer
Cette étape est, bien sûr, assez simple et explicite. Pour vous inscrire (si vous ne l'avez pas encore fait), ouvrez [https://portal.aws.amazon.com](https://portal.aws.amazon.com) dans votre navigateur, cliquez sur le bouton Créer un nouveau compte AWS et suivez les étapes. Vous aurez besoin d'une adresse e-mail et de vos informations de carte de crédit.

Amazon exécute un programme de niveau gratuit pour les nouveaux utilisateurs. Ceci est conçu pour vous aider à découvrir les services AWS gratuitement. Amazon offre un crédit gratuit sur la plupart des services. Il est probable qu'avec le temps, l'offre changera, donc ce livre ne couvrira pas les détails de cette offre, mais les détails sont disponibles sur [https://aws.amazon.com/free/](https://aws.amazon.com/free/).

Une fois que vous avez terminé le processus d'inscription, vous serez sur la page d'accueil d'AWS Management Console. Cet écran peut être un peu écrasant car Amazon dispose maintenant de beaucoup de services, mais vous vous y habituerez rapidement.

Le compte que vous venez de créer s'appelle un compte **root**. Ce compte aura toujours un accès complet à toutes les ressources. Pour cette raison, assurez-vous de conserver votre mot de passe dans un endroit sûr. La bonne pratique est d'utiliser le compte root uniquement pour créer l'utilisateur initial via le service IAM que nous découvrirons prochainement. De plus, il est fortement recommandé de passer à l'**authentification multi-facteurs (MFA)** et d'utiliser le service d'identité **IAM** - pour gérer les comptes d'utilisateurs, choisissez donc un mot de passe relativement complexe.

### Activer MFA sur le compte root

Afin d'éviter tout type de problème, la première chose que nous devons faire une fois que nous nous sommes inscrits est d'activer MFA. Au cas où vous n'auriez jamais vu ou entendu parler de cela auparavant, MFA est un système de sécurité qui nécessite plusieurs méthodes d'authentification à partir de catégories d'informations d'identification indépendantes. Ceux-ci servent à vérifier l'identité de l'utilisateur afin de se connecter. En pratique, une fois activé, vous aurez besoin du mot de passe précédemment défini lors de votre inscription pour vous connecter. Cependant, vous aurez également besoin d'un autre code fourni par une source différente. Cette deuxième source peut être fournie via un dispositif physique tel que SafeNet IDProve, qui est disponible sur [http://amzn.to/2u4K1rR](http://amzn.to/2u4K1rR), via un SMS sur votre téléphone ou via une application installée sur votre smartphone. Nous utiliserons la troisième option, une application installée sur votre smartphone, qui est entièrement gratuite :

1. Accédez à votre App Store, Google Play Store ou App Marketplace et installez une application appelée **Google Authenticator** (ou tout autre équivalent, comme **Authy**).
2. Dans AWS Management Console, ouvrez la page Mes informations d'identification de sécurité dans le coin supérieur droit :

![image](https://user-images.githubusercontent.com/107214400/176476398-d1606b51-2649-45a7-ac4b-369b1f79ea8f.png)
3. Si vous êtes invité à créer et à utiliser AWS **Identity and Access Management (IAM)**, les utilisateurs disposant d'autorisations limitées, cliquez sur le bouton Continuer vers les informations d'identification de sécurité. Nous explorerons le système IAM plus loin, __Traiter votre infrastructure comme du code__. Développez la section Authentification multifacteur (MFA) sur la page.
4. Choisissez MFA virtuel et suivez les instructions pour synchroniser l'authentification Google avec votre compte racine (notez que l'option de numérisation du code QR est la plus simple pour coupler l'appareil).

À partir de ce moment, vous aurez besoin de votre mot de passe et du jeton affiché sur l'application MFA pour vous connecter en tant que root dans la console AWS.

Comme nous l'avons vu précédemment, l'utilisation du compte root doit être limitée au strict minimum. Ainsi, pour créer des serveurs virtuels, configurer des services, etc., nous nous appuierons sur le service IAM qui nous permettra d'avoir un contrôle granulaire sur les autorisations pour chaque utilisateur.

## Créer un nouvel utilisateur dans IAM

Dans cette section, nous allons créer et configurer des comptes pour différentes personnes qui ont besoin d'accéder à AWS. Pour l'instant, nous allons garder les choses simples et ne créer un compte que pour nous-mêmes, comme suit :

1. Accédez au menu IAM dans la console AWS (https://console.aws.amazon.com/iam/) ou accédez à la liste déroulante Services dans le coin supérieur gauche de la page de la console AWS et recherchez **IAM** :
![image](https://user-images.githubusercontent.com/107214400/176477646-39edbd21-7a9e-48e3-82b2-365b1e536a86.png)
2. Choisissez l'option Utilisateurs dans le volet de navigation.

![image](https://user-images.githubusercontent.com/107214400/176478471-252b78cc-6b38-4e32-bfa3-af6489d7f62a.png)

3. Créez un nouvel utilisateur en cliquant sur le bouton Ajouter un utilisateur et assurez-vous de cocher l'option Accès par programme pour générer un ID de clé d'accès et une clé d'accès secrète pour l'utilisateur.
4. Sélectionnez les options par défaut pour l'instant et créez un utilisateur. N'oubliez pas de télécharger les identifiants.
5. De retour dans le menu Utilisateurs, cliquez sur votre nom d'utilisateur pour accéder à la page de détails.
6. Dans l'onglet Autorisations, cliquez sur le bouton Ajouter des autorisations et sélectionnez l'option Attacher directement les politiques existantes. Cliquez sur AdministratorAccess pour fournir un accès complet aux services et ressources AWS à notre utilisateur nouvellement créé.
7. Cochez la case à côté de l'option AdministratorAccess pour fournir un accès complet aux services et ressources AWS à notre utilisateur nouvellement créé. Vous vous retrouvez avec un écran qui ressemble à ceci :

![image](https://user-images.githubusercontent.com/107214400/176478925-2e88392f-0347-4d43-be7e-3ecdb404632e.png)

La dernière chose que nous devons faire est d'ajouter un mot de passe et d'activer MFA pour ce compte. Cela peut être fait comme suit:

8. Cliquez sur l'onglet Identifiants de sécurité.
9. Cliquez maintenant sur l'option Mot de passe de la console et activez le mot de passe pour l'utilisateur nouvellement créé. Définissez le mot de passe de votre choix et cliquez sur le bouton Appliquer.
10. Une fois que vous avez terminé d'ajouter un mot de passe, cliquez sur l'option Périphérique MFA attribué.
11. Sélectionnez l'option Un périphérique MFA virtuel et suivez les instructions restantes afin d'activer MFA dans votre compte nouvellement créé. Vous recevrez un message indiquant que l'appareil MFA a été associé avec succès à votre compte, comme illustré dans la capture d'écran suivante :

![image](https://user-images.githubusercontent.com/107214400/176479489-4957238b-d1d6-4644-ac08-e2ae1d0a3249.png)

12. À ce stade, vous êtes prêt à commencer à utiliser le compte d'utilisateur nouvellement créé. La chose importante à noter ici est que la connexion avec un compte utilisateur IAM est différente du compte racine. La principale différence est que vous vous connectez à l'aide d'une URL différente.
13. Accédez à [https://console.aws.amazon.com/iam/home#home](https://console.aws.amazon.com/iam/home#home) ou cliquez sur le Tableau de bord dans le menu IAM.
14. Vous verrez votre URL de connexion unique sous le lien de connexion des utilisateurs IAM. N'hésitez pas à personnaliser également le lien. Enregistrez cette nouvelle URL dans vos favoris et, à partir de maintenant, utilisez ce lien pour vous connecter à la console AWS.
15. Déconnectez-vous du compte root.
16. Reconnectez-vous, mais cette fois utilisez votre compte utilisateur IAM sur **https://AWS-account-ID** ou **alias.signin.aws.amazon.com/console**.

La prochaine étape de la configuration de notre compte consiste à configurer nos ordinateurs pour interagir avec AWS à l'aide de l'interface de ligne de commande.

## Installation et configuration de l'interface de ligne de commande (CLI)

L'utilisation de l'interface Web d'Amazon est généralement un excellent moyen d'explorer de nouveaux services. Le problème est que lorsque vous voulez aller vite, créer des étapes plus reproductibles ou créer une bonne documentation, avoir des commandes simples à exécuter devient plus efficace. Amazon fournit une interface de ligne de commande excellente et facile à utiliser. L'outil est écrit en Python et est donc multiplateforme (Windows, Mac et Linux).

Nous installerons l'outil sur notre ordinateur portable/de bureau afin de pouvoir interagir avec AWS à l'aide des commandes bash. Linux et macOS X sont livrés nativement avec bash. Si vous utilisez l'un de ces systèmes d'exploitation, vous pouvez ignorer la section suivante. Sous Windows, nous devons d'abord installer une fonctionnalité appelée **Windows Subsystem for Linux (WSL)**, qui nous permettra d'exécuter des commandes Bash très similaires à celles que vous obtenez sur Ubuntu Linux.

### Installation de WSL (Windows uniquement)

De nos jours, Linux et macOS X sont parmi les systèmes d'exploitation les plus utilisés par les développeurs. Windows a récemment lancé un partenariat avec Canonical, la société à l'origine de l'une des distributions Linux les plus populaires, de la prise en charge de Bash et de la plupart des packages Linux courants. En installant cet outil sur Windows, nous pourrons interagir plus efficacement avec nos serveurs, qui fonctionneront également sous Linux :

1. Cliquez sur le bouton Démarrer et recherchez les __paramètres__ , puis ouvrez l'application Paramètres :
2. Cela vous mènera à la fenêtre suivante, où vous devez rechercher les __paramètres de Windows Update__. Ouvrez le menu des paramètres de Windows Update :

![image](https://user-images.githubusercontent.com/107214400/176481753-f8dd3720-1bba-4920-af4e-71dc94542b17.png)

3. Dans le menu de gauche des paramètres de Windows Update, cliquez sur le sous-menu Pour les développeurs et activez l'option Mode développeur.
4. Une fois votre mode développeur activé, recherchez dans la barre de recherche du menu de gauche l'option __Panneau de configuration__ :

![image](https://user-images.githubusercontent.com/107214400/176482359-bf748560-4e16-4ee3-bd7a-1e2cb57f9e23.png)

5. Dans le tableau de bord du Panneau de configuration, sélectionnez l'option Catégorie dans le menu déroulant Afficher par, puis cliquez sur l'option Programmes. Ensuite, sous Programmes et fonctionnalités, cliquez sur l'option Activer ou désactiver les fonctionnalités Windows :

![image](https://user-images.githubusercontent.com/107214400/176482567-36e95c5a-20f8-4cb9-894d-f547a31c2b55.png)

![image](https://user-images.githubusercontent.com/107214400/176482837-2cd58f8a-7ee1-47b7-adbb-c62a96aea9f2.png)

6. Dans ce menu, trouvez la fonctionnalité appelée Windows Subsystem for Linux (Beta), et cliquez sur le bouton OK :

![image](https://user-images.githubusercontent.com/107214400/176483166-bbbdf6df-6702-4dc3-a847-e59ddcb3fae4.png)

Cela installera la fonctionnalité et vous demandera de redémarrer votre ordinateur.

7. Une fois de retour dans Windows, cliquez à nouveau sur le bouton Démarrer, recherchez __bash__ et démarrez le Bash sur Ubuntu sur l'application Windows 
8. Après quelques étapes d'initialisation, vous pourrez utiliser Bash sous Windows de la même manière que vous le feriez sous Linux.

À partir de là, allez dans votre Windows Store et installez Ubuntu 22.04 LTS et cliquez sur obtenir.


## Installation du package AWS CLI

L'utilitaire AWS CLI est écrit en Python. Bien qu'il existe plusieurs façons de l'installer, nous utiliserons **PyPA**, le gestionnaire de packages Python, pour installer cet outil.

Pour installer PyPA, selon votre système d'exploitation, vous devrez exécuter les commandes suivantes :

![image](https://user-images.githubusercontent.com/107214400/176622136-6c5cba69-359e-40f3-bc1e-4b7846a6e6c3.png)

Une fois installée lancez l'installation en cliquant sur ouvrir

![image](https://user-images.githubusercontent.com/107214400/176622341-a5a4fb50-9f51-4780-965d-e79b9c8947ed.png)

Suivez les étapes de l'installation

![image](https://user-images.githubusercontent.com/107214400/176622505-249e40f9-fc09-4479-a717-9e0252571549.png)

![image](https://user-images.githubusercontent.com/107214400/176622735-8245b634-1ab3-4a42-b81b-f3e2ad5e8e05.png)

![image](https://user-images.githubusercontent.com/107214400/176622860-1bfea026-d02e-420a-b517-93c0fdd42cd7.png)

![image](https://user-images.githubusercontent.com/107214400/176623046-17262301-1603-4ef2-9203-a2ee0a2ae072.png)

![image](https://user-images.githubusercontent.com/107214400/176623349-bcbb7dad-076c-4386-8d39-5936a178fdc2.png)

Cliquez sur finir et une fenêtre apparaît

![image](https://user-images.githubusercontent.com/107214400/176623547-d30a794a-391b-41b0-a3b2-75b824555591.png)

* Sous Windows :
```
$ sudo apt install python3-pip
```
* Sous macOS X
```
$ sudo east_install pip
```
* Sur les distributions Linux basées sur Debian :
```
$ sudo apt-get install python-pip python-dev build-essential
```
* Sur les distributions Linux basées sur Red Hat/CentOS :
```
$ sudo yum -y install python-pip
```
Une fois PyPA installé, vous aurez accès à la commande `pip`.

Enfin, pour installer l'AWS CLI  il vous suffit d'exécuter la commande suivante :
```
$ sudo apt install awscli
```

## Configuration de l'AWS CLI

Pour ce faire, vous devrez extraire l'ID de clé d'accès AWS et la clé d'accès secrète du fichier téléchargé à l'étape 4 de la section Création d'un nouvel utilisateur dans IAM :

```
$ more credentials.csv
User Name,Access Key Id,Secret Access Key "totocompteaws", AKIAII55DTLEV3X4ETAQ, mL2dEC8/
```
Nous allons exécuter la commande suivante pour configurer notre compte AWS :

```
$ aws configure
AWS Access Key ID [None]: AKIAII55DTLEV3X4ETAQ
AWS Secret Access Key [None]: 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
Default region name [None]: us-east-1
Default output format [None]:
```

À ce stade, nous sommes prêts à commencer à utiliser la CLI. On peut rapidement vérifier que tout fonctionne en listant les comptes utilisateurs, comme suit :

```
$ aws iam list-users
{
    "Users": [
        {
              "UserName": "totocompte aws",
              "PasswordLastUsed": "2018-08-07T09:57:53Z",
              "CreateDate": "2018-08-07T04:56:03Z",
              "UserId": "AIDAIN22VCQLK43UVWLMK",
              "Path": "/",
              "Arn": "arn:aws:iam::094507990803:user/totocompteaws"
        }
     ]
}
```
> AWS aws-shell
> Amazon dispose d'un deuxième outil CLI appelé `aws-shell`. Cet outil est plus interactif que la commande `awscli` classique, car il offre une auto-complétion prête à l'emploi et une vue en écran partagé qui vous permet d'accéder à la documentation lorsque vous tapez vos commandes. Si vous êtes un nouvel utilisateur AWS, essayez-le (`pip install aws-shell`).

## Création de notre premier serveur Web

Maintenant que notre environnement est configuré, nous sommes enfin prêts à lancer notre première instance EC2. Il y a plusieurs façons de le faire. Puisque nous venons d'installer et de configurer `awscli` et que nous voulons voir des moyens efficaces de gérer les infrastructures, nous allons montrer comment procéder à l'aide de la CLI.

Le lancement d'un serveur virtuel nécessite d'avoir un certain nombre d'informations en amont. Nous utiliserons la commande `aws ec2 run-instances`, mais nous devons lui fournir les éléments suivants :
* Un identifiant AMI
* Un type d'instance
* A security group
* Une paire de clés SSH

## Amazon Machine Images (AMI)

Une AMI est un package qui contient, entre autres, le système de fichiers racine avec le système d'exploitation (par exemple, Linux, UNIX ou Windows) ainsi que des logiciels supplémentaires nécessaires au démarrage du système. Pour trouver l'AMI appropriée, nous utiliserons la commande `aws ec2 describe-images`. Par défaut, la commande `describe-images` répertorie toutes les AMI publiques disponibles, soit bien plus de 3 millions à l'heure actuelle. Pour tirer le meilleur parti de cette commande, il est important de la combiner avec l'option de filtre pour n'inclure que l'AMI que nous souhaitons utiliser. Dans notre cas, nous souhaitons utiliser les éléments suivants pour filtrer nos AMI :

* Nous voulons que le nom soit Amazon Linux AMI, qui désigne la distribution Linux officiellement prise en charge par AWS. Amazon Linux est basé sur Red Hat/CentOS mais inclut quelques packages supplémentaires pour faciliter l'intégration avec d'autres services AWS. Vous pouvez en savoir plus sur AWS Linux sur http://amzn.to/2uFT13F.
* Nous voulons utiliser la version `x84_64` bits de Linux pour correspondre à l'architecture que nous utiliserons.
* Le type de virtualisation doit être HVM, qui signifie machine virtuelle matérielle. Il s'agit du type de virtualisation le plus récent et le plus performant.
* Nous voulons un support GP2, qui nous permettra d'utiliser la dernière génération d'instances qui ne sont pas livrées avec le magasin d'instances, ce qui signifie que les serveurs qui alimentent nos instances seront différents des serveurs qui stockent nos données.

De plus, nous allons trier la sortie par date et ne regarder que l'AMI la plus récemment publiée :
```
$ aws ec2 describe-images --filters "Name=description,Values=Amazon Linux AMI * x86_64 HVM
```

Le résultat de l'exécution de la commande précédente peut être affiché comme suit :
![image](https://user-images.githubusercontent.com/107214400/176629765-82f9303b-8beb-4e2a-a0d3-8a509738cbea.png)

Comme vous pouvez le constater, à l'heure actuelle, l'ID AMI le plus récent est `ami-cfe4b2b0`. Cela peut différer au moment où vous exécutez la même commande, car les fournisseurs Amazon inclus mettent régulièrement à jour leur système d'exploitation.

> Lorsque vous utilisez l'option `aws cli --query`, la sortie peut être très conséquente pour certaines commandes. En reprenant l'exemple précédent, si nous ne nous soucions que d'un sous-ensemble d'informations, nous pouvons compléter les commandes avec l'option `--query` pour filtrer uniquement les informations que nous voulons. Cette option utilise le langage de requête JMESPath.

## Types d'instances
Dans cette section, nous sélectionnerons le matériel virtuel à utiliser pour notre serveur virtuel. AWS fournit un certain nombre d'options mieux décrites dans leur documentation à l'adresse https://aws.amazon.com/ec2/instance-types/. Nous aborderons les types d'instances plus en détail dans la partie, __Faire évoluer votre infrastructure__.

1. Pour l'instant, nous allons sélectionner le type d'instance `t2.micro` car il est éligible au niveau d'utilisation gratuite d'AWS.

```
$ aws ec2 describe-vpcs 
{
    "Vpcs": [
    {
          "VpcId": "vpc-4cddce2a", "InstanceTenancy": "default", "CidrBlockAssociationSet": [
          {
              "AssociationId": "vpc-cidr-assoc-3c313154", "CidrBlock": "172.31.0.0/16", "CidrBlockState": 
                  {
                      "State": "associated"
                  }
          }
          ],
          "State": "available", "DhcpOptionsId": "dopt-c0be5fa6", "CidrBlock": "172.31.0.0/16", "IsDefault": true
    }
    ]
 }     
 ```
 2. Maintenant que nous connaissons l'ID du VPC (le vôtre sera différent), nous pouvons créer notre nouveau groupe de sécurité, comme suit :

```
$ aws ec2 create-security-group \
        --group-name HelloWorld \
        --description "Hello World Demo" \
        --vpc-id vpc-4cddce2a
    {
        "GroupId": "sg-01864b4c"
    }  
```
3. Par défaut, les groupes de sécurité autorisent tout le trafic sortant de l'instance. Nous avons juste besoin d'ouvrir SSH (tcp/22) et tcp/3000 pour le trafic entrant. Nous devons ensuite saisir les éléments suivants :

```
$ aws ec2 authorize-security-group-ingress \
         --group-name HelloWorld \
         --protocol tcp \
         --port 22 \
         --cidr 0.0.0.0/0
      $ aws ec2 authorize-security-group-ingress \
         --group-name HelloWorld \
         --protocol tcp \
         --port 3000 \
         --cidr 0.0.0.0/0
 ```
 
 4. Nous pouvons maintenant vérifier la modification apportée à l'aide du code suivant, car les commandes précédentes ne sont pas détaillées :

```
$ aws ec2 describe-security-groups \
        --group-names HelloWorld \
        --output text
    SECURITYGROUPS Hello World Demo sg-01864b4c HelloWorld
    094507990803 vpc-4cddce2a
    IPPERMISSIONS 22 tcp 22
    IPRANGES 0.0.0.0/0
    IPPERMISSIONS 3000 tcp 3000
    IPRANGES 0.0.0.0/0
    IPPERMISSIONSEGRESS -1
    IPRANGES 0.0.0.0/0
 ```
 Comme prévu, nous avons ouvert le trafic vers les ports appropriés. Si vous savez comment trouver votre adresse IP publique, vous pouvez améliorer la règle SSH en remplaçant 0.0.0.0/0 par votre adresse IP/32 afin que vous seul puissiez essayer de vous connecter en SSH à cette instance EC2.
 
**Utilisation de l'option aws cli --output**
Par défaut, la plupart des commandes renverront une sortie JSON. AWS a un certain nombre d'options disponibles dans le monde. Vous pouvez les voir un peu utilisés dans ce chapitre. La première option est --output [json | texte | table]:

![image](https://user-images.githubusercontent.com/107214400/176632938-dd242f75-6731-45e3-b469-642964634c83.png)

## Génération de vos clés SSH
Par défaut, Amazon EC2 utilise des paires de clés SSH pour vous donner un accès SSH à vos instances EC2. Vous pouvez soit générer une paire de clés dans EC2 et télécharger la clé privée, soit générer une clé vous-même à l'aide d'un outil tiers tel que OpenSSL, en important la clé publique dans EC2. Nous utiliserons la première méthode pour créer des clés EC2 SSH.

Ici, assurez-vous de définir des autorisations en lecture seule sur votre fichier de clé privée (`.pem`) nouvellement généré :

```
$ aws ec2 create-key-pair --key-name EffectiveDevOpsAWS --query
    'KeyMaterial' --output text > ~/.ssh/EffectiveDevOpsAWS.pem
    
$ aws ec2 describe-key-pairs --key-name EffectiveDevOpsAWS
{
    "KeyPairs": [
        {
            "KeyName": "EffectiveDevOpsAWS",
            "KeyFingerprint":
        "27:83:5d:9b:4c:88:f6:15:c7:39:df:23:4f:29:21:3b:3d:49:e6:af"
        }
    ]
}

$ cat ~/.ssh/EffectiveDevOpsAWS.pem
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAiZLtUMnO2OKnHvTJOiIP26fThdsU0YRdlKI60in85x9aFZXSrZsKwOhWPpMtnUMJKeGvVQut+gJ1I1PNNjPqS2Dy60jH55hntUhr/gYEAoOFjJ3KjREYpT1jnROEM2cKiVrdefJmNTel+RyF2IGmgg+1Hrjqf/OQSH8QwVmWK9SosfIwVX4X8gDqcZzDS1JXGEjIB7IipGYjiysP1D74myTF93u/-----END RSA PRIVATE KEY-----

$ chmod 400 ~/.ssh/EffectiveDevOpsAWS.pem

$ aws ec2 run-instances --instance-type t2.micro --key-name aws-devops -- security-group-id sg-01864b4c --image-id ami-cfe4b2b0
    {
        "Instances": [
        {
            "Monitoring": {
            "State": "disabled"
            },
            "PublicDnsName": "",
            "StateReason": {
            "Message": "pending",
            "Code": "pending"
            },
            "State": {
            "Code": 0,
            "Name": "pending"
            },
            "EbsOptimized": false,
            "LaunchTime": "2018-08-08T06:38:43.000Z",
            "PrivateIpAddress": "172.31.22.52",
            "ProductCodes": [],
            "VpcId": "vpc-4cddce2a",
            "CpuOptions": {
            "CoreCount": 1,
            "ThreadsPerCore": 1
            },
            "StateTransitionReason": "",
            "InstanceId": "i-057e8deb1a4c3f35d",
            "ImageId": "ami-cfe4b2b0",
            "PrivateDnsName": "ip-172-31-22-52.ec2.internal",
            "KeyName":"aws-devops",
            "SecurityGroups": [
            {
            "GroupName": "HelloWorld",
            "GroupId": "sg-01864b4c"
            }
            ],
            "ClientToken": "", "SubnetId": "subnet-6fdd7927", "InstanceType": "t2.micro", "NetworkInterfaces": 
            [
            "Status": "in-use", "MacAddress": "0a:d0:b9:db:7b:38", "SourceDestCheck": true, "VpcId": "vpc-4cddce2a", "Description": "", "NetworkInterfaceId": "eni-001aaa6b5c7f92b9f", "PrivateIpAddresses": [
            "PrivateDnsName": "ip-172-31-22-52.ec2.internal", "Primary": true, "PrivateIpAddress": "172.31.22.52"
            }
            ],
            "PrivateDnsName": "ip-172-31-22-52.ec2.internal",
            "Attachment": {
            "Status": "attaching",
            "DeviceIndex": 0,
            "DeleteOnTermination": true,
            "AttachmentId": "eni-attach-0428b549373b9f864",
            "AttachTime": "2018-08-08T06:38:43.000Z"
            },
            "Groups": [
            {
            "GroupName": "HelloWorld", 
            "GroupId": "sg-01864b4c"
            }
            ],
            "Ipv6Addresses": [], "OwnerId": "094507990803", "SubnetId": "subnet-6fdd7927", "PrivateIpAddress":  "172.31.22.52"
            }
            ],
            "SourceDestCheck": true, "Placement": {
            "Tenancy": "default", "GroupName": "", "AvailabilityZone": "us-east-1c"
            },
            "Hypervisor": "xen", "BlockDeviceMappings": [], "Architecture": "x86_64", "RootDeviceType": "ebs", "RootDeviceName": "/dev/xvda", "VirtualizationType": "hvm", "AmiLaunchIndex": 0
            }
            ], "ReservationId": "r-09a637b7a3be11d8b", "Groups": [], "OwnerId": "094507990803"
            }
 
$ aws ec2 describe-instance-status --instance-ids i-057e8deb1a4c3f35d
            "InstanceStatuses": [
            "InstanceId": "i-057e8deb1a4c3f35d", 
            "InstanceState": {
            "Code": 16, "Name": "running" },
            "AvailabilityZone": "us-east-1c", "SystemStatus": {
            "Status": "initializing", "Details": [
            "Status": "initializing", "Name": "reachability" }
            ]
            },
            "InstanceStatus": {
            "Status": "initializing", "Details": [
            {
            "Status": "initializing","Name": "reachability" 
            }
            ]
            }
          }
       ]
  }          

$ aws ec2 describe-instance-status --instance-ids i-057e8deb1a4c3f35d --output text| grep -i SystemStatus
SYSTEMSTATUS ok   

$ aws ec2 describe-instances --instance-ids i-057e8deb1a4c3f35d --query "Reservations[*].Instances[*].PublicDnsName"
[
    [
          "ec2-34-201-101-26.compute-1.amazonaws.com"
    ]
]

$ ssh -i ~/.ssh/EffectiveDevOpsAWS.pem ec2-user@ ec2-34-201-101-26.compute-1.amazonaws.com
The authenticity of host 'ec2-34-201-101-26.compute-1.amazonaws.com (172.31.22.52)' can't be established.
ECDSA key fingerprint is SHA256:V4kdXmwb5ckyU3hw/E7wkWqbnzX5DQR5zwP1xJXezPU.
ECDSA key fingerprint is MD5:25:49:46:75:85:f1:9d:f5:c0:44:f2:31:cd:e7:55:9f.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'ec2-34-201-101-26.compute-1.amazonaws.com,172.31.22.52' (ECDSA) to the list of known hosts.<br/><br/> __| __|_ )<br/> _| ( / Amazon Linux AMI
___|\___|___|
https://aws.amazon.com/amazon-linuxami/2018.03-release-notes/
1 package(s) needed for security, out of 2 available
Run "sudo yum update" to apply all updates.
[ec2-user@ip-172-31-22-52 ~]$
```
Si vous rencontrez des problèmes, ajoutez l'option `-vvv` dans votre commande SSH pour le résoudre.
          
## Créer une application Web Hello World simple

Maintenant que nous sommes connectés à notre instance EC2, nous sommes prêts à commencer à jouer avec. Ici, nous nous concentrerons sur le cas d'utilisation le plus courant d'AWS dans les entreprises technologiques : l'hébergement d'une application. En termes de langages, nous utiliserons JavaScript, qui est l'un des langages les plus populaires sur GitHub. Cela dit, cette application vise davantage à fournir une assistance afin de démontrer comment utiliser au mieux AWS en utilisant les principes DevOps. Il n'est pas nécessaire d'avoir des connaissances sur JavaScript pour comprendre cet exercice.
Certains des principaux avantages offerts par JavaScript par rapport à cet exercice incluent le fait que :
* Il est assez facile à écrire et à lire, même pour les débutants
* Il n'a pas besoin d'être compilé
* Il peut être exécuté côté serveur grâce à Node.js (https://nodejs.org)
* Il est officiellement pris en charge par AWS et, par conséquent, le SDK AWS pour JavaScript est un citoyen de première classe

Pour le reste du chapitre, toutes les commandes et le code doivent être exécutés sur notre instance via SSH.

```
[ec2-user@ip-172-31-22-52 ~]$ sudo yum install --enablerepo=epel -y nodejs 
[ec2-user@ip-172-31-22-52 ~]$ node -v
v0.10.48
```
Il s'agit certainement d'une ancienne version du nœud, mais elle suffira pour ce dont nous avons besoin.

## Exécuter une application Node.js Hello World

Maintenant que le nœud est installé, nous pouvons créer une simple application Hello World.
Voici le code pour créer ceci :

```
var http = require("http") http.createServer(function (request, response) {
// Send the HTTP header
// HTTP Status: 200 : OK
// Content Type: text/plain
response.writeHead(200, {'Content-Type': 'text/plain'})
// Send the response body as "Hello World" response.end('Hello World\n')
}).listen(3000)
// Console will print the message console.log('Server running')
```
N'hésitez pas à le copier dans un fichier. Alternativement, si vous voulez gagner du temps, téléchargez ceci depuis GitHub 
Après avoir fait un `wget du répertoire github dans ce dépôt le résultat sera : 
```
Saving to: ‘/home/ec2-user/helloworld.js’
/home/ec2-user/helloworld.js 100%[=====================================================================================>] 2018-08-19 13:06:42 (37.9 MB/s) - ‘/home/ec2-user/helloworld.js’ saved [384/384]
[ec2-user@ip-172-31-22-52 ~]$
```

Afin de lancer l'application Hello World, nous allons maintenant simplement lancer le code suivant :

```
[ec2-user@ip-172-31-22-52 ~]$ node helloworld.js
Server running
```
Si tout se passe bien, vous pourrez désormais l'ouvrir dans votre navigateur au lien suivant : `http://votre-nom-dns-public:3000` . Ou dans mon cas, cela se trouvera ici : `http://ec2-34-201-101-26.compute-1.amazonaws.com:3000`. Vous pourrez alors voir le résultat, comme suit :

![image](https://user-images.githubusercontent.com/107214400/176642589-2b0ba673-2e90-4bdd-a7e1-2129b1a9ca61.png)

Nous allons maintenant arrêter l'exécution de l'application web Hello World avec `Ctrl + C` dans votre fenêtre Terminal.

## Transformer notre code simple en service en utilisant upstart
Puisque nous avons démarré l'application de nœud manuellement dans le terminal, fermer la connexion SSH ou appuyer sur __Ctrl + C__ sur le clavier arrêtera le processus de nœud, et donc notre application Hello World ne fonctionnera plus. Amazon Linux, contrairement à une distribution standard basée sur Red Hat, est livré avec un système appelé **upstart**.

Ceci est assez facile à utiliser et fournit quelques fonctionnalités supplémentaires que les scripts de **démarrage System-V traditionnels** n'ont pas, telles que la possibilité de réapparaître un processus qui est mort de manière inattendue. Pour ajouter une configuration de démarrage, vous devez créer un fichier dans `/etc/init` sur l'instance EC2.

Voici le code pour l'insérer dans `/etc/init/helloworld.conf` : description "Hello world Daemon"

```
# Commencez lorsque le système est prêt à fonctionner en réseau. Démarrer sur les interfaces elasticnetwork démarrées
# Arrêtez-vous lorsque le système est en train de s'arrêter. Arrêt à l'extinction
respawn script exec su --session-command="/usr/bin/node /home/ec2-user/helloworld.js" ec2-user
end script
```

> Pourquoi commencer sur les interfaces réseau élastiques ? Si vous connaissez upstart en dehors d'AWS, vous avez peut-être utilisé start on run level [345]. Dans AWS, le problème avec cela est que votre réseau provient d'Elastic Network Interface (ENI), et si votre application démarre avant ce service, il se peut qu'elle ne puisse pas se connecter correctement au réseau.

Faites un Wget pour insérer le `helloworld.conf`

```
Saving to: ‘/etc/init/helloworld.conf’
/etc/init/helloworld.conf 100%[=====================================================================================>] 2018-08-19 13:09:39 (54.0 MB/s) - ‘/etc/init/helloworld.conf’ saved [301/301]
[ec2-user@ip-172-31-22-52 ~]$
```
Nous pouvons maintenant simplement démarrer notre application, comme suit :

```
[ec2-user@ip-172-31-22-52 ~]$ sudo start helloworld
helloworld start/running, process 2872
[ec2-user@ip-172-31-22-52 ~]$
```
Comme prévu, `http://your-public-dns-name:3000` fonctionne toujours, et cette fois nous pouvons fermer notre connexion SSH en toute sécurité.

```
[ec2-user@ip-172-31-22-52 ~]$ sudo stop helloworld helloworld stop/waiting
[ec2-user@ip-172-31-22-52 ~]$ ec2-metadata --instance-id instance-id: i-057e8deb1a4c3f35d 
[ec2-user@ip-172-31-22-52 ~]$ exit logout
$ aws ec2 terminate-instances --instance-ids i-057e8deb1a4c3f35d {
    "TerminatingInstances": [
    {
        "InstanceId": "i-057e8deb1a4c3f35d", "CurrentState": {
        "Code": 32, "Name": "shutting-down"
        }, "PreviousState": {
        "Code": 16, "Name": "running"
            }
         }
    ]
}

```
## Résumé
Ce chapitre était une introduction rapide et simple à AWS et à son service le plus notoire, EC2. Après avoir souscrit à AWS, nous avons configuré notre environnement de manière à pouvoir créer un serveur virtuel à l'aide de l'interface de ligne de commande. Pour cela, nous avons sélectionné notre première AMI, créé notre premier groupe de sécurité et généré nos clés SSH, que nous réutiliserons tout au long du livre. Après avoir lancé une instance EC2, nous avons déployé manuellement une simple application Node.js pour afficher Hello World.

Si le processus n'était pas très fastidieux grâce à l'AWS CLI, il nécessitait tout de même de passer par de nombreuses étapes, peu répétables. Nous avons également déployé l'application sans aucune automatisation ni validation. De plus, la seule façon de vérifier si l'application est en cours d'exécution est de vérifier manuellement le point de terminaison. Dans le reste nous reviendrons sur le processus de création et de gestion des applications et de l'infrastructure Web, mais, cette fois, nous suivrons les principes DevOps et intégrerons leurs meilleures pratiques.

Dans la partie, __Traiter votre infrastructure comme du code__ , nous aborderons l'un des premiers problèmes que nous avons rencontrés : la gestion de notre infrastructure avec l'automatisation. Pour ce faire, nous allons écrire du code pour gérer notre infrastructure.








          
