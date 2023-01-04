from typing import List
from adventofcode.day_04 import expand_range, contained_pair, overlapping_pair


class TestDay04:
    range_pairs: List[List[str]] = [
        ["2-4", "6-8"],
        ["2-3", "4-5"],
        ["5-7", "7-9"],
        ["2-8", "3-7"],
        ["6-6", "4-6"],
        ["2-6", "4-8"],
    ]

    def test_range_expansion(self):
        assert expand_range(self.range_pairs[0][0]) == [2, 3, 4]
        assert expand_range(self.range_pairs[0][1]) == [6, 7, 8]
        assert expand_range(self.range_pairs[4][0]) == [6]

    def test_is_contained(self):
        assert not contained_pair(
            self.range_pairs[0][0], self.range_pairs[0][1]
        )
        assert not contained_pair(
            self.range_pairs[1][0], self.range_pairs[1][1]
        )
        assert not contained_pair(
            self.range_pairs[2][0], self.range_pairs[2][1]
        )
        assert contained_pair(self.range_pairs[3][0], self.range_pairs[3][1])
        assert contained_pair(self.range_pairs[4][0], self.range_pairs[4][1])
        assert not contained_pair(
            self.range_pairs[5][0], self.range_pairs[5][1]
        )

    def test_is_overlapping(self):
        assert not overlapping_pair(
            self.range_pairs[0][0], self.range_pairs[0][1]
        )
        assert not overlapping_pair(
            self.range_pairs[1][0], self.range_pairs[1][1]
        )
        assert overlapping_pair(self.range_pairs[2][0], self.range_pairs[2][1])
        assert overlapping_pair(self.range_pairs[3][0], self.range_pairs[3][1])
        assert overlapping_pair(self.range_pairs[4][0], self.range_pairs[4][1])
        assert overlapping_pair(self.range_pairs[5][0], self.range_pairs[5][1])
