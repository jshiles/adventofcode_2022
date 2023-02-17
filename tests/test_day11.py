from math import pow
from adventofcode.day_11 import (
    Monkey,
    create_operation_callable,
    create_test_callable,
    monkey_turns,
)
from copy import deepcopy


class TestDay11:
    monkeys = [
        # Monkey 0:
        #   Starting items: 79, 98
        #   Operation: new = old * 19
        #   Test: divisible by 23
        #     If true: throw to monkey 2
        #     If false: throw to monkey 3
        Monkey(
            items=[79, 98],
            operation=create_operation_callable("new = old * 19"),
            test=create_test_callable("divisible by 23"),
            throw_to_test_true=2,
            throw_to_test_false=3,
        ),
        # Monkey 1:
        #   Starting items: 54, 65, 75, 74
        #   Operation: new = old + 6
        #   Test: divisible by 19
        #     If true: throw to monkey 2
        #     If false: throw to monkey 0
        Monkey(
            items=[54, 65, 75, 74],
            operation=create_operation_callable("new = old + 6"),
            test=create_test_callable("divisible by 19"),
            throw_to_test_true=2,
            throw_to_test_false=0,
        ),
        # Monkey 2:
        #   Starting items: 79, 60, 97
        #   Operation: new = old * old
        #   Test: divisible by 13
        #     If true: throw to monkey 1
        #     If false: throw to monkey 3
        Monkey(
            items=[79, 60, 97],
            operation=create_operation_callable("new = old * old"),
            test=create_test_callable("divisible by 13"),
            throw_to_test_true=1,
            throw_to_test_false=3,
        ),
        # Monkey 3:
        #   Starting items: 74
        #   Operation: new = old + 3
        #   Test: divisible by 17
        #     If true: throw to monkey 0
        #     If false: throw to monkey 1
        Monkey(
            items=[74],
            operation=create_operation_callable("new = old + 3"),
            test=create_test_callable("divisible by 17"),
            throw_to_test_true=0,
            throw_to_test_false=1,
        ),
    ]

    remainder = 23 * 19 * 13 * 17

    def test_monkey_full_round(self):
        monkeys = monkey_turns(
            deepcopy(self.monkeys), turns=1, term=self.remainder, bored_factor=3
        )
        assert monkeys[0].items == [20, 23, 27, 26]
        assert monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
        assert monkeys[2].items == []
        assert monkeys[3].items == []

    def test_monkey_two_rounds(self):
        monkeys = monkey_turns(
            deepcopy(self.monkeys),
            turns=2,
            term=self.remainder,
            bored_factor=3,
        )
        assert monkeys[0].items == [695, 10, 71, 135, 350]
        assert monkeys[1].items == [43, 49, 58, 55, 362]
        assert monkeys[2].items == []
        assert monkeys[3].items == []

    def test_monkey_most_active(self):
        monkeys = monkey_turns(
            deepcopy(self.monkeys),
            turns=20,
            term=self.remainder,
            bored_factor=3,
        )
        assert monkeys[0].items == [10, 12, 14, 26, 34]
        assert monkeys[1].items == [245, 93, 53, 199, 115]
        assert monkeys[2].items == []
        assert monkeys[3].items == []
        assert monkeys[0].inspected == 101
        assert monkeys[1].inspected == 95
        assert monkeys[2].inspected == 7
        assert monkeys[3].inspected == 105

    def test_monkey_20(self):
        monkeys = monkey_turns(
            deepcopy(self.monkeys),
            turns=20,
            term=self.remainder,
            bored_factor=3,
        )
        inspected = sorted([m.inspected for m in monkeys])
        assert inspected[-2] * inspected[-1] == 10605

    def test_monkey_10000(self):
        monkeys = monkey_turns(
            deepcopy(self.monkeys),
            turns=10000,
            term=self.remainder,
            bored_factor=1,
        )
        inspected = sorted([m.inspected for m in monkeys])
        assert inspected[-2] * inspected[-1] == 2713310158
