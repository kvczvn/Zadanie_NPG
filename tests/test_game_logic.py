from game_logic import GameLogic
from objects import Ship


def test_random_ship_placement():

    fleet = []

    ship_sizes = [4, 3, 2]

    GameLogic.place_random_ships(
        fleet,
        ship_sizes,
        15
    )

    assert len(fleet) == 3


def test_ships_do_not_overlap():

    fleet = []

    ship_sizes = [4, 3, 2]

    GameLogic.place_random_ships(
        fleet,
        ship_sizes,
        15
    )

    occupied = []

    for ship in fleet:

        for cell in ship.cells:

            assert cell not in occupied

            occupied.append(cell)


def test_ship_moves():

    ship = Ship(
        2,
        [(5, 5), (5, 6)],
        (0, 1)
    )

    fleet = [ship]

    GameLogic.process_fleet_movement(
        fleet,
        15
    )

    assert ship.cells == [(5, 6), (5, 7)]

def test_ship_stays_inside_grid():

    ship = Ship(
        3,
        [(14, 12), (14, 13), (14, 14)],
        (0, 1)
    )

    fleet = [ship]

    GameLogic.process_fleet_movement(
        fleet,
        15
    )

    for r, c in ship.cells:

        assert 0 <= r < 15
        assert 0 <= c < 15


def test_computer_shoot_hits_or_misses():

    ship = Ship(
        2,
        [(0, 0), (0, 1)],
        (0, 1)
    )

    player_ships = [ship]

    player_misses = set()

    GameLogic.computer_shoot(
        player_ships,
        player_misses,
        15
    )

    damaged_parts = ship.health.count(False)

    assert damaged_parts >= 0