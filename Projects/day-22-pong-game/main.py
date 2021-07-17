from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball
from time import sleep
from line import Line

SCREE_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREE_WIDTH, height=SCREEN_HEIGHT)
screen.title("Day 22 - Pong Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

ball = Ball()
left_paddle = Paddle(xpos=-350)
right_paddle = Paddle(xpos=350)
scoreboard = ScoreBoard()
line = Line()
game_is_on = True

screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

while game_is_on:
    sleep(ball.move_speed)
    screen.update()

    ball.move()

    # Collision with top
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddles
    elif (ball.distance(left_paddle) < 50 and ball.xcor() < -320) or \
            (ball.distance(right_paddle) < 50 and ball.xcor() > 320):
        ball.bounce_x()

    # Right misses
    elif ball.xcor() > 390:
        scoreboard.left_scored()
        ball.reset_position()

    # Left misses
    elif ball.xcor() < -390:
        scoreboard.right_scored()
        ball.reset_position()


screen.exitonclick()
