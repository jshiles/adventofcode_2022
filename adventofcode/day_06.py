import logging
from typing import Optional


def unique_character_detection(
    datastream: str, n_unique: int = 4
) -> Optional[int]:
    """
    Returns the character count (index + 1) at which the prior N characters are unique.

    :param datastream: the string of characters that go to the comms device.
    :type datastream: <str>

    :param n_unique: count of unique characters required
    :type n_unique: <int>

    :rtype: <int> or None
    """
    for idx in range(n_unique - 1, len(datastream)):
        logging.debug(
            f"Char: {idx + 1} -> {datastream[idx - n_unique + 1: idx + 1]}"
        )
        if len(set(datastream[idx - n_unique + 1 : idx + 1])) == n_unique:
            return idx + 1
    return None


def packet_marker_detection(datastream: str) -> Optional[int]:
    """
    Returns the character count (index + 1) at which the packet marker starts.
    A packet marker is when four characters are all different. Or None if not
    found.

    :param datastream: the string of characters that go to the comms device.
    :type datastream: <str>

    :rtype: <int> or None
    """
    return unique_character_detection(datastream, n_unique=4)


def message_start_detection(datastream: str) -> Optional[int]:
    """
    Returns the character count (index + 1) at which the message marker starts.
    A message marker is when fourteen characters are all different. Or None if
    not found.

    :param datastream: the string of characters that go to the comms device.
    :type datastream: <str>

    :rtype: <int> or None
    """
    return unique_character_detection(datastream, n_unique=14)
