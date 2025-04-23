import math
import pygame


class View:
    """
    class view - contains all functions related to the view of our game
    """

    def __init__(self, car, road, status):
        self._car = car
        self._road = road
        self._status = status
        self._width = road._width
        self._height = road._height
        self._scroll = 0
        self._screen = pygame.display.set_mode((self._width, self._height))
        self._font = pygame.font.Font(None, 50)
        self._start_time = pygame.time.get_ticks()
        self._pause_img = pygame.image.load(
            "images/buttons/pause_2.png"
        ).convert_alpha()
        self._pause_img = pygame.transform.scale(self._pause_img, (50, 50))
        self._pause_button = self._pause_img.get_rect(topright=(1260, 20))

    @property
    def get_pause_button(self):
        """returns the image of the pause button"""
        return self._pause_button

    def draw(self):
        """
        clears our screen and then draws components
        consists of: car, pause button, timer
        """
        self._screen.fill((0, 0, 0))  # Clear screen
        self.draw_pause_button()
        self.draw_road()
        self.draw_car()
        self.draw_timer()

    def draw_road(self):
        """
        draws the road, updates based on the speed of the car
        """
        image = self._road._image.convert()
        image_height = image.get_height()
        tiles = math.ceil(self._height / image_height) + 1

        for i in range(tiles):
            self._screen.blit(image, (0, image_height * i + self._scroll))

        self._scroll -= (
            self._car._speed
        )  # Scroll upward (positive = down, negative = up)

        # Reset when one image scrolls fully offscreen
        if abs(self._scroll) > image_height:
            self._scroll = 0

    def draw_car(self):
        """
        draws the car (currently a rectangle)
        """
        # Drawing a rectangle (the car)
        pygame.draw.rect(
            self._screen,
            (0, 0, 125),
            (
                self._car._x_coord,
                self._car._y_coord,
                self._car._width,
                self._car._height,
            ),
        )
        # # should move part of this to models

    def draw_timer(self):
        """
        finds the elapsed time and draws teh timer on the screen
        """
        elapsed_time_ms = pygame.time.get_ticks() - self._start_time
        timer_text = self._font.render(
            f"Time: {elapsed_time_ms/1000}s", True, (255, 255, 255)
        )
        self._screen.blit(timer_text, (20, 20))

    def draw_pause_button(self):
        """
        draws the pause button
        might add something to let it change between paused and unpaused states
        """
        self._screen.blit(self._pause_img, self._pause_button)

    def draw_paused_overlay(self):
        """
        draws the overlay of when the game is paused
        """
        overlay = self._font.render("Game Paused", True, (255, 255, 255))
        self._screen.blit(overlay, (self._width // 2 - 100, self._height // 2))
