from openai import OpenAI
import os 



client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"),)

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hello world! This is a streaming test.",
)

response.stream_to_file("output.mp3")