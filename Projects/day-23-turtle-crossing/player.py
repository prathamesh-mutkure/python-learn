from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.init_position()

    def init_position(self):
        self.goto(STARTING_POSITION)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        if self.ycor() > -300:
            self.forward(-MOVE_DISTANCE)

    def did_cross_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
