class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        remain = n % 4
        if remain in [1, 2, 3]:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    n = 4
    print(solution.canWinNim(n))
