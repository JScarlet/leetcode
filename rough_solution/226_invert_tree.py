# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
        else:
            return None

    def print_node(self, node):
        if node is not None:
            print(node.val)
            self.print_node(node.left)
            self.print_node(node.right)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    left_left = TreeNode(4)
    right_right = TreeNode(5)
    root.left = left
    root.right = right
    left.left = left_left
    right.right = right_right
    solution.print_node(root)
    root = solution.invertTree(root)
    solution.print_node(root)