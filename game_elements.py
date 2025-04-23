"""
Contains the classes that create the initial sprites and
sets up the elements of the game
"""

import pygame as py


class Car:
    """
    A class that contains all the attributes of the car

    Attributes:
        speed: int representing the speed of the car
        min_speed: int representing the minimum speed of the car
        max_speed: int representing the maximum speed of the car
        acceleration: int representing the increment/acceleration
        max_gas: int representing the maximum gas available

    """

    def __init__(self, speed, min_speed, max_speed, acceleration, max_gas):
        """
        sprite (private)
        speed_cap (private)
        acceleration_cap (private)
        """
        self._x_coord = 600
        self._y_coord = 550
        self._width = 100
        self._height = 140
        self._base_speed = min_speed
        self._acceleration = 0
        self._speed = speed
        self._move = 5

        self.max_speed = max_speed
        self.min_speed = min_speed
        self.acceleration = acceleration
        self.max_gas = max_gas

    def move_left(self):
        """To move left"""
        if self._x_coord > 220:
            self._x_coord -= self._move

    def move_right(self):
        """To move right"""
        if self._x_coord < 950:
            self._x_coord += self._move

    def reset_speed(self):
        """Resets speed to base speed"""
        self._speed = self._base_speed

    def speed_up(self):
        """Increases speed up to max_speed"""
        if self._speed < self.max_speed:
            self._speed += self.acceleration

    @property
    def speed(self):
        """Returns current speed of the car"""
        return self._speed


class CarModel1(Car):
    """
    First option of car
    """

    def __init__(self):
        """
        initializes the first car.
        """
        super().__init__(
            speed=3,
            max_speed=10,
            min_speed=3,
            acceleration=0.5,
            max_gas=100,
        )


class CarModel2(Car):
    """
    Second option of car
    """

    def __init__(self):
        """
        initializes the second car.

        """
        super().__init__(
            speed=5, max_speed=5, min_speed=1, acceleration=0.05, max_gas=80
        )


class CarModel3(Car):
    """
    Third option of car
    """

    def __init__(self):
        """
        initializes the third car.

        """
        super().__init__(
            speed=4, max_speed=5, min_speed=2, acceleration=0.03, max_gas=120
        )


class Obstacle:  # pylint: disable=too-few-public-methods
    """
    A class to create and control obstacles in the game
    """

    def __init__(self):
        """
        sprite (private)
        timer (private)
        x_coordinate (private)
        y_coordinate (private)
        """

    # Sub classes
    # Different types of obstacles? So they can appear at different times and
    # move at different speeds. Also move across the screen vs with the car
    # just slower
