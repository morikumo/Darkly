from typing import Any
import requests
from bs4 import BeautifulSoup, ResultSet
import os

def find_flag_in_readme(base_url: str):
    def fetch_directory(url: str) -> ResultSet[Any]:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.find_all('a')

    def is_readme_file(link):
        return link.text.strip() == 'README'

    directories_to_check = [base_url]
    flag_path = None
    flag_content = None

    while directories_to_check:
        current_url = directories_to_check.pop(0)
        links = fetch_directory(current_url)

        for link in links:
            href = link.get('href')
            if href and href not in ['.', '..']:
                full_url = os.path.join(current_url, href)
                if is_readme_file(link):
                    response = requests.get(full_url)
                    content = response.text
                    if "flag" in content:
                        flag_path = full_url
                        flag_content = content
                        return flag_path, flag_content
                elif href.endswith('/'):
                    directories_to_check.append(full_url)

    return None, None

# Utilisation
base_url = "http://192.168.1.16/.hidden/"
flag_path, flag_content = find_flag_in_readme(base_url)

if flag_path:
    print(f"Flag found in: {flag_path}")
    print(f"Content: {flag_content}")
else:
    print("No flag found.")
