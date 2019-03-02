class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        belief_dict = {}
        for i in range(0, len(trust)):
            if trust[i][0] not in belief_dict:
                belief_dict[trust[i][0]] = {trust[i][1]}
            else:
                belief_dict[trust[i][0]].add(trust[i][1])
        candidate = {i for i in range(1, N + 1)}
        for key in belief_dict:
            candidate = candidate & belief_dict[key]
        if len(candidate) == 1:
            return list(candidate)[0]
        else:
            return -1


if __name__ == '__main__':
    solution = Solution()
    N = 4
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    print(solution.findJudge(N, trust))
