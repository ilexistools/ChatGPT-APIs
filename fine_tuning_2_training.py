from openai import OpenAI
import os 

client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"),)

fine_tuning_job = client.fine_tuning.jobs.create(
  training_file="file-BM4rXPSnpmvoNXB3ZXtiO2Tw", 
  validation_file="file-qzY9xCBFk0axeEslIKYAhG5p",
  model="gpt-3.5-turbo"
)

print(fine_tuning_job)