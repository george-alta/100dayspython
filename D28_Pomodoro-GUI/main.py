from tkinter import Tk, Button, Label, Entry, Canvas, PhotoImage

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
# testing


def func():
    pass


def start():
    pass


def reset():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", font=("Courier", 30, "bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="D28_Pomodoro-GUI/tomato.png")
canvas.create_image(102, 112, image=tomato)
canvas.create_text(103, 130, text="00:00", fill="white",
                   font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", command=start)
button_start.grid(column=0, row=3)
button_stop = Button(text="Reset", command=start)
button_stop.grid(column=2, row=3)

checkmark = Label(text="✓", font=(
    "Courier", 20, "bold"), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=4)


window.mainloop()
