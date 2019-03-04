class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for i in range(n)] for i in range(n)]
        left, right, top, down = 0, n, 0, n
        flag = 1
        count = 0
        while count < n ** 2:
            if flag == 1:
                for i in range(left, right):
                    count += 1
                    result[top][i] = count
                top += 1
            elif flag == 2:
                for i in range(top, down):
                    count += 1
                    result[i][right - 1] = count
                right -= 1
            elif flag == 3:
                for i in reversed(range(left, right)):
                    count += 1
                    result[down - 1][i] = count
                down -= 1
            else:
                for i in reversed(range(top, down)):
                    count += 1
                    result[i][left] = count
                left += 1
            flag += 1
            if flag > 4:
                flag = 1
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.generateMatrix(2)
    for i in range(len(result)):
        print(result[i])