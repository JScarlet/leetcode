class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [0 for _ in range(0, len(nums)-1)]
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, len(nums)-1):
            for j in range(0, i-1):
                dp[i] = max(dp[i], dp[j] + nums[i])
        # print(dp)
        dp_2 = [0 for _ in range(0, len(nums)-1)]
        dp_2[0] = nums[1]
        dp_2[1] = nums[2]
        for i in range(3, len(nums)):
            for j in range(1, i-1):
                dp_2[i-1] = max(dp_2[i-1], dp_2[j-1] + nums[i])
        # print(dp_2)
        return max(max(dp), max(dp_2))


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,1,1]
    print(solution.rob(nums))
