class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(0, len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,5,6]
    target = 0
    print(solution.searchInsert(nums, target))


# 解题思路：
# 1. 遍历返回第一个大于或等于target的下标，否则就在最后插入
# 2. 可以用二分法但没有必要
