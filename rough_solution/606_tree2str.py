# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        if t.left is not None and t.right is not None:
            return str(t.val) + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'
        elif t.left is None and t.right is not None:
            return str(t.val) + "()(" + self.tree2str(t.right) + ")"
        elif t.left is not None and t.right is None:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"
        else:
            return str(t.val)



if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    left_left = TreeNode(4)
    root.left = left
    root.right = right
    left.right = left_left
    print(solution.tree2str(root))