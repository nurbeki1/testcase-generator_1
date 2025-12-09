import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_test_cases(topic: str):
    prompt = f"""
    Create detailed test cases for feature: {topic}.
    MUST INCLUDE:
    - UI test cases
    - API test cases
    - Negative test cases
    - Edge cases
    Format in markdown tables.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
