class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums = sorted(nums)
        for i in range(0, len(nums)//2):
            result += nums[2*i]
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1,4,3,2]
    print(solution.arrayPairSum(nums))

# 解题思路：
# 排好序后选奇数位的即可
