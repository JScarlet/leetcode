# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return None
        else:
            return self.construct(1, n)

    def construct(self, start, end):
        result = []
        if start > end:
            result.append(None)
        else:
            for i in range(start, end + 1):
                left = self.construct(start, i - 1)
                right = self.construct(i + 1, end)
                print(len(left), len(right))
                for m in range(0, len(left)):
                    for n in range(0, len(right)):
                        root = TreeNode(i)
                        root.left = left[m]
                        root.right = right[n]
                        result.append(root)
        return result


    def print_tree(self, treenode):
        if treenode is not None:
            self.print_tree(treenode.left)
            print(treenode.val)
            self.print_tree(treenode.right)


if __name__ == '__main__':
    solution = Solution()
    result = solution.generateTrees(3)

    for each in result:
        solution.print_tree(each)
