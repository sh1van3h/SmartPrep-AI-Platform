import os

from dotenv import load_dotenv
from google import genai
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_summary(text):

    prompt = f"""
You are an expert study assistant.

Summarize the following study notes.

Rules:
- Keep the summary under 150 words.
- Use simple language.
- Highlight the important concepts.
- Do not add information that is not present in the notes.

Study Notes:

{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

def generate_flashcards(text):

    prompt = f"""
You are an expert study assistant.

Generate exactly 5 flashcards from the study notes.

Return ONLY valid JSON.

Format:

[
    {{
        "question": "...",
        "answer": "..."
    }}
]

Do not write markdown.
Do not write explanation.
Return JSON only.

Study Notes:

{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return json.loads(response.text)