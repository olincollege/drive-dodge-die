import pygame
from sys import exit
from controller import Controller, CarController
from view import View
from game_elements import Car
from track import Road, StatusTracker

# main screen setup
pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption("Drive Dodge Die")

car = Car()
road = Road(5000)
status = StatusTracker()
view = View(car, road, status)
controller = Controller(status, view)

# run the game
while True:
    if status.paused is False:
        controller.basic_event()
        controller.game_event()
        # model.update()
        view.draw()

        pygame.display.update()
        clock.tick(60)  # frame/sec
    else:
        controller.basic_event()
        view.draw_paused_overlay()
        pygame.display.update()
        clock.tick(60)
