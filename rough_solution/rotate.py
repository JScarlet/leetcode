class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(0, k):
            temp = nums.pop(-1)
            nums.insert(0, temp)
        print(nums)


if __name__ == '__main__':
    solution = Solution()
    nums = [-1,-100,3,99]
    k = 2
    solution.rotate(nums, k)

# 解题思路：
# 1. 依次把最后一位放到最前面，循环k次
# 2. 把数组截成两段，前面一段长度为len(nums) - k，后一段为k，然后交换两段位置
