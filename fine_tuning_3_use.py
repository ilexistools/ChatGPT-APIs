from openai import OpenAI
import os 

client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"),)

response = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-0613:personal::8MQFomsA",
  messages=[
    {"role": "system", "content": "Um chatbot que transforma frases no estilo do mestre Yoda."},
    {"role": "user", "content": "Você deve usar suas habilidades."}
  ]
)
print(response.choices[0].message)