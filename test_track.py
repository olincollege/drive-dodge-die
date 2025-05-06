import time
import pygame as py
import pytest
from car import CarModel1
from track import Road, StatusTracker, CheckPoint

py.init()


@pytest.fixture
def road():
    return Road()


@pytest.fixture
def status():
    return StatusTracker()


@pytest.fixture
def car():
    return CarModel1()


@pytest.fixture
def checkpoint(car, road, status):
    return CheckPoint(car, road, status)


def test_road_distance_update(road):
    """Test that road distance updates correctly."""
    road.update_travel_distance(1000)
    assert road.distance_traveled == 1000


def test_toggle_pause(status):
    """Test pause state toggles correctly."""
    status.toggle_pause()
    assert status.paused
    status.toggle_pause()
    assert not status.paused


def test_toggle_powerup(status):
    """Test powerup state toggles correctly."""
    status.toggle_powerup()
    assert status.is_powerup
    status.toggle_powerup()
    assert not status.is_powerup


def test_add_time(status):
    """Test time is added correctly to countdown."""
    initial = status._countdown_time_ms
    status.add_time(2)
    assert status._countdown_time_ms - initial == pytest.approx(10000, abs=10)


def test_check_time_up(status):
    """Test time-up check returns correct result."""
    status._time_left = 0
    assert status.check_time_up()
    status._time_left = 5
    assert not status.check_time_up()


def test_checkpoint_update_coords_moving(checkpoint):
    """Test checkpoint moves with car speed."""
    checkpoint._y_coord = 100
    initial_y = 100
    checkpoint.update_coords()
    assert checkpoint.y_coord - initial_y == pytest.approx(
        checkpoint._car.speed, abs=0.01
    )


def test_checkpoint_update_coords_offscreen(checkpoint, road):
    """Test checkpoint resets when offscreen and distance exceeded segment length."""
    checkpoint._road = road
    checkpoint._y_coord = -50
    checkpoint._tracked_distance = 5000
    road.update_travel_distance(5001)
    checkpoint.update_coords()
    assert checkpoint.y_coord == 0
