from itertools import zip_longest
from re import findall
from typing import List, Tuple


def parse_file_stacks(filename: str) -> List[List[str]]:
    """
    Parse the container stacks from the file into nested list of strings.
    :rtype: List[List<str>]
    """
    stacks: List[List[str]] = []
    with open(filename) as file:
        for line in file:
            if "[" not in line.strip():
                break
            stacks.append(
                [
                    str(line[idx : min(idx + 4, len(line) - 1)]).strip()
                    for idx, _ in enumerate(line)
                    if idx % 4 == 0
                ]
            )
    return [
        list(filter(lambda elem: len(elem) > 0, s))[::-1]
        for s in list(map(list, zip_longest(*stacks, fillvalue="")))
    ]


def parse_file_moves(filename: str) -> List[Tuple[int, int, int]]:
    """
    Parse the moves file into list of tuples (quantity of containers to move,
    from stack, to stack).
    :rtype: List[Tuple[<int>, <int>, <int>]]
    """
    moves: List[Tuple[int, int, int]] = []
    moves_found = False
    with open(filename) as file:
        for line in file:
            # skip the stacks
            if not moves_found:
                if line.strip() == "":
                    moves_found = True
                continue
            if len(line.strip()):
                qty, from_stack, to_stack = findall(r"\d+", line)
                moves.append((int(qty), int(from_stack), int(to_stack)))
    return moves


def parse_file(filename: str) -> Tuple[List[List[str]], List[Tuple[int, int, int]]]:
    """
    Parse the containers and the moves from the file.
    """
    stacks = parse_file_stacks(filename)
    moves: List[str] = parse_file_moves(filename)
    return stacks, moves


def move(stacks: List[List[str]], from_s, to_s):
    """
    Execute one move. Move top container from stack at index from_s to stack
    at index to_s
    """
    stacks[to_s].append(stacks[from_s].pop())


def get_top_elements(stacks: List[List[str]]) -> str:
    """
    Return a string containing all of the letters of the top containers
    (brackets removed)
    :rtype: <str>
    """
    return "".join([s[-1] for s in stacks]).replace("[", "").replace("]", "")
