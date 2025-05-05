"""Sets up the car selection screen"""

import pygame
from car import CarModel1, CarModel2, CarModel3


def select_car():
    """function that sets up the car selection page"""
    pygame.init()
    screen = pygame.display.set_mode((1280, 950))
    pygame.display.set_caption("Select Your Car")
    pygame.font.init()
    heading_font = pygame.font.SysFont("Times New Roman", 50)
    subtext_font = pygame.font.SysFont("Times New Roman", 20)

    # Text content
    heading_text = heading_font.render("Select Your Car", True, (255, 255, 255))
    car1_subtext = subtext_font.render("Car Model 1", True, (255, 255, 255))
    car2_subtext = subtext_font.render("Car Model 2", True, (255, 255, 255))
    car3_subtext = subtext_font.render("Car Model 3", True, (255, 255, 255))

    # CarModel1: Balanced and beginner-friendly.

    # CarModel2: High top speed and fast acceleration.

    # CarModel3: Quick start and strong acceleration, great for short bursts.

    # Load images
<<<<<<< HEAD
    car1_image = pygame.transform.scale(
        pygame.image.load("media/images/cars/car.png").convert_alpha(),
        (200, 300),
    )

    car2_image = pygame.transform.scale(
        pygame.image.load("media/images/cars/car2.png").convert_alpha(),
        (200, 300),
    )

    car3_image = pygame.transform.scale(
        pygame.image.load("media/images/cars/car3.png").convert_alpha(),
        (200, 300),
    )
=======
    car1_image = pygame.image.load("media/images/cars/car.png").convert_alpha()
    car1_image = pygame.transform.scale(car1_image, (200, 300))

    car2_image = pygame.image.load("media/images/cars/car2.png").convert_alpha()
    car2_image = pygame.transform.scale(car2_image, (200, 300))

    car3_image = pygame.image.load("media/images/cars/car3.png").convert_alpha()
    car3_image = pygame.transform.scale(car3_image, (200, 300))
>>>>>>> 4b3fc43faed4f06e7de116bc00a3511d09323af4

    # Define car positions
    car1_rect = car1_image.get_rect(center=(300, 400))
    car2_rect = car2_image.get_rect(center=(600, 400))
    car3_rect = car3_image.get_rect(center=(900, 400))

    selected_car = None
    running = True
    while running:
        screen.fill((30, 30, 30))

        screen.blit(
            heading_text,
            (screen.get_width() // 2 - heading_text.get_width() // 2, 50),
        )

        # Display car images and subtexts
        screen.blit(car1_image, car1_rect)
        screen.blit(
            car1_subtext,
            (
                car1_rect.centerx - car1_subtext.get_width() // 2,
                car1_rect.bottom + 30,
            ),
        )

        screen.blit(car2_image, car2_rect)
        screen.blit(
            car2_subtext,
            (
                car2_rect.centerx - car2_subtext.get_width() // 2,
                car2_rect.bottom + 30,
            ),
        )

        screen.blit(car3_image, car3_rect)
        screen.blit(
            car3_subtext,
            (
                car3_rect.centerx - car3_subtext.get_width() // 2,
                car3_rect.bottom + 30,
            ),
        )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if car1_rect.collidepoint(event.pos):
                    selected_car = "CarModel1"
                    running = False
                elif car2_rect.collidepoint(event.pos):
                    selected_car = "CarModel2"
                    running = False
                elif car3_rect.collidepoint(event.pos):
                    selected_car = "CarModel3"
                    running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or pygame.K_KP1:
                    selected_car = "CarModel1"
                    running = False
                elif event.key == pygame.K_2 or pygame.K_KP2:
                    selected_car = "CarModel2"
                    running = False
                elif event.key == pygame.K_3 or pygame.K_KP3:
                    selected_car = "CarModel3"
                    running = False

        if selected_car == "CarModel1":
            return CarModel1()
        if selected_car == "CarModel2":
            return CarModel2()
        if selected_car == "CarModel3":
            return CarModel3()
