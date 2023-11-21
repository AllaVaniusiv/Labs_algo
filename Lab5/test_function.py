import unittest
from main import max_experience

class TestMaxExperience(unittest.TestCase):
    def test_max_experience_single_level(self):
        levels = 1
        experience = [[9999]]
        result = max_experience(levels, experience)
        self.assertEqual(result, 9999)

    def test_max_experience_different_exp(self):
        levels = 5
        experience = [[0], [1, 1], [0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1, 0]]
        result = max_experience(levels, experience)
        self.assertEqual(result, 3)

    def test_max_experience_edge_cases(self):
        levels = 1
        experience = [[0]]
        result = max_experience(levels, experience)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
