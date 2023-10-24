from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_of_depths(root: TreeNode) -> int:
    def recurs(node, depth):
        if not node:
            return 0
        
        left_depth = recurs(node.left, depth + 1)
        right_depth = recurs(node.right, depth +1)

        return depth + left_depth + right_depth

    return recurs(root, 0)


# Приклад використання
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = sum_of_depths(root)
print(result)  
