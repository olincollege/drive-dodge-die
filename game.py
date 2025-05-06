"""Main game file"""

import pygame
from controller import Controller
from view import View
from track import Road, StatusTracker, CheckPoint
from obstacle import Obstacle
import selection_screen
import end_screen
import sounds
import welcome_screen

GAME_MODE = "start"

# run the game
while True:
    if GAME_MODE == "start":
        # welcome screen
        welcome_screen.welcome()

        # start screen set up
        car = selection_screen.select_car()

        # main screen setup
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Drive Dodge Die")
        sounds.play()
        road = Road()
        status = StatusTracker()
        check_point = CheckPoint(car, road, status)
        obstacle = Obstacle(car, road, check_point)
        all_obstacles = obstacle.all_obstacles
        view = View(car, all_obstacles, road, status, check_point)
        controller = Controller(status, view, car)
        GAME_MODE = "drive"

    elif GAME_MODE == "drive":
        if status.paused is False:
            controller.basic_event()
            obstacle.update_obstacles()
            controller.game_event()
            check_point.check_reach_checkpoint()
            view.draw()
            sounds.unpause_sound()
            pygame.display.update()
            clock.tick(30)
            if obstacle.check_collision():
                GAME_MODE = end_screen.draw_end(
                    road, check_point, status, "collision"
                )
            if status.check_time_up():
                GAME_MODE = end_screen.draw_end(
                    road, check_point, status, "time"
                )

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
                GAME_MODE = status.check_home()
                pygame.display.update()
                clock.tick(60)
                sounds.pause_sound()
    else:
        break
