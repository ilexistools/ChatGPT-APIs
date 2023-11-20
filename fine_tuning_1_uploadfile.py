from openai import OpenAI
import os 

client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"),)

file_object = client.files.create(
  file=open("trainset.jsonl", "rb"),
  purpose="fine-tune"
)

print(file_object.id)