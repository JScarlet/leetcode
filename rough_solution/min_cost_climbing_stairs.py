class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        # return self.calculate(n, cost)
        min_sum_list = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            # print(min_sum_list)
            min_sum_list.append(min(min_sum_list[i-1] + cost[i], min_sum_list[i-2] + cost[i]))
        return min_sum_list[-1]


if __name__ == '__main__':
    solution = Solution()
    cost = [10, 15, 20]
    print(solution.minCostClimbingStairs(cost))
