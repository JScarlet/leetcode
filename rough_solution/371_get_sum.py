class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        total = a ^ b
        carry = (a & b) << 1
        return sum([total, carry])


if __name__ == '__main__':
    solution = Solution()
    print(solution.getSum(1, -1))