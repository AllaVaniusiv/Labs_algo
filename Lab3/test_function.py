import unittest
from main import sum_of_depths
from main import TreeNode

class TestSumOfDepths(unittest.TestCase):
    def test_empty_tree(self):
        # Тест на пусте дерево
        root = None
        result = sum_of_depths(root)
        self.assertEqual(result, 0)

    def test_single_node_tree(self):
        # Тест на один вузол у дереві
        root = TreeNode(1)
        result = sum_of_depths(root)
        self.assertEqual(result, 0)

    def test_balanced_tree(self):
        # Тест на збалансоване дерево
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        result = sum_of_depths(root)
        self.assertEqual(result, 2)


    def test_unbalanced_tree(self):
        # Тест на незбалансоване дерево
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        result = sum_of_depths(root)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
