"""Test suite for CarModel1 behavior."""

import pytest
from car import CarModel1

# pylint: disable=redefined-outer-name, protected-access


@pytest.fixture
def car():
    """Returns a CarModel1 instance."""
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
    """Idle should reduce speed and increase gas, within limits."""
    for _ in range(10):
        car.speed_up()
    top_speed = car.speed
    initial_gas = car.gas_amt
    for _ in range(10):
        car.idle()
    assert car.speed >= car._min_speed  # pylint: disable=protected-access
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
    """If gas runs out, speed_up should not increase speed."""
    while car.gas_amt > 0:
        car.speed_up()
    prev_speed = car.speed
    car.speed_up()
    assert car.speed <= prev_speed


def test_brake(car):
    """Brake lowers speed (not below min) and refills gas (up to max)."""
    for _ in range(10):
        car.speed_up()
    prev_speed = car.speed
    prev_gas = car.gas_amt
    car.brake()
    assert (
        car.speed < prev_speed or car.speed == car._min_speed
    )  # pylint: disable=protected-access
    assert car.gas_amt > prev_gas or car.gas_amt == car.max_gas


def test_inc_max_speed(car):
    """Power-up increases max speed."""
    prev_max = car.max_speed
    car.increase_max_speed()
    assert car.max_speed > prev_max


def test_inc_max_gas(car):
    """Power-up increases max gas."""
    prev_max = car.max_gas
    car.increase_max_gas()
    assert car.max_gas > prev_max


def test_inc_acceleration(car):
    """Power-up increases acceleration."""
    prev_acc = car._acceleration  # pylint: disable=protected-access
    car.increase_acceleration()
    assert car._acceleration > prev_acc  # pylint: disable=protected-access


def test_inc_gas_refresh(car):
    """Power-up increases gas refresh rate."""
    prev_refresh = car._gas_refresh  # pylint: disable=protected-access
    car.increase_gas_refresh()
    assert car._gas_refresh > prev_refresh  # pylint: disable=protected-access


def test_gas_refill(car):
    """Refilling gas increases current gas amount."""
    for _ in range(10):
        car.speed_up()
    prev_gas = car.gas_amt
    car.gas_refill()
    assert car.gas_amt > prev_gas
