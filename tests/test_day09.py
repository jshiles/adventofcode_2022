import os
from typing import List, Tuple
from adventofcode.day_09 import VisitedPoint


class TestDay08:
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

    def test_head_movement(self):
        starting_point = VisitedPoint()
        points = starting_point.moveHead(
            self.head_moves[0][0], self.head_moves[0][1]
        )
        assert points[-1] == VisitedPoint(4, 0)
        assert len(points) == 4

        points = starting_point.moveHead(
            self.head_moves[1][0], self.head_moves[1][1]
        )
        assert points[-1] == VisitedPoint(0, 4)
        assert len(points) == 4

        points = starting_point.moveHead(
            self.head_moves[2][0], self.head_moves[2][1]
        )
        assert points[-1] == VisitedPoint(-3, 0)
        assert len(points) == 3

    def test_execute_head_moves(self):
        starting_point = VisitedPoint()
        for move in self.head_moves:
            points = starting_point.moveHead(move[0], move[1])
            starting_point = points[-1]
        assert starting_point == VisitedPoint(2, 2)

    def test_tail_move_R1(self):
        starting_point_h = VisitedPoint(2, 1)
        starting_point_t = VisitedPoint(1, 1)
        head_points: List[VisitedPoint] = starting_point_h.moveHead('R', 1)
        tail_points: List[VisitedPoint] = starting_point_t.moveTail(head_points)
        assert len(tail_points) == 1
        assert tail_points[-1] == VisitedPoint(2, 1)

    def test_tail_move_D1(self):
        starting_point_h = VisitedPoint(1, 2)
        starting_point_t = VisitedPoint(1, 3)
        head_points: List[VisitedPoint] = starting_point_h.moveHead('D', 1)
        tail_points: List[VisitedPoint] = starting_point_t.moveTail(head_points)
        assert len(tail_points) == 1
        assert tail_points[-1] == VisitedPoint(1, 2)

    def test_tail_move_Diag_U1(self):
        starting_point_h = VisitedPoint(2, 2)
        starting_point_t = VisitedPoint(1, 1)
        head_points: List[VisitedPoint] = starting_point_h.moveHead('U', 1)
        tail_points: List[VisitedPoint] = starting_point_t.moveTail(head_points)
        assert len(tail_points) == 1
        assert tail_points[-1] == VisitedPoint(2, 2)

    def test_tail_move_Diag_R1(self):
        starting_point_h = VisitedPoint(2, 2)
        starting_point_t = VisitedPoint(1, 1)
        head_points: List[VisitedPoint] = starting_point_h.moveHead('R', 1)
        tail_points: List[VisitedPoint] = starting_point_t.moveTail(head_points)
        assert len(tail_points) == 1
        assert tail_points[-1] == VisitedPoint(2, 2)

    def test_tail_move_U4(self):
        starting_point_h = VisitedPoint(4, 0)
        starting_point_t = VisitedPoint(3, 0)
        head_points: List[VisitedPoint] = starting_point_h.moveHead('U', 4)
        tail_points: List[VisitedPoint] = starting_point_t.moveTail(head_points)
        assert len(tail_points) == 3
        assert tail_points[0] == VisitedPoint(4, 1)
        assert tail_points[1] == VisitedPoint(4, 2)
        assert tail_points[2] == VisitedPoint(4, 3)

    def test_tail_move_L3(self):
        starting_point_h = VisitedPoint(4, 4)
        starting_point_t = VisitedPoint(4, 3)
        head_points: List[VisitedPoint] = starting_point_h.moveHead('L', 3)
        tail_points: List[VisitedPoint] = starting_point_t.moveTail(head_points)
        assert len(tail_points) == 2
        assert tail_points[0] == VisitedPoint(3, 4)
        assert tail_points[1] == VisitedPoint(2, 4)

    def test_tail_move_D1_NoMove(self):
        starting_point_h = VisitedPoint(1, 4)
        starting_point_t = VisitedPoint(2, 4)
        head_points: List[VisitedPoint] = starting_point_h.moveHead('D', 1)
        tail_points: List[VisitedPoint] = starting_point_t.moveTail(head_points)
        assert len(tail_points) == 0

        starting_point_h = head_points[-1]
        starting_point_t = tail_points[-1] if len(tail_points) else starting_point_t
        assert starting_point_h == VisitedPoint(1, 3)
        assert starting_point_t == VisitedPoint(2, 4)

        head_points = starting_point_h.moveHead('R', 4)
        tail_points = starting_point_t.moveTail(head_points)
        assert head_points[-1] == VisitedPoint(5, 3)
        assert tail_points[-1] == VisitedPoint(4, 3)

    def test_execute_tail_moves(self):
        starting_point = VisitedPoint()
        all_tail_points: List[VisitedPoint] = [starting_point]

        for move in self.head_moves:
            head_points = starting_point.moveHead(move[0], move[1])
            tail_points = all_tail_points[-1].moveTail(head_points)
            if len(tail_points):
                all_tail_points = all_tail_points + tail_points
            starting_point = head_points[-1] if len(head_points) else starting_point

        unique_tail_points = len(set(all_tail_points))
        assert unique_tail_points == 13
