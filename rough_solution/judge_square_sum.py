class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        temp1 = int(c**0.5)
        for i in range(0, temp1+1):
            temp2 = (c - i**2)
            b2 = int(temp2**0.5)
            if b2**2 == temp2:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.judgeSquareSum(2))