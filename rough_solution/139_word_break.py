class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [0 for i in range(0, len(s) + 1)]
        dp[0] = 1
        for i in range(0, len(s)):
            for j in range(0, i+1):
                # print(s[j: i+1])
                if dp[j] != 0 and s[j: i+1] in wordDict:
                    # print(s[j: i])
                    dp[i+1] = 1
            # print(dp)
        return dp[-1] == 1


if __name__ == '__main__':
    solution = Solution()
    s = "cars"
    wordDict = ['car', 'ca', 'rs']
    print(solution.wordBreak(s, wordDict))
