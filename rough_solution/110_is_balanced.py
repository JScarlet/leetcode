# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        print(root.val, self.calculateSubLength(root.left), self.calculateSubLength(root.right))
        if abs(self.calculateSubLength(root.left) - self.calculateSubLength(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def calculateSubLength(self, root):
        if root is None:
            return 0
        else:
            return max(self.calculateSubLength(root.left) + 1, self.calculateSubLength(root.right) + 1)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    right_left = TreeNode(14)
    right_right = TreeNode(7)
    root.left = left
    root.right = right
    right.left = right_left
    right.right = right_right
    print(solution.isBalanced(root))
    # root = TreeNode(1)
    # left = TreeNode(2)
    # right = TreeNode(2)
    # left_left = TreeNode(3)
    # left_right = TreeNode(3)
    # left_left_left = TreeNode(4)
    # left_left_right = TreeNode(4)
    # root.left = left
    # root.right = right
    # left.left = left_left
    # left.right = left_right
    # left_left.left = left_left_left
    # left_left.right = left_left_right
    # print(solution.isBalanced(root))
    # root = TreeNode(1)
    # left = TreeNode(2)
    # right = TreeNode(2)
    # left_left = TreeNode(3)
    # right_right = TreeNode(3)
    # left_left_left = TreeNode(4)
    # right_right_right = TreeNode(4)
    # root.left = left
    # root.right = right
    # left.left = left_left
    # right.right = right_right
    # left_left.left = left_left_left
    # right_right.right = right_right_right
    # print(solution.isBalanced(root))
