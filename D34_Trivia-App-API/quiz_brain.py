from html import unescape
from data import QUESTIONS


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        #
        self.current_question = self.question_list[self.question_number]["question"]
        self.question_number += 1
        qtext = unescape(self.current_question)
        return qtext

    def check_answer(self, user_answer):
        this_question_is = str(
            self.question_list[self.question_number]["correct_answer"])
        if this_question_is == "True":
            self.test = True
        else:
            self.test = False
        self.correct_answer = bool(
            self.question_list[self.question_number]["correct_answer"])
        if user_answer == self.test:
            return True
        else:
            return False

    def still_has_questions(self):
        return self.question_number < QUESTIONS-1  # len(self.question_list)
