

"""================================================================================
Project: Zadanie_NPG (Battleships Game)
Module: graphics.py
Author: Michał Kapel
Version: 1.1
Description: Moduł odpowiedzialny za definicje stałych, kolory i funkcje rysujące całą planszę,
statki oraz interfejs.
================================================================================
"""


import pygame

pygame.init() 
WIDTH, HEIGHT = 1000, 750 
CELL_SIZE = 25           
GRID_SIZE = 15           
SHIP_SIZES = [4, 3, 3, 2, 2, 1, 1]

P1_OFFSET_X, P1_OFFSET_Y = 80, 120
P2_OFFSET_X, P2_OFFSET_Y = 540, 120

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)
BLUE = (50, 150, 255)
RED = (255, 50, 50)
YELLOW = (255, 220, 50)
GREEN = (50, 200, 50)
DARK_GREEN = (0, 150, 0)
PURPLE = (200, 100, 255)
ORANGE = (255, 140, 0)
GOLD = (255, 215, 0)
BG_COLOR = (30, 40, 50)

#interfejs statystyk (#27)
font = pygame.font.SysFont("arial", 18, bold=True)
small_font = pygame.font.SysFont("arial", 14)
title_font = pygame.font.SysFont("arial", 26, bold=True)

#funkcja tworząca przyciski i menu sklepu (#19)
def draw_button(screen, rect, text, color):
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)
    text_surf = font.render(text, True, BLACK)
    screen.blit(text_surf, (rect.x + rect.width//2 - text_surf.get_width()//2, 
                            rect.y + rect.height//2 - text_surf.get_height()//2))
#funkcja rysuje siatke 15X15 (#9) i statki na planszy (#15)
def draw_fleet_and_misses(screen, ships, misses, offset_x, offset_y, game_over, hide_ships=False, is_player_board=False, treasure_pos=None):
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            x = offset_x + c * CELL_SIZE
            y = offset_y + r * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            #funkcja Wizualizacja pudeł (znak "O") (#32)
            if (r, c) in misses:
                pygame.draw.rect(screen, DARK_GRAY, rect)
                text_surface = small_font.render("O", True, WHITE)
                screen.blit(text_surface, (x + 8, y + 4))
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

    if is_player_board and treasure_pos:
        tr, tc = treasure_pos
        tx = offset_x + tc * CELL_SIZE
        ty = offset_y + tr * CELL_SIZE
        pygame.draw.circle(screen, GOLD, (tx + CELL_SIZE//2, ty + CELL_SIZE//2), CELL_SIZE//2 - 2)
        pygame.draw.circle(screen, BLACK, (tx + CELL_SIZE//2, ty + CELL_SIZE//2), CELL_SIZE//2 - 2, 1)

    for ship in ships:
        for idx, (r, c) in enumerate(ship.cells):
            is_front = (idx == len(ship.cells) - 1)
            is_healthy = ship.health[idx]
            x = offset_x + c * CELL_SIZE
            y = offset_y + r * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            
            if not is_healthy:
                pygame.draw.rect(screen, RED, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)
                text_surface = small_font.render("X", True, BLACK)
                screen.blit(text_surface, (x + 8, y + 4))
            elif not hide_ships or ship.is_sunk() or game_over:
                ship_color = DARK_GREEN if getattr(ship, 'is_refinery', False) else BLUE
                pygame.draw.rect(screen, ship_color, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)
                if is_front:
                    pygame.draw.circle(screen, YELLOW, (x + CELL_SIZE//2, y + CELL_SIZE//2), 5)
