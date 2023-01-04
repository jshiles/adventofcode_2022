from typing import List


def element_priority(common_elem: str) -> int:
    """
    Converts an element into its priority. Lowercase item types a through z
    have priorities 1 through 26. Uppercase item types A through Z have
    priorities 27 through 52.
    :rtype: <int>
    """

    ascii_equiv = ord(common_elem)
    return ascii_equiv - 97 + 1 if ascii_equiv >= 97 else ascii_equiv - 65 + 27


def common_element(ruck_sack_contents: str) -> str:
    """
    split the contents in half, find the common element in both.
    :rtype: <str>
    """
    compartment_1, compartment_2 = (
        ruck_sack_contents[: len(ruck_sack_contents) // 2],
        ruck_sack_contents[len(ruck_sack_contents) // 2 :],
    )
    return "".join(set(compartment_1).intersection(compartment_2))


def rearrangement_priority(ruck_sack_contents: str) -> int:
    """
    Returns the rearrangement priority for the common element in
    both compartments.
    :rtype: <int>
    """
    common_elem = common_element(ruck_sack_contents)
    return element_priority(common_elem)


def badge_element(ruck_sack_contents_group: List[str]) -> str:
    """ """
    if len(ruck_sack_contents_group) != 3:
        raise ValueError(
            "group is too large, ruck_sack_contents_group must have len 3"
        )
    return "".join(
        set(ruck_sack_contents_group[0])
        & set(ruck_sack_contents_group[1])
        & set(ruck_sack_contents_group[2])
    )
