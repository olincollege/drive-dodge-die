"""Main game file"""

import pygame
from controller import Controller
from view import View
from track import Road, StatusTracker, CheckPoint
from obstacle import Obstacle
import selection_screen
import end_screen
import sounds

# start screen set up
car = selection_screen.select_car()

# main screen setup
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Drive Dodge Die")
sounds.play()
road = Road()
obstacle = Obstacle(car, road)
all_obstacles = obstacle.all_obstacles
status = StatusTracker()
check_point = CheckPoint(car, road, status)
view = View(car, all_obstacles, road, status, check_point)
controller = Controller(status, view, car)

# run the game
while True:
    if status.paused is False:
        controller.basic_event()
        obstacle.update_obstacles()
        controller.game_event()
        check_point.check_reach_checkpoint()
        view.draw()
        sounds.unpause_sound()

        pygame.display.update()
        clock.tick(60)
        if obstacle.check_collision():
            end_screen.draw_end(road, check_point, view)
            break

    else:
        if status.is_powerup:
            controller.basic_event()
            view.draw_powerup_overlay()
            sounds.pause_sound()
            pygame.display.update()
            clock.tick(60)
        else:
            controller.basic_event()
            view.draw_paused_overlay()
            pygame.display.update()
            clock.tick(60)
