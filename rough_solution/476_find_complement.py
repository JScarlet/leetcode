class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        length = len(bin(num)[2:])
        return (2 ** length - 1) ^ num


if __name__ == '__main__':
    solution = Solution()
    num = 1
    print(solution.findComplement(num))