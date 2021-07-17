from turtle import Turtle

MOVE_DISTANCE = 15


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.draw_line()

    def draw_line(self):
        self.setheading(90)
        self.goto(0, -300)
        self.pensize(5)

        while self.ycor() < 300:
            self.forward(MOVE_DISTANCE)
            self.pendown()
            self.forward(MOVE_DISTANCE)
            self.penup()
