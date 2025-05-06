"""
Contains the classes that create the initial sprites and
sets up the car element of the game
"""


class Car:
    """
    A class that contains all the attributes of the car

    Attributes:
        x_coord: int representing the x-coordinate of the car
        y_coord: int representing the y-coordinate of the car
        width: int representing the width of the car
        height: int representing the height of the car
        base_speed: int representing the base speed of the car
        acceleration: int representing the acceleration of the car
        speed: int representing the speed of the car
        move: int representing the amount by which the car
                moves in the x-direction
        max_speed: int representing the maximum speed of the car
        min_speed: int representing the minimum speed of the car
        acceleration: int representing the acceleration of the car
        max_gas: int representing the gas capacity of the car
        gas_amt: int representing the amount of gas in the car
        idle_speed: int representing the resting speed of the car
                    when it is not accelerating
        brake_speed: int representing the brake speed of the car
        gas_refresh: int representing the gas refresh rate of the car
        car_image: str of the path of the car image


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
        self._move = 10

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
        if self._x_coord < (1010 - self._width):
            self._x_coord += self._move

    def idle(self):
        """Slowly reduces the speed and
        refreshes gas when the acceleration is not pressed"""
        if self._speed > self._min_speed:
            self._speed -= self._idle_speed
        if self._gas_amt < self._max_gas:
            self._gas_amt += self._gas_refresh

    def speed_up(self):
        """Increases speed up to max_speed if there is gas left"""
        if self._gas_amt > 0 and self._speed < self._max_speed:
            self._gas_amt -= min(3, self._gas_amt)
            self._speed += min(
                (self._max_speed - self._speed), self._acceleration
            )
        else:
            self._gas_amt -= min(3, self._gas_amt)
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
        """Increases the maximum speed the car can attain"""
        if self._max_speed <= 12:
            self._max_speed += 2
        elif self._max_speed <= 20:
            self._max_speed += 3
        else:
            self._max_speed += 4

    def increase_max_gas(self):
        """Increases the maximum gas tank capacity of the car"""
        if self._max_gas <= 600:
            self._max_gas += 200
        elif self._max_gas <= 1200:
            self._max_gas += 250
        else:
            self._max_gas += 300

    def increase_acceleration(self):
        """Increases the rate of speeding up of the car"""
        if self._acceleration <= 0.2:
            self._acceleration += 0.05
        elif self._acceleration <= 0.3:
            self._acceleration += 0.075
        else:
            self._acceleration += 0.1

    def increase_gas_refresh(self):
        """Boosts the gas refresh rate for faster refilling
        of gas when car is idle"""
        if self._gas_refresh <= 6:
            self._gas_refresh += 1
        elif self._gas_refresh <= 10:
            self._gas_refresh += 1.6
        else:
            self._gas_refresh += 2

    def gas_refill(self):
        """Refills the gas tank"""
        if self._max_gas <= 800:
            self._gas_amt += 300
        elif self._max_gas <= 1200:
            self._gas_amt += 400
        elif self._max_gas <= 1800:
            self._gas_amt += 600
        else:
            self._gas_amt += 900

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
    Sub class containing the first option of the car
    """

    def __init__(self):
        """
        Initializes the first car, using the init method 
        from the Car class
        """
        super().__init__(
            speed=6,
            max_speed=30,
            min_speed=6,
            acceleration=0.2,
            max_gas=800,
            idle=0.2,
            brake=0.4,
            gas_refresh=10,
            car_image_path="media/images/cars/car.png",
        )


class CarModel2(Car):
    """
    Sub class containing the second option of the car
    """

    def __init__(self):
        """
        Initializes the second car, using the init method 
        from the Car class
        """
        super().__init__(
            speed=6,
            max_speed=36,
            min_speed=6,
            acceleration=0.24,
            max_gas=900,
            idle=0.2,
            brake=0.4,
            gas_refresh=6,
            car_image_path="media/images/cars/car2.png",
        )


class CarModel3(Car):
    """
    Sub class containing the third option of the car
    """

    def __init__(self):
        """
        Initializes the third car, using the init method 
        from the Car class
        """
        super().__init__(
            speed=16,
            max_speed=26,
            min_speed=10,
            acceleration=1.6,
            max_gas=1000,
            idle=0.2,
            brake=0.3,
            gas_refresh=10,
            car_image_path="media/images/cars/car3.png",
        )
