import requests
import json
import os

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item["Company"]
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
        
        dados_restaurante[nome_restaurante].append({
            "item": item["Item"],
            "price": item["price"],
            "description": item["description"]
            })
else:
    print(f'O erro foi {response.status_code}')


for nome_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f"{nome_restaurante}.json"
    caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4, ensure_ascii=False)