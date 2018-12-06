# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return -1
        if root.left is None and root.right is None:
            return -1
        else:
            if root.val == root.left.val:
                min_left = self.findSecondMinimumValue(root.left)
            else:
                min_left = root.left.val

            if root.val == root.right.val:
                min_right = self.findSecondMinimumValue(root.right)
            else:
                min_right = root.right.val

            # print(min_left, min_right)
            if min_left == -1 or min_right == -1:
                return max(min_left, min_right)
            else:
                return min(min_left, min_right)


if __name__ == '__main__':
    solution = Solution()
    # root = TreeNode(2)
    # left = TreeNode(2)
    # right = TreeNode(2)
    # root.left = left
    # root.right = right
    # print(solution.findSecondMinimumValue(root))
    root = TreeNode(2)
    left = TreeNode(2)
    right = TreeNode(2)
    left_left = TreeNode(3)
    left_right = TreeNode(4)
    right_left = TreeNode(5)
    right_right = TreeNode(6)
    root.left = left
    root.right = right
    left.left = left_left
    left.right = left_right
    right.left = right_left
    right.right = right_right
    print(solution.findSecondMinimumValue(root))
