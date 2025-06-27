# Python: Avance na Orientação a Objetos e Consuma API 🚀🐍

Este repositório contém os códigos desenvolvidos durante o curso **"Python: Avance na Orientação a Objetos e Consuma API"** da Alura. O projeto simula um sistema de cadastro de restaurantes e cardápios, utilizando conceitos avançados de orientação a objetos e a biblioteca **FastAPI** para criação de uma API REST.

## 📁 Estrutura do Projeto

- `modelos/`: Classes que representam os modelos de domínio (Restaurante, Prato, Bebida).
- `requisicoes/`: Arquivos relacionados à API com FastAPI.
- `app.py`: Script principal para execução da aplicação.
- `main.py`: Ponto de entrada da API com documentação dos endpoints.
- `requirements.txt`: Dependências do projeto.

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/nonolism/Python-Avance-na-Orientacao-a-Objetos-e-Consuma-API.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a aplicação com FastAPI:
   ```bash
   uvicorn main:app --reload
   ```
4. Acesse a documentação interativa da API:
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🧠 Conceitos Aplicados

- Programação orientada a objetos (POO)
- Encapsulamento e modularização
- Criação de APIs com FastAPI
- Documentação automática de endpoints
- Boas práticas de organização de código
