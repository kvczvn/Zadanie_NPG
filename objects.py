
"""================================================================================
Project: Zadanie_NPG (Battleships Game)
Module: objects.py
Author: Małgorzata Hycnar
Version: 1.1
Description:Moduł definiuje klasy Ship i Treasure.
Klasa Ship przechowuje informacje o statku, rozmiar, położenie na planszy, stan uszkodzeń, kierunek ruchu oraz możliwość pełnienia funkcji rafinerii.
Zawiera metody: czy statek został zatopiony, ręczny obrót wokół dziobu z kontrolą kolizji i granic planszy.
Klasa Treasure odpowiada za mechanikę skarbu: losowe pojawienie się skarbu na wolnym polu planszy gracza oraz jego przemieszczanie się.
================================================================================"""
import random

class Ship:
    def __init__(self, size, cells, direction):
        self.size = size
        self.cells = cells
        self.health = [True] * size
        self.direction = direction
        self.is_refinery = False

    def is_sunk(self):
        return not any(self.health)

    def manually_rotate(self, grid_size, other_ships):
        """Obraca statek gracza o 90 stopni wokół dziobu."""
        if self.is_sunk(): return False

        dr, dc = self.direction
        new_direction = (dc, -dr)

        pivot_r, pivot_c = self.cells[-1]
        rotated_cells = []
        for r, c in self.cells:
            new_r = pivot_r + (c - pivot_c)
            new_c = pivot_c - (r - pivot_r)
            rotated_cells.append((new_r, new_c))

        rot_oob = any(r < 0 or r >= grid_size or c < 0 or c >= grid_size for r, c in rotated_cells)
        rot_col = False
        if not rot_oob:
            for other_ship in other_ships:
                if other_ship != self and any(cell in other_ship.cells for cell in rotated_cells):
                    rot_col = True
                    break

class Treasure:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.pos = None

    def spawn(self, player_ships):
        while True:
            r = random.randint(0, self.grid_size - 1)
            c = random.randint(0, self.grid_size - 1)
            if all((r, c) not in ship.cells for ship in player_ships):
                self.pos = (r, c)
                break
    def move(self):
        if not self.pos: return
        r, c = self.pos
        dr, dc = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < self.grid_size and 0 <= new_c < self.grid_size:
            self.pos = (new_r, new_c)


