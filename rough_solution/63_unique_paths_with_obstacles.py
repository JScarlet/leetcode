class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        path_count_list = [[0 for i in range(len(obstacleGrid[0]))] for i in range(0, len(obstacleGrid))]
        for i in range(0, len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                break
            path_count_list[i][0] = 1
        for i in range(0, len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                break
            path_count_list[0][i] = 1
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    path_count_list[i][j] = 0
                else:
                    path_count_list[i][j] = path_count_list[i-1][j] + path_count_list[i][j-1]
        return path_count_list[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
    print(solution.uniquePathsWithObstacles(obstacleGrid))