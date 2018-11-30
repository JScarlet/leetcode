# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if root is None:
        #     return 0
        # max_depth = 0
        # node_list = [root]
        # while len(node_list) > 0:
        #     temp = []
        #     max_depth += 1
        #     for node in node_list:
        #         if node is not None:
        #             if node.left is not None:
        #                 temp.append(node.left)
        #             if node.right is not None:
        #                 temp.append(node.right)
        #     node_list = temp
        # return max_depth
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left, right) + 1


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(0)
    left = TreeNode(1)
    right = TreeNode(2)
    right_left = TreeNode(3)
    right_right = TreeNode(4)
    right_right_left = TreeNode(5)
    right_right_right = TreeNode(6)
    root.left = left
    root.right = right
    right.left = right_left
    right.right = right_right
    right_right.left = right_right_left
    right_right.right = right_right_right
    print(solution.maxDepth(root))
