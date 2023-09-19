from tkinter import Label, Tk, Button, PhotoImage, Canvas
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

score = 0
total_runs = 0


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivia App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, width=500)

        self.score_label = Label(text=f"Score: {score}/{total_runs}",
                                 font=(
                                     "Arial",
                                     15,
                                     "bold"),
                                 background=THEME_COLOR,
                                 foreground="white"
                                 )
        self.score_label.grid(column=1, row=0, padx=20, pady=20, sticky="e")

        self.canvas = Canvas(
            width=460, height=250,
            bg="white",
            highlightthickness=0
        )
        self.canvas.grid(
            row=2, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(
            230,
            125,
            width=440,
            text="this is a question",
            fill=THEME_COLOR,
            font=("arial", 20, "italic")
        )

        self.true_img = PhotoImage(
            file="D34_Trivia-App-API/resources/correct.png")
        self.true_button = Button(
            image=self.true_img,
            highlightthickness=0,
            bd=0,
            relief="flat",
            command=self.button_true,
            background=THEME_COLOR
        )
        self.true_button.grid(row=3, column=0, padx=60, pady=20)

        self.false_img = PhotoImage(
            file="D34_Trivia-App-API/resources/failed.png")
        self.false_button = Button(
            image=self.false_img,
            highlightthickness=0,
            bd=0,
            relief="flat",
            command=self.button_false,
            background=THEME_COLOR
        )
        self.false_button.grid(row=3, column=1, padx=60, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def button_true(self):
        global score, total_runs
        total_runs += 1
        if self.quiz.check_answer(True):
            score += 1
            self.feedback(True)
        else:
            self.feedback(False)

    def button_false(self):
        global score, total_runs
        total_runs += 1
        if self.quiz.check_answer(False):
            score += 1
            self.feedback(True)
        else:
            self.feedback(False)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            qtext = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=qtext)
            self.score_label.config(text=f"Score: {score}/{total_runs}")
        else:
            self.score_label.config(text=f"Final Score: {score}/{total_runs}")
            self.canvas.itemconfig(
                self.question_text, text=f"End of the quiz: {round(score*100/total_runs)}%")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def feedback(self, win):
        if win:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


# UI setup
