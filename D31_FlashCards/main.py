from random import choice
import time
import pandas
from tkinter import Tk, Button, Label, Entry, Canvas, PhotoImage
BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ("Arial", 40, "italic")
FONT2 = ("Arial", 60, "bold")

DataFrame = pandas.read_csv("D31_FlashCards/data/french_words.csv")
to_learn = DataFrame.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(top_text, text="French", fill="black")
    canvas.itemconfig(bottom_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(top_text, text="English", fill="white")
    canvas.itemconfig(bottom_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)


### data connection ###

#### set up the ui ####
window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="D31_FlashCards/images/card_front.png")
card_back = PhotoImage(file="D31_FlashCards/images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front)
top_text = canvas.create_text(400, 150, fill="black",
                              font=FONT1)
bottom_text = canvas.create_text(400, 263, fill="black",
                                 font=FONT2)
canvas.grid(column=0, row=0, columnspan=2)


image_wrong = PhotoImage(file="D31_FlashCards/images/wrong.png")
button_wrong = Button(
    image=image_wrong, command=next_card, highlightthickness=0)
button_wrong.grid(column=0, row=1)

image_correct = PhotoImage(file="D31_FlashCards/images/right.png")
button_correct = Button(image=image_correct,
                        command=next_card, highlightthickness=0)
button_correct.grid(column=1, row=1)

next_card()

window.mainloop()
