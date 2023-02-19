import os
from adventofcode.day_12 import file_to_graph
import networkx as nx


class TestDay12:
    test_data_filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "resources",
        "day_12.txt",
    )

    def test_network_creation(self):
        G, _, _ = file_to_graph(self.test_data_filename)
        assert G.has_edge((0, 1), (0, 2)) == True
        assert G.has_edge((0, 2), (0, 3)) == False
        assert G.has_edge((0, 3), (0, 2)) == True

        assert G.has_edge((0, 7), (1, 7)) == True
        assert G.has_edge((1, 7), (0, 7)) == True

    def test_network_shortest_path(self):
        G, start, end = file_to_graph(self.test_data_filename)
        assert len(nx.shortest_path(G, start, end)) == 31
