from tkinter import Tk, Label, PhotoImage
import random
from data import question_data
from ui import QuizInterface
from quiz_brain import QuizBrain

score = 0

# structure ["results"][n]["category","question","correct_answer"]


def ans_true():
    global score
    pass


def ans_false():
    pass


def check_answer():
    pass


def next_question():
    pass


question_bank = question_data
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# feed a first question
next_question()
