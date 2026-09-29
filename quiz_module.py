from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


def generate_quiz(topic):
    prompt = f"""
Create a simple educational quiz for a college student.

Topic:
{topic}

Create 5 multiple-choice questions.

For each question provide:

Question
A. Option
B. Option
C. Option
D. Option

Then provide the correct answer.

Keep the questions clear and educational.
"""

    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return response.output_text