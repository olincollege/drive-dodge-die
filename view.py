"""View file"""

import math
import pygame
import random


class View:
    """
    class view - contains all functions related to the view of our game
    """

    def __init__(self, car, all_obstacles, road, status, check_point):
        self._car = car
        self._all_obstacles = all_obstacles
        self._road = road
        self._status = status
        self._width = road.width
        self._height = road.height
        self._scroll = 0
        self._screen = pygame.display.set_mode((self._width, self._height))
        self._big_font = pygame.font.Font(None, 50)
        self._small_font = pygame.font.Font(None, 20)
        self._start_time = pygame.time.get_ticks()

        self._pause_img = pygame.image.load(
            "images/buttons/pause.png"
        ).convert_alpha()
        self._pause_img = pygame.transform.scale(
            self._pause_img, (50, 50)
        )  # width, height
        self._pause_button = self._pause_img.get_rect(
            topright=(1260, 20)
        )  # x_coord, y_coord

        self._check_point = check_point

        self._overlay_buttons = {}
        self._powerup_choice = {}
        self._chosen_texts = None

        self.countdown_time = (
            30 * 1000
        )  # change this to be the idle speed x distance till next checkpoint
        self._time_left = self.countdown_time

    @property
    def pause_button(self):
        """returns the image of the pause button"""
        return self._pause_button

    def draw(self):
        """
        clears our screen and then draws components
        consists of: car, pause button, timer

        note: screen size = (1280, 950)
        """
        self._screen.fill((0, 0, 0))  # Clear screen
        self.draw_road()
        self.draw_check_point()
        self.draw_car()
        self.draw_obstacles()
        self.draw_timer()
        self.draw_minimap()
        self.draw_gas()
        self.draw_speed()
        self.draw_pause_button()

    def draw_minimap(self):
        """draws the minimap
        aka how far the car has traveled and how much distance is left"""
        # draws the total length of race track
        pygame.draw.rect(
            self._screen,
            (120, 0, 0),
            (250, 30, self._road.length // 10, 20),
        )
        # draws the position of the car
        pygame.draw.rect(
            self._screen,
            (0, 120, 0),
            (250 + self._road.distance_traveled // 10, 40, 10, 10),
        )
        # writes out how far you have traveled
        distance_left = math.ceil(
            self._road.length - self._road.distance_traveled
        )
        minimap_text = self._small_font.render(
            f"Distance left until next checkpoint: {distance_left}",
            True,
            (255, 255, 255),
        )
        self._screen.blit(minimap_text, (250, 10))

    def draw_gas(self):
        """draws amount of gas left"""
        # draws gas bar gradient
        gas_img = pygame.image.load("images/gas_bar.png").convert_alpha()
        gas_img = pygame.transform.scale(gas_img, (75, 400))
        gas_bar = gas_img.get_rect(topleft=(1150, 180))

        self._screen.blit(gas_img, gas_bar)
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
        # writes the speed at the bottom of the circle
        speed_text = self._small_font.render(
            f"Speed: {math.ceil(self._car.speed)}", True, (255, 255, 255)
        )
        self._screen.blit(speed_text, (1160, 690))
        # draws the full arc
        arc_rect = pygame.Rect((1190, 670), (100, 100))
        arc_rect.center = (1190, 670)
        start_angle = -0.5
        end_angle = 3.6
        pygame.draw.arc(
            self._screen,
            (250, 140, 20),
            arc_rect,
            start_angle,
            end_angle,
            width=7,
        )
        # calculate angle of changing arc
        total = end_angle - start_angle
        angle = self._car.speed / self._car.max_speed

        start = angle * total
        start = total - start
        start = start_angle + start
        # draws changing arc
        arc_rect.scale_by_ip(0.9)
        pygame.draw.arc(
            self._screen,
            (250, 0, 20),
            arc_rect,
            start,
            end_angle,
            width=5,
        )

    def draw_road(self):
        """
        draws the road, updates based on the speed of the car
        """
        image = self._road.image.convert()
        image_height = image.get_height()

        # Calculate the exact position of the first image
        first_tile_position = self._scroll % image_height - image_height

        # Draw enough tiles to cover the screen
        tiles_needed = math.ceil(self._height / image_height) + 1

        for i in range(tiles_needed):
            position_y = first_tile_position + (image_height * i)
            self._screen.blit(image, (0, position_y))

        # Update scroll position
        self._scroll += self._car.speed
        self._road.update_travel_distance(self._scroll)

    def draw_car(self):
        """
        draws the car (currently a rectangle)
        """
        image_path = self._car.image_path
        car_image = pygame.image.load(image_path).convert_alpha()
        car_image = pygame.transform.scale(
            car_image,
            (
                self._car.width + 50,
                self._car.height + 50,
            ),  # adjusted due to original size of pic being different
        )
        self._screen.blit(car_image, (self._car.x_coord, self._car.y_coord))

    def draw_obstacles(self):
        """Randomly generate obstacles"""
        self.draw_barriers()

    def draw_barriers(self):
        """draws and updates the y coord of the barriers"""
        barriers = self._all_obstacles["barriers"]
        for barrier in barriers:
            barrier.update_obstacle()
            self._screen.blit(barrier.image, (barrier.x_coord, barrier.y_coord))

    def draw_timer(self):
        """
        finds the elapsed time and draws teh timer on the screen
        """
        elapsed_time_ms = pygame.time.get_ticks() - self._start_time
        self._time_left = max(self.countdown_time - elapsed_time_ms, 0)
        time_left_seconds = math.ceil(self._time_left / 1000)

        timer_text = self._big_font.render(
            f"Time Left: {time_left_seconds}s", True, (255, 255, 255)
        )
        self._screen.blit(timer_text, (20, 20))

    def draw_pause_button(self):
        """
        draws the pause button
        might add something to let it change between paused and unpaused states
        """
        self._screen.blit(self._pause_img, self._pause_button)

    def draw_check_point(self):
        """
        draws the checkpoint line
        """
        line_img = pygame.image.load(
            "images/other/check_point.png"
        ).convert_alpha()
        line_img = pygame.transform.scale(
            line_img,
            (self._check_point._width, self._check_point._height),
        )
        check_point = self._pause_img.get_rect(
            topleft=(
                self._check_point._x_coord,
                self._check_point.update_check_point_y_coord(),
            )
        )
        self._screen.blit(line_img, check_point)

    def draw_paused_overlay(self):
        """
        draws the overlay of when the game is paused
        """
        # Create a semi-transparent surface
        overlay_width = 750
        overlay_height = 500
        overlay = pygame.Surface(
            (overlay_width, overlay_height), pygame.SRCALPHA
        ).convert_alpha()
        overlay.fill((0, 0, 0, 0))
        overlay_x = (self._width - overlay_width) // 2
        overlay_y = (self._height - overlay_height) // 2
        self._screen.blit(overlay, (overlay_x, overlay_y))

        # "Game Paused" text
        title_text = self._big_font.render("Game Paused", True, (255, 255, 255))
        title_rect = title_text.get_rect(
            center=(self._width // 2, overlay_y + 70)
        )
        self._screen.blit(title_text, title_rect)

        # Draw button rectangles
        button_width = 150
        button_height = 50
        button_spacing = 50

        button_texts = ["Resume", "Back to Home Screen"]

        start_y = overlay_y + 175

        for i, text in enumerate(button_texts):
            rect = pygame.Rect(0, 0, button_width, button_height)
            rect.center = (
                self._width // 2,
                start_y + i * (button_height + button_spacing),
            )
            button = pygame.draw.rect(
                self._screen, (255, 255, 255), rect, border_radius=10
            )
            self._overlay_buttons[text] = button
            button_text = self._small_font.render(text, True, (0, 0, 0))
            button_text_rect = button_text.get_rect(center=rect.center)
            self._screen.blit(button_text, button_text_rect)

    def draw_powerup_overlay(self):
        """
        Draws two powerup choices
        """
        self._powerup_choice.clear()
        button_width = 400
        button_height = 700
        button_spacing = 50

        button_texts = [
            "Increase Max Speed",
            "Increase Max Gas",
            "Increase Acceleration",
            "Increase Gas Refresh Rate",
            "Immediate Gas Refill",
        ]

        # Calculate button positions so that they are centered
        total_width = 2 * button_width + button_spacing
        start_x = (self._width - total_width) // 2
        center_y = self._height // 2

        if self._chosen_texts is None:
            self._chosen_texts = random.sample(button_texts, 2)

        for i, text in enumerate(self._chosen_texts):
            rect = pygame.Rect(0, 0, button_width, button_height)
            rect.center = (
                start_x
                + i * (button_width + button_spacing)
                + button_width // 2,
                center_y,
            )
            button = pygame.draw.rect(
                self._screen, (200, 50, 100, 200), rect, border_radius=20
            )
            self._powerup_choice[text] = button

            button_text = self._small_font.render(text, True, (0, 0, 0))
            button_text_rect = button_text.get_rect(center=rect.center)
            self._screen.blit(button_text, button_text_rect)

    def reset_chosen_texts(self):
        self._chosen_texts = None

    @property
    def overlay_buttons(self):
        """
        returns the dictionary of all buttons on pause overlay
        """
        return self._overlay_buttons

    @property
    def powerup_choice(self):
        """
        returns the dictionary of all choices on powerup overlay
        """
        return self._powerup_choice

    @property
    def start_time(self):
        """returns start time"""
        return self._start_time
