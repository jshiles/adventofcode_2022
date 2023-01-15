from typing import List, Tuple
from adventofcode.utils import read_file_strings
from adventofcode.day_09 import VisitedPoint, Rope


def main():
    filename: str = "resources/day_09.txt"
    moves: List[str] = read_file_strings(filename)

    # Part 1
    starting_point = VisitedPoint()
    rope: Rope = Rope(starting_point, num_knots=2)
    for move in moves:
        direction, length = move.strip().split(" ")
        rope.simulate_motion(direction, int(length))
    unique_tail_points = len(set(rope.historical_tail_locations))
    print(unique_tail_points)  # 6642


if __name__ == "__main__":
    main()
