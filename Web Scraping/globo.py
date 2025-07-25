import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.globo.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36"
}

resposta = requests.get(url, headers=headers)
soup = BeautifulSoup(resposta.text, "html.parser")

titulos = soup.find_all("a")

# Lista para armazenar os títulos
titulos_filtrados = []

print("Títulos de notícias encontradas:\n")

contador = 0
for link in titulos:
    texto = link.get_text(strip=True)
    if texto and len(texto) > 30:
        contador += 1
        print(f"{contador}. {texto}")
        titulos_filtrados.append([texto])  # título como lista para gravar no CSV
        if contador >= 15:
            break

# Salva os títulos em um arquivo CSV (fora do loop!)
with open("titulos_globo.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(["Título da Notícia"])  # Cabeçalho
    writer.writerows(titulos_filtrados)

print("\n Títulos salvos com sucesso no arquivo 'titulos_globo.csv'")
