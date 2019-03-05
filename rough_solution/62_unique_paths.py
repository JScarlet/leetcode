class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        total = m + n - 2
        result = 1
        for i in range(0, m - 1):
            result *= (total - i)
        # print(result)
        temp = 1
        for i in range(1, m):
            temp *= i
        # print(temp)
        return int(result / temp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(3, 2))