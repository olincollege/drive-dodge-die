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

    def __init__(
        self,
        speed,
        min_speed,
        max_speed,
        acceleration,
        max_gas,
        idle,
        brake,
        gas_refresh,
    ):
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
        self.gas_amt = max_gas
        self.idle_speed = idle
        self.brake_speed = brake
        self.gas_refresh = gas_refresh

    def move_left(self):
        """To move left"""
        if self._x_coord > 220:
            self._x_coord -= self._move

    def move_right(self):
        """To move right"""
        if self._x_coord < 950:
            self._x_coord += self._move

    def idle(self):
        """slowly reduces the speed when the acceleration is not pressed"""
        if self._speed > self.min_speed:
            self._speed -= self.idle_speed
        if self.gas_amt < self.max_gas:
            self.gas_amt += self.gas_refresh

    def speed_up(self):
        """Increases speed up to max_speed if there is gas left, 
        otherwise it idles"""
        if self.gas_amt > 0 and self._speed < self.max_speed:
            self._speed += self.acceleration
            self.gas_amt -= 10
        else:
            self.accel = False
            if self._speed > self.min_speed:
                self._speed -= self.idle_speed

    def brake(self):
        """Decreases speed to min_speed"""
        if self._speed > self.min_speed:
            self._speed -= self.brake_speed
        if self.gas_amt < self.max_gas:
            self.gas_amt += self.gas_refresh

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
            max_speed=20,
            min_speed=3,
            acceleration=0.5,
            max_gas=1000,
            idle=0.1,
            brake=0.2,
            gas_refresh=2,
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
            speed=5,
            max_speed=5,
            min_speed=1,
            acceleration=0.05,
            max_gas=80,
            idle=0.005,
            brake=0.008,
            gas_refresh=3,
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
            speed=4,
            max_speed=5,
            min_speed=2,
            acceleration=0.03,
            max_gas=120,
            idle=0.003,
            brake=0.006,
            gas_refresh=5,
        )


class Obstacle:
    """
    A class to create and control obstacles in the game

    Attributes:
        car: contains all the methods of the car class
        all_obstacles: dictionary to store all obstacles
                        keys: strings representing type of obstacle
                        values: list of all instances of obstacles
        y_coord: int representing the y-coordinate of the obstacle
        speed: int representing the car's current speed
    """

    def __init__(self, car):
        self._car = car
        self._all_obstacles = {"barriers": [], "holes": []}
        self._y_coord = 0
        self._speed = car._speed

    @property
    def get_all_obstacles(self):
        """Returns the dictionary of all obstacles"""
        return self._all_obstacles

    def update_obstacles(self):
        """Method that updates obstacles"""
        self.update_obstacle(self._car)
        self.check_remove_obstacles()
        self.create_obstacles()

    def check_remove_obstacles(self):
        """Removes obstacles once they reach the end of the screen"""
        for object_list in self._all_obstacles.values():
            for obstacle in object_list:
                if obstacle._y_coord > 750:
                    object_list.remove(obstacle)

    def update_obstacle(self, car):
        """Updates speed of the obstacle"""
        self._speed = car.get_speed
        if self._y_coord < 760:
            self._y_coord += self._speed
        else:
            self._y_coord = 0
        return self._y_coord

    def create_obstacles(self):
        """Calls all functions to make the obstacles"""
        self.create_barriers()

    def create_barriers(self):
        """Generates barriers randomly"""
        barriers = self._all_obstacles["barriers"]
        if random.random() < 0.01 and len(barriers) < 5:
            new_barrier = Barrier(self._car)
            barriers.append(new_barrier)

    def check_collision(self):
        """Checks if the car collides with an obstacle."""
        car_rect = py.Rect(
            self._car._x_coord,
            self._car._y_coord,
            self._car._width,
            self._car._height,
        )
        for obstacle_list in self._all_obstacles.values():
            for obstacle in obstacle_list:
                obstacle_rect = py.Rect(
                    obstacle._x_coord,
                    obstacle._y_coord,
                    obstacle._width,
                    obstacle._height,
                )
                if car_rect.colliderect(obstacle_rect):
                    return True
        return False


class Barrier(Obstacle):
    """Class that creates a barrier shape"""

    def __init__(self, car):
        super().__init__(car)
        self._x_coord = random.randint(220, 950)
        self._y_coord = 0
        self._width = 5 * road._lane_size
        self._height = 15
