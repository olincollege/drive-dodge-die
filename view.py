import pygame
from game_elements import Car

class View:
    def __init__(self, screen, car):
        self.screen = screen
        self.car = car
    def draw(self):
        # Drawing a rectangle
        # pygame.draw.rect(screen, color, (x_coord, y_coord, rect_w, rect_h))
        pygame.draw.rect(self.screen, (0,0,125), (self.car.x_coord, self.car.y_coord, 100, 140)) # should move part of this to model
