"""Writes the classes that have to do with obstacles."""

import random
import pygame as py


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

    def __init__(self, car, road):
        self._car = car
        self._road = road
        self._all_obstacles = {"barriers": [], "holes": []}
        self._y_coord = 0
        self._speed = car._speed

    @property
    def all_obstacles(self):
        """Returns the dictionary of all obstacles"""
        return self._all_obstacles

    def update_obstacles(self):
        """Method that updates obstacles"""
        self.update_obstacle()
        self.check_remove_obstacles()
        self.create_obstacles()

    def check_remove_obstacles(self):
        """Removes obstacles once they reach the end of the screen"""
        for object_list in self._all_obstacles.values():
            for obstacle in object_list:
                if obstacle.get_y_coord > 950:
                    object_list.remove(obstacle)

    def update_obstacle(self):
        """Updates speed of the obstacle"""
        self._speed = self._car.speed
        if self._y_coord < 950:
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
            new_barrier = Barrier(self._car, self._road)
            barriers.append(new_barrier)

    def check_collision(self):
        """Checks if the car collides with an obstacle."""
        car_rect = py.Rect(
            self._car.x_coord,
            self._car.y_coord,
            self._car.width,
            self._car.height,
        )
        for obstacle_list in self._all_obstacles.values():
            for obstacle in obstacle_list:
                obstacle_rect = py.Rect(
                    obstacle.get_x_coord,
                    obstacle.get_y_coord,
                    obstacle.get_width,
                    obstacle.get_height,
                )
                if car_rect.colliderect(obstacle_rect):
                    return True
        return False

    @property
    def get_y_coord(self):
        """return y_coord"""
        return self._y_coord


class Barrier(Obstacle):
    """Class that creates a barrier shape"""

    def __init__(self, car, road):
        super().__init__(car, road)
        self._x_coord = random.randint(220, 950)
        self._y_coord = 0
        self._width = 5 * self._road._lane_size
        self._height = 15

    @property
    def get_x_coord(self):
        """return x_coord"""
        return self._x_coord

    @property
    def get_width(self):
        """return width"""
        return self._width

    @property
    def get_height(self):
        """return height"""
        return self._height
