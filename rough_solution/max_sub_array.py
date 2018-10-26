class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time out
        max_sum = nums[0]
        for i in range(0, len(nums)):
            temp = 0
            for j in range(i + 1, len(nums)):
                temp += nums[j]
                if temp > max_sum:
                    max_sum = temp
        return max_sum

    def maxSubArray2(self, nums):
        current = max_sum = nums[0]
        for i in range(1, len(nums)):
            if current < 0:
                current = nums[i]
            else:
                current += nums[i]
            if current > max_sum:
                max_sum = current
        return max_sum


if __name__ == "__main__":
    solution = Solution()
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [-2, 1]
    # nums = [-1, -2]
    # nums = [-3,1,-2,2]
    nums = [-2,-2,-3,0,-3,1,-3]
    print(solution.maxSubArray2(nums))


# 解题思路：
# 1. 暴力循环两次，但是会超时
# 2. 一个数加上负数肯定会变小，因此如果当前得到的和是个负数，那么这个和在接下来的累加中应该抛弃并重新清零，不然的话这个负数将会减少接下来的和。
