# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        max_depth = 0
        if root is None:
            return max_depth
        max_depth = 1
        if len(root.children) > 0:
            # max_depth += 1
            temp = []
            for child in root.children:
                temp.append(self.maxDepth(child))
            max_depth += max(temp)
        return max_depth


if __name__ == '__main__':
    solution = Solution()
    root = Node(1, [])
    left = Node(2, [])
    middle = Node(3, [])
    right = Node(4, [])
    left_left = Node(5, [])
    left_right = Node(6, [])
    left.children = [left_left, left_right]
    root.children = [left, middle, right]
    print(solution.maxDepth(root))
