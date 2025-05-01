"""Unit Tests for selection screen functions"""

import pytest
import pygame
from game_elements import CarModel1, CarModel2, CarModel3
from selection_screen import select_car


@pytest.fixture(autouse=True)
def pygame_setup():
    """Fixture to initialize pygame before each test."""
    pygame.init()
    yield
    pygame.quit()


def test_select_car_car_model_1():
    """Test the selection of CarModel1 by simulating a mouse click."""

    # Set up a small window to simulate the game screen
    pygame.display.set_mode((1280, 950))

    # Set up Pygame event to simulate a mouse click on the first car's area
    car1_rect = pygame.Rect(100, 300, 200, 300)  # The area of car 1 (approx)
    pygame.event.post(
        pygame.event.Event(
            pygame.MOUSEBUTTONDOWN, pos=(car1_rect.centerx, car1_rect.centery)
        )
    )

    # Run the select_car function to check which car gets selected
    selected_car = select_car()

    # Verify that CarModel1 was selected
    assert isinstance(selected_car, CarModel1)


def test_select_car_car_model_2():
    """Test the selection of CarModel2 by simulating a mouse click."""

    # Set up a small window to simulate the game screen
    pygame.display.set_mode((1280, 950))

    # Set up Pygame event to simulate a mouse click on the second car's area
    car2_rect = pygame.Rect(400, 300, 200, 300)  # The area of car 2 (approx)
    pygame.event.post(
        pygame.event.Event(
            pygame.MOUSEBUTTONDOWN, pos=(car2_rect.centerx, car2_rect.centery)
        )
    )

    # Run the select_car function to check which car gets selected
    selected_car = select_car()

    # Verify that CarModel2 was selected
    assert isinstance(selected_car, CarModel2)


def test_select_car_car_model_3():
    """Test the selection of CarModel3 by simulating a mouse click."""

    # Set up a small window to simulate the game screen
    pygame.display.set_mode((1280, 950))

    # Set up Pygame event to simulate a mouse click on the third car's area
    car3_rect = pygame.Rect(700, 300, 200, 300)  # The area of car 3 (approx)
    pygame.event.post(
        pygame.event.Event(
            pygame.MOUSEBUTTONDOWN, pos=(car3_rect.centerx, car3_rect.centery)
        )
    )

    # Run the select_car function to check which car gets selected
    selected_car = select_car()

    # Verify that CarModel3 was selected
    assert isinstance(selected_car, CarModel3)


def test_quit_event():
    """Test the behavior when a quit event occurs."""

    # Set up a small window to simulate the game screen
    pygame.display.set_mode((1280, 950))

    # Simulate a quit event
    pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Run the select_car function (it should exit without selecting a car)
    selected_car = select_car()

    # Verify that no car was selected (it should return None)
    assert selected_car is None
