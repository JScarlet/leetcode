# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    maxLen = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.getMaxLen(root, root.val)
        return self.maxLen

    def getMaxLen(self, root, val):
        if not root:
            return 0
        left = self.getMaxLen(root.left, root.val)
        right = self.getMaxLen(root.right, root.val)
        self.maxLen = max(self.maxLen, left + right)
        if root.val == val:
            return max(left, right) + 1
        return 0


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(4)
    left = TreeNode(4)
    right = TreeNode(5)
    left_left = TreeNode(4)
    left_right = TreeNode(4)
    right_right = TreeNode(5)
    left_left_left = TreeNode(4)
    root.left = left
    root.right = right
    left.left = left_left
    left.right = left_right
    right.right = right_right
    left_left.left = left_left_left

    print(solution.longestUnivaluePath(root))