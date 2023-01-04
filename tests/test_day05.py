import os
from typing import List
from adventofcode.day_05 import parse_file, move, get_top_elements


class TestDay05:
    test_data_filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "resources",
        "day_05.txt",
    )

    def test_parse_file_stacks_len(self):
        stacks, _ = parse_file(self.test_data_filename)
        assert len(stacks) == 3
        assert len(stacks[0]) == 2
        assert len(stacks[1]) == 3
        assert len(stacks[2]) == 1

    def test_parse_file_stacks_contents(self):
        stacks, _ = parse_file(self.test_data_filename)
        assert stacks[0] == ["[Z]", "[N]"]
        assert stacks[1] == ["[M]", "[C]", "[D]"]
        assert stacks[2] == ["[P]"]

    def test_parse_file_moves(self):
        _, moves = parse_file(self.test_data_filename)
        assert len(moves) == 4
        assert moves[2] == (2, 2, 1)

    def test_execute_single_move(self):
        stacks, _ = parse_file(self.test_data_filename)
        move(stacks, 0, 1)
        assert stacks[0] == ["[Z]"]
        assert stacks[1] == ["[M]", "[C]", "[D]", "[N]"]

    def test_execute_moves(self):
        stacks, moves = parse_file(self.test_data_filename)
        for qty, from_stack, to_stack in moves:
            for _ in range(qty):
                move(stacks, from_stack - 1, to_stack - 1)

        assert stacks[0] == ["[C]"]
        assert stacks[1] == ["[M]"]
        assert stacks[2] == ["[P]", "[D]", "[N]", "[Z]"]

    def test_get_top_elements(self):
        stacks, moves = parse_file(self.test_data_filename)
        for qty, from_stack, to_stack in moves:
            for _ in range(qty):
                move(stacks, from_stack - 1, to_stack - 1)
        assert get_top_elements(stacks) == "CMZ"
