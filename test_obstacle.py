import pytest
from car import CarModel1
from track import Road, StatusTracker, CheckPoint
from obstacle import Obstacle


@pytest.fixture
def car():
    return CarModel1()


@pytest.fixture
def road():
    return Road()


@pytest.fixture
def status():
    return StatusTracker()


@pytest.fixture
def checkpoint(car, road, status):
    return CheckPoint(car, road, status)


@pytest.fixture
def obstacle(car, road, checkpoint):
    return Obstacle(car, road, checkpoint)


def test_check_distance(obstacle):
    """Tests check_distance returns False when an obstacle is nearby."""

    class NewObstacle:
        y_coord = 100

    obstacle.all_obstacles["barriers"].append(NewObstacle())
    assert obstacle.check_distance(300) is False


def test_check_distance_when_empty(obstacle):
    """Tests check_distance returns True when no obstacles are present."""
    assert obstacle.check_distance(300) is True


def test_obstacle_removal(obstacle):
    """Tests that obstacles beyond the screen height are removed."""

    class NewObstacle:
        y_coord = 960

    obstacle.all_obstacles["holes"].append(NewObstacle())
    obstacle.check_remove_obstacles()
    assert len(obstacle.all_obstacles["holes"]) == 0


def test_update_obstacle_y_coord(obstacle):
    """Tests that obstacle y-coordinate increases with car speed."""
    initial_y = obstacle.y_coord
    obstacle.update_obstacle()
    assert obstacle.y_coord == initial_y + obstacle._car.speed
