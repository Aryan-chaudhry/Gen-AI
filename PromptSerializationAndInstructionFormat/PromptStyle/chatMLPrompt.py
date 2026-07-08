'''
    chatML propmting

    {"role":"system"|"user"|"assistant"
    "content":"string"}
'''

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = "You have to answer only maths-related queries. Any query not related to maths should not be answered."

user_query = "What is my name? Did you know my name?"

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_query
        }
    ]
)

print(response.choices[0].message.content)