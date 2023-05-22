from html import unescape


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        self.current_question = self.question_list[self.question_number]["question"]
        self.question_number += 1
        qtext = unescape(self.current_question)

        # user_answer = input(
        # f"Q{self.question_number}: {qtext} (true/false): "
        # ).lower()
        # self.check_answer(user_answer, qtext.answer)
        return qtext

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}\n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # this will provide a true/false answer
