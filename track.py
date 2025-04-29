"""
Creates two classes which are part of the track:
Road and StatusTracker.
"""

import pygame as py
import selection_screen


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
        self._height = 950
        self._length = length
        self._lane_size = 30  # should be 1/3 of the car width
        self._image = py.image.load("images/track.png")
        self._distance_traveled = 0

    def update_travel_distance(self, new_distance):
        """updates the distance traveled of the car"""
        self._distance_traveled = new_distance

    @property
    def distance_traveled(self):
        """returns distance traveled"""
        return self._distance_traveled

    @property
    def length(self):
        """
        returns length
        """
        return self._length

    @property
    def height(self):
        """
        returns height
        """
        return self._height

    @property
    def width(self):
        """
        returns width
        """
        return self._width

    @property
    def image(self):
        """returns image"""
        return self._image


class StatusTracker:
    """
    tracks the status of various things

    self.paused: boolean that tracks whether the game is paused or not
    """

    def __init__(self):
        self.paused = False
        self.is_powerup = False

    def toggle_pause(self):
        """
        toggles between paused and unpaused state
        """
        self.paused = not self.paused

    def toggle_powerup(self):
        self.is_powerup = not self.is_powerup

    def back_to_home(self):
        """
        goes back to start screen
        """
        selection_screen.select_car()


class CheckPoint(Road):
    def __init__(self, length, car, road, status):
        super().__init__(length)
        self._car = car
        self._speed = car._speed
        self._x_coord = 0
        self._y_coord = 500
        self._width = 1280
        self._height = 50
        self._length = length
        self._road = road
        self._status = status
        self._distance_track = length
        self._checkpoints_reached = 0
        self.is_colliding_checkpoint = False

    def update_check_point_y_coord(self):
        self._speed = self._car.speed
        distance_traveled = self._road.distance_traveled
        if self._y_coord < 960:
            self._y_coord += self._speed
        elif distance_traveled - self._distance_track > 0:
            self._y_coord = 0
            self._distance_track += self._length
        return self._y_coord

    def check_reach_checkpoint(self):
        """Checks if the car collides with the check point."""
        car_rect = py.Rect(
            self._car.x_coord,
            self._car.y_coord,
            self._car.width,
            self._car.height,
        )
        checkpoint_rect = py.Rect(
            self._x_coord,
            self._y_coord,
            self._width,
            self._height,
        )

        if car_rect.colliderect(checkpoint_rect):
            if not self.is_colliding_checkpoint:
                self.checkpoints_reached += 1
                self.is_colliding_checkpoint = True
        else:
            self.is_colliding_checkpoint = False

    @property
    def checkpoints_reached(self):
        """returns checkpoints reached"""
        return self._checkpoints_reached

    @checkpoints_reached.setter
    # has to be the same name as the previous property
    def checkpoints_reached(self, value):
        """trigger powerup when checkpoints count changes"""
        if value > self._checkpoints_reached:
            self._status.toggle_powerup()
            self._status.toggle_pause()
        self._checkpoints_reached = value
