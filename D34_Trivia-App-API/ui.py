from tkinter import Label, Tk, Button, PhotoImage, Canvas
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

score = 0


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivia App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0

        # UI setup

        self.score_label = Label(text=f"Score: {score}",
                                 font=(
                                     "Arial",
                                     15,
                                     "bold"),
                                 background=THEME_COLOR,
                                 foreground="white"
                                 )
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        self.canvas = Canvas(
            width=300, height=250,
            bg="white",
            highlightthickness=0
        )
        self.canvas.grid(
            row=2, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="this is a question",
            fill=THEME_COLOR,
            font=("arial", 15, "italic")
        )

        self.true_img = PhotoImage(
            file="D34_Trivia-App-API/resources/correct.png")
        self.true_button = Button(
            image=self.true_img,
            highlightthickness=0,
            bd=0,
            relief="flat",
            command=self.get_next_question,
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
            command=self.get_next_question,
            background=THEME_COLOR
        )
        self.false_button.grid(row=3, column=1, padx=60, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_quote(self):
        pass

    def get_next_question(self):
        qtext = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=qtext)

# UI setup
