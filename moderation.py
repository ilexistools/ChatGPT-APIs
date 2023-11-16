import requests
import os 
from secret import secret_key

# Substitua com sua chave de API da OpenAI
api_key = secret_key

# Dados para a solicitação
data = {
    "input": "You are beautiful."
}

# Headers para a solicitação
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# URL da API
url = "https://api.openai.com/v1/moderations"

# Fazendo a solicitação POST
response = requests.post(url, json=data, headers=headers)

# Imprime a resposta
print(response.json())
