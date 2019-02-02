class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        value = re.match(p, s)
        if value == None or value.group(0) != s:
            return False
        else:
            return True
    #     if s == '':
    #         p = p[self.check_pattern(p) + 1:]
    #         if ('*' in p and '.' not in p) or p == '':
    #             return True
    #         else:
    #             return False
    #     if s != '' and p == '':
    #         return False
    #     pattern = p[0: self.check_pattern(p) + 1]
    #     print(pattern)
    #     if '*' not in pattern:
    #         length = len(pattern)
    #         if len(set(pattern)) == 1 and '.' in pattern:
    #             s = s[length:]
    #             p = p[length:]
    #             return self.isMatch(s, p)
    #         elif s[0: length] == pattern:
    #             s = s[length:]
    #             p = p[length:]
    #             return self.isMatch(s, p)
    #         else:
    #             return False
    #     else:
    #         if s[0] == pattern[0] or pattern[0] == '.':
    #             s = s[1:]
    #             return self.isMatch(s, p)
    #         else:
    #             p = p[len(pattern):]
    #             return self.isMatch(s, p)
    #
    # def check_pattern(self, p):
    #     if len(p) == 1:
    #         return 0
    #     result = 1
    #     while result < len(p):
    #         if p[result] == '*' or (p[result] == p[0] and p[0] != '.'):
    #             result += 1
    #         else:
    #             return result - 1
    #     return result - 1

if __name__ == '__main__':
    solution = Solution()
    # s = "mississippi"
    # p = "mis*is*ip*."
    s = "a"
    p = ".*..a*"
    print(solution.isMatch(s, p))
