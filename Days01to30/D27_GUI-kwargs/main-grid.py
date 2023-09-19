import turtle
from datetime import date
from tkinter import Tk, Button, Label, Entry

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
today = date.today()


def button_clicked():  # the label content will change with the textbox content once the button is clicked
    text_entered = input.get()
    window.clipboard_clear()
    window.clipboard_append(f"{text_entered} {today.strftime('%d-%m-%Y')}")
    print("I got clicked")
    print(text_entered)
    my_label.config(text=text_entered)
    # my_label.config(text="I got clicked")


# 1st create component
# 2nd define how is going to be shown
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)  # this is necessary to show the element
my_label.config(padx=10, pady=10)
# my_label["text"] = "New Text" ### one of the ways to change the label content

# tim = turtle.Turtle()
# tim.write("some text", font=("Times new Roman", 8, "normal"))
input = Entry(width=10)
input.grid(column=3, row=2)


# button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=10, pady=10)

# pack goes from top to bottom
# place gives precise location (x,y)
# eg: my_label.place(x=100, y=100)
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)
new_button.config(padx=10, pady=10)

window.mainloop()
