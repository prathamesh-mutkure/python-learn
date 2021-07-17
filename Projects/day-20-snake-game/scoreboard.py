from turtle import Turtle

SCORE_FONT = ("Arial", 16, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()

        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(x=0, y=280)
        self.display_score()

    @staticmethod
    def get_high_score():
        with open("data.txt") as file:
            high_score = int(file.read())
            return high_score

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} \t High Score: {self.high_score}", align=ALIGNMENT, font=SCORE_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=SCORE_FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.display_score()

    def increment_score(self):
        self.score += 1
        self.display_score()
