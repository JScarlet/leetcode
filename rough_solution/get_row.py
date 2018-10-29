class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        for i in range(0, rowIndex + 1):
            num = self.factorial(rowIndex) // (self.factorial(i) * self.factorial(rowIndex - i))
            result.append(num)
        return result

    def factorial(self, n):
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.getRow(1))


# 解题思路：
# 杨辉三角形的第i行是(a+b)**i的展开式的系数，每一项的系数可以用c(m, n)来计算