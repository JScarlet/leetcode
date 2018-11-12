class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((2 * n + 1/4) ** 0.5 - 1/2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.arrangeCoins(9))

    
# 解题思路：
# 求跟公司 i*(i+1)/2 = n，求出i的解析式
