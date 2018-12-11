class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s_list = S.split('-')
        new_s = ''.join(s_list).upper()
        result = []
        while len(new_s) > K:
            result.append(new_s[-K:])
            new_s = new_s[:-K]
        result.append(new_s)
        return '-'.join(result[::-1])


if __name__ == '__main__':
    solution = Solution()
    S = "2-5g-3-J"
    K = 2
    print(solution.licenseKeyFormatting(S, K))