import os
import openai

from dotenv import load_dotenv

load_dotenv()

client = openai.AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_API_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version=os.getenv("AZURE_API_VERSION")
)

model = os.getenv("CHAT_COMPLETION_NAME")

prompt = str(input("Prompt: "))

response = client.chat.completions.create(
    model=model,
    messages=[{"role": "system", "content": "You are a helpful assistant."},
              {"role": "user", "content": prompt}]
)