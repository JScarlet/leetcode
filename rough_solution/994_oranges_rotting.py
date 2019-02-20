class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if self.check(grid):
            return 0
        queue = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j))
        time = 0
        while len(queue) > 0:
            temp = set()
            direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for each in queue:
                rotted_x = each[0]
                rotted_y = each[1]
                for direct in direction:
                    new_x = rotted_x + direct[0]
                    new_y = rotted_y + direct[1]
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                        if grid[new_x][new_y] == 1:
                            grid[new_x][new_y] = 2
                            temp.add((new_x, new_y))
            time += 1
            queue = list(temp)
        if self.check(grid):
            return time - 1
        return -1

    def check(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(solution.orangesRotting(grid))
