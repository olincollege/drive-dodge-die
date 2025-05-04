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

    def __init__(self, car, road, status):
        self._car = car
        self._road = road
        self._status = status
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
                if obstacle.y_coord > 950:
                    object_list.remove(obstacle)

    def update_obstacle(self):
        """Updates speed of the obstacle"""
        self._speed = self._car.speed
        if self._y_coord < 950:
            self._y_coord += self._speed
        else:
            self._y_coord = 0

    def create_obstacles(self):
        """
        Calls all functions to make the obstacles
        The chance increase over time
        """
        elapsed_time = (py.time.get_ticks() - self._status.start_time) / 1000
        scale = min(
            1 + elapsed_time / 60, 2
        )  # cap at 2x the base chance at 1 minute

        if random.random() < 0.5 * scale:
            self.create_barriers(scale)
        if random.random() < 0.5 * scale:
            self.create_holes(scale)

    def create_barriers(self, scale):
        """Generates barriers randomly"""
        barriers = self._all_obstacles["barriers"]
        if (
            random.random() < 0.05
            and len(barriers) < 5
            and self.check_distance(400 - scale * 100)
        ):
            new_barrier = Barrier(self._car, self._road, self._status)
            barriers.append(new_barrier)

    def create_holes(self, scale):
        """Generates holes randomly"""
        holes = self._all_obstacles["holes"]
        if (
            random.random() < 0.05
            and len(holes) < 5
            and self.check_distance(400 - scale * 100)
        ):
            new_hole = Hole(self._car, self._road, self._status)
            holes.append(new_hole)

    def check_distance(self, distance):
        """checks the distance of the closest obstacle.
        returns true if there can be another obstacle, false if there can't"""
        min_y = 950
        for item in self._all_obstacles:
            for obstacle in self._all_obstacles[item]:
                min_y = min(min_y, obstacle.y_coord)
        if min_y > distance:
            return True
        return False

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
                    obstacle.x_coord,
                    obstacle.y_coord,
                    obstacle.width,
                    obstacle.height,
                )
                if car_rect.colliderect(obstacle_rect):
                    return True
        return False

    @property
    def y_coord(self):
        """return y_coord"""
        return self._y_coord


class Barrier(Obstacle):
    """Class that creates a barrier shape"""

    def __init__(self, car, road, status):
        super().__init__(car, road, status)
        self._x_coord = random.randint(220, 950)
        self._y_coord = 0
        self._width = 150
        self._height = 30
        self._image = py.image.load(
            "images/obstacles/barrier.png"
        ).convert_alpha()

    @property
    def x_coord(self):
        """return x_coord"""
        return self._x_coord

    @property
    def width(self):
        """return width"""
        return self._width

    @property
    def height(self):
        """return height"""
        return self._height

    @property
    def image(self):
        """return image"""
        return self._image


class Hole(Obstacle):
    """class that creates a hole object as an obstacle in the road"""

    def __init__(self, car, road, status):
        super().__init__(car, road, status)
        self._x_coord = random.randint(220, 950)
        self._y_coord = 0
        self._width = 150
        self._height = 50
        self._image = py.image.load("images/obstacles/hole.png").convert_alpha()

    @property
    def x_coord(self):
        """return x_coord"""
        return self._x_coord

    @property
    def width(self):
        """return width"""
        return self._width

    @property
    def height(self):
        """return height"""
        return self._height

    @property
    def image(self):
        """return image"""
        return self._image
