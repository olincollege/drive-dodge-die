import pygame
from sys import exit
from controller import Controller, CarController
from view import View
from game_elements import Car

# main screen setup
width = 1280
height = 720
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drive Dodge Die")

car = Car(width / 2, 550)
view = View(screen, car)
controller = Controller()

# run the game
while True:
    controller.handle_events()
    # model.update()
    view.draw()
    pygame.display.update()
    clock.tick(60)  # frame/sec
