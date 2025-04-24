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
        self.__width = 1280
        self.__height = 750
        self.__length = length
        self._lane_size = 30  # should be 1/3 of the car width
        self.__image = py.image.load("images/test_track.png")
        self._distance_traveled = 0

    def update_travel_distance(self, new_distance):
        """updates the distance traveled of the car"""
        self._distance_traveled = new_distance

    @property
    def _length(self):
        """
        returns length
        """
        return self.__length

    @property
    def _height(self):
        """
        returns height
        """
        return self.__height

    @property
    def _width(self):
        """
        returns width
        """
        return self.__width
    
    
    @property
    def _image(self):
        """returns image"""
        return self.__image


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
