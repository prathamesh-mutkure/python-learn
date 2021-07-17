import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_backward, "Down")

game_is_on = True
iterations = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    iterations += 1

    car_manager.move_all_cars()

    if player.did_cross_finish_line():
        scoreboard.next_level()
        car_manager.speed_up()
        player.init_position()

    if car_manager.did_player_collide(player):
        game_is_on = False
        scoreboard.game_over()

    if iterations >= 8:
        car_manager.new_car()
        iterations = 0

screen.exitonclick()
