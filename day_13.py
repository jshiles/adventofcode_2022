import os
from typing import List, Tuple
from adventofcode.day_13 import PacketData, str2packetdata


def main():
    filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "resources",
        "day_13.txt",
    )
    packet_pairs: bool = []

    # Part 1
    # Print the index (starting at 1) for all properly order paket pairs.
    with open(filename) as file:
        pair: List[PacketData] = []
        for line in file:
            if line.strip() == "":
                packet_pairs.append(pair[0] <= pair[1])
                pair = []
            else:
                pair.append(str2packetdata(line.strip()))
    print(sum([idx + 1 for idx, x in enumerate(packet_pairs) if x]))


if __name__ == "__main__":
    main()
