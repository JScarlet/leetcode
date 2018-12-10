class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        length = len(bin(n)[2:])
        if (2 ** length - 1) ^ n == n >> 1:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.hasAlternatingBits(1))