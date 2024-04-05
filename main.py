from car import Car
from player import Player
from random import randint
from time import sleep
from turtle import Screen

# set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create the player turtle
sam = Player()

# create a car controller
car_contoller = Car()

# listen for movement
screen.listen()

screen.onkey(sam.up, "Up")

# main game loop
game_on = True
while game_on:
    sleep(0.1)
    screen.update()
    car_contoller.create_car()
    car_contoller.car_move()
    for car in car_contoller.cars:
        if car.distance(sam) <= 20:
            game_on = False
    if sam.player_win():
        car_contoller.next_level()
        sam.goto(0, -280)

screen.exitonclick()
