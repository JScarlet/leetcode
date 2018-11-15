class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        reversed_s = s[::-1]
        if s == reversed_s:
            return True
        for i in range(0, len(s)):
            if s[i] != reversed_s[i]:
                s = s[:i] + s[i+1:]
                reversed_s = reversed_s[:i] + reversed_s[i+1:]
                break
        if s == s[::-1] or reversed_s == reversed_s[::-1]:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    s = 'accccbcba'
    print(solution.validPalindrome(s))


# 解题思路：
# 如果s和翻转后的reversed_s相同，返回True；
# 否则的话，找到第一个s和reversed_s不同的字符，删去后如果s或者reversed_s是回文数，就返回True，否则返回False
