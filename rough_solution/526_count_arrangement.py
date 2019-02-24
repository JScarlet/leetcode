class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        n_list = [i for i in range(1, N + 1)]
        result = []
        self.dfs([], n_list, result)
        # print(result)
        return len(result)

    def dfs(self, head, n_list, result):
        if len(n_list) == 0:
            result.append(head)
            return
        for i in range(0, len(n_list)):
            if n_list[i] % (len(head) + 1) == 0 or (len(head) + 1) % n_list[i] == 0:
                self.dfs(head + [n_list[i]], n_list[0:i] + n_list[i+1:], result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.countArrangement(15))
