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
states_guessed = []
state_labels = []
while len(states_guessed) < 50:
    answer_state = screen.textinput(
        title=f"Guess a state {len(states_guessed)}/50", prompt="Enter a name").title()

    if answer_state == "Exit":
        missing_states = [
            state for state in all_states if state not in states_guessed]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("D25_CSV/US-states/states_to_learn.csv")
        break

    # check if answer if part of the state list
    if answer_state in all_states:
        states_guessed.append(answer_state)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        # how to hold data of a particular row
        state_data = data[data.state == answer_state]
        state_x = int(state_data.x)
        state_y = int(state_data.y)
        new_turtle.goto(state_x, state_y)
        new_turtle.write(state_data.state.item())
        state_labels.append(new_turtle)
