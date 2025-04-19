"""
Creates two classes which are part of the track:
Road and StatusTracker.
"""


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
        self._total_length = length
        self._lane_size = 30  # should be 1/3 of the car width

    @property
    def _display_height(self):
        """
        returns display height
        """
        return self._display_height

    @property
    def _display_width(self):
        """
        returns display width
        """
        return self._display_width


class StatusTracker:
    def __init__(self):
        self.paused = False

    def toggle_pause(self):
        self.paused = not self.paused
