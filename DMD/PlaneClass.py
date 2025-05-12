import pygame
import random


pygame.init()


class Plane():
    def __init__(self, screen, CELL_SIZE = 80, GRID_SIZE = 5):
        self.screen = screen
        self.CELL_SIZE = CELL_SIZE
        self.GRID_SIZE = GRID_SIZE
        self.DARK_BLUE = (0,   0, 139)
        self.LIGHT_BLUE = (173, 216, 230)
        self.HOVER_COLOR = (255, 215, 0)
        self.CORRECT_CLICK_COLOR = (0, 255, 0)
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.game_over = False

    def draw(self, clicked, cell_ind, show_level, green_cell):
        self.screen.fill(self.LIGHT_BLUE)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                if self.game_over:
                    rect = pygame.Rect(col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
                    pygame.draw.rect(self.screen, (255, 0, 0), rect)
                    pygame.draw.rect(self.screen, (255, 255, 255), rect, width=2)

                elif show_level and (row, col) == self.path[cell_ind]:
                    rect = pygame.Rect(col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
                    pygame.draw.rect(self.screen, (255, 0, 0), rect)
                    pygame.draw.rect(self.screen, (255, 255, 255), rect, width=2)

                elif (row, col) == green_cell:
                    rect = pygame.Rect(col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
                    pygame.draw.rect(self.screen, (0, 255, 0), rect)
                    pygame.draw.rect(self.screen, (255, 255, 255), rect, width=2)

                elif col * self.CELL_SIZE <= mouse_x < (col + 1) * self.CELL_SIZE and row * self.CELL_SIZE <= mouse_y < (row + 1) * self.CELL_SIZE:
                    if clicked:
                        rect = pygame.Rect(col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
                        pygame.draw.rect(self.screen, self.HOVER_COLOR, rect)
                        pygame.draw.rect(self.screen, (255, 255, 255), rect, width=2)
                    else:
                        rect = pygame.Rect(col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
                        pygame.draw.rect(self.screen, self.LIGHT_BLUE, rect)
                        pygame.draw.rect(self.screen, (255, 255, 255), rect, width=2)

                else:
                    rect = pygame.Rect(col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
                    pygame.draw.rect(self.screen, self.DARK_BLUE, rect)
                    pygame.draw.rect(self.screen, (255, 255, 255), rect, width=2)

    def Create_Path(self, LEVEL):
        start = (random.randint(0, self.GRID_SIZE - 1), random.randint(0, self.GRID_SIZE-  1))
        self.path = [start]
        for _ in range(LEVEL-1):
            x, y = self.path[-1]
            valid_directions = []
            for (dx, dy) in self.directions:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < 5 and 0 <= new_y < 5:
                    valid_directions.append((dx, dy))
            random_direction = random.choice(valid_directions)
            new_x, new_y = x + random_direction[0], y + random_direction[1]
            self.path.append((new_x, new_y))
        self.click_index = 0
        self.reveal_index = 0
        return self.path

    def handle_click(self, pos):
        self.green_cell_ = None
        row = pos[1] // self.CELL_SIZE
        col = pos[0] // self.CELL_SIZE
        if self.click_index < len(self.path) and (row, col) == self.path[self.click_index]:
            self.click_index += 1
            self.green_cell_ = (row, col)
        return self.green_cell_

    def GAME_OVER(self):
        self.game_over = True

    def START_GAME(self):
        self.game_over = False






