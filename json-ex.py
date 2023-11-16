from openai import OpenAI
import os 

client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"))


messages = [
    {
      "role": "system", 
      "content": "Você é um assistente que entende de futebol."
    },
     {
      "role": "user", 
      "content": "Qual país ganhou a copa em 94. Resposta em json, campo vencedor.ss"
    },
]

response = completion = client.chat.completions.create(
  model="gpt-4-1106-preview",
  messages=messages,
  response_format= { "type":"json_object" }
)

print(completion.choices[0].message.content)
