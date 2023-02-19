import networkx as nx
from adventofcode.utils import read_file_strings
from typing import Tuple


def file_to_graph(filename: str) -> Tuple[nx.Graph, tuple, tuple]:
    """
    Convert the puzzle input, a file of elevations in a grid, into a Directed
    Network with edges representing the walking path. Return the resulting
    Graph, and the names of the nodes labeled "S" and "E" by the puzzle input.
    """
    G = nx.MultiDiGraph()
    start, end = None, None

    for row_idx, row in enumerate(read_file_strings(filename)):
        for col_idx, col in enumerate(list(row)):
            # Convert the start end end labeled nodes to the appropriate
            # elevation.
            if col == "S":
                start = (row_idx, col_idx)
                col = "a"
            if col == "E":
                end = (row_idx, col_idx)
                col = "z"

            # create the node
            current_node_loc = (row_idx, col_idx)
            current_node_height = ord(col) - 96
            G.add_node(current_node_loc, height=current_node_height)

            # add links to left node
            if col_idx > 0:
                left_node_loc = (row_idx, col_idx - 1)
                left_node_height = G.nodes[left_node_loc].get("height")
                if left_node_height <= current_node_height + 1:
                    G.add_edge(current_node_loc, left_node_loc)
                if current_node_height <= left_node_height + 1:
                    G.add_edge(left_node_loc, current_node_loc)

            # add links to upper node
            if row_idx > 0:
                upper_node_loc = (row_idx - 1, col_idx)
                upper_node_height = G.nodes[upper_node_loc].get("height")
                if upper_node_height <= current_node_height + 1:
                    G.add_edge(current_node_loc, upper_node_loc)
                if current_node_height <= upper_node_height + 1:
                    G.add_edge(upper_node_loc, current_node_loc)

    return G, start, end
