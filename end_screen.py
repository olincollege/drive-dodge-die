"""Contains functions needed to draw and run the end screen"""

import math
import pygame
import pandas as pd


def draw_end(road, checkpoint, view):
    """draws the end screen"""
    # initialize things
    pygame.init()
    screen = pygame.display.set_mode((1250, 750))
    pygame.display.set_caption("End Screen")
    pygame.font.init()
    subtext_font = pygame.font.Font(None, 20)
    heading_font = pygame.font.Font(None, 50)

    # text content
    score = calculate_score(road, checkpoint, view)
    lines = get_text(score)
    rendered = render_lines(lines, subtext_font, heading_font)

    # initialize user input variables
    base_font = pygame.font.Font(None, 32)
    user_text = ""
    input_rect = pygame.Rect(500, 360, 140, 32)
    input_rect.centerx = screen.get_width() // 2 + 5

    color_active = (0, 0, 0)
    color_passive = (255, 0, 0)
    color = color_passive
    active = False

    # display
    running = True
    while running:
        # give screen a color and draw text that does not change
        screen.fill((50, 168, 76))
        draw_text(screen, rendered)
        draw_high_score(screen)

        # check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    save_score(user_text, score["total"])
                    running = False
                if active is True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        # draw user input
        if active:
            color = color_active
        else:
            color = color_passive
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        input_rect.w = max(100, text_surface.get_width() + 10)
        pygame.draw.rect(screen, color, input_rect, 6)
        screen.blit(text_surface, (input_rect.x + 2, input_rect.y + 2))

        # update screen
        pygame.display.update()
        pygame.time.Clock().tick(60)


def draw_high_score(screen):
    """draw high scores"""
    heading_font = pygame.font.Font(None, 40)
    score_rect = pygame.Rect((300, 480), (400, 200))
    score_rect.centerx = screen.get_width() // 2
    header_text = heading_font.render("High Scores:", True, (0, 0, 0))
    x_pos = score_rect.w // 2 - header_text.get_width() // 2 + score_rect.x
    screen.blit(header_text, (x_pos, 430))
    heading_font = pygame.font.Font(None, 40)
    subtext_font = pygame.font.Font(None, 20)
    pygame.draw.rect(screen, (0, 0, 255), score_rect)
    username_header = heading_font.render("Username: ", True, (0, 0, 0))
    score_header = heading_font.render("Score: ", True, (0, 0, 0))
    screen.blit(username_header, (score_rect.x + 10, score_rect.y + 10))
    screen.blit(
        score_header,
        ((score_rect.w // 2) + score_rect.x + 10, score_rect.y + 10),
    )
    all_scores = pd.read_csv("high_score.csv")
    for i, (_, row) in enumerate(all_scores.iterrows()):
        username_text = subtext_font.render(
            str(row["Username"]), True, (0, 0, 0)
        )
        score_text = subtext_font.render(str(row["Score"]), True, (0, 0, 0))
        screen.blit(
            username_text, (score_rect.x + 10, score_rect.y + 50 + i * 25)
        )
        screen.blit(
            score_text,
            (
                (score_rect.w // 2) + score_rect.x + 10,
                score_rect.y + 50 + i * 25,
            ),
        )


def save_score(username, score):
    """saves the username and the score onto a csv"""
    all_scores = pd.read_csv("high_score.csv")
    new_row = pd.DataFrame({"Username": [username], "Score": [score]})
    all_scores = pd.concat([all_scores, new_row], ignore_index=True)
    all_scores = all_scores.sort_values(by="Score", ascending=False)
    all_scores.to_csv("high_score.csv", index=False)


def draw_text(screen, rendered):
    """draws all necessary text"""
    y_pos = [200, 230, 280, 310, 330]
    for i in range(5):
        screen.blit(
            rendered[i + 1],
            (
                screen.get_width() // 2 - rendered[i + 1].get_width() // 2,
                y_pos[i],
            ),
        )


def get_text(score):
    """returns a dictionary of the 5 lines of text"""
    line = {}
    line[1] = "oh no! you died."
    line[2] = f"Total Score: {score["total"]}"
    line[3] = "Good job!"
    line[4] = (
        f"You ran {score['distance']} pixels in {score['time']} seconds, going"
        f" through a total of {score['checkpoints']} checkpoints!"
    )
    line[5] = (
        "To save your score, input your name in the box below and press ENTER."
    )
    return line


def render_lines(lines, subtext_font, heading_font):
    """returns a dictionary of the rendered 5 lines of text"""
    rendered = {}
    for i in [1, 3, 4, 5]:
        rendered[i] = subtext_font.render(lines[i], True, (0, 0, 0))
    rendered[2] = heading_font.render(lines[2], True, (0, 0, 0))
    return rendered


def calculate_score(road, checkpoint, view):
    """calculate total score"""
    score = {}
    score["distance"] = math.ceil(road.get_distance_traveled)
    score["checkpoints"] = checkpoint.get_checkpoints_reached
    score["time"] = (pygame.time.get_ticks() - view.get_start_time) // 1000

    score["total"] = score["distance"] // score["time"] + score["checkpoints"]

    return score
