import pygame
from game_elements import Car


class View:
    def __init__(self, car, road):
        self._car = car
        self._road = road
        self._width = 1280
        self._height = 720
        self._screen = pygame.display.set_mode(
            (self._road._width, self._road._height)
        )
        self._start_time = pygame.time.get_ticks()

    def draw(self):
        self._screen.fill((0, 0, 0))  # Clear screen
        self.draw_car()
        self.draw_clock()

    def draw_car(self):
        pass
        # Drawing a rectangle (the car)
        # pygame.draw.rect(self._screen, (0,0,125), (self._car._x_coord, self._car._y_coord, self._car._width, self._car._height)) # should move part of this to model

    def draw_clock(self):
        elapsed_seconds = (pygame.time.get_ticks() - self._start_time) // 1000

        font = pygame.font.Font(None, 50)
        timer_text = font.render(
            f"Time: {elapsed_seconds}s", True, (255, 255, 255)
        )

        self._screen.blit(timer_text, (20, 20))
