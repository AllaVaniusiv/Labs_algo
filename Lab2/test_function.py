import unittest
from main import paint_billboards

class TestPaintBillboards(unittest.TestCase):
    def test_example_case(self):
        K = 10
        T = 5
        lengths = [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]
        result = paint_billboards(K, T, lengths)
        self.assertEqual(result, 100)

    def test_edge_case(self):
        K = 1
        T = 10
        lengths = [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]
        result = paint_billboards(K, T, lengths)
        self.assertEqual(result, 1400)

if __name__ == '__main__':
    unittest.main()
