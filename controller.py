import pygame


class Controller:
    def __init__(self, status, view, car):
        self._status = status
        self._view = view
        self._car_controller = CarController(car)

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
        self._car_controller.handle_input()


class CarController:
    """
    Controller class for the car
    """

    def __init__(self, car):
        self._car = car

    def handle_input(self):
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
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self._car.brake()
        else:
            self._car.idle()
