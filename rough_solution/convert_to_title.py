class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        letter_map = {1: 'A',
                      2: 'B',
                      3: 'C',
                      4: 'D',
                      5: 'E',
                      6: 'F',
                      7: 'G',
                      8: 'H',
                      9: 'I',
                      10: 'J',
                      11: 'K',
                      12: 'L',
                      13: 'M',
                      14: 'N',
                      15: 'O',
                      16: 'P',
                      17: 'Q',
                      18: 'R',
                      19: 'S',
                      20: 'T',
                      21: 'U',
                      22: 'V',
                      23: 'W',
                      24: 'X',
                      25: 'Y',
                      26: 'Z'}
        result = ''
        temp = n
        while temp > 26:
            temp = n // 26
            temp2 = n % 26
            if temp2 == 0:
                temp2 = 26
                temp -= 1
            result += letter_map[temp2]
            n = temp
        # if temp > 0:
        result += letter_map[temp]

        return result[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.convertToTitle(701))


# 解题思路：
# 写了这么复杂，想了想好像还是先减1然后当成26进制的数来做...
