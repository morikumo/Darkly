
---

# Cross-Site Scripting (XSS)

## Description de la faille

Une vulnérabilité de Cross-Site Scripting (XSS) a été découverte dans le formulaire de feedback. En injectant du code dans les champs de saisie du formulaire, il est possible d'exécuter du code malveillant et de récupérer des informations sensibles, ce qui a permis de révéler un flag.

## Étapes pour découvrir la faille

1. **Accès à la page de feedback** :
   - Accédez à la page de feedback en utilisant l'URL suivante : `http://192.168.108.182/index.php?page=feedback`.

2. **Injection de code JavaScript** :
   - Juste a mettre "script" dans le champs name ou message.

3. **Soumission du formulaire** :
   - Soumettez le formulaire après avoir entré le mot "script" dans l'un des champs de saisie.

4. **Obtention du flag** :
   - Après avoir soumis le formulaire avec le mot "script", le flag a été révélé, ce qui confirme la présence d'une faille XSS.

## Nom de la faille

Cette faille est connue sous le nom de **Cross-Site Scripting (XSS)**.

## Flag

```
0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e
```

## Recommandations pour corriger la faille

Pour corriger cette faille, voici quelques recommandations :

1. **Validation et échappement des entrées utilisateur** : Assurez-vous que toutes les entrées utilisateur sont correctement validées et échappées avant d'être affichées dans le navigateur.
2. **Utilisation de Content Security Policy (CSP)** : Implémentez une politique de sécurité de contenu pour restreindre les sources de scripts exécutables.
3. **Sanitisation des données** : Utilisez des bibliothèques de sanitisation pour nettoyer les entrées utilisateur et empêcher l'injection de scripts.
4. **Encoder les sorties** : Encodez les caractères spéciaux dans les sorties HTML pour empêcher l'exécution de code JavaScript.

## Conclusion

Cette faille montre l'importance de valider et de filtrer toutes les entrées utilisateur pour empêcher l'exécution de code malveillant via des injections XSS. En suivant les recommandations ci-dessus, la sécurité de l'application peut être significativement améliorée.

---

