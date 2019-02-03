class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(0, len(nums) + 1):
            self.dfs(nums, i, [], result, 0)
        return result

    def dfs(self, nums, count, subset, result, start):
        if len(subset) == count:
            result.append(subset)
            return
        for i in range(start, len(nums)):
            self.dfs(nums, count, subset + [nums[i]], result, i+1)


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.subsets(nums))
