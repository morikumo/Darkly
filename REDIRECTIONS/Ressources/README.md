
---

# Niveau 3 - Redirection ouverte

## Description de la faille

Une redirection ouverte a été découverte sur le site, ce qui peut être exploité pour des attaques de phishing ou pour accéder à des ressources non autorisées. En modifiant l'URL de redirection, il est possible d'accéder directement au flag.

## URL

```
http://ip-addr/index.php?page=redirect&site="*Le site en question*"
```

## Étapes pour découvrir la faille

1. **Accès à la page d'accueil** :
   - Accédez à la page d'accueil en utilisant l'URL suivante : `http://ip-addr/`.

2. **Inspection des liens de réseaux sociaux** :
   - En bas de la page d'accueil, repérez les liens vers les réseaux sociaux tels que Twitter, Facebook, etc.

3. **Identification de l'URL de redirection** :
   - Les liens de réseaux sociaux utilisent l'URL de redirection suivante :

     ```
     http://ip-addr/index.php?page=redirect&site="site en question"
     ```

4. **Modification de l'URL de redirection** :
   - Remplacez le paramètre `site="site en question"` par une autre URL ou un site spécifique.
   - Essayez différentes valeurs pour le paramètre `site`.

5. **Obtention du flag** :
   - En remplaçant le site par certaines valeurs, vous êtes redirigé directement vers une page contenant le flag.

## Nom de la faille

Cette faille est connue sous le nom de **redirection ouverte**.

## Flag

```
<Insérez le flag ici>
```

## Recommandations pour corriger la faille

Pour corriger cette faille, voici quelques recommandations :

1. **Validation et filtrage des URL** : Validez et filtrez strictement les URL de redirection pour s'assurer qu'elles ne pointent que vers des sites autorisés.
2. **Utilisation de tokens de redirection** : Utilisez des tokens ou des identifiants de redirection au lieu de permettre des URL libres dans les paramètres.
3. **Avertissements de redirection** : Affichez un avertissement à l'utilisateur avant de le rediriger vers une URL externe et demandez confirmation.

## Conclusion

Cette faille montre l'importance de valider et de filtrer toutes les entrées utilisateur, en particulier celles impliquant des redirections, pour prévenir les attaques de phishing et les accès non autorisés. En suivant les recommandations ci-dessus, la sécurité des redirections sur le site peut être significativement améliorée.

---
