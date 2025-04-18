import pygame

class View:
    def draw(self, screen, x_coord, y_coord):
        # Drawing a rectangle
        # pygame.draw.rect(screen, color, (x_coord, y_coord, rect_w, rect_h))
        pygame.draw.rect(screen, (0,0,125), (x_coord, y_coord, 100, 140)) # should move part of this to model
