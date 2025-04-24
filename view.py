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
        self._big_font = pygame.font.Font(None, 50)
        self._small_font = pygame.font.Font(None, 20)
        self._start_time = pygame.time.get_ticks()

        self._pause_img = pygame.image.load(
            "images/buttons/pause_2.png"
        ).convert_alpha()
        self._pause_img = pygame.transform.scale(self._pause_img, (50, 50))
        self._pause_button = self._pause_img.get_rect(topright=(1260, 20))

        self._gas_img = pygame.image.load("images/gas_bar.png").convert_alpha()
        self._gas_img = pygame.transform.scale(self._gas_img, (75, 400))
        self._gas_bar = self._gas_img.get_rect(topleft=(1150, 180))

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
        self.draw_minimap()
        self.draw_gas()
        self.draw_speed()

    def draw_minimap(self):
        """draws the minimap
        aka how far the car has traveled and how much distance is left"""
        # draws the total length of race track
        pygame.draw.rect(
            self._screen,
            (120, 0, 0),
            (250, 30, self._road._length // 10, 20),
        )
        # draws the position of the car
        pygame.draw.rect(
            self._screen,
            (0, 120, 0),
            (250 + self._road._distance_traveled // 10, 40, 10, 10),
        )
        # writes out how far you have traveled
        distance_left = math.ceil(
            self._road._length - self._road._distance_traveled
        )
        minimap_text = self._small_font.render(
            f"Distance left: {distance_left}",
            True,
            (255, 255, 255),
        )
        self._screen.blit(minimap_text, (250, 10))

    def draw_gas(self):
        """draws amount of gas left"""
        # draws gas bar gradient
        self._screen.blit(self._gas_img, self._gas_bar)
        background_color = (0, 0, 0)
        percent_gas_used = (
            self._car.max_gas - self._car.gas_amt
        ) / self._car.max_gas
        percent_covered = percent_gas_used * 400
        pygame.draw.rect(
            self._screen, background_color, (1150, 180, 75, percent_covered)
        )
        # writes how much gas is left
        gas_text = self._small_font.render(
            f"Gas left:{self._car.gas_amt}", True, (255, 255, 255)
        )
        self._screen.blit(gas_text, (1150, 585))

    def draw_speed(self):
        """draws the speed of the car"""
        # draw circle that speed will be on
        pygame.draw.circle(self._screen, (100, 100, 100), (1190, 670), 60)

    def draw_road(self):
        """
        draws the road, updates based on the speed of the car
        """
        image = self._road._image.convert()
        image_height = image.get_height()

        # Calculate the exact position of the first image
        first_tile_position = self._scroll % image_height - image_height

        # Draw enough tiles to cover the screen
        tiles_needed = math.ceil(self._height / image_height) + 2

        for i in range(tiles_needed):
            position_y = first_tile_position + (image_height * i)
            self._screen.blit(image, (0, position_y))

        # Update scroll position
        self._scroll += self._car._speed
        self._road.update_travel_distance(self._scroll)

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
        # should move part of this to models

    def draw_timer(self):
        """
        finds the elapsed time and draws teh timer on the screen
        """
        elapsed_time_ms = pygame.time.get_ticks() - self._start_time
        timer_text = self._big_font.render(
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
        overlay = self._big_font.render("Game Paused", True, (255, 255, 255))
        self._screen.blit(overlay, (self._width // 2 - 100, self._height // 2))
