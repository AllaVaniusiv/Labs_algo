import unittest
import sys
sys.path.append("D:\Labs_algo\Lab6")

from src.main import boyer_moore_search

class TestBoyerMooreSearch(unittest.TestCase):

    def test_empty_needle(self):
        haystack = "ababcababcabcabc"
        needle = ""
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [])

    def test_empty_haystack(self):
        haystack = ""
        needle = "abc"
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [])

    def test_needle_longer_than_haystack(self):
        haystack = "abc"
        needle = "abcd"
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [])

    def test_no_occurrence(self):
        haystack = "ababababab"
        needle = "xyz"
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [])


    def test_multiple_occurrences(self):
        haystack = "ababcababcabcabc"
        needle = "abc"
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [2, 7, 10, 13])

if __name__ == '__main__':
    unittest.main()
