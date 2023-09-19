from random import choice
import time
import pandas
from tkinter import Tk, Button, Label, Entry, Canvas, PhotoImage
BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ("Arial", 40, "italic")
FONT2 = ("Arial", 60, "bold")
FONT3 = ("Arial", 10, "bold")

current_card = {}
to_learn = {}
### data connection ###
# "D31_FlashCards/data/words_to_learn.csv"

try:
    data = pandas.read_csv("D31_FlashCards/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("D31_FlashCards/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(top_text, text="French", fill="black")
    canvas.itemconfig(bottom_text, text=current_card["French"], fill="black")
    canvas.itemconfig(cards_left, text=len(to_learn)-1, fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(top_text, text="English", fill="white")
    canvas.itemconfig(bottom_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(cards_left, text=len(to_learn)-1, fill="white")


def is_known():
    to_learn.remove(current_card)  # remove the current card from dictionary
    data = pandas.DataFrame(to_learn)
    data.to_csv("D31_FlashCards/data/words_to_learn.csv", index=False)

    next_card()


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
cards_left = canvas.create_text(400, 470, fill="black", text=len(to_learn)-1,
                                font=FONT3)

canvas.grid(column=0, row=0, columnspan=2)


image_wrong = PhotoImage(file="D31_FlashCards/images/wrong.png")
button_unknown = Button(
    image=image_wrong, command=next_card, highlightthickness=0)
button_unknown.grid(column=0, row=1)

image_correct = PhotoImage(file="D31_FlashCards/images/right.png")
button_known = Button(image=image_correct,
                      command=is_known, highlightthickness=0)
button_known.grid(column=1, row=1)

next_card()

window.mainloop()
