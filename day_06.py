from typing import List
from adventofcode.utils import read_file_strings
from adventofcode.day_06 import packet_marker_detection, message_start_detection


def main():
    # Part 1
    filename: str = "resources/day_06.txt"
    datastream: str = read_file_strings(filename)[0]
    print(packet_marker_detection(datastream))  # 1210

    # Part 2
    print(message_start_detection(datastream))  # 3476


if __name__ == "__main__":
    main()
