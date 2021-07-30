import turtle

import pandas

screen= turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guess_states= []

states = pandas.read_csv("50_states.csv")
state_list= states["state"].to_list()
while len(guess_states) < 50:

    answer_state= screen.textinput(title= f"{len(guess_states)} / 50 Guess the State", prompt= "Whats another states' name? ").title()
    if answer_state == "Exit":
        missing_state=[]
        for i in state_list:
            if i not in guess_states:
                missing_state.append(i)
        new_data= pandas.DataFrame(missing_state)
        new_data.to_csv("The State you missed.csv")
        break
    if answer_state in state_list:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states["state"] == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer_state)













screen.exitonclick()
