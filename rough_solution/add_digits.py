class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num_str = str(num)
            num = 0
            for letter in num_str:
                num += int(letter)
        return num


if __name__ == '__main__':
    solution = Solution()
    print(solution.addDigits(38))
