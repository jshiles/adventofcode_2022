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
    print(sum([idx + 1 for idx, x in enumerate(packet_pairs) if x]))  # 5675

    # Part 2
    # Ignore blank lines and sort everthing plus two divider packets.
    # Print the multiplication of the indexes (starting at 1) of the divider
    # packets.
    with open(filename) as file:
        packets = [str2packetdata(x.strip()) for x in file if x.strip() != ""]

        # Add two divider packets
        div1 = str2packetdata("[[2]]")
        packets.append(div1)
        div2 = str2packetdata("[[6]]")
        packets.append(div2)

        # sort packets
        packets_sorted = sorted(packets)

        # indexes start at 1, not zero
        print(
            (packets_sorted.index(div1) + 1) * (packets_sorted.index(div2) + 1)
        )  # 20383


if __name__ == "__main__":
    main()
