import requests
from bs4 import BeautifulSoup

def get_dolar_quote():
    url = "https://www.google.com/search?q=cotação+do+dólar"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # O valor da cotação geralmente está em um span com a classe abaixo (pode mudar com o tempo)
    valor_span = soup.find("span", class_="DFlfde.SwHCTb", attrs={"data-precision": "2"})

    if valor_span:
        print("💵 Cotação do Dólar hoje:")
        print("R$", valor_span.text.strip())
    else:
        print("⚠️ Não foi possível encontrar a cotação. O layout da página pode ter mudado.")

if __name__ == "__main__":
    get_dolar_quote()
