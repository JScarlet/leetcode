class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        result = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[result]:
                result += 1
                nums[i], nums[result] = nums[result], nums[i]
        return result + 1


if __name__ == '__main__':
    # nums = [0,0,1,1,1,2,2,3,3,4]
    nums = [1,1,2]
    solution = Solution()
    print(solution.removeDuplicates(nums))


# 解题思路：
# 遍历一遍，遇到与开头游标所指的值不同的就交换
