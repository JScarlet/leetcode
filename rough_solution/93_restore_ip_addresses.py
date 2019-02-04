class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        result = []
        self.dfs(s, [], result, 0, 0)
        result = ['.'.join(each) for each in result]
        return result

    def dfs(self, s, head, result, start, number):
        if number == 3 and s[start:] != '' and 0 <= int(s[start:]) <= 255:
            if len(s[start:]) > 1:
                if s[start:][0] != '0':
                    result.append(head + [s[start:]])
                    return
            else:
                result.append(head + [s[start:]])
                return
        for i in range(start, len(s)):
            if s[start: i] != '' and 0 <= int(s[start: i]) <= 255:
                # print(s[start:i])
                if len(s[start:i]) > 1:
                    if s[start:i][0] != '0':
                        self.dfs(s, head + [s[start: i]], result, i, number + 1)
                else:
                    self.dfs(s, head + [s[start: i]], result, i, number + 1)


if __name__ == '__main__':
    solution = Solution()
    s = "25525511135"
    print(solution.restoreIpAddresses(s))
