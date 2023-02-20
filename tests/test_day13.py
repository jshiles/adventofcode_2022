import os
from adventofcode.day_13 import PacketData, str2packetdata

# import networkx as nx


class TestDay13:
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
