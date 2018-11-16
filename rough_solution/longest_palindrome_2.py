class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = {}
        for letter in s:
            if letter not in s_dict:
                s_dict[letter] = 1
            else:
                s_dict[letter] += 1

        print(s_dict)
        result = 0
        odd_len = 0
        for key in s_dict:
            value = s_dict[key]
            if value % 2 != 0:
                odd_len += 1
            result += value
        if odd_len != 0:
            result -= (odd_len - 1)
        return result


if __name__ == '__main__':
    solution = Solution()
    s = "bbaaaccc"
    print(solution.longestPalindrome(s))
    print(len(s))
