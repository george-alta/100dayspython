import turtle
from datetime import date
from tkinter import Tk, Button, Label, Entry

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)
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
my_label.pack()  # this is necessary to show the element
# my_label["text"] = "New Text" ### one of the ways to change the label content

# tim = turtle.Turtle()
# tim.write("some text", font=("Times new Roman", 8, "normal"))
input = Entry(width=10)
input.pack()

# button
button = Button(text="Click me", command=button_clicked)
button.pack()

# pack goes from top to bottom
# place gives precise location (x,y)
# eg: my_label.place(x=100, y=100)


window.mainloop()
