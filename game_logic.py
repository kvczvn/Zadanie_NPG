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
                    
    def process_fleet_movement(fleet, grid_size):

        for ship in fleet:

            if ship.is_sunk():
                continue

            dr, dc = ship.direction

            new_cells = [
                (r + dr, c + dc)
                for r, c in ship.cells
            ]

            out_of_bounds = any(
                r < 0 or r >= grid_size or
                c < 0 or c >= grid_size
                for r, c in new_cells
            )

            collision = False

            if not out_of_bounds:

                for other_ship in fleet:

                    if other_ship != ship and any(
                        cell in other_ship.cells
                        for cell in new_cells
                    ):

                        collision = True
                        break

            if not out_of_bounds and not collision:
                ship.cells = new_cells