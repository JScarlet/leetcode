class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(nums, [], result)
        return result

    def dfs(self, nums, head, result):
        if len(nums) == 1:
            if head + nums not in result:
                result.append(head + nums)
            return
        else:
            for i in range(0, len(nums)):
                first = nums[i]
                self.dfs(nums[0:i] + nums[i+1:], head + [first], result)


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2]
    print(solution.permuteUnique(nums))
