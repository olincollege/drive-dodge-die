import pygame


class Controller:
    def __init__(self, status, view):
        self._status = status
        self._view = view

    def basic_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._status.toggle_pause()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self._view.get_pause_button.collidepoint(event.pos):
                    self._status.toggle_pause()

    def game_event(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("Left arrow was pressed!")
                if event.key == pygame.K_ESCAPE:
                    self._status.toggle_pause()
            # more function here


class CarController:
    pass
