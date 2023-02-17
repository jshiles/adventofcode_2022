from adventofcode.day_11 import (
    Monkey,
    create_operation_callable,
    create_test_callable,
    monkey_turns,
)
from copy import deepcopy

MONKEYS = [
    Monkey(
        items=[83, 97, 95, 67],
        operation=create_operation_callable("new = old * 19"),
        test=create_test_callable("divisible by 17"),
        throw_to_test_true=2,
        throw_to_test_false=7,
    ),
    Monkey(
        items=[71, 70, 79, 88, 56, 70],
        operation=create_operation_callable("new = old + 2"),
        test=create_test_callable("divisible by 19"),
        throw_to_test_true=7,
        throw_to_test_false=0,
    ),
    Monkey(
        items=[98, 51, 51, 63, 80, 85, 84, 95],
        operation=create_operation_callable("new = old + 7"),
        test=create_test_callable("divisible by 7"),
        throw_to_test_true=4,
        throw_to_test_false=3,
    ),
    Monkey(
        items=[77, 90, 82, 80, 79],
        operation=create_operation_callable("new = old + 1"),
        test=create_test_callable("divisible by 11"),
        throw_to_test_true=6,
        throw_to_test_false=4,
    ),
    Monkey(
        items=[68],
        operation=create_operation_callable("new = old * 5"),
        test=create_test_callable("divisible by 13"),
        throw_to_test_true=6,
        throw_to_test_false=5,
    ),
    Monkey(
        items=[60, 94],
        operation=create_operation_callable("new = old + 5"),
        test=create_test_callable("divisible by 3"),
        throw_to_test_true=1,
        throw_to_test_false=0,
    ),
    Monkey(
        items=[81, 51, 85],
        operation=create_operation_callable("new = old * old"),
        test=create_test_callable("divisible by 5"),
        throw_to_test_true=5,
        throw_to_test_false=1,
    ),
    Monkey(
        items=[98, 81, 63, 65, 84, 71, 84],
        operation=create_operation_callable("new = old + 3"),
        test=create_test_callable("divisible by 2"),
        throw_to_test_true=2,
        throw_to_test_false=3,
    ),
]


def main():
    # Part 1
    remainder = 17 * 19 * 7 * 11 * 13 * 3 * 5 * 2
    monkeys = monkey_turns(
        deepcopy(MONKEYS), turns=20, term=remainder, bored_factor=3
    )
    inspected = sorted([m.inspected for m in monkeys])
    print(inspected[-2] * inspected[-1])  # 108240

    # Part 2
    monkeys = monkey_turns(
        deepcopy(MONKEYS), turns=10000, term=remainder, bored_factor=1
    )
    inspected = sorted([m.inspected for m in monkeys])
    print(inspected[-2] * inspected[-1])  # 25712998901


if __name__ == "__main__":
    main()
