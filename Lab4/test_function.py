import unittest
from lab4 import find_root

class TestFindRootVertex(unittest.TestCase):
    def test_graph_with_one_vertex(self):
        graph = {1: []}
        self.assertEqual(find_root(graph), 1)

    def test_graph_with_multiple_vertices(self):
        graph = {1: [2], 2: [3], 3: []}
        self.assertEqual(find_root(graph), 1)

    def test_graph_with_no_vertex(self):
        graph = {1: [2], 2: [3], 3:[1]}
        self.assertEqual(find_root(graph), -1)

if __name__ == '__main__':
    unittest.main()