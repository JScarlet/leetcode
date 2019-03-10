class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        dp = []
        for i in range(0, len(triangle)):
            temp = []
            for j in range(0, len(triangle[i])):
                temp.append(0)
            dp.append(temp)
        # print(dp)
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][-1] = dp[i-1][-1] + triangle[i][-1]

        for i in range(1, len(triangle)):
            for j in range(1, len(triangle[i])-1):
                # print(i, j)
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        return min(dp[-1])


if __name__ == '__main__':
    solution = Solution()
    triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    print(solution.minimumTotal(triangle))