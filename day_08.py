from typing import List
from adventofcode.utils import read_file_strings
from adventofcode.day_08 import visible_invisible, highest_scenic_score


def main():
    # Part 1
    filename: str = "resources/day_08.txt"

    # create grid
    grid: List[List[int]] = []
    for row in read_file_strings(filename):
        grid.append([int(x) for x in list(row)])

    vis, _ = visible_invisible(grid)
    print(vis)  # 1560

    # Part 2
    print(highest_scenic_score(grid))  # 252000


if __name__ == "__main__":
    main()
