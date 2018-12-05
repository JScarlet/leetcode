# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        result.append(root.val)
        if root.children is not None:
            for child in root.children:
                result += self.preorder(child)
        return result


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
    print(solution.preorder(root))
