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

7. Une fois de retour dans Windows, cliquez à nouveau sur le bouton Démarrer, recherchez __bash__ et démarrez le Bash sur Ubuntu sur l'application Windows :
