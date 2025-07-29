import requests
from bs4 import BeautifulSoup

url = "https://g1.globo.com/"

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36"
}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.text, 'html.parser')

noticias = soup.find_all("a")

Noticias_filtrados = []

print("Noticias encontradas:\n")

contador = 0
for link in noticias:
    texto = link.get_text(strip=True)
    if texto and len(texto) >30:
        contador += 1
        print(f"{contador}. {texto}")
        Noticias_filtrados.append([texto])
        if contador >=15:
           break

        