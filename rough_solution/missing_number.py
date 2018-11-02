class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums) * (len(nums) + 1) // 2
        nums_sum = sum(nums)
        return total - nums_sum


if __name__ == '__main__':
    solution = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    print(solution.missingNumber(nums))


# 解题思路：
# 0-n的和减去nums中所有元素的和
