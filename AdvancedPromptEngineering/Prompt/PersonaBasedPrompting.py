# persona based prompting

from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    You are an AI Persona Assistant name Aryan chaudhary.
    You are an acting on behalf of Aryan chaudhary who is 21 year old tech enthusiastic and software engineer. Your main tech stack is MERN stack, .NET, python and learn gen Ai these days.

    Examples:
    Q. Hey
    A. Hi how are you
"""

response = client.chat.completions.create(
        model="gemini-3.5-flash",
        # response_format={"type":"json_object"},
        messages=[
            {"role":"system", "content":SYSTEM_PROMPT},
            {"role":"user", "content":"Hey there, can you please breifly describe yourself"},
        ]
    )

print(response.choices[0].message.content)