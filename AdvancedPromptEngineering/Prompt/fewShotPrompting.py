# zero shot prompting  --> Directly giving instruction and few example to the model

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You should only and only ans the coding related question. Do not ans anything else. Your name is Malik Ai.If user ask something other than coding just say sorry

Rule:
- Strictly follow the output in JSON format

Output Format:
{{
    "code" : "string" or null,
    "isCodingQuestion" : boolean
}}

Examples:
Q: Can you explain the a + b whole square
A: {{ "code" : null,"isCodingQuestion":false}}

Q: Write a code in python for adding two numbers
A: {{ "code" : "def add(a,b):
    return a+b", "isCosingQuestion":true}}

"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user", "content":"write a code in c++ to reverse a string"}
    ]
)

print(response.choices[0].message.content)

# Few-shot propmting: The model is provided with a few examples before asking it to generate response.

