from decouple import config
from openai import OpenAI

api_key = config("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Olá, quem é você?"},
    ],
    model="gpt-4o",
)

print(chat_completion.choices[0].message.content)