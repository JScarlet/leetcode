class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if len(s) == 0:
        #     return 0
        # for letter in s:
        #     if not letter.isalpha() and letter != ' ':
        #         s = s.replace(letter, '', 1)
        return len(s.split())


if __name__ == '__main__':
    solution = Solution()
    s = "Ha"
    print(solution.countSegments(s))
