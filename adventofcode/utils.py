from typing import List


def read_file_strings(filename: str) -> List[str]:
    """
    Returns contents of the file as a list of strings, with newlines removed.

    :param filename: the extracted google for jobs structured data.
    :type filename: <str>

    :rtype: List<str>
    """
    with open(filename) as file:
        return [line.rstrip() for line in file]
