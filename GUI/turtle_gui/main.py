from turtle import Turtle, Screen
import random

pen = Turtle()
pen.shape("turtle")
pen.color("green")


def set_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    pen.pencolor((r, g, b))


def draw_square():
    for _ in range(4):
        pen.right(90)
        pen.forward(200)


def draw_dashed_line():
    for _ in range(20):
        pen.forward(5)
        pen.penup()
        pen.forward(5)
        pen.pendown()


def draw_angle_pattern():
    for i in range(3, 11):
        r = random.random()
        g = random.random()
        b = random.random()
        pen.pencolor((r, g, b))
        for _ in range(i):
            angle = 360 / i
            pen.forward(100)
            pen.right(angle)


def draw_random_wak():
    direction = [0, 90, 180, 270]
    pen.pensize(10)
    pen.speed("fastest")

    for _ in range(200):
        set_random_color()
        pen.forward(20)
        pen.setheading(random.choice(direction))

    pen.pensize(1)
    pen.speed("normal")


def draw_circle_pattern():
    pen.speed("fastest")
    for angle in range(0, 361, 5):
        set_random_color()
        pen.circle(100)
        pen.setheading(angle)
    pen.speed("normal")


draw_circle_pattern()

screen = Screen()
screen.exitonclick()
