import pygame
from sys import exit
from controller import Controller, CarController
from view import View

view = View()
controller = Controller()

# main screen setup
width = 1280
height = 720
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drive Dodge Die")

# run the game
while True:
    controller.handle_events()
    # model.update()
    view.draw(screen, width / 2, 550)
    pygame.display.update()
    clock.tick(60)  # frame/sec
