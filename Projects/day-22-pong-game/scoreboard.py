from turtle import Turtle

SCORE_FONT = ("Arial", 48, "bold")
Y_COORD = 240


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.goto(x=0, y=Y_COORD)
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def left_scored(self):
        self.left_score += 1
        self.update_score()

    def right_scored(self):
        self.right_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.left_score}   {self.right_score}", align="center", font=SCORE_FONT)
