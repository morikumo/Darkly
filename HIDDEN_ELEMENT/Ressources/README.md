
---

# Réinitialisation de mot de passe

## Description de la faille

Lors de la tentative de réinitialisation du mot de passe via la fonction "Mot de passe oublié", il a été découvert qu'il n'y avait pas de champ visible pour entrer un email. Cependant, en inspectant le code source de la page, un champ de type `hidden` a été trouvé, contenant une adresse email déjà configurée. 

## Étapes pour découvrir la faille

1. **Accès à la page de réinitialisation de mot de passe** :
   - Accédez à la page de connexion du site.
   - Cliquez sur le lien "Mot de passe oublié" pour accéder à la page de réinitialisation.

2. **Inspection du code source** :
   - Faites un clic droit sur la page et sélectionnez "Inspecter" pour ouvrir les outils de développement du navigateur.
   - Cherchez les champs de formulaire dans l'onglet "Éléments" de l'inspecteur.

3. **Identification du champ `hidden`** :
   - Dans le formulaire de réinitialisation, un champ de type `hidden` a été trouvé, contenant une adresse email par défaut. Voici le code trouvé :

     ```html
     <form action="#" method="POST">
         <input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
         <input type="submit" name="Submit" value="Submit">
     </form>
     ```

4. **Modification de l'email** :
   - Changez la valeur de l'input `hidden` pour une autre adresse email légitime, par exemple :

     ```html
     <input type="hidden" name="mail" value="monadresse@exemple.com" maxlength="15">
     ```

   - Soumettez le formulaire après avoir modifié l'email.

5. **Obtention du flag** :
   - Une fois le formulaire soumis avec l'email modifié, le système a retourné un message de succès avec le flag suivant :
     ```
     1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0
     ```

## Flag

```
1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0
```

## Recommandations pour corriger la faille

Pour corriger cette faille, voici quelques recommandations :

1. **Validation côté serveur** : Assurez-vous que toutes les entrées utilisateurs sont validées côté serveur, et non seulement côté client.
2. **Suppression des champs `hidden` pour les données critiques** : Évitez d'utiliser des champs de type `hidden` pour des informations critiques comme les adresses email. Utilisez des mécanismes sécurisés pour obtenir et valider ces informations.
3. **Authentification par email** : Envoyez un lien de réinitialisation du mot de passe à l'adresse email de l'utilisateur au lieu de permettre une modification directe sur la page.

## Conclusion

Cette faille illustre l'importance de valider et sécuriser toutes les entrées utilisateurs, et de ne pas se fier uniquement aux validations côté client. En suivant les recommandations ci-dessus, la sécurité de ce processus de réinitialisation de mot de passe peut être significativement améliorée.

---
