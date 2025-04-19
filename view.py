import pygame
from game_elements import Car


class View:
    def __init__(self, car, road, status):
        self._car = car
        self._road = road
        self._status = status
        self._width = 1280
        self._height = 720
        self._screen = pygame.display.set_mode(
            (self._road._width, self._road._height)
        )
        self._font = pygame.font.Font(None, 50)
        self._start_time = pygame.time.get_ticks()
        self._pause_img = pygame.image.load(
            "images/buttons/pause_2.png"
        ).convert_alpha()
        self._pause_img = pygame.transform.scale(self._pause_img, (50, 50))
        self._pause_button = self._pause_img.get_rect(topright=(1260, 20))

    @property
    def get_pause_button(self):
        return self._pause_button

    def draw(self):
        self._screen.fill((0, 0, 0))  # Clear screen
        self.draw_pause_button()
        self.draw_car()
        self.draw_timer()

    def draw_car(self):
        pass
        # Drawing a rectangle (the car)
        # pygame.draw.rect(self._screen, (0,0,125), (self._car._x_coord, self._car._y_coord, self._car._width, self._car._height)) # should move part of this to model

    def draw_timer(self):
        elapsed_time_ms = pygame.time.get_ticks() - self._start_time
        timer_text = self._font.render(
            f"Time: {elapsed_time_ms/1000}s", True, (255, 255, 255)
        )
        self._screen.blit(timer_text, (20, 20))

    def draw_pause_button(self):
        self._screen.blit(self._pause_img, self._pause_button)

    def draw_paused_overlay(self):
        overlay = self._font.render("Game Paused", True, (255, 255, 255))
        self._screen.blit(overlay, (self._width // 2 - 100, self._height // 2))
