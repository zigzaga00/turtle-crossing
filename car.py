from random import randint
from turtle import Turtle

COLORS = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple"
]
START_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car:
    def __init__(self):
        self.cars = []

    def create_car(self):
        car_chance = randint(1, 6)
        if car_chance == 1:
            car = Turtle("square")
            car.color(COLORS[randint(0, 5)])
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(280, randint(-250, 250))
            car.setheading(180)
            self.cars.append(car)

    def car_move(self):
        for car in self.cars:
            car.fd(START_MOVE_DISTANCE)