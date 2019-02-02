class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], result)
        return result

    def dfs(self, candidates, target, start, temp, result):
        for i in range(start, len(candidates)):
            if candidates[i] == target:
                if (temp + [candidates[i]]) not in result:
                    result.append(temp + [candidates[i]])
                return
            elif candidates[i] < target:
                self.dfs(candidates, target - candidates[i], i + 1, temp + [candidates[i]], result)


if __name__ == '__main__':
    solution = Solution()
    candidates = [2,5,2,1,2]
    target = 5
    print(solution.combinationSum2(candidates, target))
