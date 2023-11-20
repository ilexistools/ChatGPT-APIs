from openai import OpenAI
import os 

client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"))

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Qual a diferença entre as imagens?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Laptop_collage.jpg/2560px-Laptop_collage.jpg",
          },
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Apple_II_Plus%2C_Museum_of_the_Moving_Image.jpg/440px-Apple_II_Plus%2C_Museum_of_the_Moving_Image.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)
print(response.choices[0])