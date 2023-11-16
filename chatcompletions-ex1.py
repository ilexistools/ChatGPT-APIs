from openai import OpenAI
import os 
import json 

client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"),)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Você é um assistente com conhecimento de futebol."},
    {"role": "user", "content": "Quem ganhou a copa do mundo de 2022?"},
    {"role": "assistant", "content": "Argentina"},
    {"role": "user", "content": "Qual país sediou?"}
  ]
)
print(response.choices[0].message.content)