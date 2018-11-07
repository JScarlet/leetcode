class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) < 3:
            return 0

        matrix_list = []
        for i in range(0, len(grid) - 2):
            for j in range(0, len(grid[i]) - 2):
                single = []
                for m in range(i, i+3):
                    row = []
                    for n in range(j, j+3):
                        row.append(grid[m][n])
                    single.append(row)
                matrix_list.append(single)

        result = 0
        new_matrix_list = []
        for i in range(0, len(matrix_list)):
            temp = []
            for j in range(0, len(matrix_list[i])):
                temp.extend(matrix_list[i][j])
            count = 0
            for m in range(1, 10):
                if m in temp:
                    count += 1
            if count == 9:
                new_matrix_list.append(matrix_list[i])

        for matrix in new_matrix_list:
            if sum(matrix[0]) == sum([matrix[i][0] for i in range(0, len(matrix))]) == sum(matrix[i][i] for i in range(0, len(matrix))):
                result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    grid = [[10,3,5],[1,6,11],[7,9,2]]
    print(solution.numMagicSquaresInside(grid))
