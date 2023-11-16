from openai import OpenAI
import os 
import webbrowser

client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"),)

response = client.images.generate(
  model="dall-e-3",
  prompt="um gato sorrindo",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
webbrowser.open(image_url)