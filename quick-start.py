from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"),)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Você é um tradutor."},
    {"role": "user", "content": "Traduza: The book is on the table."}
  ]
)
print(completion.choices[0].message)