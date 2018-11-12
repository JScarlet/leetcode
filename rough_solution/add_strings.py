class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) > len(num2):
            short_num = num2[::-1]
            long_num = num1[::-1]
        else:
            short_num = num1[::-1]
            long_num = num2[::-1]

        result = ''
        flag = 0
        for i in range(0, len(short_num)):
            temp = int(short_num[i]) + int(long_num[i]) + flag
            if temp >= 10:
                temp -= 10
                flag = 1
            else:
                flag = 0
            result += str(temp)

        for i in range(len(short_num), len(long_num)):
            temp = int(long_num[i]) + flag
            if temp >= 10:
                temp -= 10
                flag = 1
            else:
                flag = 0
            result += str(temp)

        if flag == 1:
            result += '1'
        return result[::-1]


if __name__ == '__main__':
    solution = Solution()
    num1 = '408'
    num2 = '5'
    print(solution.addStrings(num1, num2))
