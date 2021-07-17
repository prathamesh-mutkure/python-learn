from turtle import Turtle, Screen


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def move_clockwise():
    turtle.setheading(turtle.heading() - 5)


def move_counter_clockwise():
    turtle.setheading(turtle.heading() + 5)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


turtle = Turtle()
screen = Screen()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear, "c")

screen.exitonclick()
