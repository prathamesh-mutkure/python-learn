import turtle
from game_controller import GameController

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_controller = GameController()
game_is_on = True
score = 0

while game_is_on:
    answer = game_controller.get_input(score)
    game_is_on = game_controller.check_answer(answer)
    if game_is_on:
        score += 1

screen.mainloop()
