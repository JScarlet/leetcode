class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val not in nums:
            return len(nums)

        result = len(nums) - 1
        for i in reversed(range(0, len(nums))):
            if nums[i] == val:
                nums[i], nums[result] = nums[result], nums[i]
                result -= 1
        return result + 1


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print(solution.removeElement(nums, val))


# 解题思路：
# 把要删的元素移到最后即可
