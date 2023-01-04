import logging


class RockPaperScissorsRound:
    opponent: str = None
    player: str = None

    def __init__(self, opponent: str, outcome: str):
        match opponent:  # A for Rock, B for Paper, and C for Scissors.
            case "A":
                self.opponent = "R"
            case "B":
                self.opponent = "P"
            case "C":
                self.opponent = "S"
            case _:
                raise ValueError("opponent must by A, B, or C")

        match outcome:  # X for Rock, Y for Paper, and Z for Scissors
            case "X":
                if self.opponent == "R":
                    self.player = "S"
                elif self.opponent == "P":
                    self.player = "R"
                else:
                    self.player = "P"
            case "Y":
                self.player = self.opponent
            case "Z":
                if self.opponent == "R":
                    self.player = "P"
                elif self.opponent == "P":
                    self.player = "S"
                else:
                    self.player = "R"
            case _:
                raise ValueError("outcome must by X, Y, or Z")

    def hand_result_points(self) -> int:
        """
        Outcome of the round (0 if you lost, 3 if the round was a draw,
        and 6 if you won)

        :rtype: int
        """
        if self.opponent == self.player:
            logging.debug(
                f"DRAW: Player: {self.player} and Opponent: {self.opponent}"
            )
            return 3
        elif (
            (self.opponent == "R" and self.player == "S")
            or (self.opponent == "P" and self.player == "R")
            or (self.opponent == "S" and self.player == "P")
        ):
            logging.debug(
                f"LOSS: Player: {self.player} and Opponent: {self.opponent}"
            )
            return 0

        logging.debug(
            f"WIN: Player: {self.player} and Opponent: {self.opponent}"
        )
        return 6

    def choice_points(self) -> int:
        """
        Returns value for player's choice. Rock = 1, Paper = 2, Scissor = 3

        :rtype: int
        """
        points = 0
        match self.player:
            case "R":
                points = 1
            case "P":
                points = 2
            case "S":
                points = 3
        logging.debug(f"Choice: {self.player} = {points} points.")
        return points

    def hand_score(self) -> int:
        """
        Returns points for hand resultand points for the player's choice.
           - 0 if you lost, 3 if the round was a draw, and 6 if you won
           - player's choice. Rock = 1, Paper = 2, Scissor = 3

        :rtype: int
        """
        return self.hand_result_points() + self.choice_points()
