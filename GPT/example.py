# Creates a human-like response to a hard-coded prompt, API Key must be stored in the environment variable OPENAI_API_KEY.
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a disaster response assistant."},
        {
            "role": "user",
            "content": "My street has started to flood. What should I do?"
        }
    ]
)

print(completion.choices[0].message["content"])