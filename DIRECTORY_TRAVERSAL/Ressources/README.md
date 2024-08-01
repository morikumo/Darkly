
---

# Directory Traversal

## Description de la faille

Une vulnérabilité de Directory Traversal a été découverte, permettant d'accéder à des fichiers sensibles du serveur en manipulant les paramètres de l'URL.

## Étapes pour découvrir la faille

1. **Essais initiaux** :
   - En accédant à des URL inexistantes, divers messages d'erreur comme "Still nope", "Wrong again", etc., ont été affichés.
   - En continuant à ajouter des séquences `../` dans l'URL, le message "You can DO it !!! :]" a été affiché.

2. **Construction de l'URL pour accéder au fichier `/etc/passwd`** :
   - Finalement, en accédant à l'URL suivante, le fichier `/etc/passwd` a été révélé :
     ```
     http://192.168.108.182/?page=/../../../../../../../etc/passwd
     ```

## Nom de la faille

Cette faille est connue sous le nom de **Directory Traversal** ou **Path Traversal**.

## Flag

```
b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0
```

## Recommandations pour corriger la faille

Pour corriger cette faille, voici quelques recommandations :

1. **Valider et assainir les entrées utilisateur** : Assurez-vous que les entrées utilisateur ne contiennent pas de séquences de traversée de répertoires (`../`).
2. **Utiliser des chemins relatifs sécurisés** : Ne jamais utiliser directement les entrées utilisateur pour construire des chemins de fichiers.
3. **Configurer les permissions du système de fichiers** : Limitez les permissions sur les fichiers sensibles et assurez-vous que l'application web n'a accès qu'aux répertoires nécessaires.

## Conclusion

Cette faille montre l'importance de valider et de filtrer toutes les entrées utilisateur pour empêcher l'accès non autorisé aux fichiers du système. En suivant les recommandations ci-dessus, la sécurité de l'application peut être significativement améliorée.

---
