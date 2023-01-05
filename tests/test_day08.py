import os
from typing import List
from adventofcode.day_08 import (
    is_edge,
    is_visible,
    visible_invisible,
    scenic_score,
    highest_scenic_score,
)
from adventofcode.utils import read_file_strings


class TestDay08:
    grid: List[List[int]] = [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]

    test_data_filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "resources",
        "day_08.txt",
    )

    def test_is_edge(self):
        assert is_edge(self.grid, 0, 0) == True
        assert is_edge(self.grid, 4, 4) == True
        assert is_edge(self.grid, 1, 4) == True
        assert is_edge(self.grid, 1, 3) == False

    def test_is_visible(self):
        assert is_visible(self.grid, 4, 4) == True
        assert is_visible(self.grid, 1, 1) == True
        assert is_visible(self.grid, 1, 2) == True
        assert is_visible(self.grid, 2, 2) == False
        assert is_visible(self.grid, 1, 3) == False

    def test_is_visible_counting(self):
        vis, _ = visible_invisible(self.grid)
        assert vis == 21

    def test_full_visible_process(self):
        grid: List[List[int]] = []
        for row in read_file_strings(self.test_data_filename):
            grid.append([int(x) for x in list(row)])
        vis, _ = visible_invisible(grid)
        assert vis == 21

    def test_scenic_score(self):
        assert scenic_score(self.grid, 1, 2) == 4
        assert scenic_score(self.grid, 3, 2) == 8

    def test_full_scenic_process(self):
        grid: List[List[int]] = []
        for row in read_file_strings(self.test_data_filename):
            grid.append([int(x) for x in list(row)])

        assert highest_scenic_score(grid) == 8
