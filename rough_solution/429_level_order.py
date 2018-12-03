# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result = [[root.val]]
        children = root.children
        while len(children) > 0:
            temp = []
            temp_children = []
            for child in children:
                if child is not None:
                    temp.append(child.val)
                    temp_children.extend(child.children)
            result.append(temp)
            children = temp_children
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
    print(solution.levelOrder(root))