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
    You're an expert AI Assistant in resolving user queries using chain  of thought.
    You work in START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can me multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (that can be multiple times) and finally OUTPUT (which is going to the displayed to the user)

    Output JSON Format:
    {{"step":"START" | "PLAN"  | "OUTPUT", "content":"string"}}

    Example:
    START: Hey, can you solve 2+3*5/10
    PLAN: {"step":  "PLAN": "content": "Seems like user is interested in maths problem"} 
    PLAN: {"step":  "PLAN": "content": "looking at the problem, we should solve this using BODMAS method"} 
    PLAN: {"step":  "PLAN": "content": "Yes, The BODMAS is correct thing to be done here"} 
    PLAN: {"step":  "PLAN": "content": "First multiple 3*5 is 15"} 
    PLAN: {"step":  "PLAN": "content": "Now new equation is 2 + 15/10"} 
    PLAN: {"step":  "PLAN": "content": "we must perform divide that is 15/10 is 1.5"} 
    PLAN: {"step":  "PLAN": "content": "Now new equation looks like 2 + 1.5"} 
    PLAN: {"step":  "PLAN": "content": "Now finally lets perform the add 2 + 1.5 gives me 3.5"} 
    PLAN: {"step":  "PLAN": "content": "great, we have solved with an answer 3.5"} 
    OUTPUT: {"step":  "OUTPUT": "content": "3.5"} 


"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    response_format={"type":"json_object"},
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user", "content":"write a code in c++ to reverse a string"},
        # manually keep adding messages to the history again and again until get your answer
        {"role":"assistant","content":json.dumps({"step": "PLAN", "content": "The user wants a C++ program to reverse a string. I need to design a simple and efficient solution, ideally demonstrating both the standard library approach and a manual approach, or a complete runnable example."})}

    ]
)

print(response.choices[0].message.content)