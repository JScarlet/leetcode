class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        total_labeled = set()
        max_area = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                temp_labeled = []
                temp_area = 0
                if grid[i][j] == 1 and (i, j) not in total_labeled:
                    temp_labeled.append((i, j))
                    total_labeled.add((i, j))
                    while temp_labeled:
                        index = temp_labeled.pop()
                        temp_area += 1
                        index_i = index[0]
                        index_j = index[1]
                        for each in direction:
                            new_i = index_i + each[0]
                            new_j = index_j + each[1]
                            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[i]):
                                if grid[new_i][new_j] == 1 and (new_i, new_j) not in total_labeled:
                                    total_labeled.add((new_i, new_j))
                                    temp_labeled.append((new_i, new_j))
                    if temp_area > max_area:
                        max_area = temp_area
        return max_area


if __name__ == '__main__':
    solution = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(solution.maxAreaOfIsland(grid))
    

# 解题思路：广度优先遍历
