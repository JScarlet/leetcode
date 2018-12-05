# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root

    def print_node(self, root):
        if root is not None:
            print(root.val)
            self.print_node(root.left)
            self.print_node(root.right)


if __name__ == '__main__':
    solution = Solution()
    # root = TreeNode(1)
    # left = TreeNode(0)
    # right = TreeNode(2)
    # root.left = left
    # root.right = right
    # solution.print_node(root)
    # root = solution.trimBST(root, 1, 2)
    # solution.print_node(root)
    root = TreeNode(3)
    left = TreeNode(0)
    right = TreeNode(4)
    left_right = TreeNode(2)
    left_right_left = TreeNode(1)
    root.left = left
    root.right = right
    left.right = left_right
    left_right.left = left_right_left
    solution.print_node(root)
    root = solution.trimBST(root, 1, 3)
    solution.print_node(root)