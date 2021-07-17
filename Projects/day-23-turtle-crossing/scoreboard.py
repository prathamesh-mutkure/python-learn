from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-235, 270)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.speed("fastest")
        self.goto(POSITION)

        self.level = 1
        self._show_level()

    def _show_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def next_level(self):
        self.level += 1
        self._show_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
