class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            if s == '0':
                return 0
            else:
                return 1
        dp = [0 for i in range(0, len(s)+1)]
        if s[0] == '0':
            return 0
        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i+1] += dp[i]
            print(dp)
            if 1 <= int(s[i-1: i+1]) <= 26 and s[i-1] != '0':
                dp[i+1] += dp[i-1]
            print(dp)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    s = '101'
    print(solution.numDecodings(s))
