class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        final_s = ''
        final_t = ''
        for letter in S:
            if letter == '#':
                if len(final_s) > 0:
                    final_s = final_s[:-1]
            else:
                final_s += letter

        for letter in T:
            if letter == '#':
                if len(final_t) > 0:
                    final_t = final_t[:-1]
            else:
                final_t += letter

        return final_s == final_t


if __name__ == '__main__':
    solution = Solution()
    S = "a#c"
    T = "b"
    print(solution.backspaceCompare(S, T))