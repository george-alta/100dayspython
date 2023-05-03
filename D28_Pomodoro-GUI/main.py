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
SPEED = 1000  # in miliseconds
reps = 0
checkmark_text = ""
timer = None
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        countdown(work_sec)
        title.config(text="Work", fg=RED)

    elif reps % 8 == 0:
        countdown(long_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        countdown(break_sec)
        title.config(text="Break", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global checkmark_text
    # global reps
    minutes = int(count/60)  # another option is using math.floor (import math)
    seconds = count % 60
    if seconds < 10:
        canvas.itemconfig(timertext, text=f"{minutes}:0{seconds}")
    else:
        canvas.itemconfig(timertext, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(SPEED, countdown, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark_text += "✓"
            checkmark.config(text=checkmark_text)
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global checkmark_text, reps
    window.after_cancel(timer)
    canvas.itemconfig(timertext, text=f"25:00")
    checkmark_text = ""
    checkmark.config(text=checkmark_text)
    title.config(text="Timer", fg=GREEN)
    reps = 0


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(width=800, padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
title = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

tomato = PhotoImage(file="D28_Pomodoro-GUI/tomato.png")
canvas.create_image(102, 112, image=tomato)
timertext = canvas.create_text(103, 130, text=f"{WORK_MIN}:00", fill="white",
                               font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
button_reset.grid(column=2, row=2)

checkmark = Label(text=checkmark_text, font=(
    FONT_NAME, 20), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()
