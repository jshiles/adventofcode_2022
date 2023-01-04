from typing import List
from adventofcode.utils import read_file_strings
from adventofcode.day_01 import (
    greatest_elf_calorie_count,
    top_n_elf_calorie_count,
)


def main():
    file_contents = read_file_strings("resources/day_01.txt")
    print(greatest_elf_calorie_count(file_contents))  # 70296
    print(top_n_elf_calorie_count(file_contents, 3))  # 205381


if __name__ == "__main__":
    main()
