import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
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

def generate_quiz(text):

    prompt = f"""
You are an expert study assistant.

Generate exactly 10 multiple-choice questions from the study notes.

Question Writing Rules:

- Write natural multiple-choice questions.
- Do not mention "study notes", "according to the notes", or similar phrases.
- Ask the question directly.
- Make the questions sound like a real exam.

Each question must have:

A

B

C

D

Only one correct answer.

Return ONLY valid JSON.

The correct_option must be exactly one of:
"A"
"B"
"C"
or
"D"

Format:
[
    
    {{
        "question": "...",
        "option_a": "...",
        "option_b": "...",
        "option_c": "...",
        "option_d": "...",
        "correct_option": "A"
    }}

]

No markdown.

No explanation.

Do not wrap the JSON inside markdown code blocks.

Return raw JSON only.

Study Notes:

{text}
"""

    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
        response_mime_type="application/json"))
    
        return json.loads(response.text)

    except Exception as e:
        print(e)
        return None