class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_list = []
        temp = 1
        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                temp += 1
            else:
                count_list.append(temp)
                temp = 1
        count_list.append(temp)
        # print(count_list)
        result = 0
        for i in range(0, len(count_list) - 1):
            result += min(count_list[i], count_list[i+1])
        return result


if __name__ == '__main__':
    solution = Solution()
    s = "10101"
    print(solution.countBinarySubstrings(s))


# 解题思路：
# 先把连续出现的数字的次数都存下来，然后把相邻两个数字出现次数的最小值相加即可
