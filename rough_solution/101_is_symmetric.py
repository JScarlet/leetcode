# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        temp = [root]
        while temp.count(None) != len(temp):
            for i in range(0, len(temp)//2):
                if temp[i] is not None or temp[len(temp)-1-i] is not None:
                    if temp[i] is None:
                        return False
                    elif temp[len(temp)-1-i] is None:
                        return False
                    elif temp[i].val != temp[len(temp)-1-i].val:
                        return False

            temp2 = []
            for each in temp:
                if each is not None:
                    temp2.append(each.left)
                    temp2.append(each.right)
            temp = temp2
        return True


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(2)
    left_left = TreeNode(3)
    left_right = TreeNode(4)
    right_left = TreeNode(4)
    right_right = TreeNode(3)
    root.left = left
    root.right = right
    left.left = left_left
    left.right = left_right
    right.left = right_left
    right.right = right_right
    print(solution.isSymmetric(root))