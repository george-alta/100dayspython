from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# create question bank

question_bank = []
for element in question_data:
    question_text = element["text"]
    question_answer = element["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
