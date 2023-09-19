# this small app used TKinter and the quotes API from API-ninjas.com
# to show a random quote related to "happiness"

from tkinter import Tk, Canvas, PhotoImage, Button
import requests
APIKEY = "gA38jRh7gSNpS7ZbFEvQ9A==T6hFbbNddMI1govT"


def get_quote():
    category = 'happiness'
    api_url = f"https://api.api-ninjas.com/v1/quotes?category={category}"
    response = requests.get(api_url, headers={'X-Api-Key': APIKEY})
    if response.status_code == requests.codes.ok:
        print(response.text)
        quote = response.json()[0]["quote"]
        author = response.json()[0]["author"]
        canvas.itemconfig(quote_text, text=f"{quote}\n\n{author}")
        print(f"'{quote}' - {author}")

    else:
        print("Error:", response.status_code, response.text)

    pass
    # Write your code here.


window = Tk()
window.title("the key to happiness...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="D33_API/resources/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 180, text="", width=250, font=(
    "Arial", 12, "bold"), fill="black")
canvas.grid(row=0, column=0)

emoji = PhotoImage(file="D33_API/resources/emoji.png")
emoji_button = Button(image=emoji, highlightthickness=0, command=get_quote)
emoji_button.grid(row=1, column=0)
get_quote()

window.mainloop()
