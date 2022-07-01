Nom de rôle
=========

Une brève description du rôle va ici.

Conditions
------------

Tous les prérequis qui peuvent ne pas être couverts par Ansible lui-même ou le rôle doivent être mentionnés ici. Par exemple, si le rôle utilise le module EC2, il peut être judicieux de mentionner dans cette section que le package boto est requis.

Variables de rôle
--------------

Une description des variables définissables pour ce rôle doit aller ici, y compris toutes les variables qui se trouvent dans defaults/main.yml, vars/main.yml et toutes les variables qui peuvent/devraient être définies via des paramètres pour le rôle. Toutes les variables lues à partir d'autres rôles et/ou de la portée globale (c'est-à-dire les variables d'hôte, les variables de groupe, etc.) doivent également être mentionnées ici.

Dépendances
------------

Une liste des autres rôles hébergés sur Galaxy devrait aller ici, ainsi que tous les détails concernant les paramètres qui peuvent devoir être définis pour d'autres rôles, ou les variables qui sont utilisées à partir d'autres rôles.

Exemple de Playbook
----------------

Inclure un exemple d'utilisation de votre rôle (par exemple, avec des variables transmises en tant que paramètres) est toujours agréable pour les utilisateurs :

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Informations sur l'auteur
------------------

Une section facultative pour les auteurs du rôle afin d'inclure des informations de contact ou un site Web (HTML n'est pas autorisé).
