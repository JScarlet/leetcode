class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None or k is None:
            return False
        queue = [root]
        temp = []
        num_set = set()
        while len(queue) > 0:
            element = queue.pop(0)
            if element.left is not None:
                temp.append(element.left)
            if element.right is not None:
                temp.append(element.right)
            if k - element.val in num_set:
                return True
            else:
                num_set.add(element.val)

            if len(queue) == 0:
                queue = temp
                temp = []
        return False


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)
    left = TreeNode(3)
    right = TreeNode(6)
    left_left = TreeNode(2)
    left_right = TreeNode(4)
    right_right = TreeNode(7)
    root.left = left
    root.right = right
    left.left = left_left
    left.right = left_right
    right.right = right_right
    print(solution.findTarget(root, 9))
    # root = TreeNode(2)
    # left = TreeNode(1)
    # right = TreeNode(3)
    # root.left = left
    # root.right = right
    # print(solution.findTarget(root, 4))