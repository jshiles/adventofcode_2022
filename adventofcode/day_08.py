from typing import List, Tuple

# from itertools import takewhile


def is_edge(grid: List[List[int]], row: int, col: int) -> bool:
    """
    Return if tree is on the edge

    :param grid: the map of the tree grid
    :type grid: List[List<int>]

    :param row: row index
    :type row: <int>

    :param col: col index
    :type col: <int>

    :rtype: <bool>
    """

    if (row == 0 or row == len(grid[0]) - 1) or (
        col == 0 or col == len(grid) - 1
    ):
        return True
    return False


def is_visible(grid: List[List[int]], row: int, col: int) -> bool:
    """
    Return if tree can be seen from the outside of the grid.

    :param grid: the map of the tree grid
    :type grid: List[List<int>]

    :param row: row index
    :type row: <int>

    :param col: col index
    :type col: <int>

    :rtype: <bool>
    """

    if is_edge(grid, row, col):
        return True

    visible = False

    # check right and left
    visible = (
        visible
        or all(val < grid[row][col] for val in grid[row][col + 1 :])
        or all(val < grid[row][col] for val in grid[row][:col])
    )

    # check up and down
    t_grid = list(zip(*grid))  # transpose grid, proceed list right/left
    visible = (
        visible
        or all(val < t_grid[col][row] for val in t_grid[col][row + 1 :])
        or all(val < t_grid[col][row] for val in t_grid[col][:row])
    )

    return visible


def visible_invisible(grid: List[List[int]]) -> Tuple[int, int]:
    """
    Return count of all visible and invisible trees as seen from outside of
    the grid.

    :param grid: the map of the tree grid
    :type grid: List[List<int>]

    :rtype: Tuple[<int>, <int>]
    """
    row_len = len(grid[0])
    col_len = len(grid)

    visible = 0
    for r in range(row_len):
        for c in range(col_len):
            visible = visible + 1 if is_visible(grid, r, c) else visible

    return visible, row_len * col_len - visible


def scenic_score(grid: List[List[int]], row: int, col: int) -> int:
    """
    count in all directions until, and including, you reach a tree that
    is the same size or larger.

    :param grid: the map of the tree grid
    :type grid: List[List<int>]

    :param row: row index
    :type row: <int>

    :param col: col index
    :type col: <int>

    :rtype: <int>
    """

    def takewhile(predicate: int, iterable):
        """
        returns the iterable until the predicate is violated plus
        first violation.
        """
        for x in iterable:
            if x < predicate:
                yield x
            else:
                yield x
                break

    r = [n for n in takewhile(grid[row][col], grid[row][col + 1 :])]
    l = [n for n in takewhile(grid[row][col], reversed(grid[row][:col]))]

    t_grid = list(zip(*grid))
    u = [n for n in takewhile(t_grid[col][row], reversed(t_grid[col][:row]))]
    d = [n for n in takewhile(t_grid[col][row], t_grid[col][row + 1 :])]

    score = len(r) * len(l) * len(u) * len(d)
    return score


def highest_scenic_score(grid: List[List[int]]) -> int:
    """
    Return the highest scenic score in the grid.

    :param grid: the map of the tree grid
    :type grid: List[List<int>]

    :rtype: <int>
    """
    highest_scenic_score = 0
    for r in range(len(grid[0])):
        for c in range(len(grid)):
            sc = scenic_score(grid, r, c)
            if sc > highest_scenic_score:
                highest_scenic_score = sc
    return highest_scenic_score
