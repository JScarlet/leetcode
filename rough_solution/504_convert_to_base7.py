class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        positive = True
        result = ''
        if num < 0:
            num = -num
            positive = False
        if num == 0:
            return '0'
        while num != 0:
            result += str(num % 7)
            num = num // 7
        if not positive:
            result += '-'
        return result[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.convertToBase7(-7))