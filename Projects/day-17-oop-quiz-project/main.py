from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
