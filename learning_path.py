from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


def create_learning_path(topic):
    prompt = f"""
Create a simple learning path for a college student.

Topic:
{topic}

Include:

1. Beginner level
2. Basic concepts
3. Intermediate level
4. Practice activities
5. Advanced level
6. Final revision

Explain each step briefly.
"""

    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return response.output_text