"""file for controller class in Model, View, Controller Architecture"""

import sys
import pygame


class Controller:
    """
    Controller class. Contains all functions to control
    the car and other buttons during the game

    Private Attributes:
        status: status tracker object
        view: view object
        car: car object
    """

    def __init__(self, status, view, car):
        self._status = status
        self._view = view
        self._car = car

    def basic_event(self):  # pylint: disable=R0912
        """
        Maps out what to do in a basic event
        (events that have to do with buttons)
        This includes pausing the game, going home,
        and choosing a power up option.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
                and not self._status.is_powerup
            ):
                # disable pause when choosing powerups
                self._status.toggle_pause()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (
                    self._view.pause_button.collidepoint(event.pos)
                    and not self._status.is_powerup
                ):
                    self._status.toggle_pause()
                for text, button in self._view.overlay_buttons.items():
                    if (
                        text == "Resume"
                        and self._status.paused
                        and self._status.is_powerup is False
                        and button.collidepoint(event.pos)
                    ):
                        self._status.toggle_pause()
                    if (
                        text == "Return Home"
                        and self._status.paused
                        and self._status.is_powerup is False
                        and button.collidepoint(event.pos)
                    ):
                        self._status.back_to_home()

                for text, button in self._view.powerup_choice.items():
                    if (
                        text == "Increase Max Speed"
                        and self._status.is_powerup
                        and button.collidepoint(event.pos)
                    ):
                        self._status.toggle_powerup()
                        self._status.toggle_pause()
                        self._car.increase_max_speed()
                        self._view.reset_chosen_texts()

                    if (
                        text == "Increase Max Gas"
                        and self._status.is_powerup
                        and button.collidepoint(event.pos)
                    ):
                        self._status.toggle_powerup()
                        self._status.toggle_pause()
                        self._car.increase_max_gas()
                        self._view.reset_chosen_texts()

                    if (
                        text == "Increase Acceleration"
                        and self._status.is_powerup
                        and button.collidepoint(event.pos)
                    ):
                        self._status.toggle_powerup()
                        self._status.toggle_pause()
                        self._car.increase_acceleration()
                        self._view.reset_chosen_texts()

                    if (
                        text == "Increase Gas Refresh Rate"
                        and self._status.is_powerup
                        and button.collidepoint(event.pos)
                    ):
                        self._status.toggle_powerup()
                        self._status.toggle_pause()
                        self._car.increase_gas_refresh()
                        self._view.reset_chosen_texts()

                    if (
                        text == "Immediate Gas Refill"
                        and self._status.is_powerup
                        and button.collidepoint(event.pos)
                    ):
                        self._status.toggle_powerup()
                        self._status.toggle_pause()
                        self._car.gas_refill()
                        self._view.reset_chosen_texts()

    def game_event(self):
        """
        Determines what actions must be taken by the car
        when arrow keys are pressed in the game
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self._car.move_left()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self._car.move_right()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self._car.speed_up()
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self._car.brake()
        else:
            self._car.idle()
