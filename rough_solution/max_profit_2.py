class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        is_bought = False
        buy = 0
        sell = 0
        for i in range(0, len(prices) - 1):
            if not is_bought:
                if prices[i] <= prices[i+1]:
                    buy = prices[i]
                    is_bought = True
            else:
                if prices[i] > prices[i+1]:
                    sell = prices[i]
                    print(buy, sell)
                    max_profit += (sell - buy)
                    is_bought = False
        if is_bought:
            sell = prices[len(prices) - 1]
            max_profit += (sell - buy)
        return max_profit

    def maxProfit2(self, prices):
        profit = 0
        if len(prices) == 1 or len(prices) == 0:
            return profit
        else:
            # price=prices[0]
            for i in range(0, len(prices) - 1):
                if prices[i + 1] >= prices[i]:
                    # price=prices[i]
                    profit += prices[i + 1] - prices[i]
            return profit


if __name__ == '__main__':
    solution = Solution()
    prices = [7, 5, 1, 8, 7, 6, 4]
    print(solution.maxProfit(prices))


# 解题思路：
# 只买涨的不买跌的，for循环的意思相当于 (x[i] - x[i-1]) + (x[i+1] - x[i]) = x[i+1] - x[i-1]
