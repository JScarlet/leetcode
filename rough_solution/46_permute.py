class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        result = []
        self.dfs(nums, [], result)
        return result

    def dfs(self, nums, head, result):
        if len(nums) == 2:
            result.append(head + nums)
            result.append(head + nums[::-1])
            return
        else:
            for i in range(0, len(nums)):
                first = nums[i]
                self.dfs(nums[0:i] + nums[i+1:], head + [first], result)


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4]
    print(solution.permute(nums))
