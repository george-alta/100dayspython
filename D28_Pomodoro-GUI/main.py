from tkinter import Tk, Button, Label, Entry, Canvas, PhotoImage
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checktext = ""
# ---------------------------- TIMER RESET ------------------------------- #
# testing


def func():
    pass


def reset():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    global checktext
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        countdown(work_sec)
    elif reps % 8 == 0:
        countdown(long_break_sec)
    else:
        countdown(break_sec)

    while True:
        countdown(work_sec)
        # reps += 1
        # for i in range(reps):
        #     checktext += "✓"
        checkmark.config(text=checktext)
        if reps % 3 != 0:
            countdown(break_sec)
        else:
            countdown(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    minutes = int(count/60)  # another option is using math.floor (import math)
    seconds = count % 60
    if seconds < 10:
        canvas.itemconfig(timertext, text=f"{minutes}:0{seconds}")
    else:
        canvas.itemconfig(timertext, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, countdown, count-1)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
title = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

tomato = PhotoImage(file="D28_Pomodoro-GUI/tomato.png")
canvas.create_image(102, 112, image=tomato)
timertext = canvas.create_text(103, 130, text=f"{WORK_MIN}:00", fill="white",
                               font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# countdown(5)

button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", command=reset, highlightthickness=0)
button_reset.grid(column=2, row=2)

checkmark = Label(text=checktext, font=(
    FONT_NAME, 20), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)


window.mainloop()
