from typing import List
from adventofcode.utils import read_file_strings
from adventofcode.day_02 import RockPaperScissorsRound


def main():
    # Part 1
    # result: int = 0
    # for hand_input in read_file_strings("resources/day_02.txt"):
    #     opponent, player = hand_input.strip().split()
    #     result += RockPaperScissorsRound(opponent, player).hand_score()
    # print(result)  # 15337

    # Part 2
    result: int = 0
    for hand_input in read_file_strings("resources/day_02.txt"):
        opponent, player = hand_input.strip().split()
        result += RockPaperScissorsRound(opponent, player).hand_score()
    print(result)  # 11696


if __name__ == "__main__":
    main()
