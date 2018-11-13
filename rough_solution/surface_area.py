class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        columns = len(grid[0])
        sum_all = 0
        for i in range(rows):
            for j in range(columns):
                sum_all += grid[i][j] * 6
                if grid[i][j] > 1:
                    sum_all -= (grid[i][j] - 1) * 2

                if j > 0:
                    sum_all -= min(grid[i][j], grid[i][j - 1]) * 2
                if i > 0:
                    sum_all -= min(grid[i][j], grid[i - 1][j]) * 2

        return sum_all


if __name__ == '__main__':
    solution = Solution()
    grid = [[3,3,3],[3,4,5],[5,0,4]]
    # grid = [[1,2,1],[2,1,1],[2,0,4]]
    print(solution.surfaceArea(grid))
