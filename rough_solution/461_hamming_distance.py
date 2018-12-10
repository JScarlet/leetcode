class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        temp = bin(x ^ y)[2:]
        return temp.count('1')


if __name__ == '__main__':
    solution = Solution()
    x = 1
    y = 4
    print(solution.hammingDistance(x, y))
