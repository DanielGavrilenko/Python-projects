from data import question_data
from quiz_brain import QuizBrain
import question_model

question_bank = []
for question in question_data:
    question_bank.append(question_model.Question(question["text"], question["answer"]))


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"Your final score {quiz.score}/{quiz.question_number}")