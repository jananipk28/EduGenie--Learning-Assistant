from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


def ask_question(question):
    prompt = f"""
You are EduGenie, a helpful learning assistant.

Answer the student's question clearly and simply.

Question:
{question}

Give an easy-to-understand answer suitable for a college student.
"""

    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return response.output_text