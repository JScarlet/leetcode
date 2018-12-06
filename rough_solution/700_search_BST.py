# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    def print_node(self, root):
        if root is not None:
            print(root.val)
            self.print_node(root.left)
            self.print_node(root.right)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(4)
    left = TreeNode(2)
    right = TreeNode(7)
    left_left = TreeNode(1)
    left_right = TreeNode(3)
    root.left = left
    root.right = right
    left.left = left_left
    left.right = left_right
    solution.print_node(root)
    root = solution.searchBST(root, 2)
    print()
    solution.print_node(root)
