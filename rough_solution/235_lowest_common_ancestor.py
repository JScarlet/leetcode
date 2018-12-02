# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < q.val:
            min_node = p
            max_node = q
        else:
            min_node = q
            max_node = p
        if root is None:
            return None
        if min_node.val <= root.val <= max_node.val:
            return root.val
        elif root.val > max_node.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(6)
    left = TreeNode(2)
    right = TreeNode(8)
    left_left = TreeNode(0)
    left_right = TreeNode(4)
    right_left = TreeNode(7)
    right_right = TreeNode(9)
    left_right_left = TreeNode(3)
    left_right_right = TreeNode(5)
    root.left = left
    root.right = right
    left.left = left_left
    left.right = left_right
    right.left = right_left
    right.right = right_right
    left_right.left = left_right_left
    left_right.right = left_right_right
    print(solution.lowestCommonAncestor(root, left_right_left, left_right_right))