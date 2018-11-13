class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        xy_area = 0
        yz_area = 0
        zx_area = 0
        for i in range(0, len(grid)):
            max_xz = 0
            for j in range(0, len(grid[i])):
                if grid[i][j] != 0:
                    xy_area += 1
                if grid[i][j] > max_xz:
                    max_xz = grid[i][j]
            zx_area += max_xz

        for i in range(0, len(grid[0])):
            max_yz = 0
            for j in range(0, len(grid)):
                if grid[j][i] > max_yz:
                    max_yz = grid[j][i]
            yz_area += max_yz
        return xy_area + yz_area + zx_area


if __name__ == '__main__':
    solution = Solution()
    grid = [[2,2,2],[2,1,2],[2,2,2]]
    print(solution.projectionArea(grid))
