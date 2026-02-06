import os, openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_llm(prompt):
    r = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return r.choices[0].message.content
