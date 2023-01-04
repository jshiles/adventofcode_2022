from typing import List
from adventofcode.utils import read_file_strings
from adventofcode.day_03 import (
    rearrangement_priority,
    badge_element,
    element_priority,
)


def main():
    # Part 1
    result: int = sum(
        [
            rearrangement_priority(x)
            for x in read_file_strings("resources/day_03.txt")
            if len(x) > 0
        ]
    )
    print(result)  # 7691

    elf_bags = read_file_strings("resources/day_03.txt")
    result: int = sum(
        [
            element_priority(badge_element(elf_bags[idx : idx + 3]))
            for idx, _ in enumerate(elf_bags)
            if idx % 3 == 0
        ]
    )
    print(result)  # 2508


if __name__ == "__main__":
    main()
