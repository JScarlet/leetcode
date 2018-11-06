class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        start_list = [matrix[i][0] for i in range(len(matrix))]
        for i in range(1, len(start_list)):
            temp = matrix[i-1]
            temp.pop()
            temp.insert(0, start_list[i])
            # print(matrix[i], temp)
            if matrix[i] != temp:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2]
    ]
    print(solution.isToeplitzMatrix(matrix))

# 解题思路：
# 每一行的数据等于去掉最后一个数据再加上下一行的第一个数据
