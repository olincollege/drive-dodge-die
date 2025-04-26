"""
Creates two classes which are part of the track:
Road and StatusTracker.
"""

import pygame as py


class Road:
    """
    our road is one really long road. It is meant
    to scroll as the car(what the user is controlling)
    moves forward.
    """

    def __init__(self, length):
        """
        initializes the road
        """
        self._positions = 20
        self._width = 1280
        self._height = 750
        self._length = length
        self._width = 1280
        self._height = 750
        self._length = length
        self._lane_size = 30  # should be 1/3 of the car width
        self._image = py.image.load("images/test_track.png")
        self._image = py.image.load("images/test_track.png")
        self._distance_traveled = 0

    def update_travel_distance(self, new_distance):
        """updates the distance traveled of the car"""
        self._distance_traveled = new_distance

    @property
    def get_distance_traveled(self):
        """returns distance traveled"""
        return self._distance_traveled

    @property
    def get_length(self):
        """
        returns length
        """
        return self._length
        return self._length

    @property
    def getget_height(self):
        """
        returns height
        """
        return self._height
        return self._height

    @property
    def getget_width(self):
        """
        returns width
        """
        return self._width

        return self._width

    @property
    def getget_image(self):
        """returns image"""
        return self._image

    @property
    def get_distance_traveled(self):
        """returns distance traveled"""
        return self._distance_traveled


class StatusTracker:
    """
    tracks the status of various things

    self.paused: boolean that tracks whether the game is paused or not
    """

    def __init__(self):
        self.paused = False

    def toggle_pause(self):
        """
        toggles between paused and unpaused state
        """
        self.paused = not self.paused


class CheckPoint(Road):
    def __init__(self, length, car, road):
        super().__init__(length)
        self._car = car
        self._speed = car._speed
        self._x_coord = 0
        self._y_coord = 500
        self._width = 1280
        self._height = 50
        self._length = length
        self._road = road
        self._distance_track = length

    def update_check_point(self):
        self._speed = self._car.get_speed
        distance_traveled = self._road.get_distance_traveled
        if self._y_coord < 760:
            self._y_coord += self._speed
        elif distance_traveled - self._distance_track > 0:
            self._y_coord = 0
            self._distance_track += self._length
        return self._y_coord
