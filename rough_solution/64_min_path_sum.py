class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        path_sum = [[0 for i in range(len(grid[0]))] for i in range(0, len(grid))]
        path_sum[0][0] = grid[0][0]
        for i in range(1, len(path_sum[0])):
            path_sum[0][i] = path_sum[0][i-1] + grid[0][i]
        for i in range(1, len(path_sum)):
            path_sum[i][0] = path_sum[i-1][0] + grid[i][0]
        for i in range(1, len(path_sum)):
            for j in range(1, len(path_sum[0])):
                path_sum[i][j] = min(path_sum[i-1][j], path_sum[i][j-1]) + grid[i][j]
        return path_sum[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
    print(solution.minPathSum(grid))