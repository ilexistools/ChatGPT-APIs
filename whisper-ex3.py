from openai import OpenAI
import os 

client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"),)

audio_file= open("output_pt.mp3", "rb")
transcript = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file
)
print(transcript)