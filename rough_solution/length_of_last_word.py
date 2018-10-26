class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        if ' ' not in s:
            return len(s)
        s = s.strip()
        s_list = s.split(' ')
        return len(s_list[-1])


if __name__ == '__main__':
    solution = Solution()
    s = "Hello "
    print(solution.lengthOfLastWord(s))


# 解题思路：
# 去除两端的空格，返回最后一个单词的长度
