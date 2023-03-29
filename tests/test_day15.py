import os
from adventofcode.day_15 import (
    Coordinate,
    Sensor,
    no_beacon,
    find_distress_beacon,
)
from typing import List


class TestDay15:

    puzzle_input: List[Sensor] = [
        Sensor(Coordinate(x=2, y=18), Coordinate(x=-2, y=15)),
        Sensor(Coordinate(x=9, y=16), Coordinate(x=10, y=16)),
        Sensor(Coordinate(x=13, y=2), Coordinate(x=15, y=3)),
        Sensor(Coordinate(x=12, y=14), Coordinate(x=10, y=16)),
        Sensor(Coordinate(x=10, y=20), Coordinate(x=10, y=16)),
        Sensor(Coordinate(x=14, y=17), Coordinate(x=10, y=16)),
        Sensor(Coordinate(x=8, y=7), Coordinate(x=2, y=10)),
        Sensor(Coordinate(x=2, y=0), Coordinate(x=2, y=10)),
        Sensor(Coordinate(x=0, y=11), Coordinate(x=2, y=10)),
        Sensor(Coordinate(x=20, y=14), Coordinate(x=25, y=17)),
        Sensor(Coordinate(x=17, y=20), Coordinate(x=21, y=22)),
        Sensor(Coordinate(x=16, y=7), Coordinate(x=15, y=3)),
        Sensor(Coordinate(x=14, y=3), Coordinate(x=15, y=3)),
        Sensor(Coordinate(x=20, y=1), Coordinate(x=15, y=3)),
    ]

    def test_manh_distance(self):
        """Grid distance."""
        assert Coordinate(1, 1).manh_distance(Coordinate(1, 1)) == 0
        assert Coordinate(5, 4).manh_distance(Coordinate(3, 2)) == 4
        assert Coordinate(1, 1).manh_distance(Coordinate(0, 3)) == 3

    def test_no_sensor(self):
        """ """
        coords = no_beacon(self.puzzle_input, y=10)
        assert len(coords) == 26

    def test_beach_location(self):
        """ """
        target = Coordinate(14, 11)
        assert find_distress_beacon(self.puzzle_input) == target
