import random
import pygame
from objects import Ship

class GameLogic:

    @staticmethod
    def place_random_ships(fleet_list, ship_sizes, grid_size):

        for size in ship_sizes:

            placed = False

            while not placed:

                orientation = random.choice(['H', 'V'])

                if orientation == 'H':

                    r = random.randint(0, grid_size - 1)
                    c = random.randint(0, grid_size - size)

                    cells = [(r, c + i) for i in range(size)]

                    direction = (0, 1)

                else:

                    r = random.randint(0, grid_size - size)
                    c = random.randint(0, grid_size - 1)

                    cells = [(r + i, c) for i in range(size)]

                    direction = (1, 0)

                collision = False

                for existing_ship in fleet_list:

                    if any(cell in existing_ship.cells for cell in cells):

                        collision = True
                        break

                if not collision:

                    fleet_list.append(
                        Ship(size, cells, direction)
                    )

                    placed = True