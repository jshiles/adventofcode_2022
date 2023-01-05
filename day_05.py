from typing import List
from adventofcode.day_05 import parse_file, move, move_n, get_top_elements


def main():
    # Part 1
    filename: str = "resources/day_05.txt"
    stacks, moves = parse_file(filename)
    for qty, from_stack, to_stack in moves:
        for _ in range(qty):
            move(stacks, from_stack - 1, to_stack - 1)
    print(get_top_elements(stacks))  # GFTNRBZPF

    # Part 2
    stacks, moves = parse_file(filename)
    for qty, from_stack, to_stack in moves:
        move_n(stacks, from_stack - 1, to_stack - 1, qty)
    print(get_top_elements(stacks))  # VRQWPDSGP


if __name__ == "__main__":
    main()
