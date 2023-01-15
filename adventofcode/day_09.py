from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from copy import copy


@dataclass(frozen=True)
class VisitedPoint:
    x: int = field(default=0)
    y: int = field(default=0)


class Knot:
    current_location: VisitedPoint
    trail: List[VisitedPoint]

    def __init__(self, loc: VisitedPoint):
        """ """
        self.current_location = loc
        self.trail = [loc]

    def move(self, direction: str, spaces: int) -> List[VisitedPoint]:
        """
        Move the knot according direction and number of moves (spaces) and
        return a list of visited points by the head.

        :param direction: R = right, L = left, U = up, D = down
        :type direction: str

        :param spaces: numbers of times we should move in direction
        :type spaces: int

        :rtype: List<VisitedPoint>
        """

        points: List[VisitedPoint] = [self.current_location]
        for _ in range(spaces):
            match direction:
                case "R":
                    points.append(VisitedPoint(points[-1].x + 1, points[-1].y))
                case "L":
                    points.append(VisitedPoint(points[-1].x - 1, points[-1].y))
                case "U":
                    points.append(VisitedPoint(points[-1].x, points[-1].y + 1))
                case "D":
                    points.append(VisitedPoint(points[-1].x, points[-1].y - 1))
                case "_":
                    raise ValueError('direction must be "R", "L", "D" or "U".')

        if len(points) > 1:
            self.trail = self.trail + points[1:]
            self.current_location = points[-1]

        return points[1:]

    def follow(self, prior_knot: VisitedPoint) -> Optional[VisitedPoint]:
        """
        Move the tail according the the head's movement (in head_trail) and
        return a list of visited points by the tail.

        :param head_trail: all points the head moves
        :type head_trail: List<VisitedPoint>

        :rtype: VisitedPoint
        """
        if (
            abs(self.current_location.x - prior_knot.x) <= 1
            and abs(self.current_location.y - prior_knot.y) <= 1
        ):
            return None
        else:
            tail_x: int = self.current_location.x
            tail_y: int = self.current_location.y

            if prior_knot.x - tail_x > 0:
                tail_x += 1
            elif tail_x - prior_knot.x > 0:
                tail_x -= 1

            if prior_knot.y - tail_y > 0:
                tail_y += 1
            elif tail_y - prior_knot.y > 0:
                tail_y -= 1

            self.current_location = VisitedPoint(tail_x, tail_y)
            self.trail.append(self.current_location)
            return self.current_location


class Rope:
    knots: List[Knot]
    historical_tail_locations: List[VisitedPoint]

    def __init__(self, starting_point: VisitedPoint, num_knots: int):
        """Create our rope with all knots overlapping."""
        self.knots = []
        self.historical_tail_locations = []
        for _ in range(num_knots):
            self.knots.append(Knot(copy(starting_point)))
        self.historical_tail_locations.append(starting_point)

    def _move_head(self, direction: str, spaces: int) -> List[VisitedPoint]:
        """ """
        return self.knots[0].move(direction, spaces)

    def _move_non_head(
        self, knot_idx: int, prior_knot_moves: List[VisitedPoint]
    ) -> List[VisitedPoint]:
        """ """
        locations: List[VisitedPoint] = []
        for pk_loc in prior_knot_moves:
            new_loation = self.knots[knot_idx].follow(pk_loc)
            if new_loation:
                locations.append(new_loation)
        return locations

    def simulate_motion(self, direction: str = "R", spaces: int = 1) -> None:
        """ """
        print(
            f"s: {self.get_head().current_location}, "
            f"{self.get_curr_tail_location()}, {direction}, {spaces}"
        )

        # move head
        leading_knot_trail: List[VisitedPoint] = self._move_head(
            direction, spaces
        )

        # move all following knots
        for idx in range(1, len(self.knots)):
            is_tail_node = idx == len(self.knots) - 1
            trail: List[VisitedPoint] = self._move_non_head(
                idx, leading_knot_trail
            )
            if len(trail):
                leading_knot_trail = trail
                if idx == len(self.knots) - 1:  # is tail
                    self.historical_tail_locations = (
                        self.historical_tail_locations + trail
                    )

        print(
            f"e: {self.get_head().current_location}, "
            f"{self.get_curr_tail_location()}, {direction}, {spaces}"
        )

    def get_head(self) -> Knot:
        return self.knots[0]

    def get_curr_tail_location(self) -> VisitedPoint:
        """
        Returns the current location of tail node.
        :rtype: VisitedPoint
        """
        return self.historical_tail_locations[-1]
