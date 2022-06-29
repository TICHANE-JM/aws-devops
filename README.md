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
