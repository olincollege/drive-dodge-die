import math
import pygame


class View:
    """
    class view - contains all functions related to the view of our game
    """

    def __init__(self, car, all_obstacles, road, status):
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
        self.draw_obstacles()
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

    def draw_speed(self):
        """writes the speed of the car and draws a speedometer"""
        # draw circle that speed will be on
        pygame.draw.circle(self._screen, (100, 100, 100), (1190, 670), 60)
        # writes the speed at the bottom of the circle
        speed_text = self._small_font.render(
            f"Speed: {math.ceil(self._car.get_speed)}", True, (255, 255, 255)
        )
        self._screen.blit(speed_text, (1160, 690))
        # creates the arc
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
        total = end_angle - start_angle
        angle = self._car.get_speed / self._car.get_max_speed

        start = angle * total
        start = total - start
        start = start_angle + start
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
        # Drawing a rectangle (the car)
        car_rect = pygame.Rect(
            self._car.get_x_coord,
            self._car.get_y_coord,
            self._car.get_width,
            self._car.get_height,
        )
        pygame.draw.rect(self._screen, (0, 0, 125), car_rect)

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
                    barrier.update_obstacle(self._car),
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

    def draw_paused_overlay(self):
        """
        draws the overlay of when the game is paused
        """
        overlay = self._big_font.render("Game Paused", True, (255, 255, 255))
        self._screen.blit(overlay, (self._width // 2 - 100, self._height // 2))
