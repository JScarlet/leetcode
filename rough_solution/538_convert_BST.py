# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.lSum = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.convertBST(root.right)
        self.lSum += root.val
        root.val = self.lSum
        self.convertBST(root.left)
        return root

    def print_node(self, root):
        if root is not None:
            print(root.val)
            self.print_node(root.left)
            self.print_node(root.right)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(2)
    left = TreeNode(0)
    right = TreeNode(3)
    left_left = TreeNode(-4)
    left_right = TreeNode(1)
    root.left = left
    root.right = right
    left.left = left_left
    left.right = left_right
    # print(solution.sum(root))
    solution.print_node(root)
    print()
    root = solution.convertBST(root)
    solution.print_node(root)