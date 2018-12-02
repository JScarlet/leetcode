# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if sum == root.val and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)
    left = TreeNode(4)
    right = TreeNode(8)
    left_left = TreeNode(11)
    right_left = TreeNode(13)
    right_right = TreeNode(4)
    left_left_left = TreeNode(7)
    left_left_right = TreeNode(2)
    right_right_right = TreeNode(1)
    root.left = left
    root.right = right
    left.left = left_left
    right.left = right_left
    right.right = right_right
    left_left.left = left_left_left
    left_left.right = left_left_right
    right_right.right = right_right_right
    print(solution.hasPathSum(root, 22))
