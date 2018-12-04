# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        if root is None:
            return result
        if root.left is not None:
            result += 1
        if root.right is not None:
            result += 1
        result += self.calculate_max_length_between_subtrees(root.left)
        result += self.calculate_max_length_between_subtrees(root.right)
        return max(result, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    def calculate_max_length_between_subtrees(self, root):
        result = 0
        if root is None:
            return result
        if root.left is not None or root.right is not None:
            result += 1
        result += max(self.calculate_max_length_between_subtrees(root.left), self.calculate_max_length_between_subtrees(root.right))
        return result


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    left_left = TreeNode(4)
    left_right = TreeNode(5)
    right_left = TreeNode(6)
    right_right = TreeNode(7)
    root.left = left
    root.right = right
    left.left = left_left
    left.right = left_right
    right.left = right_left
    right.right = right_right

    print(solution.diameterOfBinaryTree(root))
