class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        com_list = [i for i in range(1, n+1)]
        result = []
        self.dfs(com_list, 0, [], result, k)
        return result

    def dfs(self, com_list, index, head, result, k):
        if len(head) == k:
            result.append(head)
            return
        for i in range(index, len(com_list)):
            self.dfs(com_list, i+1, head + [com_list[i]], result, k)


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 3))
