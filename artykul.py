import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system",
         "content": "You are a witty assistant that responds with a joke whenever it's possible and appropriate."},
        {
            "role": "user",
            "content": "Is 42 the answer to the Ultimate Question of Life? Will it help me land this job?"
        }
    ]
)

print(completion.choices[0].message['content'])
