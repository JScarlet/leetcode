class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 1:
            return False
        while n > 1:
            temp = n % 2
            if temp != 0:
                return False
            n = n //2
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfTwo(1))
