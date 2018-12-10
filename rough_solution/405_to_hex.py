class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        num2letter = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        result = ''
        if num > 0:
            while num != 0:
                temp = num % 16
                if temp >= 10:
                    temp = num2letter[temp]
                else:
                    temp = str(temp)
                result += temp
                num = num // 16
            result = result[::-1]
            if len(result) > 8:
                result = result[-8:]
            while len(result) > 1 and result[0] == '0':
                result = result[1:]
            return result
        else:
            num = 2 ** 32 + num
            return self.toHex(num)


if __name__ == '__main__':
    solution = Solution()
    print(solution.toHex(-1))