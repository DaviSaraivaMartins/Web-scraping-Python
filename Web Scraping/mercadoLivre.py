import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

url_base = "https://lista.mercadolivre.com.br/"

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36"
}

produto_nome = input("Qual produto você deseja comprar ? ")
produto_formatado = quote(produto_nome)

resposta = requests.get(url_base + produto_formatado, headers=headers)
site = BeautifulSoup(resposta.text, "html.parser")

produtos = site.findAll('div', attrs={'class': 'poly-card__content'})

for produto in produtos:
    titulo = produto.find('h3', attrs={'class': 'poly-component__title-wrapper'})
    link = produto.find("a", attrs={'class': 'poly-component__title'})
    real = produto.find('span', attrs={'class': 'andes-money-amount__fraction'})
    centavos = produto.find('span', attrs={'class': 'andes-money-amount__cents andes-money-amount__cents--superscript-20'})

    if titulo and link and real:
        print("Título do produto:", titulo.text.strip())
        print("Link do produto:", link['href'])

        if centavos:
            preco = f"{real.text},{centavos.text}"
        else:
            preco = f"{real.text},00"

        print("Valor do produto: R$", preco)
        print("\n\n")
