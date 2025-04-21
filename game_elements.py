"""
Contains the classes that create the initial sprites and
sets up the elements of the game
"""


class Car:  # pylint: disable=too-few-public-methods
    """
    A class that contains all the attributes of the car
    """

    def __init__(self):
        """
        sprite (private)
        speed_cap (private)
        acceleration_cap (private)
        maneuverability (private)
        """
        self._x_coord = 600
        self._y_coord = 550
        self._width = 100
        self._height = 140
        self._speed = 2
        self._acceleration = 0
        self._gas = 100

    # Sub classes-
    # Different types of cars have different attributes(shape, color, size)
    # and they will have different gas tank percentages and reload times.
    # This is chosen by the user in the initial setup of the game.


class CarModel1(Car):
    """
    first subclass of class car
    (the original car)
    """

    def __init__(self):
        self.max_speed = 4
        self.min_speed = 1
        self.max_acceleration = 0.01
        self.max_gas = 100


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
