
---

# Exploitation de Faille et Prévention de Web Scraping

## Description de la Faille

Cette faille a été découverte grâce au fichier `robots.txt` du site web. Le fichier `robots.txt` indique les répertoires ou fichiers que le propriétaire du site souhaite exclure des moteurs de recherche. En examinant ce fichier, nous avons trouvé des répertoires cachés qui contiennent potentiellement des fichiers sensibles comme des README.

## Découverte de la Faille

1. **Accéder au fichier `robots.txt`** :
   - En visitant `http://ip-addr/robots.txt`, nous avons trouvé des instructions révélant des répertoires cachés.

2. **Analyser le contenu de `robots.txt`** :
   - Le fichier `robots.txt` contenait des directives `Disallow` qui indiquaient les répertoires et fichiers que les moteurs de recherche ne doivent pas indexer.

3. **Explorer les répertoires cachés** :
   - Nous avons décidé de développer un script pour explorer automatiquement ces répertoires et trouver des fichiers README contenant des informations sensibles, comme des flags.

## Script de Web Scraping

Nous avons développé un script Python optimisé pour parcourir l'arborescence des répertoires, rechercher des fichiers README et télécharger leur contenu. Voici le script :

```python
import requests
from bs4 import BeautifulSoup
import os
import concurrent.futures

def fetch_directory(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.find_all('a')

def is_readme_file(link):
    return link.text.strip() == 'README'

def process_directory(current_url, max_depth, current_depth):
    if current_depth > max_depth:
        return None, None
    
    links = fetch_directory(current_url)
    directories_to_check = []

    for link in links:
        href = link.get('href')
        if href and href not in ['.', '..']:
            full_url = os.path.join(current_url, href)
            if is_readme_file(link):
                response = requests.get(full_url)
                content = response.text
                if "flag" in content:
                    return full_url, content
            elif href.endswith('/'):
                directories_to_check.append(full_url)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_directory, url, max_depth, current_depth + 1) for url in directories_to_check]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result[0]:  # if flag_path is not None
                return result

    return None, None

def find_flag_in_readme(base_url, max_depth=10):
    return process_directory(base_url, max_depth, 0)

# Utilisation
base_url = "http://ip-addr/.hidden/"
flag_path, flag_content = find_flag_in_readme(base_url)

if flag_path:
    print(f"Flag found in: {flag_path}")
    print(f"Content: {flag_content}")
else:
    print("No flag found.")
```

### Fonctionnement du Script

1. **Fonction `fetch_directory(url)`** :
   - Effectue une requête HTTP GET pour récupérer le contenu HTML d'un répertoire.
   - Utilise BeautifulSoup pour parser le contenu et trouver tous les liens (`<a>`).

2. **Fonction `is_readme_file(link)`** :
   - Vérifie si un lien correspond à un fichier README.

3. **Fonction `process_directory(current_url, max_depth, current_depth)`** :
   - Explore récursivement les répertoires jusqu'à une profondeur maximale (`max_depth`).
   - Utilise `ThreadPoolExecutor` pour télécharger et vérifier les fichiers en parallèle.
   - Retourne le chemin et le contenu du fichier README contenant le flag, s'il est trouvé.

4. **Fonction `find_flag_in_readme(base_url, max_depth)`** :
   - Démarre l'exploration à partir de `base_url` avec une profondeur maximale de 10 (modifiable selon vos besoins).

### Exécution

- Le script explore les répertoires de manière récursive et parallèle, limitant la profondeur pour améliorer la performance.
- Il télécharge et analyse les fichiers README pour détecter la présence de flags.

## Prévention contre le Web Scraping

Pour éviter que votre site web soit vulnérable au web scraping, suivez ces recommandations :

1. **Restreindre l'accès aux répertoires sensibles** :
   - Configurez votre serveur web pour restreindre l'accès aux répertoires et fichiers sensibles en utilisant des fichiers `.htaccess` ou des règles de configuration du serveur.

2. **Masquer les répertoires et fichiers critiques** :
   - Évitez de stocker des fichiers critiques ou sensibles dans des répertoires accessibles publiquement. Utilisez des chemins non prévisibles et des techniques de camouflage.

3. **Implémenter des contrôles d'accès robustes** :
   - Assurez-vous que seuls les utilisateurs autorisés peuvent accéder aux répertoires et fichiers sensibles en utilisant des systèmes d'authentification et d'autorisation.

4. **Utiliser des CAPTCHAs** :
   - Intégrez des CAPTCHAs dans les formulaires pour différencier les utilisateurs humains des bots et scripts automatisés.

5. **Surveiller et loguer les accès** :
   - Mettez en place des mécanismes de surveillance et de journalisation des accès aux répertoires et fichiers sensibles. Analysez régulièrement les logs pour détecter des comportements suspects.

6. **Utiliser des outils de sécurité pour analyser les vulnérabilités** :
   - Effectuez des analyses régulières de sécurité sur votre serveur et vos applications web pour détecter et corriger les vulnérabilités potentielles.

7. **Mettre en place des limites de taux (rate limiting)** :
   - Implémentez des limites de taux pour les requêtes sur votre serveur afin de prévenir les abus et les attaques par force brute.

8. **Former les développeurs et les administrateurs système** :
   - Sensibilisez et formez vos équipes aux meilleures pratiques de sécurité pour éviter les erreurs de configuration et les mauvaises pratiques de développement.

En suivant ces recommandations, vous pouvez réduire le risque de vulnérabilités exploitables par des scripts automatisés et améliorer la sécurité globale de votre infrastructure.

---

