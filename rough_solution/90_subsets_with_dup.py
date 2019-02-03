class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(0, len(nums) + 1):
            self.dfs(nums, i, [], result, 0)
        return result

    def dfs(self, nums, count, subset, result, start):
        if len(subset) == count:
            if subset not in result:
                result.append(subset)
        for i in range(start, len(nums)):
            self.dfs(nums, count, subset + [nums[i]], result, i + 1)


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 2]
    print(solution.subsetsWithDup(nums))
