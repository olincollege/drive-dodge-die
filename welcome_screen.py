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
    play = pygame.image.load(
        "media/images/buttons/play-button.png"
    ).convert_alpha()
    info = pygame.transform.scale(
        pygame.image.load("media/images/buttons/info.png").convert_alpha(),
        (150, 150),
    )
    high_score = pygame.transform.scale(
        pygame.image.load(
            "media/images/buttons/high_score.png"
        ).convert_alpha(),
        (150, 150),
    )
    flag_left = pygame.transform.scale(
        pygame.image.load("media/images/flag_left.png").convert_alpha(),
        (300, 300),
    )
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
        pygame.init()
        screen.fill((30, 30, 30))

        screen.blit(
            heading_text,
            (screen.get_width() // 2 - heading_text.get_width() // 2, 150),
        )

        # Display images and subtexts
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
                    info_text()
                if highscore_rect.collidepoint(event.pos):
                    running = True
                    show_high_scores()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = True
                    return


def clear_score():
    """clears the high score board"""
    with open("high_score.csv", "w", encoding="utf-8") as file:
        file.truncate()
    headers = pd.DataFrame({"Username": [], "Score": []})
    headers.to_csv("high_score.csv", index=False)


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
    lines = {}
    lines[1] = big_font.render("How to Play:", True, (255, 255, 255))
    lines[2] = small_font.render(
        "Avoid obstacles, survive, and race to victory!", True, (255, 255, 255)
    )
    lines[3] = small_font.render(
        "Press the _up_ arrow key or _w_ to accelerate", True, (255, 255, 255)
    )
    lines[4] = small_font.render(
        "Press the _down_ arrow key or _s_ to decelerate", True, (255, 255, 255)
    )
    lines[5] = small_font.render(
        "Press the _left_ arrow key or _a_ to move left", True, (255, 255, 255)
    )
    lines[6] = small_font.render(
        "Press the _right_ arrow key or _d_ to move left", True, (255, 255, 255)
    )
    lines[7] = small_font.render(
        "_Click_ on power-up choices to choose them", True, (255, 255, 255)
    )
    lines[8] = small_font.render("Press ESC to close", True, (255, 255, 255))

    running = True
    while running:
        popup_screen.fill((50, 50, 50))

        y_coord = [50, 150, 180, 210, 240, 270, 300, 380]
        for i in range(8):
            popup_screen.blit(
                lines[i + 1],
                (popup_width // 2 - lines[i + 1].get_width() // 2, y_coord[i]),
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
    height = 700
    width = 700
    screen = pygame.display.set_mode((width, height))
    # initiate variables
    heading_font = pygame.font.SysFont("Times New Roman", 40)
    header_text = heading_font.render("Leaderboard", True, (255, 255, 255))
    subtext_font = pygame.font.SysFont("Times New Roman", 20)

    # initiate and write words inside of the high score box
    username_header = heading_font.render("Username: ", True, (255, 255, 255))
    score_header = heading_font.render("Score: ", True, (255, 255, 255))
    exit_message = subtext_font.render(
        "Press ESC to exit, press C to clear scores", True, (255, 255, 255)
    )

    running = True
    while running:
        screen.fill((50, 50, 50))
        screen.blit(header_text, (width // 3, 50))
        screen.blit(username_header, (width // 3 - 50, 150))
        screen.blit(
            score_header,
            (2 * width // 3, 150),
        )
        for i, (_, row) in enumerate(pd.read_csv("high_score.csv").iterrows()):
            username_text = subtext_font.render(
                str(row["Username"]), True, (255, 255, 255)
            )
            score_text = subtext_font.render(
                str(row["Score"]), True, (255, 255, 255)
            )
            screen.blit(username_text, (width // 3 - 50, 150 + 50 + i * 25))
            screen.blit(
                score_text,
                (
                    2 * width // 3,
                    150 + 50 + i * 25,
                ),
            )
        screen.blit(exit_message, (width // 3, height - 50))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    welcome()
                if event.key == pygame.K_c:
                    clear_score()
