import pygame


class View:
    def __init__(self, car, road):
        self._car = car
        self._road = road
        self._width = 1280
        self._height = 720
        self._screen = pygame.display.set_mode(
            (self._road._width, self._road._height)
        )

    def draw(self):
        # Drawing a rectangle
        # pygame.draw.rect(screen, color, (x_coord, y_coord, rect_w, rect_h))
        pygame.draw.rect(
            self._screen,
            (0, 0, 125),
            (
                self._car.x_coord,
                self._car.y_coord,
                self._car.width,
                self._car.height,
            ),
        )  # should move part of this to model
