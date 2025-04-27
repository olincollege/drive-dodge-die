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
from track import Road, StatusTracker, CheckPoint
from obstacle import Obstacle
import start_screen

# start screen set up
car = start_screen.select_car()

# main screen setup
pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption("Drive Dodge Die")

road = Road(5000)
obstacle = Obstacle(car, road)
all_obstacles = obstacle.get_all_obstacles
status = StatusTracker()
check_point = CheckPoint(5000, car, road)
view = View(car, all_obstacles, road, status, check_point)
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
        if check_point.check_reach_checkpoint():
            print("Hit Checkpoint!")

    else:
        controller.basic_event()
        view.draw_paused_overlay()
        pygame.display.update()
        clock.tick(60)
