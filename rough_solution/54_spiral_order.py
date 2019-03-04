class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        result = []
        count = 0
        top, down, left, right = 0, len(matrix), 0, len(matrix[0])
        total = down * right
        flag = 1
        while count < total:
            if flag == 1:
                for m in range(left, right):
                    result.append(matrix[top][m])
                    count += 1
                top += 1
            elif flag == 2:
                for m in range(top, down):
                    result.append(matrix[m][right - 1])
                    count += 1
                right -= 1
            elif flag == 3:
                for m in reversed(range(left, right)):
                    result.append(matrix[down - 1][m])
                    count += 1
                down -= 1
            else:
                for m in reversed(range(top, down)):
                    result.append(matrix[m][left])
                    count += 1
                left += 1
            flag += 1
            if flag > 4:
                flag = 1
        return result


if __name__ == '__main__':
    solution = Solution()
    matrix = []
    print(solution.spiralOrder(matrix))