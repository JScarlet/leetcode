class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        int2roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        num_str = str(num)
        for i in range(0, len(num_str)):
            position = 10 ** (len(num_str)-i-1)
            n = int(num_str[i])
            if n == 9:
                result += int2roman[position] + int2roman[position*10]
            elif n > 5:
                result += int2roman[position*5] + int2roman[position] * (n - 5)
            elif n == 5:
                result += int2roman[position*5]
            elif n == 4:
                result += int2roman[position] + int2roman[position*5]
            else:
                result += int2roman[position] * n
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.intToRoman(199))