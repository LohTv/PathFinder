import pygame
import sys
from PlaneClass import Plane
import tkinter as tk


def run():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    print(screen_width)
    pygame.init()
    CELL_SIZE = (80/1536) * screen_width
    print(CELL_SIZE)
    GRID_SIZE = 5
    WIDTH = CELL_SIZE * GRID_SIZE
    HEIGHT = CELL_SIZE * GRID_SIZE + (100/400) * WIDTH
    print(WIDTH)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Path Recall")
    clock = pygame.time.Clock()
    plane = Plane(screen)
    last_reveal_time = pygame.time.get_ticks()
    last_reveal_time_2 = pygame.time.get_ticks()
    new_lvl = True
    score = 0
    green_cell = None
    LVL = 1

    while True:
        now = pygame.time.get_ticks()
        clicked = False
        click_pos = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
                click_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and plane.game_over:
                new_lvl = True
                plane.START_GAME()

        if new_lvl:
            last_reveal_time = pygame.time.get_ticks()
            path = plane.Create_Path(LVL)
            show_ind = 0
            show_level = True
            new_lvl = False

        plane.draw(clicked, show_ind, show_level, green_cell)

        if show_ind <= len(path) and now - last_reveal_time > 1000:
            last_reveal_time = now
            show_ind += 1

        if green_cell and now - last_reveal_time_2 > 1000:
            last_reveal_time_2 = now
            green_cell = None

        if show_ind == len(path):
            show_level = False

        if not show_level and clicked and click_pos:
            green_cell = plane.handle_click(click_pos)
            if green_cell:
                score += 1
                last_reveal_time_2 = now
            else:
                plane.GAME_OVER()
                LVL = 1
                score = 0
                new_lvl = False

        if score == LVL and not plane.game_over:
            score = 0
            LVL += 1
            new_lvl = True


        font = pygame.font.SysFont('Arial', 36)
        score_surf = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_surf, (10, HEIGHT - 40))
        font = pygame.font.SysFont('Arial', 36)
        score_surf = font.render(f"Level: {LVL}", True, (0, 0, 0))
        screen.blit(score_surf, (WIDTH/2 + 10, HEIGHT - 40))

        pygame.display.flip()
        clock.tick(60)