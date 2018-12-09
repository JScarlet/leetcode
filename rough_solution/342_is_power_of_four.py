class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        while num > 1:
            if num % 4 != 0:
                return False
            num = num // 4
        return True


if __name__ == '__main__':
    solution = Solution()
    num = 16
    print(solution.isPowerOfFour(num))