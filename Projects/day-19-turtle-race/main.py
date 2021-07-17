from turtle import Turtle, Screen
import random

color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

screen = Screen()
screen.setup(width=500, height=400)


def on_your_marks():
    x = -230
    y = -150
    for color in color_list:
        turtle = Turtle("turtle")
        turtle.color(color)
        turtle.penup()
        turtle.goto(x, y)
        turtle.speed(random.randint(4, 10))
        turtle_list.append(turtle)
        y += 60


def go():
    while True:
        for turtle in turtle_list:
            turtle.forward(random.randint(0, 10))
            if turtle.xcor() > 230:
                return turtle.pencolor()


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you think will win? ").lower()
on_your_marks()
if user_bet in color_list:
    winner = go()

    if winner == user_bet:
        print("WON")
    else:
        print("LOSE")

screen.exitonclick()
