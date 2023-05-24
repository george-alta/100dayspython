# this trivia game pulls data from opentdb.com, using the API and creating
# a data model, then in the interface you can select if the statement is TRUE or FALSE
# when the quiz is over, you get your final result


from data import question_data
from ui import QuizInterface
from quiz_brain import QuizBrain

# the question bank is created from OpenTDB
question_bank = question_data
# We create a QuizBrain object using the Question Bank
quiz = QuizBrain(question_bank)

# We initialise the UI, and we are going to use the QUIZ object
quiz_ui = QuizInterface(quiz)
