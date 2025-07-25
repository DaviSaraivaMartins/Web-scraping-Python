import requests
from bs4 import BeautifulSoup
import csv

def get_news():
    url = "https://www.r7.com/"
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36"
    }

    resposta = requests.get(url, headers=headers)
    soup = BeautifulSoup(resposta.text, "html.parser")
    titulos = soup.find_all("a")

    titulos_filtrados = []
    print("Títulos de notícias encontradas:\n")
    
    contador = 0
    for link in titulos:
        texto = link.get_text(strip=True)
        if texto and len(texto) > 40:
            contador += 1
            print(f"{contador}. {texto}")
            titulos_filtrados.append([texto])
            if contador >= 15:
                break

    # Salvar no CSV
    with open("titulos_globo.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(["Título da Notícia"])
        writer.writerows(titulos_filtrados)

    print("\n✅ Títulos salvos com sucesso no arquivo 'titulos_r7.csv'")

# Executa a função
if __name__ == "__main__":
    get_news()
