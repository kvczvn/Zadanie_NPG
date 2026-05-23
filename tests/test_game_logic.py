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