class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs([], k, n, 1, result)
        return result

    def dfs(self, head, k, n, target, result):
        # print(head, k, n, target)
        if n == 0 and k == 0:
            result.append(head)
            return
        elif k == 0:
            return
        elif n == 0:
            return
        for i in range(target, 10):
            if i <= n:
                self.dfs(head + [i], k - 1, n - i, i+1, result)


if __name__ == '__main__':
    solution = Solution()
    k = 3
    n = 15
    print(solution.combinationSum3(k, n))
