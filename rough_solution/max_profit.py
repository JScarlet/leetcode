class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        min = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] - min > max_profit:
                max_profit = prices[i] - min
            if prices[i] < min:
                min = prices[i]
        return max_profit


if __name__ == '__main__':
    solution = Solution()
    prices = [7,1,5,3,6,4]
    print(solution.maxProfit(prices))


# 解题思路：
# 用当天的股价减去之前的最低股价，最后找出最大的利润即可
