'''
    [INST] what is time now [/INST]
'''

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = (
    "You have to answer only maths-related queries. "
    "Any query not related to maths should not be answered."
)

user_query = "What is my name? Did you know my name?"

inst_prompt = f"""<s>[INST] <<SYS>>
{system_prompt}
<</SYS>>

{user_query}
[/INST]"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {
            "role": "user",
            "content": inst_prompt
        }
    ]
)

print(response.choices[0].message.content)