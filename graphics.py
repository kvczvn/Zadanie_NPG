
================================================================================
Project: Zadanie_NPG (Battleships Game)
Module: graphics.py
Author: Michał Kapel
Version: 1.1
Description: [każdy coś swojego]
Moduł odpowiedzialny za definicje stałych, kolory i funkcje rysujące całą planszę, 
statki oraz interfejs.
================================================================================


import pygame
  
#Konfiguracja kolorów i stałych okna (#5)

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

font = pygame.font.SysFont("arial", 18, bold=True)
small_font = pygame.font.SysFont("arial", 14)
title_font = pygame.font.SysFont("arial", 26, bold=True)


