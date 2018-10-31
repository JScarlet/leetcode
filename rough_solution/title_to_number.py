class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(0, len(s)):
            result += (26**(len(s) - 1 - i)) * (ord(s[i]) - 64)
        return result


if __name__ == '__main__':
    solution = Solution()
    s = 'AAA'
    print(solution.titleToNumber(s))


# 解题思路：
# 26进制数字的转化，ord()能将字符转化为整数