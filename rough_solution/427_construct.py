# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        gridSum = 0
        for i in range(0, len(grid)):
            gridSum += sum(grid[i])
        if gridSum == len(grid) * len(grid[0]):
            return Node(True, True, None, None, None, None)
        elif gridSum == 0:
            return Node(False, True, None, None, None, None)
        else:
            topLeftGrid = [[grid[i][j] for j in range(0, len(grid[0])//2)] for i in range(0, len(grid)//2)]
            topRightGrid = [[grid[i][j] for j in range(len(grid[0])//2, len(grid[0]))] for i in range(0, len(grid)//2)]
            bottomLeftGrid = [[grid[i][j] for j in range(0, len(grid[0])//2)] for i in range(len(grid)//2, len(grid))]
            bottomRightGrid = [[grid[i][j] for j in range(len(grid[0])//2, len(grid[0]))] for i in range(len(grid)//2, len(grid))]

            topLeft = self.construct(topLeftGrid)
            topRight = self.construct(topRightGrid)
            bottomLeft = self.construct(bottomLeftGrid)
            bottomRight = self.construct(bottomRightGrid)
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)


if __name__ == '__main__':
    solution = Solution()
    grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    print(solution.construct(grid))