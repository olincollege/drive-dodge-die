# pylint: disable=missing-function-docstring,missing-module-docstring,protected-access,redefined-outer-name,too-few-public-methods

"""Tests for the Obstacle class and its behavior."""

import pytest
from car import CarModel1
from track import Road, StatusTracker, CheckPoint
from obstacle import Obstacle


@pytest.fixture
def car():
    return CarModel1()


@pytest.fixture
def road_fixture():
    return Road()


@pytest.fixture
def status_fixture():
    return StatusTracker()


@pytest.fixture
def checkpoint(car, road_fixture, status_fixture):
    return CheckPoint(car, road_fixture, status_fixture)


@pytest.fixture
def obstacle(car, road_fixture, checkpoint):
    return Obstacle(car, road_fixture, checkpoint)


def test_check_distance(obstacle):
    """Returns False when an obstacle is nearby."""

    class MockObstacle:
        """create a mock obstacle at y=100."""

        y_coord = 100

    obstacle.all_obstacles["barriers"].append(MockObstacle())
    assert obstacle.check_distance(300) is False


def test_check_distance_when_empty(obstacle):
    """Returns True when no obstacles are present."""
    assert obstacle.check_distance(300) is True


def test_obstacle_removal(obstacle):
    """Removes obstacles that go beyond screen height."""

    class MockObstacle:
        """create a mock obstacle off screen."""

        y_coord = 960

    obstacle.all_obstacles["holes"].append(MockObstacle())
    obstacle.check_remove_obstacles()
    assert len(obstacle.all_obstacles["holes"]) == 0


def test_update_obstacle_y_coord(obstacle):
    """Obstacle y-coordinate should increase based on car speed."""
    initial_y = obstacle.y_coord
    obstacle.update_obstacle()
    assert obstacle.y_coord == initial_y + obstacle._car.speed
