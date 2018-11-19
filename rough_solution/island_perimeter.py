class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    count = 0
                    for each in directions:
                        new_i = i + each[0]
                        new_j = j + each[1]
                        if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[i]) and grid[new_i][new_j] == 1:
                            count += 1
                    result += (4 - count)
        return result


if __name__ == '__main__':
    solution = Solution()
    grid = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    print(solution.islandPerimeter(grid))


# 解题思路：
# 判断岛屿的每一块周围有几块与之相连，初始为4，每有一块就减1，累加起来即可
