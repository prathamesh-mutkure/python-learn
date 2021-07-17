from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizUI
import requests


def get_questions():
    api_url = "https://opentdb.com/api.php"

    params = {
        "amount": 10,
        "category": 18,
        "type": "boolean",
    }

    response = requests.get(api_url, params=params)
    response.raise_for_status()

    data = response.json()
    return data["results"]


question_bank = []
question_data = get_questions()
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
