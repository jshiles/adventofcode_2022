from typing import List
from adventofcode.utils import read_file_strings
from adventofcode.day_04 import contained_pair, overlapping_pair


def main():
    # Part 1
    pairs = [x.strip().split(',') for x in read_file_strings("resources/day_04.txt")]
    print(sum([1 for x, y in pairs if contained_pair(x, y)]))  # 513

    # Part 2
    print(sum([1 for x, y in pairs if overlapping_pair(x, y)]))  # 878


if __name__ == "__main__":
    main()
