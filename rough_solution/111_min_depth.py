# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if root.left is not None and root.right is not None:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left is None and root.right is not None:
            return self.minDepth(root.right) + 1
        elif root.left is not None and root.right is None:
            return self.minDepth(root.left) + 1
        else:
            return 1


if __name__ == '__main__':
    solution = Solution()
    # root = TreeNode(3)
    # left = TreeNode(8)
    # right = TreeNode(2)
    # right_left = TreeNode(1)
    # right_right = TreeNode(6)
    # root.left = left
    # root.right = right
    # right.left = right_left
    # right.right = right_right
    # print(solution.minDepth(root))
    root = TreeNode(1)
    left = TreeNode(2)
    root.left = left
    print(solution.minDepth(root))
