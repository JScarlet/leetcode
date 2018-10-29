class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        simple_str = ''
        for letter in s:
            if letter.isalnum():
                simple_str += letter.lower()
        print(simple_str)
        if simple_str == simple_str[::-1]:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    s = "0P"
    print(solution.isPalindrome(s))

# 解题思路：
# 考察字符串的isalnum()方法以及倒序输出
