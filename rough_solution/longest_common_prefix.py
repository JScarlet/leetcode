class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        if len(strs) == 0:
            return ''
        prefix = ''
        for i in range(0, len(strs[0])):
            temp = strs[0][0: i+1]
            count = 0
            for j in range(1, len(strs)):
                if strs[j][0: i+1] == temp:
                    count += 1
            if count == len(strs) - 1:
                prefix = temp
        return prefix


if __name__ == '__main__':
    strs = ["dog","racecar","car"] #["flower","flow","flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs))


# 解题思路：
# 取第一个字符串的每一个前缀，看列表里的其他元素都含有该前缀，最后返回最长的即可
