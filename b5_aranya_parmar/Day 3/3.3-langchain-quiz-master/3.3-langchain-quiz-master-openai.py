from datetime import datetime

from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain_openai import ChatOpenAI


class HistoryQuiz:

    def __init__(self, key_file_path):

        # Read OpenAI API key from file
        with open(key_file_path, "r") as f:
            api_key = f.read().strip()

        self.llm = ChatOpenAI(
            api_key=api_key,
            model="gpt-4o-mini",
            temperature=0
        )

    def create_history_question(self, topic):

        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
                "You are a history quiz generator."
            ),
            HumanMessagePromptTemplate.from_template(
                "Create one history question about {topic} where the answer is a specific date. "
                "Return only the question."
            )
        ])

        chain = prompt | self.llm

        response = chain.invoke({"topic": topic})

        return response.content.strip()

    def get_ai_answer(self, question):

        prompt = ChatPromptTemplate.from_messages([
            HumanMessagePromptTemplate.from_template(
                "Answer ONLY in YYYY-MM-DD format.\n\nQuestion: {question}"
            )
        ])

        chain = prompt | self.llm

        response = chain.invoke({"question": question})

        date_text = response.content.strip()

        # Convert AI response to datetime (safe and reliable)
        return datetime.strptime(date_text, "%Y-%m-%d")

    def get_user_answer(self, question):
        
        print("\nQuestion:", question)
        
        while True:
            try:
                year = int(input("Enter Year (YYYY): "))
                month = int(input("Enter Month (MM): "))
                day = int(input("Enter Day (DD): "))
                
                if month < 1 or month > 12:
                    print("Invalid month. Please enter between 1 and 12.")
                    continue
                
                if day < 1 or day > 31:
                    print("Invalid day. Please enter between 1 and 31.")
                    continue
                
                return datetime(year, month, day)
            
            except ValueError:
                print("Invalid input. Please enter numbers only (no text or decimals).")

    def check_user_answer(self, user_answer, ai_answer):

        diff = abs((user_answer - ai_answer).days)

        print("\nCorrect Answer:", ai_answer.date())
        print("Your Answer:", user_answer.date())
        print("Difference in days:", diff)

        return diff


def run_quiz():

    key_path = r"C:\Users\DELL\Desktop\ai-upskill-5\share\ey-ai-upskill-b4-11052026-main\key-vault\openai\api.key"

    quiz_bot = HistoryQuiz(key_path)

    topics = [
        "World War 2",
        "Indian Independence",
        "Cold War",
        "Renaissance",
        "French Revolution",
        "American Revolution",
        "Space Exploration",
        "Mughal Empire",
        "British Empire",
        "Ancient Rome"
    ]

    score = 0

    print("\nWelcome to History Quiz Bot (10 Questions)\n")

    for i in range(10):

        print("\n================ Question", i + 1, "================")

        topic = topics[i]

        question = quiz_bot.create_history_question(topic)
        ai_answer = quiz_bot.get_ai_answer(question)
        user_answer = quiz_bot.get_user_answer(question)

        diff = quiz_bot.check_user_answer(user_answer, ai_answer)

        if diff == 0:
            print("Perfect Answer")
            score += 10
        elif diff <= 30:
            print("Very Close")
            score += 7
        elif diff <= 365:
            print("Close Guess")
            score += 5
        else:
            print("Wrong")

    print("\n================ FINAL SCORE ================")
    print("Total Score:", score, "/ 100")


if __name__ == "__main__":
    run_quiz()