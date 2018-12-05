# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        elif t1 is not None and t2 is None:
            return t1
        elif t1 is None and t2 is not None:
            return t2
        else:
            t1.val = t1.val + t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1

    def printNode(self, root):
        if root is not None:
            print(root.val)
            self.printNode(root.left)
            self.printNode(root.right)


if __name__ == '__main__':
    solution = Solution()
    root1 = TreeNode(1)
    left1 = TreeNode(3)
    right1 = TreeNode(2)
    left_left1 = TreeNode(5)
    root1.left = left1
    root1.right = right1
    left1.left = left_left1

    root2 = TreeNode(2)
    left2 = TreeNode(1)
    right2 = TreeNode(3)
    left_right2 = TreeNode(4)
    right_right2 = TreeNode(7)
    root2.left = left2
    root2.right = right2
    left2.right = left_right2
    right2.right = right_right2

    solution.printNode(root1)
    print()
    solution.printNode(root2)
    print()
    root = solution.mergeTrees(root1, root2)
    solution.printNode(root)