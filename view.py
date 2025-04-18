import pygame
from game_elements import Car

class View:
    def __init__(self, car):
        self.car = car
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw(self):
        # Drawing a rectangle
        # pygame.draw.rect(screen, color, (x_coord, y_coord, rect_w, rect_h))
        pygame.draw.rect(self.screen, (0,0,125), (self.car.x_coord, self.car.y_coord, self.car.width, self.car.height)) # should move part of this to model
