# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def postOrder(root):
            result = []
            if root is None:
                return result
            result.extend(postOrder(root.left))
            result.append(root.val)
            result.extend(postOrder(root.right))
            return result
        if root is None:
            return None
        sequence = postOrder(root)
        node_list = []
        for each in sequence:
            node = TreeNode(each)
            node_list.append(node)
        for i in range(0, len(node_list) - 1):
            node_list[i].right = node_list[i+1]
        return node_list[0]

