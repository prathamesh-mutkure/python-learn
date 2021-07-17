import turtle
import pandas


class GameController(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.screen = turtle.Screen()
        self.state_data = pandas.read_csv("50_states.csv")

        self.hideturtle()
        self.penup()

    def get_input(self, score):
        answer = self.screen.textinput(title=f"Guess the State: {score}/50", prompt="What's another state's name?")
        return answer.title()

    def check_answer(self, answer):
        state = self.state_data[self.state_data.state == answer]

        if not state.empty:
            self.plot_state(state)
            return True
        else:
            return False

    def plot_state(self, state):
        name = state.iloc[0]['state']
        x = state.iloc[0]['x']
        y = state.iloc[0]['y']

        self.goto(x, y)
        self.write(name)
