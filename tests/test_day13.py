import os
from adventofcode.day_13 import PacketData, str2packetdata

# import networkx as nx


class TestDay13:
    test_packets = [
        "[1,1,3,1,1]",
        "[1,1,5,1,1]",
        "[[1],[2,3,4]]",
        "[[1],4]",
        "[9]",
        "[[8,7,6]]",
        "[[4,4],4,4]",
        "[[4,4],4,4,4]",
        "[7,7,7,7]",
        "[7,7,7]",
        "[]",
        "[3]",
        "[[[]]]",
        "[[]]",
        "[1,[2,[3,[4,[5,6,7]]]],8,9]",
        "[1,[2,[3,[4,[5,6,0]]]],8,9]",
    ]

    def test_packet_input_comparisons(self):
        assert str2packetdata("[1]") <= str2packetdata("[1]")
        assert not str2packetdata("[2]") <= str2packetdata("[1]")
        assert str2packetdata("[1,1,3,1,1]") <= str2packetdata("[1,1,5,1,1]")

        assert str2packetdata("[[1],[2,3,4]]") <= str2packetdata("[[1],4]")
        assert not str2packetdata("[[1],4]") <= str2packetdata("[[1],[2,3,4]]")

        assert str2packetdata("[[8,7,6]]") <= str2packetdata("[9]")
        assert not str2packetdata("[9]") <= str2packetdata("[[8,7,6]]")

        assert str2packetdata("[1,[2,[3,[4,[5,6,0]]]],8,9]") <= str2packetdata(
            "[1,[2,[3,[4,[5,6,7]]]],8,9]"
        )
        assert not str2packetdata(
            "[1,[2,[3,[4,[5,6,7]]]],8,9]"
        ) <= str2packetdata("[1,[2,[3,[4,[5,6,0]]]],8,9]")

        assert str2packetdata("[]") <= str2packetdata("[3]")
        assert not str2packetdata("[3]") <= str2packetdata("[]")

        assert not str2packetdata("[[[]]]") <= str2packetdata("[[]]")
        assert str2packetdata("[[]]") <= str2packetdata("[[[]]]")

    def test_put_all_packets_order(self):
        packets = [str2packetdata(x) for x in self.test_packets]

        div1 = str2packetdata("[[2]]")
        packets.append(div1)

        div2 = str2packetdata("[[6]]")
        packets.append(div2)

        packets_sorted = sorted(packets)

        # indexes start at 1, not zero
        assert (packets_sorted.index(div1) + 1) * (
            packets_sorted.index(div2) + 1
        ) == 140
