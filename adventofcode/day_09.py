from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class VisitedPoint:
    x: int = field(default=0)
    y: int = field(default=0)

    def moveHead(self, direction: str, spaces: int) -> List[VisitedPoint]:
        """
        Move the head according direction and number of moves (spaces) and
        return a list of visited points by the head.

        :param direction: R = right, L = left, U = up, D = down
        :type direction: str

        :param spaces: numbers of times we should move in direction
        :type spaces: int

        :rtype: List<VisitedPoint>
        """

        points: List[VisitedPoint] = [self]
        for _ in range(spaces):
            match direction:
                case "R":
                    points.append(VisitedPoint(points[-1].x + 1, points[-1].y))
                case "L":
                    points.append(VisitedPoint(points[-1].x - 1, self.y))
                case "U":
                    points.append(VisitedPoint(points[-1].x, points[-1].y + 1))
                case "D":
                    points.append(VisitedPoint(points[-1].x, points[-1].y - 1))
                case "_":
                    raise ValueError('direction must be "R", "L", "D" or "U".')
        return points[1:]

    def moveTail(self, head_trail: List[VisitedPoint]) -> List[VisitedPoint]:
        """
        Move the tail according the the head's movement (in head_trail) and
        return a list of visited points by the tail.

        :param head_trail: all points the head moves
        :type head_trail: List<VisitedPoint>

        :rtype: List<VisitedPoint>
        """
        points: List[VisitedPoint] = [self]

        for move in head_trail:
            if (
                abs(points[-1].x - move.x) <= 1
                and abs(points[-1].y - move.y) <= 1
            ):
                continue
            else:
                tail_x: int = points[-1].x
                if move.x - tail_x > 0:
                    tail_x += 1
                elif tail_x - move.x > 0:
                    tail_x -= 1

                tail_y: int = points[-1].y
                if move.y - tail_y > 0:
                    tail_y += 1
                elif tail_y - move.y > 0:
                    tail_y -= 1
                points.append(VisitedPoint(tail_x, tail_y))

        return points[1:]
