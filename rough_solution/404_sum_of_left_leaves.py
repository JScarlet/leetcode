# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        result = self.calculate(root, result)
        return result

    def calculate(self, root, result):
        if root is None:
            return result
        else:
            if root.left is not None:
                if root.left.left is None and root.left.right is None:
                    result += root.left.val
            result = self.calculate(root.left, result)
            result = self.calculate(root.right, result)
            return result


if __name__ == '__main__':
    solution = Solution()
    # root = TreeNode(3)
    # left = TreeNode(9)
    # right = TreeNode(20)
    # right_left = TreeNode(15)
    # right_right = TreeNode(7)
    # root.left = left
    # root.right = right
    # right.left = right_left
    # right.right = right_right
    # print(solution.sumOfLeftLeaves(root))
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    left_left = TreeNode(4)
    left_right = TreeNode(5)
    root.left = left
    root.right = right
    left.left = left_left
    left.right = left_right
    print(solution.sumOfLeftLeaves(root))
