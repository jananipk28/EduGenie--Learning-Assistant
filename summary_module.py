from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


def summarize_text(text):
    prompt = f"""
Summarize the following text in a simple and student-friendly way.

Text:
{text}

Give:

1. Short summary
2. Main points
3. Important keywords
"""

    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return response.output_text