from openai import OpenAI

with open(r"C:\Users\DELL\Desktop\ai-upskill-5\share\ey-ai-upskill-b4-11052026-main\key-vault\openai\api.key") as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)

MODEL = "gpt-4.1-mini"

def chat():
    print("Welcome to the chatbot! Type 'exit', 'quit', or 'end' to stop. \n")

    conversation = []

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "end"]:
            print("Goodbye!")
            break

        conversation.append({"role": "user", "content": user_input})

        try:
            messages = conversation.copy()

            response = client.chat.completions.create(
                model=MODEL,
                messages=messages
            )  

            output_text = response.choices[0].message.content

            print("Bot:", output_text)

            conversation.append({"role": "assistant", "content": output_text})

        except Exception as e:
            print("Error occured:", str(e))

if __name__ == "__main__":
    chat()