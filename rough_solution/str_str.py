class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        return haystack.find(needle)


if __name__ == "__main__":
    solution = Solution()
    haystack = "hello"
    needle = "lll"
    print(solution.strStr(haystack, needle))


# 解题思路：
# 从第一位开始找到子串为止