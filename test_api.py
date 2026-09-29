from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

response = client.interactions.create(
    model="gemini-3.8-flash",
    input="Say Hello in one sentence."
)

print(response.output_text)