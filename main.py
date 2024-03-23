from time import sleep
from turtle import Screen

# set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# main game loop
game_on = True
while game_on:
    sleep(0.1)
    screen.update()
