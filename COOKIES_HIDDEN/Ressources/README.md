
---

# Manipulation de Cookies

## Description de la faille

Une vulnérabilité a été découverte dans la gestion des cookies de l'application web. En modifiant la valeur d'un cookie spécifique, il est possible de changer les permissions utilisateur et d'obtenir un flag.

## Étapes pour découvrir la faille

1. **Observation des cookies** :
   - Utilisez `curl` pour envoyer une requête à l'application web :
     ```sh
     curl -I http://ip-addr/
     ```
   - Réponse :
     ```
     HTTP/1.1 200 OK
     Server: nginx/1.4.6 (Ubuntu)
     Date: Thu, 01 Aug 2024 11:34:23 GMT
     Content-Type: text/html
     Connection: keep-alive
     X-Powered-By: PHP/5.5.9-1ubuntu4.29
     Set-Cookie: I_am_admin=68934a3e9455fa72420237eb05902327; expires=Thu, 01-Aug-2024 12:34:23 GMT; Max-Age=3600
     ```

2. **Analyse de la valeur du cookie** :
   - La valeur du cookie `I_am_admin` est `68934a3e9455fa72420237eb05902327`. En la passant dans un outil de décryptage MD5, elle correspond à "false".

3. **Génération de la valeur pour "true"** :
   - En générant la valeur MD5 pour "true", on obtient `b326b5062b2f0e69046810717534cb09`.

4. **Modification du cookie** :
   - Modifiez le cookie `I_am_admin` dans votre navigateur pour que sa valeur soit `b326b5062b2f0e69046810717534cb09`.

5. **Obtenir le flag** :
   - Rafraîchissez la page avec le cookie modifié. Vous obtiendrez le flag.

## Flag

```
df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
```

## Recommandations pour corriger la faille

Pour corriger cette faille, voici quelques recommandations :

1. **Utilisation de cookies sécurisés** : Ne pas stocker des informations sensibles ou critiques directement dans les cookies.
2. **Utilisation de signatures de cookies** : Ajoutez une signature sécurisée aux cookies pour vérifier leur intégrité et empêcher les modifications malveillantes.
3. **Validation côté serveur** : Assurez-vous que les informations de session et d'autorisation sont toujours validées côté serveur et non basées uniquement sur les cookies.
4. **Hachage sécurisé** : Utilisez des algorithmes de hachage sécurisés et des salt pour éviter les attaques par hachage inverse.

## Conclusion

Cette faille montre l'importance de sécuriser les cookies et de ne pas stocker des informations sensibles dans des cookies non protégés. En suivant les recommandations ci-dessus, la sécurité de l'application peut être significativement améliorée.

---


