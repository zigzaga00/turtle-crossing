from player import Player
from time import sleep
from turtle import Screen

# set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create the player turtle
sam = Player()

# listen for movement
screen.listen()

screen.onkey(sam.up, "Up")

# main game loop
game_on = True
while game_on:
    sleep(0.1)
    screen.update()


screen.exitonclick()
