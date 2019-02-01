class Solution:
    # def combinationSum(self, candidates, target):
    #     """
    #     :type candidates: List[int]
    #     :type target: int
    #     :rtype: List[List[int]]
    #     """
    #     ret = []
    #     self.recursive(candidates, target, 0, [], ret)
    #     return ret
    #
    # def recursive(self, candidates, target, i, pre, ret):
    #     if i == len(candidates):
    #         return
    #
    #     st = []
    #     while target >= candidates[i]:
    #         target -= candidates[i]
    #         st.append(candidates[i])
    #
    #     if target == 0:
    #         ret.append(pre + st)
    #     else:
    #         self.recursive(candidates, target, i + 1, pre + st, ret)
    #     # print(st)
    #     while st:
    #         target += st.pop()
    #         self.recursive(candidates, target, i + 1, pre + st, ret)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], result)
        return result

    def dfs(self, candidates, target, index, result, final):
        for i in range(index, len(candidates)):
            if target == candidates[i]:
                final.append(result + [candidates[i]])
                # print('condition1: ', result)
                return
            elif target > candidates[i]:
                self.dfs(candidates, target-candidates[i], i, result + [candidates[i]], final)


if __name__ == '__main__':
    solution = Solution()
    candidates = [2, 3, 5]
    target = 8
    print(solution.combinationSum(candidates, target))
