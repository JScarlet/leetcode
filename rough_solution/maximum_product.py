class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        if nums[0] < 0 and nums[1] < 0:
            return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
        else:
            return nums[-1] * nums[-2] * nums[-3]


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3]
    print(solution.maximumProduct(nums))


# 解题思路：
# 先对数组进行排序，如果前两位是负数的话就把前两位与最后一位的乘积和最后三位的乘积比较，返回最大的，否则就返回最后三个数的乘积
