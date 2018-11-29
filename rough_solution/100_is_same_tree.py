# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_value = []
        q_value = []

        self.list_tree_value(p, p_value)
        self.list_tree_value(q, q_value)
        return p_value == q_value

    def list_tree_value(self, tree_node, value_list):
        if tree_node is not None:
            value_list.append(tree_node.val)
        else:
            value_list.append(None)
            return
        self.list_tree_value(tree_node.left, value_list)

        self.list_tree_value(tree_node.right, value_list)


if __name__ == '__main__':
    solution = Solution()
    root1 = TreeNode(1)
    left1 = TreeNode(2)
    right1 = TreeNode(3)
    root1.left = left1
    root1.right = right1

    root2 = TreeNode(1)
    left2 = TreeNode(2)
    right2 = TreeNode(3)
    root2.left = left2
    root2.right = right2

    print(solution.isSameTree(root1, root2))