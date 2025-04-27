import math
import pygame


class View:
    """
    class view - contains all functions related to the view of our game
    """

    def __init__(self, car, all_obstacles, road, status, check_point):
        self._car = car
        self._all_obstacles = all_obstacles
        self._road = road
        self._status = status
        self._width = road.get_width
        self._height = road.get_height
        self._scroll = 0
        self._screen = pygame.display.set_mode((self._width, self._height))
        self._big_font = pygame.font.Font(None, 50)
        self._small_font = pygame.font.Font(None, 20)
        self._start_time = pygame.time.get_ticks()

        self._pause_img = pygame.image.load(
            "images/buttons/pause_2.png"
        ).convert_alpha()
        self._pause_img = pygame.transform.scale(
            self._pause_img, (50, 50)
        )  # width, height
        self._pause_button = self._pause_img.get_rect(
            topright=(1260, 20)
        )  # x_coord, y_coord

        self._gas_img = pygame.image.load("images/gas_bar.png").convert_alpha()
        self._gas_img = pygame.transform.scale(self._gas_img, (75, 400))
        self._gas_bar = self._gas_img.get_rect(topleft=(1150, 180))

        self._check_point = check_point
        self._line_img = pygame.image.load(
            "images/other/check_point.png"
        ).convert_alpha()
        self._line_img = pygame.transform.scale(
            self._line_img,
            (self._check_point._width, self._check_point._height),
        )
        self._overlay_buttons = {}

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
        self.draw_check_point()
        self.draw_car()
        self.draw_obstacles()
        self.draw_timer()
        self.draw_minimap()
        self.draw_gas()
        # self.draw_speed()

    def draw_minimap(self):
        """draws the minimap
        aka how far the car has traveled and how much distance is left"""
        # draws the total length of race track
        pygame.draw.rect(
            self._screen,
            (120, 0, 0),
            (250, 30, self._road.get_length // 10, 20),
        )
        # draws the position of the car
        pygame.draw.rect(
            self._screen,
            (0, 120, 0),
            (250 + self._road.get_distance_traveled // 10, 40, 10, 10),
        )
        # writes out how far you have traveled
        distance_left = math.ceil(
            self._road.get_length - self._road.get_distance_traveled
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
            self._car.get_max_gas - self._car.get_gas_amt
        ) / self._car.get_max_gas
        percent_covered = percent_gas_used * 400
        pygame.draw.rect(
            self._screen, background_color, (1150, 180, 75, percent_covered)
        )
        # writes how much gas is left
        gas_text = self._small_font.render(
            f"Gas left:{self._car.get_gas_amt}", True, (255, 255, 255)
        )
        self._screen.blit(gas_text, (1150, 585))

    # def draw_speed(self):
    #     """draws the speed of the car"""
    #     # draw circle that speed will be on
    #     pygame.draw.circle(self._screen, (100, 100, 100), (1190, 670), 60)
    #     # writes the speed at the bottom of the circle
    #     speed_text = self._small_font.render(
    #         f"Speed: {math.ceil(self._car.get_speed)}", True, (255, 255, 255)
    #     )
    #     self._screen.blit(speed_text, (1160, 690))
    #     # creates the arc
    #     arc_rect = pygame.Rect(120, 120, center=(1190, 670))
    #     pygame.draw.arc(self._screen, (250, 140, 20), arc_rect, 0, 260)

    def draw_road(self):
        """
        draws the road, updates based on the speed of the car
        """
        image = self._road.get_image.convert()
        image_height = image.get_height()

        # Calculate the exact position of the first image
        first_tile_position = self._scroll % image_height - image_height

        # Draw enough tiles to cover the screen
        tiles_needed = math.ceil(self._height / image_height) + 2

        for i in range(tiles_needed):
            position_y = first_tile_position + (image_height * i)
            self._screen.blit(image, (0, position_y))

        # Update scroll position
        self._scroll += self._car.get_speed
        self._road.update_travel_distance(self._scroll)

    def draw_car(self):
        """
        draws the car (currently a rectangle)
        """
        car_image = pygame.image.load("images/cars/car.png").convert_alpha()
        car_image = pygame.transform.scale(
            car_image,
            (
                self._car.get_width + 50,
                self._car.get_height + 50,
            ),  # adjusted due to original size of pic being different
        )
        self._screen.blit(
            car_image, (self._car.get_x_coord, self._car.get_y_coord)
        )

    def draw_obstacles(self):
        """Randomly generate obstacles"""
        self.draw_barriers()

    def draw_barriers(self):
        barriers = self._all_obstacles["barriers"]
        for barrier in barriers:
            pygame.draw.rect(
                self._screen,
                (255, 255, 0),
                (
                    barrier._x_coord,
                    barrier.update_obstacle(),
                    barrier._width,
                    barrier._height,
                ),
            )

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

    def draw_check_point(self):
        check_point = self._pause_img.get_rect(
            topleft=(
                self._check_point._x_coord,
                self._check_point.update_check_point(),
            )
        )
        self._screen.blit(self._line_img, check_point)

    def draw_paused_overlay(self):
        """
        draws the overlay of when the game is paused
        """
        # Create a semi-transparent surface
        overlay_width = 750
        overlay_height = 500
        overlay = pygame.Surface((overlay_width, overlay_height))

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

        button_texts = ["Resume", "Save", "Back to Home Screen"]

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
    
    @property
    def get_overlay_buttons(self):
        """
        returns the dictionary of all buttons on pause overlay
        """
        return self._overlay_buttons
