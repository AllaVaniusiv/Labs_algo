import unittest
import sys
sys.path.append("D:\Labs_algo\Lab5_test")

from src.main import max_experience
from src.main import build_graph

class TestMaxExperience(unittest.TestCase):
    def test_max_experience_single_level(self):
        levels = 1
        experience = [[9999]]
        graph = build_graph(levels)
        result = max_experience(graph, levels, experience)
        self.assertEqual(result, 9999)

    def test_max_experience_different_exp(self):
        levels = 5
        experience = [[0], [1, 1], [0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1, 0]]
        graph = build_graph(levels)
        result = max_experience(graph, levels, experience)
        self.assertEqual(result, 3)

    def test_max_experience_edge_cases(self):
        levels = 1
        experience = [[0]]
        graph = build_graph(levels)
        result = max_experience(graph, levels, experience)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()