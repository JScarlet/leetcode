# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is not None:
            hierachy = [root]
            while len(hierachy) > 0:
                temp_hierachy = []
                temp_value_list = []
                for node in hierachy:
                    if node is not None:
                        temp_value_list.append(node.val)
                        if node.left is not None:
                            temp_hierachy.append(node.left)
                        if node.right is not None:
                            temp_hierachy.append(node.right)
                result.append(temp_value_list)
                hierachy = temp_hierachy
        return result[::-1]


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
    print(solution.levelOrderBottom(root))
