from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory


# 1. Load API Key

import os

api_key = open(r"C:\Users\DELL\Desktop\ai-upskill-5\share\ey-ai-upskill-b4-11052026-main\key-vault\openai\api.key").read().strip()


# 2. Create LLM

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=api_key,
    temperature=0.7
)


# 3. Prompt with Memory Slot

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful, friendly chatbot assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])


# 4. Base Chain

chain = prompt | llm


# 5. Memory Store (Session-based)

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


# 6. Wrap with Memory

chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)


# 7. Chat Function

def chat(session_id: str, user_input: str):
    response = chatbot.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": session_id}}
    )
    return response.content


# 8. CLI Chat Loop

if __name__ == "__main__":
    session_id = "user_1"

    print("Chatbot started (type 'exit' to stop)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chat ended.")
            break

        response = chat(session_id, user_input)
        print("Bot:", response)