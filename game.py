import pygame
from sys import exit
from controller import Controller, CarController
from view import View
from game_elements import (
    Car,
    CarModel1,
    CarModel2,
    CarModel3,
)
from track import Road, StatusTracker
from obstacle import Obstacle
from start_screen import select_car

# start screen set up
car = select_car()

# main screen setup
pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption("Drive Dodge Die")

obstacle = Obstacle(car)
all_obstacles = obstacle.get_all_obstacles
road = Road(5000)
status = StatusTracker()
view = View(car, all_obstacles, road, status)
controller = Controller(status, view, car)

# run the game
while True:
    if status.paused is False:
        controller.basic_event()
        obstacle.update_obstacles()
        controller.game_event()
        # model.update()
        view.draw()

        pygame.display.update()
        clock.tick(60)  # frame/sec
        if obstacle.check_collision():
            break

    else:
        controller.basic_event()
        view.draw_paused_overlay()
        pygame.display.update()
        clock.tick(60)
