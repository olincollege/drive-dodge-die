"""
Contains the classes that create the initial sprites and 
sets up the elements of the game
"""
class Car: #pylint: disable=too-few-public-methods
    '''
    A class that contains all the attributes of the car
    '''
    def __init__(self):
        '''
            sprite (private)
            x_coordinate (public)
            y_coordinate (public)
            speed_cap (private)
            acceleration_cap (private)
            maneuverability (private)
        '''

    # Sub classes-
    # Different types of cars have different attributes(shape, color, size)
    # and they will have different gas tank percentages and reload times.
    # This is chosen by the user in the initial setup of the game.


class Obstacle: #pylint: disable=too-few-public-methods
    '''
    A class to create and control obstacles in the game
    '''
    def __init__(self):
        '''
            sprite (private)
            timer (private)
            x_coordinate (private)
            y_coordinate (private)
        '''
    # Sub classes
    # Different types of obstacles? So they can appear at different times and
    # move at different speeds. Also move across the screen vs with the car 
    # just slower
