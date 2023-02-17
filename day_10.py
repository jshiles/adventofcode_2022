import os
from adventofcode.utils import read_file_strings
from adventofcode.day_10 import CPU, execute_commands


def main():
    # Part 1
    data_filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "resources",
        "day_10.txt",
    )
    _, signal_strength, _ = execute_commands(
        read_file_strings(data_filename)
    )
    print(signal_strength)  # 15880

    # Part 2
    cpu, _, _ = execute_commands(
        read_file_strings(data_filename)
    )
    for crt_l in cpu.crt.lines:
        print(crt_l)  # PLGFKAZG


if __name__ == "__main__":
    main()
