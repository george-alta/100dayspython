import time
from tkinter import Tk, Button, Label, Entry, Canvas, PhotoImage
BACKGROUND_COLOR = "#B1DDC6"

# D31_FlashCards/data/french_words.csv
#
#
#
# D31_FlashCards/images/card_back.png


def correct():
    pass


def wrong():
    pass


#### set up the ui ####
window = Tk()
window.title("Flashcard")
window.config(width=1200, padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="D31_FlashCards/images/card_front.png")
card_back = PhotoImage(file="D31_FlashCards/images/card_back.png")

canvas.create_image(400, 263, image=card_front)
top_text = canvas.create_text(400, 150, text=f"text1", fill="black",
                              font=("Arial", 40, "italic"))
top_text = canvas.create_text(400, 263, text=f"text2", fill="black",
                              font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


image_wrong = PhotoImage(file="D31_FlashCards/images/wrong.png")
button_wrong = Button(image=image_wrong, command=wrong, highlightthickness=0)
button_wrong.grid(column=0, row=1)

image_correct = PhotoImage(file="D31_FlashCards/images/right.png")
button_correct = Button(image=image_correct,
                        command=correct, highlightthickness=0)
button_correct.grid(column=1, row=1)


window.mainloop()
