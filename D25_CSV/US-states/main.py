import pandas
import turtle

screen = turtle.Screen()
# turtle = turtle.Turtle()
screen.title("US States Game")
image = "D25_CSV/US-states/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("D25_CSV/US-states/50_states.csv")
all_states = data["state"].to_list()
print(data)
states_guessed = 0
state_labels = []
while states_guessed < 50:
    answer_state = screen.textinput(
        title=f"Guess a state {states_guessed}/50", prompt="Enter a name")
    # answer_state = answer_state.lower()
    print(answer_state)

    # check if answer if part of the state list
    if answer_state in all_states:
        data[data.state == answer_state]
        states_guessed += 1
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        # how to hold data of a particular row
        state_data = data[data.state == answer_state]
        state_x = int(state_data.x)
        state_y = int(state_data.y)
        print(f"Coord: {state_x},{state_y}")
        new_turtle.goto(state_x, state_y)
        new_turtle.write(state_data.state.item())
        state_labels.append(new_turtle)


screen.exitonclick()
