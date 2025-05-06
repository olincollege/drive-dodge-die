import pytest
from car import CarModel1


@pytest.fixture
def car():
    return CarModel1()


def test_left_bound(car):
    """Moves car left repeatedly; x_coord should never go below 220."""
    for _ in range(100):
        car.move_left()
    assert car.x_coord >= 220


def test_right_bound(car):
    """Moves car right repeatedly; x_coord should never go above 950."""
    for _ in range(100):
        car.move_right()
    assert car.x_coord <= 950


def test_idle(car):
    """
    After speeding up, idling should reduce speed but not below min_speed,
    and gas should increase up to max_gas.
    """
    for _ in range(10):
        car.speed_up()
    top_speed = car.speed
    initial_gas = car.gas_amt
    for _ in range(10):
        car.idle()
    assert car.speed >= car._min_speed
    assert car.speed < top_speed
    assert car.gas_amt > initial_gas or car.gas_amt == car.max_gas


def test_speed_up(car):
    """Speed up uses gas and increases speed (if gas is available)."""
    prev_speed = car.speed
    prev_gas = car.gas_amt
    car.speed_up()
    assert car.speed >= prev_speed
    assert car.gas_amt <= prev_gas


def test_speed_up_no_gas(car):
    """If gas runs out, speed_up should not increase speed and may decrease it."""
    while car.gas_amt > 0:
        car.speed_up()
    prev_speed = car.speed
    car.speed_up()
    assert car.speed <= prev_speed


def test_brake(car):
    """
    Brake should lower speed but not below min_speed,
    and gas should refill up to max_gas.
    """
    for _ in range(10):
        car.speed_up()
    prev_speed = car.speed
    prev_gas = car.gas_amt
    car.brake()
    assert car.speed < prev_speed or car.speed == car._min_speed
    assert car.gas_amt > prev_gas or car.gas_amt == car.max_gas


def test_inc_max_speed(car):
    """Power-up that increases max speed should raise max_speed value."""
    prev_max = car.max_speed
    car.increase_max_speed()
    assert car.max_speed > prev_max


def test_inc_max_gas(car):
    """Power-up that increases max gas should raise max_gas value."""
    prev_max = car.max_gas
    car.increase_max_gas()
    assert car.max_gas > prev_max


def test_inc_acceleration(car):
    """Increase acceleration power-up should raise _acceleration value."""
    prev_acc = car._acceleration
    car.increase_acceleration()
    assert car._acceleration > prev_acc


def test_inc_gas_refresh(car):
    """Increase gas refresh power-up should raise _gas_refresh value."""
    prev_refresh = car._gas_refresh
    car.increase_gas_refresh()
    assert car._gas_refresh > prev_refresh


def test_gas_refill(car):
    """Refilling gas should increase the current gas amount."""
    for _ in range(10):
        car.speed_up()  # use some gas
    prev_gas = car.gas_amt
    car.gas_refill()
    assert car.gas_amt > prev_gas
