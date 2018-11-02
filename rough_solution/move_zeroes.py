class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num = 0
        j = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                if num == 0:
                    j = i
                num += 1
            else:
                if num > 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
        print(nums)


if __name__ == '__main__':
    solution = Solution()
    nums = [2,0,0,1,0,3,12]
    solution.moveZeroes(nums)


# 解题思路：
# 从头开始，把0当成一个整体，遇到非0数字就与第一个0交换位置，一直迭代到最后
