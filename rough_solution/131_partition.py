class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.dfs(s, [], result)
        return result

    def dfs(self, s, head, result):
        if s == '':
            result.append(head)
            return
        for i in range(0, len(s)):
            if s[0:i+1] == s[0:i+1][::-1]:
                self.dfs(s[i+1:], head+[s[0:i+1]], result)


if __name__ == '__main__':
    solution = Solution()
    s = "aab"
    print(solution.partition(s))
