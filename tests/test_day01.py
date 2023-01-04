import os
from adventofcode import utils, day_01


class TestDay01:
    def test_elf_calorie_count_greatest(self):
        test_data_filename = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "resources",
            "day_01.txt",
        )
        file_contents = utils.read_file_strings(test_data_filename)
        expected: int = 24000
        result: int = day_01.greatest_elf_calorie_count(file_contents)
        assert result == expected

    def test_elf_calorie_count_top3(self):
        test_data_filename = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "resources",
            "day_01.txt",
        )
        file_contents = utils.read_file_strings(test_data_filename)
        expected: int = 45000
        result: int = day_01.top_n_elf_calorie_count(file_contents, 3)
        assert result == expected
