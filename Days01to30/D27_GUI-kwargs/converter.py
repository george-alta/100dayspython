from tkinter import Tk, Button, Label, Entry
window = Tk()
window.title("Mile to KM converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

FONT_SIZE = 10
PADDING = 20


def button_clicked():
    number = input.get()
    km = round(float(number) * 1.609, 2)
    label3.config(text=km)


input = Entry(width=10)
input.grid(column=1, row=0)


label1 = Label(text="Miles", font=("Arial", FONT_SIZE, "bold"))
label1.grid(column=2, row=0)
label1.config(padx=PADDING, pady=PADDING)

label2 = Label(text="Is equal to", font=("Arial", FONT_SIZE, "bold"))
label2.grid(column=0, row=1)
label2.config(padx=PADDING, pady=PADDING)

label3 = Label(text="", font=("Arial", FONT_SIZE, "bold"))
label3.grid(column=1, row=1)
label3.config(padx=PADDING, pady=PADDING)

label4 = Label(text="Km", font=("Arial", FONT_SIZE, "bold"))
label4.grid(column=2, row=1)
label4.config(padx=PADDING, pady=PADDING)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
# button.config(padx=10, pady=10)
# button.config(padx=10, pady=10)

window.mainloop()
