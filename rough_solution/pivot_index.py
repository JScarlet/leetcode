class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        total = sum(nums)
        if total - nums[0] == 0:
            return 0
        temp = 0
        for i in range(0, len(nums) - 1):
            temp += nums[i]
            if 2 * temp == total - nums[i+1]:
                return i+1

        if total - nums[-1] == 0:
            return len(nums) - 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [-1,-1,0,1,1, 1]
    print(solution.pivotIndex(nums))


# 解题思路：
# 先求出nums的总和，然后从左向右找出第一个相等的index，否则返回-1
