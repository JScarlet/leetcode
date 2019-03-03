class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}
        for i in range(0, len(strs)):
            key = ''.join(sorted(strs[i]))
            group.setdefault(key, []).append(strs[i])
        result = []
        for key in group:
            result.append(group[key])
        return result


if __name__ == '__main__':
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))