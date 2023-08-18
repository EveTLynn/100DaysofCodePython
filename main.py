import turtle
import pandas as pd

FONT = ("Courier", 7, "normal")

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_name = turtle.Turtle()
state_name.hideturtle()
df = pd.read_csv("50_states.csv")

guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_state)}/50 States Correct',
                                    prompt="What's another state name?").title()
    if answer_state == 'Exit':
        break
    for state in df.state:
        if answer_state == state:
            df_state = df[df['state'] == answer_state]
            x_cor = int(df_state['x'])
            y_cor = int(df_state['y'])
            state_name.penup()
            state_name.goto(x_cor, y_cor)
            state_name.write(answer_state, align='center', font=FONT)
            guessed_state.append(answer_state)

all_state = df.state.tolist()
learn_state = [state for state in all_state if state not in guessed_state]

learn_df = pd.DataFrame(learn_state)
learn_df.to_csv("learn.csv")

screen.exitonclick()
