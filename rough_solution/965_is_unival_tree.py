# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        return self.check(root, root.val)

    def check(self, root, num):
        if root is not None:
            if root.val != num:
                return False
            return self.check(root.left, num) & self.check(root.right, num)
        return True


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    left = TreeNode(1)
    right = TreeNode(1)
    left_left = TreeNode(1)
    left_right = TreeNode(1)
    root.left = left
    root.right = right
    left.left = left_left
    left.right = left_right
    print(solution.isUnivalTree(root))
