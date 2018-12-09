# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        result = self.getNodeList(root)
        result = sorted(result)
        min_diff = result[-1]
        for i in range(0, len(result) - 1):
            if result[i+1] - result[i] < min_diff:
                min_diff = result[i+1] - result[i]
        return min_diff

    def getNodeList(self, root):
        result = []
        if root is None:
            return result
        result.append(root.val)
        result.extend(self.getNodeList(root.left))
        result.extend(self.getNodeList(root.right))
        return result


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    right = TreeNode(3)
    right_left = TreeNode(2)
    root.right = right
    right.left = right_left
    print(solution.getMinimumDifference(root))
