# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        value_list = self.get_values(root)
        value_dict = {}
        for value in value_list:
            if value not in value_dict:
                value_dict[value] = 1
            else:
                value_dict[value] += 1
        sorted_value_list = sorted(value_dict.items(), key=lambda x:x[1])
        max_count = sorted_value_list[-1][1]
        result = []
        for i in range(0, len(sorted_value_list)):
            if sorted_value_list[i][1] == max_count:
                result.append(sorted_value_list[i][0])
        return result

    def get_values(self, root):
        num_dict = []
        if root is None:
            return num_dict
        else:
            num_dict.append(root.val)

            num_dict += self.get_values(root.left)
            num_dict += self.get_values(root.right)
            return num_dict


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    right = TreeNode(2)
    right_left = TreeNode(2)
    root.right = right
    right.left = right_left
    print(solution.findMode(root))