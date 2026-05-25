from openai import OpenAI

# Load API key
with open(r"C:\Users\DELL\Desktop\ai-upskill-5\share\ey-ai-upskill-b4-11052026-main\key-vault\openai\api.key") as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)

# System prompt with strict domain control
messages = [
    {
        "role": "system",
        "content": (
            "You are a cybersecurity specialist chatbot. "
            "You only answer questions related to cybersecurity, cyber risk, threat intelligence, "
            "network security, application security, cloud security, and related topics. "
            "If the user asks anything outside cybersecurity, you must politely and respectfully decline "
            "and say you can only assist with cybersecurity-related queries."
        )
    }
]

print("Cyber Security Chatbot is running. Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    bot_reply = response.choices[0].message.content

    print("Chatbot:", bot_reply)

    messages.append({"role": "assistant", "content": bot_reply})