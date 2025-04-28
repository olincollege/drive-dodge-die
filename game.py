"""Main game file"""

import pygame
from controller import Controller
from view import View
from track import Road, StatusTracker, CheckPoint
from obstacle import Obstacle
import selection_screen
import end_screen

# start screen set up
car = selection_screen.select_car()

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
        view.draw()

        pygame.display.update()
        clock.tick(60)
        if obstacle.check_collision():
            end_screen.draw_end(road, check_point, view)
            break
        if check_point.check_reach_checkpoint():
            check_point.add_one()

    else:
        controller.basic_event()
        view.draw_paused_overlay()
        pygame.display.update()
        clock.tick(60)
