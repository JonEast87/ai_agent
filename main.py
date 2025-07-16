import os
import sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)

try:
    user_prompt = sys.argv[1]
except:
    print("No question provided")
    exit(1)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

try:
    if sys.argv[2] == "--verbose":
        print("User prompt: {}".format(sys.argv[1]))
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens: ", response.usage_metadata.candidates_token_count)
except:
    print(response.text)
