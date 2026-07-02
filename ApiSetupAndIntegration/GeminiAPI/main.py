from dotenv import load_dotenv
from google import genai

load_dotenv()


client = genai.Client()

interactions = client.interactions.create(
    model="gemini-3.5-flash",
    input="hello how are you"
)

print(interactions.output_text)