class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_seq = 1
        temp = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                temp += 1
                if max_seq < temp:
                    max_seq = temp
            else:
                temp = 1
        return max_seq


if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,5,4,7]
    print(solution.findLengthOfLCIS(nums))