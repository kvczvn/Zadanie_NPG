import random
import pygame
from src.objects import Ship

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

    @staticmethod            
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

            if out_of_bounds or collision:

                ship.direction = (dc, -dr)

                pivot_r, pivot_c = ship.cells[-1]

                rotated_cells = []

                for r, c in ship.cells:

                    rotated_cells.append(
                        (
                            pivot_r + (c - pivot_c),
                            pivot_c - (r - pivot_r)
                        )
                    )

                rot_oob = any(
                    r < 0 or r >= grid_size or
                    c < 0 or c >= grid_size
                    for r, c in rotated_cells
                )

                rot_col = False

                if not rot_oob:

                    for other_ship in fleet:

                        if other_ship != ship and any(
                            cell in other_ship.cells
                            for cell in rotated_cells
                        ):

                            rot_col = True
                            break

                if not rot_oob and not rot_col:
                    ship.cells = rotated_cells

            else:
                ship.cells = new_cells
                
    @staticmethod
    def computer_shoot(player_ships, player_misses, grid_size):

        while True:

            r = random.randint(0, grid_size - 1)
            c = random.randint(0, grid_size - 1)

            if (r, c) in player_misses:
                continue

            hit_already = False

            for ship in player_ships:

                if (r, c) in ship.cells:

                    idx = ship.cells.index((r, c))

                    if not ship.health[idx]:
                        hit_already = True

            if hit_already:
                continue

            break

        pygame.time.delay(300)

        hit_something = False

        for ship in player_ships:

            if (r, c) in ship.cells:

                idx = ship.cells.index((r, c))

                ship.health[idx] = False

                hit_something = True
                break

        if not hit_something:
            player_misses.add((r, c))