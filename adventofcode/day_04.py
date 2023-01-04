from typing import List


def expand_range(range_str: str) -> List[int]:
    """
    Expands a range into a list of integers.
    :rtype: List<int>
    """
    range_start, range_end = range_str.split("-")
    return list(range(int(range_start), int(range_end) + 1))


def contained_pair(range_1: str, range_2: str) -> bool:
    """
    Returns true if all elements of range_1 are in range_2 or vice versa.
    :rtype: bool
    """
    return all(
        item in expand_range(range_1) for item in expand_range(range_2)
    ) or all(item in expand_range(range_2) for item in expand_range(range_1))


def overlapping_pair(range_1: str, range_2: str) -> bool:
    """
    Returns true any elements overlap.
    :rtype: bool
    """
    return any(item in expand_range(range_1) for item in expand_range(range_2))
