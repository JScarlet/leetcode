# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t is None:
            return False
        if s is not None:
            if s.val != t.val:
                return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            else:
                return self.isEqual(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        else:
            return False

    def isEqual(self, root1, root2):
        # result = True
        if root1 is None and root2 is None:
            return True
        elif root1 is not None and root2 is not None:
            if root1.val == root2.val:
                return True & self.isEqual(root1.left, root2.left) & self.isEqual(root1.right, root2.right)
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    root1 = TreeNode(3)
    left1 = TreeNode(4)
    right1 = TreeNode(5)
    left_left1 = TreeNode(1)
    left_right1 = TreeNode(2)
    left_right_left1 = TreeNode(0)
    root1.left = left1
    root1.right = right1
    left1.left = left_left1
    left1.right = left_right1
    left_right1.left = left_right_left1

    root2 = TreeNode(4)
    left2 = TreeNode(1)
    right2 = TreeNode(2)
    root2.left = left2
    root2.right = right2

    print(solution.isSubtree(root1, left1))
