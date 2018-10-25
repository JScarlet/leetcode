class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(0, len(s)):
            if i != len(s) - 1:
                if roman_dict[s[i]] >= roman_dict[s[i+1]]:
                    result += roman_dict[s[i]]
                else:
                    result -= roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]
        return result


if __name__ == "__main__":
    str = 'MCMXCIV'
    solution = Solution()
    print(solution.romanToInt(str))


# 解题思路：
# 实际上就是把罗马数字的每一位都加起来，如果前一位比后一位数字小的话，前一位数字就取负数即可
