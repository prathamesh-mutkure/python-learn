from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, xpos):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.goto(x=xpos, y=0)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def down(self):
        self.sety(self.ycor() - MOVE_DISTANCE)

    def up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)
