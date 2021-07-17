# Day 18 - Turtle Challenge

import colorgram
from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)

colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
          (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
          (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
          (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209), ]

pen = Turtle()
pen.hideturtle()
pen.speed("fastest")
pen.penup()
pen.setpos(-200, -200)


def extract_colors():
    rgb_colors = []
    image_colors = colorgram.extract('image.jpg', 30)

    for color in image_colors:
        r, g, b = color.rgb.r, color.rgb.g, color.rgb.b
        rgb_colors.append((r, g, b))

    return rgb_colors


def draw_dots():
    for _ in range(0, 10):
        for _ in range(0, 10):
            random_color = random.choice(colors)
            pen.dot(20, random_color)
            pen.forward(50)
        pen.backward(500)
        pen.left(90)
        pen.forward(50)
        pen.right(90)


draw_dots()

screen = Screen()
screen.exitonclick()
