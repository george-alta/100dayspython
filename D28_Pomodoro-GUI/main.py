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
#testing
def func():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="D28_Pomodoro-GUI/tomato.png")
canvas.create_image(102, 112, image=tomato)
canvas.create_text(103, 130, text="00:00", fill="white",
                   font=(FONT_NAME, 35, "bold"))
canvas.pack()


window.mainloop()
