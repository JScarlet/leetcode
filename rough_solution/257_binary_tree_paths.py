# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        else:
            result = self.construct_path(root)
            return list(result)

    def construct_path(self, root):
        if root is None:
            return []
        else:
            if root.left is None and root.right is None:
                # print(str(root.val))
                return [str(root.val)]
            elif root.left is None and root.right is not None:
                result = self.construct_path(root.right)
                for i in range(0, len(result)):
                    result[i] = str(root.val) + '->' + result[i]
                # print(result)
                return result
            elif root.left is not None and root.right is None:
                result = self.construct_path(root.left)
                for i in range(0, len(result)):
                    result[i] = str(root.val) + '->' + result[i]
                # print(result)
                return result
            else:
                result1 = self.construct_path(root.left)
                for i in range(0, len(result1)):
                    result1[i] = str(root.val) + '->' + result1[i]
                result2 = self.construct_path(root.right)
                for i in range(0, len(result2)):
                    result2[i] = str(root.val) + '->' + result2[i]
                result1.extend(result2)
                # print(result1)
                return result1


if __name__ == '__main__':
    solution = Solution()
    # root = TreeNode(1)
    # left = TreeNode(2)
    # right = TreeNode(3)
    # left_right = TreeNode(5)
    # root.left = left
    # root.right = right
    # left.right = left_right
    # print(solution.binaryTreePaths(root))
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    left_left = TreeNode(5)
    left_right = TreeNode(6)
    root.left = left
    root.right = right
    left.left = left_left
    left.right = left_right
    print(solution.binaryTreePaths(root))
