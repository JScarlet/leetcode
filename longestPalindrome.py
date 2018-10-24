class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        i = 1
        while i <= len(s):
            for j in range(0, len(s) + 1 - i):
                temp = s[j: j+i]
                if temp == temp[::-1]:
                    result = temp
                    break
            i += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    str = 'bb'
    print(solution.longestPalindrome(str))