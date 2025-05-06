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
    description_font = pygame.font.SysFont("Times New Roman", 14)

    # Text content
    display = {}
    heading_text = heading_font.render("Select Your Car", True, (255, 255, 255))
    display["car1_subtext"] = subtext_font.render(
        "Car Model 1", True, (255, 255, 255)
    )
    display["car2_subtext"] = subtext_font.render(
        "Car Model 2", True, (255, 255, 255)
    )
    display["car3_subtext"] = subtext_font.render(
        "Car Model 3", True, (255, 255, 255)
    )

    display["car1_description"] = description_font.render(
        "Balanced and beginner-friendly.", True, (255, 255, 255)
    )
    display["car2_description"] = description_font.render(
        "High top speed and fast acceleration.", True, (255, 255, 255)
    )
    display["car3_description"] = description_font.render(
        "Quick start and large gas capacity.",
        True,
        (255, 255, 255),
    )

    # Load images
    display["car1_image"] = pygame.transform.scale(
        pygame.image.load("media/images/cars/car.png").convert_alpha(),
        (200, 300),
    )

    display["car2_image"] = pygame.transform.scale(
        pygame.image.load("media/images/cars/car2.png").convert_alpha(),
        (200, 300),
    )

    display["car3_image"] = pygame.transform.scale(
        pygame.image.load("media/images/cars/car3.png").convert_alpha(),
        (200, 300),
    )

    # Define car positions
    display["car1_rect"] = display["car1_image"].get_rect(center=(300, 400))
    display["car2_rect"] = display["car2_image"].get_rect(center=(600, 400))
    display["car3_rect"] = display["car3_image"].get_rect(center=(900, 400))

    selected_car = None
    running = True
    while running:
        screen.fill((30, 30, 30))

        screen.blit(
            heading_text,
            (screen.get_width() // 2 - heading_text.get_width() // 2, 50),
        )

        # Display car images and subtexts
        for i in range(1, 4):
            screen.blit(display[f"car{i}_image"], display[f"car{i}_rect"])
            screen.blit(
                display[f"car{i}_subtext"],
                (
                    display[f"car{i}_rect"].centerx
                    - display[f"car{i}_subtext"].get_width() // 2,
                    display[f"car{i}_rect"].bottom + 30,
                ),
            )
            screen.blit(
                display[f"car{i}_description"],
                (
                    display[f"car{i}_rect"].centerx
                    - display[f"car{i}_description"].get_width() // 2,
                    display[f"car{i}_rect"].bottom + 60,
                ),
            )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if display["car1_rect"].collidepoint(event.pos):
                    selected_car = "CarModel1"
                    running = False
                elif display["car2_rect"].collidepoint(event.pos):
                    selected_car = "CarModel2"
                    running = False
                elif display["car3_rect"].collidepoint(event.pos):
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
