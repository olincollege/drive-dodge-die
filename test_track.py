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
    road.update_travel_distance(1000)
    assert road.distance_traveled == 1000


def test_toggle_pause(status):
    status.toggle_pause()
    assert status.paused
    status.toggle_pause()
    assert not status.paused


def test_toggle_powerup(status):
    status.toggle_powerup()
    assert status.is_powerup
    status.toggle_powerup()
    assert not status.is_powerup


def test_update_time_left(status):
    # Wait 100ms to simulate some time passing
    time.sleep(0.1)
    remaining = status.update_time_left()
    assert 0 <= remaining <= 15


def test_statustracker_add_time(status):
    initial = status._countdown_time_ms
    status.add_time(2)
    assert status._countdown_time_ms > initial


def test_statustracker_check_time_up(status):
    status._time_left = 0
    assert status.check_time_up()
    status._time_left = 5
    assert not status.check_time_up()


# ----------- CheckPoint Tests ----------- #


def test_checkpoint_initial_values(checkpoint):
    assert checkpoint.x_coord == 0
    assert checkpoint.y_coord == -100
    assert checkpoint.checkpoints_reached == 0
    assert checkpoint.checkpoint_length == 5000
    assert checkpoint.tracked_distance == 5000


def test_checkpoint_update_coords_moves_when_visible(checkpoint):
    checkpoint._y_coord = 100
    checkpoint._car.speed = 5
    checkpoint.update_coords()
    assert checkpoint.y_coord == 105


def test_checkpoint_update_coords_reset_after_passing(checkpoint, road):
    checkpoint._y_coord = -50
    checkpoint._tracked_distance = 1000
    road.update_travel_distance(500)
    checkpoint._road = road
    checkpoint.update_coords()
    assert checkpoint.y_coord == 0


def test_checkpoint_trigger_logic(checkpoint):
    checkpoint.trigger_checkpoint()
    assert checkpoint.checkpoints_reached == 1
    assert checkpoint.checkpoint_length == 5500
    assert checkpoint.length > 5000
