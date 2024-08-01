
---

# Utilisation de `curl` pour exploiter une faille de header

## Étapes pour découvrir la faille

1. **Accéder à la page cible** :
   - Accédez à l'URL suivante : `http://192.168.1.10/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f`.
   
2. **Inspecter la page** :
   - Ouvrez l'inspecteur du navigateur (clic droit sur la page et sélectionnez "Inspecter" ou appuyez sur `Ctrl+Shift+I`).
   - Allez dans l'onglet "Elements" pour voir le code source de la page.
   
3. **Trouver les commentaires** :
   - Faites défiler jusqu'en bas du code source pour trouver les commentaires suivants :
     ```html
     <!--Let's use this browser : "ft_bornToSec". It will help you a lot.-->
     <!--You must come from : "https://www.nsa.gov/".-->
     ```

4. **Interprétation des commentaires** :
   - Le commentaire `<!--Let's use this browser : "ft_bornToSec". It will help you a lot.-->` suggère que le serveur s'attend à ce que la requête provienne d'un navigateur ou d'un client spécifique. Le terme "browser" fait référence à un navigateur web, et "ft_bornToSec" est probablement la chaîne `User-Agent` que le serveur attend.
   - Le commentaire `<!--You must come from : "https://www.nsa.gov/".-->` indique clairement que la requête doit sembler provenir de `https://www.nsa.gov/`. Le terme "come from" fait référence à l'en-tête HTTP `Referer`, qui indique l'origine de la requête.
   
5. **Explication de la logique** :
   - En utilisant les en-têtes `User-Agent` et `Referer` spécifiés dans les commentaires, vous pouvez tromper le serveur en lui faisant croire que la requête provient du client et de la source attendus.
   
6. **Exécuter la commande `curl`** :
   - Utilisez la commande suivante pour envoyer une requête HTTP GET avec les en-têtes personnalisés et rechercher le flag dans la réponse :
     ```sh
     curl -s -H "Referer: https://www.nsa.gov/" -H "User-Agent: ft_bornToSec" "http://192.168.1.10/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" | grep flag
     ```
   - **Explication de la commande** :
     - **`curl`** : Outil en ligne de commande pour transférer des données avec des URL.
     - **`-s`** : Option "silent mode". Elle empêche `curl` d'afficher la barre de progression et les messages d'erreur. Utile pour des scripts où seule la sortie de la commande est nécessaire.
     - **`-H "Referer: https://www.nsa.gov/"`** : Définit un en-tête HTTP personnalisé `Referer`. Cet en-tête indique au serveur d'où provient la requête. Ici, il est défini sur `https://www.nsa.gov/` pour simuler que la requête provient du site de la NSA.
     - **`-H "User-Agent: ft_bornToSec"`** : Définit un en-tête HTTP personnalisé `User-Agent`. Cet en-tête identifie le client logiciel effectuant la requête HTTP. Ici, il est défini sur `ft_bornToSec` pour simuler un client spécifique.
     - **`"http://192.168.1.10/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"`** : L'URL vers laquelle la requête HTTP est envoyée. Cette URL semble contenir un identifiant de page qui pourrait révéler un flag.
     - **`| grep flag`** : Filtre la sortie de `curl` pour ne montrer que les lignes contenant le mot "flag". `grep` est un utilitaire de recherche de texte utilisé pour filtrer et afficher les lignes correspondant à un motif donné.

7. **Récupérer le flag** :
   - En exécutant la commande ci-dessus, vous devriez obtenir le flag suivant :
     ```
     f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
     ```

## Flag

```
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```

---

