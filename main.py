import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player1=Player()
Ccar_manager=CarManager()
screen.listen()
screen.onkey(player1.move_on,"Up")
game_is_on = True
wynik=Scoreboard()

while game_is_on:
    time.sleep(0.1)
    #player1.move_on()
    screen.update()
    Ccar_manager.create_cars()
    Ccar_manager.move_cars()

    for car in Ccar_manager.all_cars:
        if car.distance(player1) <20:
            wynik.game_over()
            game_is_on=False

    if player1.is_at_finish():
        player1.go_to_start()
        Ccar_manager.move_faster()
        wynik.increase_level()


screen.exitonclick()