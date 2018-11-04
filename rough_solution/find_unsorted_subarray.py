class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        while i <= len(nums) - 1:
            if nums[i] != sorted_nums[i]:
                break
            else:
                i += 1

        while j >= 0:
            if nums[j] != sorted_nums[j]:
                break
            else:
                j -= 1

        if i > j:
            return 0
        return j - i + 1


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(solution.findUnsortedSubarray(nums))

# 解题思路：
# 先把原数组排序，然后当前数组与元素组不对应的地方即为结果

