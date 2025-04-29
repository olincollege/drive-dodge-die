"""
Contains the classes that create the initial sprites and
sets up the elements of the game
"""


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
        car_image_path,
    ):
        """
        sprite (private)
        speed_cap (private)
        acceleration_cap (private)
        """
        self._x_coord = 600
        self._y_coord = 750
        self._width = 60
        self._height = 120
        self._base_speed = min_speed
        self._acceleration = 0
        self._speed = speed
        self._move = 5

        self._max_speed = max_speed
        self._min_speed = min_speed
        self._acceleration = acceleration
        self._max_gas = max_gas
        self._gas_amt = max_gas
        self._idle_speed = idle
        self._brake_speed = brake
        self._gas_refresh = gas_refresh
        self._car_image = car_image_path

    @property
    def image_path(self):
        """Returns the image of selected car"""
        return self._car_image

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
        if self._speed > self._min_speed:
            self._speed -= self._idle_speed
        if self._gas_amt < self._max_gas:
            self._gas_amt += self._gas_refresh

    def speed_up(self):
        """Increases speed up to max_speed if there is gas left,
        otherwise it idles"""
        if self._gas_amt > 0 and self._speed < self._max_speed:
            self._speed += self._acceleration
            self._gas_amt -= 10
        else:
            if self._speed > self._min_speed:
                self._speed -= self._idle_speed

    def brake(self):
        """Decreases speed to min_speed"""
        if self._speed > self._min_speed:
            self._speed -= self._brake_speed
        if self._gas_amt < self._max_gas:
            self._gas_amt += self._gas_refresh

    # Power ups
    def increase_max_speed(self):
        if self._max_speed <= 6:
            self._max_speed += 1
        elif self._max_speed <= 10:
            self._max_speed += 1.5
        else:
            self._max_speed += 2

    def increase_max_gas(self):
        if self._max_gas <= 600:
            self._max_gas += 200
        elif self._max_gas <= 1200:
            self._max_gas += 250
        else:
            self._max_gas += 300

    def increase_acceleration(self):
        if self._acceleration <= 0.3:
            self._acceleration += 0.1
        elif self._acceleration <= 0.6:
            self._acceleration += 0.15
        else:
            self._acceleration += 0.2

    def increase_gas_refresh(self):
        if self._gas_refresh <= 3:
            self._gas_refresh += 1
        elif self._gas_refresh <= 6:
            self._gas_refresh += 1.5
        else:
            self._gas_refresh += 2

    # immediately get gas refill; more time; shield; faster gas refresh

    @property
    def speed(self):
        """Returns current speed of the car"""
        return self._speed

    @property
    def max_speed(self):
        """Returns max speed of the car"""
        return self._max_speed

    @property
    def gas_amt(self):
        """return how much gas the car has"""
        return self._gas_amt

    @property
    def max_gas(self):
        """return what the max gas tank is"""
        return self._max_gas

    @property
    def x_coord(self):
        """return x_coord of car"""
        return self._x_coord

    @property
    def y_coord(self):
        """return y_coord of car"""
        return self._y_coord

    @property
    def width(self):
        """return width of car"""
        return self._width

    @property
    def height(self):
        """return height of car"""
        return self._height


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
            max_speed=8,
            min_speed=3,
            acceleration=0.5,
            max_gas=800,
            idle=0.1,
            brake=0.2,
            gas_refresh=2,
            car_image_path="images/cars/car.png",
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
            speed=3,
            max_speed=5,
            min_speed=3,
            acceleration=0.7,
            max_gas=600,
            idle=0.5,
            brake=0.8,
            gas_refresh=3,
            car_image_path="images/cars/car2.png",
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
            max_speed=6,
            min_speed=2,
            acceleration=0.4,
            max_gas=1000,
            idle=0.3,
            brake=0.6,
            gas_refresh=5,
            car_image_path="images/cars/car3.png",
        )
