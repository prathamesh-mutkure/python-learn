from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self._init_cars()

    def _init_cars(self):
        for i in range(0, 5):
            self.new_car()

    def new_car(self):
        car = self.create_car()
        self.cars.append(car)
        self.remove_cars()

    def create_car(self):
        car = Turtle("square")
        car.setheading(180)
        car.color(random.choice(COLORS))
        car.penup()
        car.shapesize(stretch_len=2.5)

        x = 320 + random.randint(20, 80)        # Shift out of screen by x_shift
        y = random.randint(-250, 250)

        car.goto(x, y)
        car.forward(self.car_speed)

        return car

    def move_all_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

    def did_player_collide(self, player):
        for car in self.cars:
            if car.distance(player) < 25:
                return True

        return False

    def remove_cars(self):
        for car in self.cars:
            if car.xcor() < -350:
                self.cars.remove(car)
