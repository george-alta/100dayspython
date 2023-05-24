from data import question_data
from ui import QuizInterface
from quiz_brain import QuizBrain

# structure ["results"][n]["category","question","correct_answer"]

question_bank = question_data
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
