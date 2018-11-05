class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        temp = max_sum = sum(nums[0: k])
        for i in range(0, len(nums) - k):
            temp = temp + nums[i + k] - nums[i]
            if temp > max_sum:
                max_sum = temp
        return max_sum / k


if __name__ == '__main__':
    solution = Solution()
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(solution.findMaxAverage(nums, k))


# 解题思路：
# 初始前k项的和，然后加上后一项减去前一项，滑动窗口的方法，找出最大的和
