import os
from typing import List, Tuple
from adventofcode.day_09 import VisitedPoint, Knot, Rope


class TestDay09:
    head_moves: List[Tuple[str, int]] = [
        ("R", 4),
        ("U", 4),
        ("L", 3),
        ("D", 1),
        ("R", 4),
        ("D", 1),
        ("L", 5),
        ("R", 2),
    ]

    head_moves_p2: List[Tuple[str, int]] = [
        ("R", 5),
        ("U", 8),
        ("L", 8),
        ("D", 3),
        ("R", 17),
        ("D", 10),
        ("L", 25),
        ("U", 20),
    ]

    def test_move_single_knot(self):
        knot: Knot = Knot(VisitedPoint())
        points = knot.move(self.head_moves[0][0], self.head_moves[0][1])
        assert knot.current_location == VisitedPoint(4, 0)
        assert len(points) == 4

        points = knot.move(self.head_moves[1][0], self.head_moves[1][1])
        assert knot.current_location == VisitedPoint(4, 4)
        assert len(points) == 4

        points = knot.move(self.head_moves[2][0], self.head_moves[2][1])
        assert knot.current_location == VisitedPoint(1, 4)
        assert len(points) == 3

    def test_follow_knot_R4(self):
        knot_h: Knot = Knot(VisitedPoint())
        knot_t: Knot = Knot(VisitedPoint())
        points = knot_h.move(self.head_moves[0][0], self.head_moves[0][1])
        for point in points:
            knot_t.follow(point)
        assert knot_t.current_location == VisitedPoint(3, 0)

    def test_follow_knot_D1(self):
        knot_h: Knot = Knot(VisitedPoint(1, 2))
        knot_t: Knot = Knot(VisitedPoint(1, 3))
        points = knot_h.move("D", 1)
        for point in points:
            knot_t.follow(point)
        assert knot_t.current_location == VisitedPoint(1, 2)

    def test_rope_movement_R2(self):
        rope: Rope = Rope(VisitedPoint(1, 1), num_knots=2)
        rope.simulate_motion("R", 2)
        assert len(rope.historical_tail_locations) == 2
        assert rope.get_curr_tail_location() == VisitedPoint(2, 1)

    def test_rope_movement_all(self):
        starting_point: VisitedPoint = VisitedPoint(x=0, y=0)
        rope: Rope = Rope(starting_point, num_knots=2)
        for move in self.head_moves:
            rope.simulate_motion(move[0], move[1])
        assert (
            rope.historical_tail_locations[-1]
            == rope.knots[-1].current_location
        )
        assert rope.knots[-1].current_location == VisitedPoint(1, 2)
        unique_tail_points = len(set(rope.historical_tail_locations))
        assert unique_tail_points == 13

    def test_long_rope_R12(self):
        starting_point: VisitedPoint = VisitedPoint(x=0, y=0)
        rope: Rope = Rope(starting_point, num_knots=10)

        assert len(rope.knots) == 10
        assert rope.get_head().current_location == starting_point
        assert rope.get_curr_tail_location() == starting_point

        rope.simulate_motion("R", 12)
        assert rope.get_curr_tail_location() == VisitedPoint(x=3, y=0)

    def test_long_rope_all(self):
        starting_point: VisitedPoint = VisitedPoint(x=11, y=5)
        rope: Rope = Rope(starting_point, num_knots=10)
        for move in self.head_moves_p2:
            rope.simulate_motion(move[0], move[1])
        unique_tail_points = len(set(rope.historical_tail_locations))
        assert unique_tail_points == 36
