from typing import List
from adventofcode.day_03 import (
    common_element,
    rearrangement_priority,
    badge_element,
    element_priority,
)


class TestDay03:
    ruck_sack_contents: List[str] = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]

    def test_common_element(self):
        assert common_element(self.ruck_sack_contents[0]) == "p"
        assert common_element(self.ruck_sack_contents[1]) == "L"
        assert common_element(self.ruck_sack_contents[2]) == "P"
        assert common_element(self.ruck_sack_contents[3]) == "v"
        assert common_element(self.ruck_sack_contents[4]) == "t"
        assert common_element(self.ruck_sack_contents[5]) == "s"

    def test_priority_computation(self):
        assert rearrangement_priority(self.ruck_sack_contents[0]) == 16
        assert rearrangement_priority(self.ruck_sack_contents[1]) == 38
        assert rearrangement_priority(self.ruck_sack_contents[2]) == 42
        assert rearrangement_priority(self.ruck_sack_contents[3]) == 22
        assert rearrangement_priority(self.ruck_sack_contents[4]) == 20
        assert rearrangement_priority(self.ruck_sack_contents[5]) == 19

    def test_priority_computation_all(self):
        expected: int = 157
        result: int = sum(
            [rearrangement_priority(x) for x in self.ruck_sack_contents]
        )
        assert result == expected

    def test_find_badge(self):
        assert badge_element(self.ruck_sack_contents[0:3]) == "r"
        assert badge_element(self.ruck_sack_contents[3:6]) == "Z"

    def test_sum_elf_group_badge_priority(self):
        expected: int = 70
        result: int = sum(
            [
                element_priority(
                    badge_element(self.ruck_sack_contents[idx : idx + 3])
                )
                for idx, _ in enumerate(self.ruck_sack_contents)
                if idx % 3 == 0
            ]
        )
        assert result == expected
