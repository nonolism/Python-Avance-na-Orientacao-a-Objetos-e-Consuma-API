from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Exemplo de endpoint que retorna uma mensagem simples.
    '''
    return {'Hello': 'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para obter o cardápio de um restaurante específico ou todos os restaurantes.
    
    Parâmetros:
    - restaurante: Nome do restaurante (opcional). Se não fornecido, retorna todos os restaurantes.
    
    Retorna:
    - Dados de todos os restaurantes ou o cardápio de um restaurante específico.
    
    Exemplo de uso:
    - Para obter todos os restaurantes: /api/restaurantes/
    - Para obter o cardápio de um restaurante específico: /api/restaurantes/?restaurante=nome_do_restaurante
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item["Item"],
                    "price": item["price"],
                    "description": item["description"]
                    })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return {'Erro': f'{response.status_code} - {response.text}'}