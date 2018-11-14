class Solution:
    def firstUniqChar(self, s):
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

        for i in range(0, len(s)):
            if s_dict[s[i]] == 1:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    s = "loveleetcode"
    print(solution.firstUniqChar(s))
