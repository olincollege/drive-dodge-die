"""
Contains the classes that create the initial sprites and
sets up the elements of the game
"""

import pygame as py
import random
from track import Road

road = Road(5000)


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
    def get_speed(self):
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

    def __init__(self, car):
        self._car = car
        # create a dictrionary to store all obstacle, so that we can track crash more easily later
        # values: a list of instances of different Obstacle subclasses
        self._all_obstacles = {"barriers": [], "holes": []}
        self._y_coord = 0
        self._speed = car._speed

    @property
    def get_all_obstacles(self):
        return self._all_obstacles

    def update_obstacles(self):
        self.update_obstacle(self._car)
        self.check_remove_obstacles()
        self.create_obstacles()

    def check_remove_obstacles(self):
        for object_list in self._all_obstacles.values():
            for obstacle in object_list:
                if obstacle._y_coord > 750:
                    object_list.remove(obstacle)

    def update_obstacle(self, car):
        self._speed = car.get_speed
        if self._y_coord < 760:
            self._y_coord += self._speed
        else:
            self._y_coord = 0
        return self._y_coord

    def create_obstacles(self):
        self.create_barriers()

    def create_barriers(self):
        barriers = self._all_obstacles["barriers"]
        if random.random() < 0.01 and len(barriers) < 5:
            new_barrier = Barrier(self._car)
            barriers.append(new_barrier)

    # Sub classes
    # Different types of obstacles? So they can appear at different times and
    # move at different speeds. Also move across the screen vs with the car
    # just slower


class Barrier(Obstacle):
    def __init__(self, car):
        super().__init__(car)
        self._x_coord = random.randint(220, 950)
        self._y_coord = 0
        self._width = 5 * road._lane_size
        self._height = 15
