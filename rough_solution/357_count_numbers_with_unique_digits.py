class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 10
        if n <= 1:
            return 10 ** n
        for i in range(1, n):
            temp = 9
            for j in range(0, i):
                temp *= (9 - j)
            result += temp
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countNumbersWithUniqueDigits(4))
