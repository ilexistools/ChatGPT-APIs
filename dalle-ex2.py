from openai import OpenAI
import os 
import webbrowser

client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"),)

response = client.images.create_variation(
  image=open("shark.png", "rb"),
  n=2,
  size="1024x1024"
)

image_url = response.data[0].url
webbrowser.open(image_url)