# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total = 0
        if root is None:
            return total
        left = self.calculate_tree_sum(root.left)
        right = self.calculate_tree_sum(root.right)

        total += abs(left - right)
        total += self.findTilt(root.left)
        total += self.findTilt(root.right)
        return total

    def calculate_tree_sum(self, root):
        total = 0
        if root is None:
            return total
        else:
            total += root.val
            total += self.calculate_tree_sum(root.left)
            total += self.calculate_tree_sum(root.right)
            return total


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    left_left = TreeNode(4)
    left_right = TreeNode(5)
    root.left = left
    root.right = right
    left.left = left_left
    left.right = left_right
    print(solution.findTilt(root))