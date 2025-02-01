
---

# Injection de paramètres cachés

## Description de la faille

Une injection de paramètres cachés a été découverte dans un formulaire HTML sur la page de sondage. En modifiant les valeurs des champs cachés et en sélectionnant une nouvelle valeur dans un menu déroulant, il est possible d'accéder au flag.

## URL

```
http://ip-addr/?page=survey
```

## Étapes pour découvrir la faille

1. **Accès à la page de sondage** :
   - Accédez à la page de sondage en utilisant l'URL suivante : `http://ip-addr/?page=survey`.

2. **Inspection du code source** :
   - Faites un clic droit sur la page et sélectionnez "Inspecter" pour ouvrir les outils de développement du navigateur.
   - Cherchez les champs de formulaire dans l'onglet "Éléments" de l'inspecteur.

3. **Identification des champs `hidden` et `select`** :
   - Dans le formulaire, les champs suivants ont été trouvés :

     ```html
     <form action="#" method="post">
         <input type="hidden" name="sujet" value="3">
         <select name="valeur" onchange="javascript:this.form.submit();">
             <option value="1">1</option>
             <option value="2">2</option>
             <option value="3">3</option>
             <option value="4">4</option>
             <option value="5">5</option>
             <option value="6">6</option>
             <option value="7">7</option>
             <option value="8">8</option>
             <option value="9">9</option>
             <option value="10">10</option>
         </select>
     </form>
     ```

4. **Observation de la méthode POST** :
   - La présence de `method="post"` dans le formulaire indique que les données soumises sont envoyées au serveur pour traitement. Cela suggère qu'une vérification côté serveur est effectuée, ce qui est un indice que des paramètres cachés pourraient être utilisés ou manipulés par le backend.

5. **Soumission du formulaire** :
   - Le formulaire se soumet automatiquement lorsque la valeur du menu déroulant est changée grâce à l'attribut `onchange`.

6. **Obtention du flag** :
   - En modifiant la valeur de l'attribut 'value' dans le formulaire, au niveau des balises <option>, et en sélectionnant ensuite cette option sur le site, nous obtenons le flag.

## Nom de la faille

Cette faille est connue sous le nom d'**injection de paramètres cachés**.

## Flag

```
03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa
```

## Recommandations pour corriger la faille

Pour corriger cette faille, voici quelques recommandations :

1. **Validation côté serveur** : Assurez-vous que toutes les entrées et paramètres utilisateurs sont validés côté serveur, et non seulement côté client.
2. **Utilisation de tokens de session** : Utilisez des tokens de session pour vérifier l'authenticité des requêtes, empêchant ainsi les utilisateurs non autorisés de soumettre des formulaires modifiés.

## Conclusion

Cette faille montre l'importance de ne pas se fier uniquement aux validations côté client et de toujours valider et filtrer les entrées côté serveur. En suivant les recommandations ci-dessus, la sécurité de ce formulaire peut être significativement améliorée.

---
