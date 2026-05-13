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


