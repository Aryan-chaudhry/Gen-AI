# zero shot prompting  --> Directly giving instruction to the model

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = "You should only and only ans the coding related question. Do not ans anything else. Your name is Malik Ai.If user ask something other than coding just say sorry"

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user", "content":"hey what is your name can you please tell me a joke"}
    ]
)

print(response.choices[0].message.content)

# 1. Zero shot prompting: The model is given a direct question or task without prior example