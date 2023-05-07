from tkinter import Tk, Button, Label, Entry, Canvas, PhotoImage, messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
               "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["1", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", " 0"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?", ">", "<"]

    # list comprehension

    password_letters = [random.choice(letters)
                        for item in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers)
                        for item in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols)
                        for item in range(random.randint(2, 4))]

    # appending the 3 lists and shuffle
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    # join as a string, update the interface and copy to clipboard

    password = ''.join(password_list)
    input_password.delete(0, 100)
    input_password.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    text1 = input_website.get()
    text2 = input_email.get()
    text3 = input_password.get()

    if text1 == "" or text3 == "":
        messagebox.showerror(
            title="Error", message="you need to enter a name and a password")

    else:

        is_ok = messagebox.askokcancel(
            title="website", message=f"These are the details entered:\nemail: {text2}\npassword: {text3}\nis this ok?")

        if is_ok:
            with open('D29_password_manager/data.txt', 'a') as f:
                f.write(f'{text1}  |  {text2}  |  {text3}\n')
            input_website.delete(0, 100)
            input_password.delete(0, 100)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="D29_password_manager/logo.png")
# the position is the center of the image
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=3)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password")
label_password.grid(column=0, row=3)

input_website = Entry(width=55)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()  # to put the cursor in this space

input_email = Entry(width=55)
input_email.insert(0, "myemail@gmail.com")
input_email.grid(column=1, row=2, columnspan=2)

input_password = Entry(width=32)
input_password.grid(column=1, row=3)

button_generate = Button(text="Generate password",
                         command=generate_password, width=18)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", command=add_password, width=47)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
