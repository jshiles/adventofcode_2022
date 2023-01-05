from typing import List
from adventofcode.utils import read_file_strings
from adventofcode.day_07 import Command, parse_command_line, process_commands


def main():
    # Part 1
    filename: str = "resources/day_07.txt"
    terminal_output: str = read_file_strings(filename)
    commands: List[Command] = parse_command_line(terminal_output)
    active_dir = process_commands(commands)
    print(active_dir.sum_dirs_lte_n(n=100000))  # 1648397

    # Part 2
    disk_used = active_dir.file_size()
    disk_required = 30000000 - (70000000 - disk_used)
    dirs = active_dir.dir_sizes()
    _, size = min(
        [(k, v) for k, v in dirs.items() if v >= disk_required],
        key=lambda t: t[1],
    )
    print(size)  # 1815525


if __name__ == "__main__":
    main()
