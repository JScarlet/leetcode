class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n = n // 3
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfThree(9))