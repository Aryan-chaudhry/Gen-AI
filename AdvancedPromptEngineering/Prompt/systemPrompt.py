from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role":"system","content":"you have to answer only maths related query. any query not related to math do not ans that"},
        {"role":"user", "content":"what is my name. did you know my name"}
    ]
)

print(response.choices[0].message.content)