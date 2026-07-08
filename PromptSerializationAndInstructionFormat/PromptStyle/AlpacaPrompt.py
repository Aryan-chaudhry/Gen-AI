# Alpaca Prompt

### Instructions: <system Prompt>\n 
### input: <user_query> 
### response: \n 

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

alpaca_prompt = f"""
### Instruction:
{system_prompt}

### Input:
{user_query}

### Response:
"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
      messages=[
        {
            "role": "user",
            "content": alpaca_prompt
        }
    ]
)

print(response.choices[0].message.content)