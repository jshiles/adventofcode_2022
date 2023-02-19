import networkx as nx
import os
from adventofcode.day_12 import file_to_graph


def main():
    # Part 1
    # Start with the space "S" and find the shortest path to "E"

    data_filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "resources",
        "day_12.txt",
    )
    G, start, end = file_to_graph(data_filename)
    print(len(nx.shortest_path(G, start, end)) - 1)  # 330

    # Part 2
    # Start with any elevation "a" space and go to "E".

    nodes_elevation_a = [x for x, y in G.nodes(data=True) if y["height"] == 1]
    lengths = []
    for new_start in nodes_elevation_a:
        try:
            lengths.append(len(nx.shortest_path(G, new_start, end)) - 1)
        except nx.NetworkXNoPath as e:
            print(f'no path from {new_start} to {end}')
    print(sorted(lengths)[0])  # 321


if __name__ == "__main__":
    main()
