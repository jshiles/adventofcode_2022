import os
from adventofcode import day_02, utils


class TestDay02:
    def test_hand_score_win(self):
        hand = day_02.RockPaperScissorsRound("A", "Y")
        result: int = hand.hand_score()
        expected: int = 4
        print(result, expected)
        assert result == expected

    def test_hand_score_loss(self):
        hand = day_02.RockPaperScissorsRound("B", "X")
        result = hand.hand_score()
        expected = 1
        assert result == expected

    def test_hand_score_draw(self):
        hand = day_02.RockPaperScissorsRound("C", "Z")
        result: int = hand.hand_score()
        expected: int = 7
        assert result == expected

    def test_multiple_hands(self):
        test_data_filename = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "resources",
            "day_02.txt",
        )
        expected: int = 12
        result: int = 0
        for hand_input in utils.read_file_strings(test_data_filename):
            opponent, player = hand_input.strip().split()
            result += day_02.RockPaperScissorsRound(
                opponent, player
            ).hand_score()
        assert result == expected
