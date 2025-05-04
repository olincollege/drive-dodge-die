"""Sets up the welcome screen"""

import pygame
import pandas as pd


def welcome():
    """function that sets up the car selection page"""
    pygame.init()
    screen = pygame.display.set_mode((1280, 950))
    pygame.display.set_caption("Welcome to drive-dodge-die")
    pygame.font.init()
    heading_font = pygame.font.SysFont("Times New Roman", 50)
    subtext_font = pygame.font.SysFont("Times New Roman", 20)

    # Text content
    heading_text = heading_font.render("drive-dodge-die", True, (255, 255, 255))
    subtext = subtext_font.render("Click to play", True, (255, 255, 255))
    option1 = subtext_font.render("Info", True, (255, 255, 255))
    option2 = subtext_font.render("Leaderboard", True, (255, 255, 255))

    # Load images
    play = pygame.image.load("images/buttons/play-button.png").convert_alpha()
    info = pygame.image.load("images/buttons/info.png").convert_alpha()
    info = pygame.transform.scale(info, (150, 150))
    high_score = pygame.image.load(
        "images/buttons/high_score.png"
    ).convert_alpha()
    high_score = pygame.transform.scale(high_score, (150, 150))
    flag_left = pygame.image.load("images/flag_left.png").convert_alpha()
    flag_left = pygame.transform.scale(flag_left, (300, 300))
    flag_right = pygame.transform.flip(flag_left, True, False)

    # Define button positions
    play_rect = play.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2)
    )
    info_rect = info.get_rect(center=(screen.get_width() // 3, 800))
    highscore_rect = high_score.get_rect(
        center=(2 * screen.get_width() // 3, 800)
    )
    flag_left_rect = flag_left.get_rect(
        center=(screen.get_width() // 4, screen.get_height() // 2)
    )
    flag_right_rect = flag_right.get_rect(
        center=(3 * screen.get_width() // 4, screen.get_height() // 2)
    )

    running = True
    while running:
        screen.fill((30, 30, 30))

        screen.blit(
            heading_text,
            (screen.get_width() // 2 - heading_text.get_width() // 2, 150),
        )

        # Display car images and subtexts

        screen.blit(play, play_rect)
        screen.blit(
            subtext,
            (
                screen.get_width() // 2 - subtext.get_width() // 2,
                play_rect.bottom + 30,
            ),
        )

        screen.blit(info, info_rect)
        screen.blit(
            option1,
            (
                info_rect.centerx - 20,
                info_rect.bottom + 30,
            ),
        )

        screen.blit(high_score, highscore_rect)
        screen.blit(
            option2,
            (
                highscore_rect.centerx - 50,
                highscore_rect.bottom + 30,
            ),
        )

        screen.blit(flag_left, flag_left_rect)
        screen.blit(flag_right, flag_right_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    running = True
                    return
                if info_rect.collidepoint(event.pos):
                    running = True
                    pygame.quit()
                    info_text()
                if highscore_rect.collidepoint(event.pos):
                    running = True
                    pygame.quit()
                    show_high_scores()


def info_text():
    """
    Creates a pop-up window with game info
    """
    popup_width, popup_height = 700, 700
    popup_screen = pygame.display.set_mode((popup_width, popup_height))
    pygame.display.set_caption("Game Info")

    pygame.font.init()
    big_font = pygame.font.SysFont("Times New Roman", 30)
    small_font = pygame.font.SysFont("Times New Roman", 20)

    # Text content
    info_content = big_font.render(
        "Welcome to Drive-Dodge-Die! Here are the rules", True, (255, 255, 255)
    )
    description = small_font.render(
        "Avoid obstacles, survive, and race to victory!", True, (255, 255, 255)
    )
    close_text = small_font.render("Press ESC to close", True, (255, 255, 255))

    running = True
    while running:
        popup_screen.fill((50, 50, 50))

        popup_screen.blit(
            info_content, (popup_width // 2 - info_content.get_width() // 2, 50)
        )
        popup_screen.blit(
            description, (popup_width // 2 - description.get_width() // 2, 150)
        )
        popup_screen.blit(
            close_text, (popup_width // 2 - close_text.get_width() // 2, 300)
        )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                welcome()


def show_high_scores():
    """Displays all the highscores"""
    pygame.init()
    h = 700
    w = 700
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Leaderboard")
    # initiate variables
    heading_font = pygame.font.SysFont("Times New Roman", 40)
    header_text = heading_font.render("Leaderboard", True, (255, 255, 255))

    heading_font = pygame.font.SysFont("Times New Roman", 30)
    subtext_font = pygame.font.SysFont("Times New Roman", 20)

    # initiate and write words inside of the high score box
    username_header = heading_font.render("Username: ", True, (255, 255, 255))
    score_header = heading_font.render("Score: ", True, (255, 255, 255))
    exit_message = subtext_font.render(
        "Press ESC to exit", True, (255, 255, 255)
    )

    running = True
    while running:
        screen.fill((50, 50, 50))
        screen.blit(header_text, (w // 3, 50))
        screen.blit(username_header, (w // 3 - 50, 150))
        screen.blit(
            score_header,
            (2 * w // 3, 150),
        )
        all_scores = pd.read_csv("high_score.csv")
        for i, (_, row) in enumerate(all_scores.iterrows()):
            username_text = subtext_font.render(
                str(row["Username"]), True, (255, 255, 255)
            )
            score_text = subtext_font.render(
                str(row["Score"]), True, (255, 255, 255)
            )
            screen.blit(username_text, (w // 3 - 50, 150 + 50 + i * 25))
            screen.blit(
                score_text,
                (
                    2 * w // 3,
                    150 + 50 + i * 25,
                ),
            )
        screen.blit(exit_message, (w // 3, h - 50))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                welcome()
