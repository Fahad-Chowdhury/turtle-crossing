from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """ Generate a new car with a random chance of 1/6 and of of random color.
        Set car at starting position on the right and at random y-axis position,
        and add it to cars list. """
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            new_car.goto(300, rand_y)
            self.cars.append(new_car)

    def move_cars(self):
        """ Move all cars towards the left of the screen with STARTING_MOVE_DISTANCE. """
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        """ On levelling up, increase car speed by MOVE_INCREMENT. """
        self.car_speed += MOVE_INCREMENT
