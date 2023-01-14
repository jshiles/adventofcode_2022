from typing import List, Tuple
from adventofcode.utils import read_file_strings
from adventofcode.day_09 import VisitedPoint


def main():
    # Part 1
    filename: str = "resources/day_09.txt"
    starting_point = VisitedPoint()
    all_tail_points: List[VisitedPoint] = [starting_point]

    for move in read_file_strings(filename):
        direction, length = move.strip().split(" ")

        head_points = starting_point.moveHead(direction, int(length))
        tail_points = all_tail_points[-1].moveTail(head_points)
        if len(tail_points):
            all_tail_points = all_tail_points + tail_points
        starting_point = (
            head_points[-1] if len(head_points) else starting_point
        )

    unique_tail_points = len(set(all_tail_points))
    print(unique_tail_points)


if __name__ == "__main__":
    main()
