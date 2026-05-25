from openai import OpenAI

with open(r"C:\Users\DELL\Desktop\ai-upskill-5\share\ey-ai-upskill-b4-11052026-main\key-vault\openai\api.key") as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)

reponse = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        { "role": "system", "content": "You are a helpful assistant"},
        { "role": "user", "content": "Tell me about quantum computing"}
    ]
)

print(reponse.choices[0].message.content)