import os
import sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

try:
    question = sys.argv[1]
except:
    print("No question provided")
    exit(1)

response = client.models.generate_content(model="gemini-2.0-flash-001", contents=question)
print(response.text)
print("Prompt tokens:", response.usage_metadata.prompt_token_count)
print("Response tokens: ", response.usage_metadata.candidates_token_count)
