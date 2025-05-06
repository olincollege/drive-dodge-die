"""
Creates two classes which are part of the track:
Road and StatusTracker.
"""

import math
import pygame as py
import welcome_screen


class Road:
    """
    A class to create and control a scrolling road.

    Private Attributes:
        width: int of the width of the road, which is also the width
            of the screen
        height: int of the height of the road, which is also the width
            of the screen
        length: int of the total length of the road (this increases as
            you pass checkpoints)
        image: pygame image of the road
        distance_traveled: how far the car has traveled
    """

    def __init__(self):
        self._width = 1280
        self._height = 950
        self._length = 5000
        self._image = py.image.load("media/images/track.png")
        self._distance_traveled = 0

    def update_travel_distance(self, new_distance):
        """
        updates the distance traveled of the car

        Args:
            new_distance: an integer of the new distance
        """
        self._distance_traveled = new_distance

    @property
    def distance_traveled(self):
        """returns distance traveled"""
        return self._distance_traveled

    @property
    def length(self):
        """returns length"""
        return self._length

    @property
    def height(self):
        """returns height"""
        return self._height

    @property
    def width(self):
        """returns width"""
        return self._width

    @property
    def image(self):
        """returns image"""
        return self._image


class CheckPoint(Road):
    """
    A subclass of Road that creates and tracks the checkpoints

    Private Attributes:
        car: car object
        x_coord: int of x coordinate of the checkpoint
        y_coord: int of y coordinate of the checkpoint
        width: int of the width of the checkpoint
        height: int of the height of the checkpoint
        road: road object
        status: status tracker object
        tracked_distance: int of the sum of all previous checkpoint lengths
        checkpoints_reached: int of the number of checkpoints reached
        is_colliding_checkpoint: boolean of if the car and the checkpoint
            are touching
        checkpoint_length: int of the length of the checkpoint
    """

    def __init__(self, car, road, status):
        super().__init__()
        self._car = car
        self._x_coord = 0
        self._y_coord = -100
        self._width = 1280
        self._height = 50
        self._road = road
        self._status = status
        self._tracked_distance = self._length
        self._checkpoints_reached = 0
        self.is_colliding_checkpoint = False
        self._checkpoint_length = 5000

    def update_coords(self):
        """updates y coordinate of the checkpoint"""
        print(f"tracked distance: {self._tracked_distance}")
        print(f"road length: {self._length}")
        print(f"distance traveled: {self._road.distance_traveled}")
        speed = self._car.speed
        if self._y_coord < 960 and self._y_coord >= 0:
            self._y_coord += speed
        elif self._road.distance_traveled + 720 >= self._tracked_distance:
            self._y_coord = 0

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
                self.trigger_checkpoint()
                self.is_colliding_checkpoint = True
                print("reached checkpoint")
        else:
            self.is_colliding_checkpoint = False

    def trigger_checkpoint(self):
        """
        triggers the things that happen when the car reaches
        the checkpoint: pause game/timer, show power up options,
        update number of checkpoints reached, update length of
        the next checkpoint, add time to the countdown clock"""
        self._status.toggle_pause()
        self._status.toggle_powerup()
        self._checkpoints_reached += 1
        self._checkpoint_length = 5000 + 500 * int(self._checkpoints_reached)
        self._length = self.length + self._checkpoint_length
        self._status.add_time(self._checkpoints_reached)
        self._distance_traveled = self._tracked_distance
        self._tracked_distance = self._length

        print(f"distance traveled: imm: {self._distance_traveled}")

    @property
    def checkpoints_reached(self):
        """returns checkpoints reached"""
        return self._checkpoints_reached

    @property
    def checkpoint_length(self):
        """returns checkpoint length"""
        return self._checkpoint_length

    @property
    def x_coord(self):
        """returns x_coord"""
        return self._x_coord

    @property
    def y_coord(self):
        """returns y_coord"""
        return self._y_coord

    @property
    def tracked_distance(self):
        """returns distance_track"""
        return self._tracked_distance


class StatusTracker:
    """
    tracks the status of various things

    Public Attributes:
        self.paused: boolean that tracks whether the game is paused or not
        is_powerup: boolean of if the power up screen is showing
    Private Attributes:
        start_time: int of ticks at the start time
        countown_time_ms: integer of the total milliseconds a player has
            per checkpoint
        time_left: integer of the milliseconds the player has left to
             get past a checkpoint
    """

    def __init__(self):
        self.paused = False
        self.is_powerup = False
        self._start_time = py.time.get_ticks()
        self._countdown_time_ms = 15 * 1000
        self._time_left = None

    def toggle_pause(self):
        """
        toggles between paused and unpaused state
        """
        self.paused = not self.paused

    def toggle_powerup(self):
        """toggles between the power up screen and the game screen"""
        self.is_powerup = not self.is_powerup

    def back_to_home(self):
        """
        goes back to start screen
        """
        welcome_screen.welcome()

    def update_time_left(self):
        """update time left"""
        elapsed_time_ms = py.time.get_ticks() - self._start_time
        time_left_ms = max(self._countdown_time_ms - elapsed_time_ms, 0)
        self._time_left = math.ceil(time_left_ms / 1000)
        return self._time_left

    def add_time(self, checkpoint_num):
        """adds time to the countdown clock"""
        self._countdown_time_ms = self._countdown_time_ms + (
            5 + int(5 * checkpoint_num) * 1000
        )

    def check_time_up(self):
        """check if time is up"""
        if self._time_left == 0:
            return True
        return False

    @property
    def time_left(self):
        """returns time left"""
        return self._time_left

    @property
    def start_time(self):
        """returns start time"""
        return self._start_time
