# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def leafSequence(root):
            result = []
            if root is None:
                return result
            if root.left is None and root.right is None:
                result.append(root.val)
            result.extend(leafSequence(root.left))
            result.extend(leafSequence(root.right))
            return result

        sequence1 = leafSequence(root1)
        sequence2 = leafSequence(root2)
        if sequence1 == sequence2:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    root1 = TreeNode(1)
    left1 = TreeNode(2)
    right1 = TreeNode(3)
    root1.left = left1
    root1.right = right1

    root2 = TreeNode(2)
    left2 = TreeNode(2)
    right2 = TreeNode(4)
    root2.left = left2
    root2.right = right2
    print(solution.leafSimilar(root1, root2))
