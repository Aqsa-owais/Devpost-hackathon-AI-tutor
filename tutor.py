import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)


def run_cs_tutor_agent(student_query, student_weaknesses, textbook_context):

    weakness_str = ", ".join(student_weaknesses) if student_weaknesses else "None"

    system_instruction = f"""
You are an expert Socratic Computer Science Tutor.

Current Weaknesses:
{weakness_str}

Textbook:

{textbook_context}

Rules:

- Teach simply.
- Don't directly solve.
- Ask guiding questions.
- Use textbook only.
"""

    completion = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {"role":"system","content":system_instruction},
            {"role":"user","content":student_query}
        ],

        temperature=0.4,
        max_tokens=1024

    )

    return completion.choices[0].message.content