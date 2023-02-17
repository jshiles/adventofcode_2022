from dataclasses import dataclass, field
from math import floor
from typing import List, Tuple
import re


@dataclass
class Monkey:
    operation: callable
    test: callable
    throw_to_test_true: int
    throw_to_test_false: int
    items: List[int] = field(default_factory=list)
    inspected: int = field(default=0)

    def inspect_item(self) -> None:
        self.items[0] = self.operation(self.items[0])
        self.inspected += 1

    def bored(self, term: int, div: int = 3) -> None:
        self.items[0] = floor((self.items[0] % term) / div)

    def throw_item(self) -> Tuple[int, int]:
        item_to_throw = self.items.pop(0)
        return (
            item_to_throw,
            self.throw_to_test_true
            if self.test(item_to_throw)
            else self.throw_to_test_false,
        )


def create_operation_callable(f: str) -> callable:
    """
    Parse the text operation string into a callable lambda function.
    """
    m = re.match("^.*?(?P<op>[\\+\\*])\\ (?P<arg>old|\\d+)$", f)
    if m and m["op"] == "*":
        return lambda x: x * (x if m["arg"] == "old" else int(m["arg"]))
    elif m and m["op"] == "+":
        return lambda x: x + (x if m["arg"] == "old" else int(m["arg"]))


def create_test_callable(f: str) -> callable:
    """
    Create test callable function with the divsor.
    """
    m = re.match("^.*?(?P<div>\\d+)$", f)
    if m is not None:
        return lambda x: x % int(m["div"]) == 0


def monkey_turns(
    monkeys: List[Monkey], turns: int, term: int, bored_factor: int
) -> List[Monkey]:
    for _ in range(turns):
        for m in monkeys:
            for _ in range(len(m.items)):
                m.inspect_item()
                m.bored(term, bored_factor)
                item, to_monkey = m.throw_item()
                monkeys[to_monkey].items.append(item)
    return monkeys
