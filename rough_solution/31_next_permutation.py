class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # print(i)
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # print(j)
            if j >= 0:
                nums[i], nums[j] = nums[j], nums[i]
            # print(nums)
        l = len(nums) - 1
        nums[i+1:] = sorted(nums[i+1:])
        # print(nums)


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
    # nums = [3, 2 ,1]
    solution.nextPermutation(nums)
