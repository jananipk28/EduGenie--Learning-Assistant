from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


def explain_topic(topic):
    prompt = f"""
Explain the following topic in a simple and student-friendly way.

Topic:
{topic}

Give:

1. Simple definition
2. Main points
3. Simple example
4. Short conclusion
"""

    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return response.output_text