# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return None
        queue = [root]
        temp = []
        result = []
        sum = 0
        num = 0
        while len(queue) > 0:
            element = queue.pop(0)
            num += 1
            sum += element.val
            if element.left is not None:
                temp.append(element.left)
            if element.right is not None:
                temp.append(element.right)
            if len(queue) == 0:
                queue = temp
                temp = []
                result.append(sum/num)
                print(sum, num)
                sum = 0
                num = 0
        return result


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    right_left = TreeNode(15)
    right_right = TreeNode(7)
    root.left = left
    root.right = right
    right.left = right_left
    right.right = right_right
    print(solution.averageOfLevels(root))