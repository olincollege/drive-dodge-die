import pygame
from sys import exit
from controller import Controller, CarController
from view import View
from game_elements import Car
from track import Road

# main screen setup
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Drive Dodge Die")

car = Car()
road = Road(5000)
view = View(car, road)
controller = Controller()

# run the game
while True:
    controller.handle_events()
    # model.update()
    view.draw()
    pygame.display.update()
    clock.tick(60)  # frame/sec
